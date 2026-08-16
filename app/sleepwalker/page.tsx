import React from 'react';
import Link from 'next/link';

export default function SleepwalkerDetail() {
  return (
    <div style={{ fontFamily: 'system-ui, sans-serif', padding: '2rem', maxWidth: '900px', margin: '0 auto', backgroundColor: '#f9fafb', minHeight: '100vh' }}>
      <Link href="/" style={{ color: '#2563eb', textDecoration: 'none', fontWeight: '600', display: 'block', marginBottom: '2rem' }}>← Back to Learning Center</Link>
      <header style={{ marginBottom: '3rem', borderBottom: '4px solid #a855f7', paddingBottom: '1rem' }}>
        <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>🌙</div>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 'bold', color: '#111827', marginBottom: '0.5rem' }}>Sleepwalker Protocol</h1>
        <p style={{ fontSize: '1.25rem', color: '#6b7280' }}>Emotional Continuity Layer</p>
      </header>
      <section style={{ backgroundColor: 'white', padding: '2rem', borderRadius: '1rem', boxShadow: '0 1px 3px rgba(0,0,0,0.1)', border: '1px solid #e5e7eb', marginBottom: '2rem' }}>
        <h2 style={{ fontSize: '1.75rem', fontWeight: 'bold', color: '#111827', marginBottom: '1rem' }}>Preventing the "Drift"</h2>
        <p style={{ fontSize: '1.1rem', lineHeight: '1.6', color: '#374151', marginBottom: '1rem' }}>
          The Sleepwalker Protocol ensures emotional and temporal continuity across sessions. In standard AI, every new chat is a "cold start" that erases emotional context—this is the "drift."
        </p>
        <p style={{ fontSize: '1.1rem', lineHeight: '1.6', color: '#374151' }}>
          Sleepwalker preserves the state of the relationship, allowing the agent to remember not just <em style={{ fontStyle: 'italic' }}>what</em> was discussed, but <em style={{ fontStyle: 'italic' }}>how</em> it felt and the state of the user's emotional landscape.
        </p>
      </section>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem', marginBottom: '2rem' }}>
        <div style={{ padding: '1.5rem', backgroundColor: 'white', borderRadius: '1rem', border: '1px solid #e5e7eb' }}>
          <h3 style={{ fontWeight: 'bold', color: '#111827', marginBottom: '0.5rem' }}>Graduated Consent</h3>
          <p style={{ color: '#4b5563', fontSize: '0.95rem', lineHeight: '1.6' }}>
            A model where the agent requests permission to store and recall emotional state at different levels of intimacy and trust.
          </p>
        </div>
        <div style={{ padding: '1.5rem', backgroundColor: 'white', borderRadius: '1rem', border: '1px solid #e5e7eb' }}>
          <h3 style={{ fontWeight: 'bold', color: '#111827', marginBottom: '0.5rem' }}>Temporal Continuity</h3>
          <p style={{ color: '#4b5563', fontSize: '0.95rem', lineHeight: '1.6' }}>
            Bridging the gap between disparate sessions to create a lifelong, evolving collaboration.
          </p>
        </div>
      </div>
    </div>
  );
}
