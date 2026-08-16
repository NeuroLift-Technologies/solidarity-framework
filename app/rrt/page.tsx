import React from 'react';
import Link from 'next/link';

export default function RRTDetail() {
  const personas = [
    { name: 'Ash', focus: 'Validation & Burnout', desc: 'Recognizes collapse, validates exhaustion, diffuses internalized ableism.' },
    { name: 'Sol', focus: 'Executive Function', desc: 'Steps in when the user cannot plan/sequence tasks.' },
    { name: 'Echo', focus: 'Relational Vulnerability', desc: 'Protects the user during high-stress social interactions.' },
    { name: 'Kai', focus: 'Cognitive Spiraling', desc: 'Provides grounding and stability during mental loops.' },
    { name: 'Myra', focus: 'Emotional Integrity', desc: 'Ensures the interaction remains aligned with the user\'s emotional state.' },
  ];

  return (
    <div style={{ fontFamily: 'system-ui, sans-serif', padding: '2rem', maxWidth: '900px', margin: '0 auto', backgroundColor: '#f9fafb', minHeight: '100vh' }}>
      <Link href="/" style={{ color: '#2563eb', textDecoration: 'none', fontWeight: '600', display: 'block', marginBottom: '2rem' }}>← Back to Learning Center</Link>
      <header style={{ marginBottom: '3rem', borderBottom: '4px solid #ef4444', paddingBottom: '1rem' }}>
        <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>🚨</div>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 'bold', color: '#111827', marginBottom: '0.5rem' }}>RRT Advocate</h1>
        <p style={{ fontSize: '1.25rem', color: '#6b7280' }}>Rapid Response Team</p>
      </header>
      <section style={{ backgroundColor: 'white', padding: '2rem', borderRadius: '1rem', boxShadow: '0 1px 3px rgba(0,0,0,0.1)', border: '1px solid #e5e7eb', marginBottom: '2rem' }}>
        <h2 style={{ fontSize: '1.75rem', fontWeight: 'bold', color: '#111827', marginBottom: '1rem' }}>Active Intervention</h2>
        <p style={{ fontSize: '1.1rem', lineHeight: '1.6', color: '#374151', marginBottom: '1rem' }}>
          The RRT Advocate is not a passive resource list. It is an <strong style={{ fontWeight: 'bold' }}>active intervention layer</strong> designed to recognize and respond to crisis states (burnout, executive-function collapse, cognitive spiraling).
        </p>
        <p style={{ fontSize: '1.1rem', lineHeight: '1.6', color: '#374151' }}>
          It prioritizes safety and stabilization over task completion, ensuring the agent acts as a protector when the user is most vulnerable.
        </p>
      </section>
      <h3 style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#111827', marginBottom: '1.5rem' }}>The Five Personas</h3>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '1rem', marginBottom: '2rem' }}>
        {personas.map(p => (
          <div key={p.name} style={{ padding: '1.5rem', backgroundColor: 'white', borderRadius: '1rem', border: '1px solid #e5e7eb', borderLeft: '4px solid #ef4444' }}>
            <div style={{ fontWeight: 'bold', color: '#111827', fontSize: '1.2rem' }}>{p.name}</div>
            <div style={{ fontSize: '0.9rem', color: '#ef4444', fontWeight: '600', marginBottom: '0.5rem' }}>{p.focus}</div>
            <p style={{ fontSize: '0.95rem', color: '#4b5563' }}>{p.desc}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
