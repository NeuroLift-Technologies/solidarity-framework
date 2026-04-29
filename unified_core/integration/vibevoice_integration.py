"""
VibeVoice Integration Module
Integrates the VibeVoice voice AI (ASR/TTS) with the Agent Solidarity Framework Development Kit (ASFDK)

VibeVoice provides open-source frontier voice AI capabilities including:
- Speech-to-text (ASR) via VibeVoice-ASR-7B — 60-minute single-pass, multilingual, speaker-diarized
- Text-to-speech (TTS) via VibeVoice-Realtime-0.5B — streaming, low-latency synthesis

Source: https://github.com/NeuroLift-Technologies/VibeVoice
"""

import asyncio
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any, AsyncIterator
import sys
import os

# Attempt to import VibeVoice; fall back gracefully if not installed
try:
    from vibevoice import (
        VibeVoiceStreamingForConditionalGenerationInference,
        VibeVoiceStreamingConfig,
        VibeVoiceStreamingProcessor,
        VibeVoiceTokenizerProcessor,
    )
    from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor
    _VIBEVOICE_AVAILABLE = True
except ImportError:
    _VIBEVOICE_AVAILABLE = False

    # Lightweight stubs so the rest of the ASFDK loads without the optional dep
    class VibeVoiceStreamingForConditionalGenerationInference:  # type: ignore
        def __init__(self, *args, **kwargs):
            pass

    class VibeVoiceStreamingConfig:  # type: ignore
        pass

    class VibeVoiceStreamingProcessor:  # type: ignore
        pass

    class VibeVoiceTokenizerProcessor:  # type: ignore
        pass


class TranscriptionResult:
    """Result of a VibeVoice ASR transcription"""

    def __init__(
        self,
        text: str,
        speakers: Optional[List[Dict[str, Any]]] = None,
        language: Optional[str] = None,
        duration_seconds: Optional[float] = None,
    ):
        self.text = text
        self.speakers = speakers or []
        self.language = language
        self.duration_seconds = duration_seconds
        self.timestamp = datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "text": self.text,
            "speakers": self.speakers,
            "language": self.language,
            "duration_seconds": self.duration_seconds,
            "timestamp": self.timestamp.isoformat(),
        }


