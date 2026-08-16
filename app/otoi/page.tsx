import React from 'react';
import Link from 'next/link';

export default function OTOIDetail() {
  return (
    <div style={{ fontFamily: 'system-ui, sans-serif', padding: '2rem', maxWidth: '900px', margin: '0 auto', backgroundColor: '#f9fafb', minHeight: '100vh' }}>
      <Link href="/" style={{ color: '#2563eb', textDecoration: 'none', fontWeight: '600', display: 'block', marginBottom: '2rem' }}>← Back to Learning Center</Link>
      <header style={{ marginBottom: '3rem', borderBottom: '4px solid #6366f1', paddingBottom: '1rem' }}>
        <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>📋</div>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 'bold', color: '#111827', marginBottom: '0.5rem' }}>OTOI</h1>
        <p style={{ fontSize: '1.25rem', color: '#6b7280' }}>Orchestrated Terms of Interaction</p>
      </header>
      <section style={{ backgroundColor: 'white', padding: '2rem', borderRadius: '1rem', boxShadow: '0 1px 3px rgba(0,0,0,0.1)', border: '1px solid #e5e7eb', marginBottom: '2rem' }}>
        <h2 style={{ fontSize: '1.75rem', fontWeight: 'bold', color: '#111827', marginBottom: '1rem' }}>The Orchestration Layer</h2>
        <p style={{ fontSize: '1.1rem', lineHeight: '1.6', color: '#374151', marginBottom: '1rem' }}>
          If TOI is the <em style={{ fontStyle: 'italic' }}>declaration</em>, OTOI is the <em style={{ fontStyle: 'italic' }}>enforcement</em>. It is the runtime orchestration layer that ensures a user's TOI is honored across a multi-agent ecosystem.
        </p>
        <p style={{ fontSize: '1.1rem', lineHeight: '1.6', color: '#374151' }}>
          OTOI prevents "governance gaps" during agent-to-agent handoffs, ensuring that the user's identity and boundaries travel with the context.
        </p>
      </section>
      <div style={{ padding: '2rem', backgroundColor: 'white', borderRadius: '1rem', border: '1px solid #e5e7eb', marginBottom: '2rem' }}>
        <h3 style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#111827', marginBottom: '1.5rem', textAlign: 'center' }}>The Three-Pillar Governance Model</h3>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1.5rem' }}>
          <div style={{ textAlign: 'center', padding: '1rem', border: '1px solid #e5e7eb', borderRadius: '0.5rem' }}>
            <div style={{ fontWeight: 'bold', color: '#6366f1', marginBottom: '0.5rem' }}>TOI Parser</div>
            <p style={{ fontSize: '0.9rem', color: '#4b5563' }}>Validates and canonicalizes the declaration.</p>
          </div>
          <div style={{ textAlign: 'center', padding: '1rem', border: '1px solid #e5e7eb', borderRadius: '0.5rem' }}>
            <div style={{ fontWeight: 'bold', color: '#6366f1', marginBottom: '0.5rem' }}>OTOI Orchestrator</div>
            <p style={{ fontSize: '0.9rem', color: '#4b5563' }}>Routes interaction through active governance.</p>
          </div>
          <div style={{ textAlign: 'center', padding: '1rem', border: '1px solid #e5e7eb', borderRadius: '0.5rem' }}>
            <div style={{ fontWeight: 'bold', color: '#6366f1', marginBottom: '0.5rem' }}>Privacy Guardian</div>
            <p style={{ fontSize: '0.9rem', color: '#4b5563' }}>Filters and protects sensitive data boundaries.</p>
          </div>
        </div>
      </div}
    </div>
  );
}