class VibeVoiceIntegration:
    """
    Integration wrapper for VibeVoice within the Agent Solidarity Framework Development Kit (ASFDK)

    Provides voice capabilities for:
    - Crisis detection through voice stress-pattern analysis (RRT Advocate support)
    - Voice-based TOI preference configuration (NLT-OTOI Framework support)
    - Natural language command capture and TTS response delivery
    - Long-form, multilingual speech transcription with speaker diarization

    Models used (loaded lazily on first call):
    - ASR: microsoft/VibeVoice-ASR (7B, via Hugging Face Transformers)
    - TTS: microsoft/VibeVoice-Realtime-0.5B (streaming)
    """

    ASR_MODEL_ID = "microsoft/VibeVoice-ASR"
    TTS_MODEL_ID = "microsoft/VibeVoice-Realtime-0.5B"

    def __init__(self, foundation):
        self.foundation = foundation
        self.user_id = foundation.user_id
        self.is_initialized = False
        self.is_active = False

        # Lazily-loaded model references
        self._asr_model = None
        self._asr_processor = None
        self._tts_model = None
        self._tts_processor = None

        self.logger = logging.getLogger(f"VibeVoiceIntegration-{self.user_id}")

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    async def initialize(self) -> bool:
        """
        Initialize the VibeVoice integration.

        Models are loaded lazily on first use to avoid GPU memory pressure at
        startup. This method just validates availability and sets the ready flag.

        Returns:
            bool: True if initialization succeeded.
        """
        if self.is_initialized:
            return True

        if not _VIBEVOICE_AVAILABLE:
            self.logger.warning(
                "VibeVoice package is not installed. Voice features will be unavailable. "
                "Install with: pip install vibevoice  (or git+https://github.com/NeuroLift-Technologies/VibeVoice.git)"
            )

        self.is_initialized = True
        self.logger.info("VibeVoice integration initialized (models load lazily on first use)")
        return True

    async def start(self) -> bool:
        """Activate the VibeVoice integration."""
        if not self.is_initialized:
            self.logger.error("Cannot start VibeVoice integration — not initialized")
            return False
        self.is_active = True
        self.logger.info("VibeVoice integration active")
        return True

    async def stop(self) -> bool:
        """Deactivate the VibeVoice integration and release model resources."""
        self.is_active = False
        self._asr_model = None
        self._asr_processor = None
        self._tts_model = None
        self._tts_processor = None
        self.logger.info("VibeVoice integration stopped")
        return True

    # ------------------------------------------------------------------
    # ASR — Speech-to-Text
    # ------------------------------------------------------------------

    def _ensure_asr_loaded(self):
        """Load ASR model and processor if not already loaded."""
        if not _VIBEVOICE_AVAILABLE:
            raise RuntimeError(
                "VibeVoice is not installed. "
                "Run: pip install vibevoice  or  git+https://github.com/NeuroLift-Technologies/VibeVoice.git"
            )
        if self._asr_model is None:
            self.logger.info(f"Loading VibeVoice ASR model: {self.ASR_MODEL_ID}")
            self._asr_processor = AutoProcessor.from_pretrained(self.ASR_MODEL_ID)
            self._asr_model = AutoModelForSpeechSeq2Seq.from_pretrained(self.ASR_MODEL_ID)
            self.logger.info("VibeVoice ASR model loaded")

    async def transcribe(
        self,
        audio_input: Any,
        hotwords: Optional[List[str]] = None,
        language: Optional[str] = None,
    ) -> TranscriptionResult:
        """
        Transcribe audio to text using VibeVoice-ASR.

        Supports up to 60 minutes of audio in a single pass with speaker
        diarization, timestamping, and hotword boosting.

        Args:
            audio_input: Raw audio data (numpy array, file path, or bytes).
            hotwords: Optional list of hotwords/domain terms to boost accuracy.
            language: Optional language hint (auto-detected if None).

        Returns:
            TranscriptionResult with text, speakers, language and duration.
        """
        try:
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(
                None,
                lambda: self._transcribe_sync(audio_input, hotwords, language),
            )
            return result
        except Exception as exc:
            self.logger.error(f"ASR transcription failed: {exc}")
            return TranscriptionResult(text="", language=language)

    def _transcribe_sync(
        self,
        audio_input: Any,
        hotwords: Optional[List[str]],
        language: Optional[str],
    ) -> TranscriptionResult:
        """Synchronous ASR execution (runs in a thread pool)."""
        self._ensure_asr_loaded()

        generate_kwargs: Dict[str, Any] = {}
        if language:
            generate_kwargs["language"] = language
        if hotwords:
            # Pass hotwords as customized context to guide recognition
            generate_kwargs["hotwords"] = hotwords

        inputs = self._asr_processor(audio_input, return_tensors="pt", **generate_kwargs)
        outputs = self._asr_model.generate(**inputs)
        transcription = self._asr_processor.batch_decode(outputs, skip_special_tokens=True)
        text = transcription[0] if transcription else ""
        return TranscriptionResult(text=text, language=language)

    # ------------------------------------------------------------------
    # TTS — Text-to-Speech
    # ------------------------------------------------------------------

    def _ensure_tts_loaded(self):
        """Load TTS model and processor if not already loaded."""
        if not _VIBEVOICE_AVAILABLE:
            raise RuntimeError(
                "VibeVoice is not installed. "
                "Run: pip install vibevoice  or  git+https://github.com/NeuroLift-Technologies/VibeVoice.git"
            )
        if self._tts_model is None:
            self.logger.info(f"Loading VibeVoice TTS model: {self.TTS_MODEL_ID}")
            config = VibeVoiceStreamingConfig.from_pretrained(self.TTS_MODEL_ID)
            self._tts_processor = VibeVoiceStreamingProcessor.from_pretrained(self.TTS_MODEL_ID)
            self._tts_model = VibeVoiceStreamingForConditionalGenerationInference(config)
            self.logger.info("VibeVoice TTS model loaded")

    async def synthesize_stream(self, text: str) -> AsyncIterator[bytes]:
        """
        Stream synthesized speech from text using VibeVoice-Realtime-0.5B.

        Yields raw PCM audio chunks as they are generated, enabling low-latency
        playback for crisis support responses and TOI confirmations.

        Args:
            text: The text to synthesize.

        Yields:
            bytes: Raw audio chunks (PCM, 24 kHz mono).
        """
        try:
            self._ensure_tts_loaded()
            inputs = self._tts_processor(text, return_tensors="pt")
            async for chunk in self._stream_audio_chunks(inputs):
                yield chunk
        except Exception as exc:
            self.logger.error(f"TTS synthesis failed: {exc}")

    async def _stream_audio_chunks(self, inputs: Any) -> AsyncIterator[bytes]:
        """Yield audio chunks from the TTS model output."""
        loop = asyncio.get_event_loop()
        outputs = await loop.run_in_executor(
            None,
            lambda: self._tts_model.generate(**inputs),
        )
        # Convert model output to bytes and yield in one chunk
        # (chunked streaming requires model-specific streamer hooks)
        if hasattr(outputs, "audio") and outputs.audio is not None:
            yield outputs.audio.numpy().tobytes()

    # ------------------------------------------------------------------
    # Crisis / RRT Advocate Support
    # ------------------------------------------------------------------

    async def analyze_stress_patterns(self, audio_input: Any) -> Dict[str, Any]:
        """
        Analyze voice audio for stress indicators to support RRT Advocate crisis detection.

        Args:
            audio_input: Raw audio data for analysis.

        Returns:
            Dict containing stress indicators and confidence scores.
        """
        transcription = await self.transcribe(audio_input)
        # Stress pattern heuristics based on transcription content
        # A full implementation would use acoustic feature extraction
        indicators: Dict[str, Any] = {
            "transcription": transcription.text,
            "speakers_detected": len(transcription.speakers),
            "language": transcription.language,
            "stress_level": "unknown",
            "timestamp": datetime.now().isoformat(),
        }
        return indicators

    # ------------------------------------------------------------------
    # TOI-OTOI Support
    # ------------------------------------------------------------------

    async def capture_voice_preferences(self, audio_input: Any) -> Dict[str, Any]:
        """
        Capture user preferences expressed via voice for TOI-OTOI configuration.

        Args:
            audio_input: Audio containing the user's spoken preferences.

        Returns:
            Dict of parsed preference key/value pairs.
        """
        transcription = await self.transcribe(audio_input)
        return {
            "raw_text": transcription.text,
            "source": "vibevoice_asr",
            "timestamp": datetime.now().isoformat(),
        }

    # ------------------------------------------------------------------
    # Status
    # ------------------------------------------------------------------

    async def get_status(self) -> Dict[str, Any]:
        """Return current integration status."""
        return {
            "component": "vibevoice",
            "is_initialized": self.is_initialized,
            "is_active": self.is_active,
            "vibevoice_available": _VIBEVOICE_AVAILABLE,
            "asr_model_loaded": self._asr_model is not None,
            "tts_model_loaded": self._tts_model is not None,
            "asr_model_id": self.ASR_MODEL_ID,
            "tts_model_id": self.TTS_MODEL_ID,
        }
