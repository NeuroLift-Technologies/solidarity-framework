import React from 'react';

export default function SolidarityLearningHome() {
  const pillars = [
    {
      id: 'toi',
      path: '/toi',
      name: 'TOI',
      fullName: 'Terms of Interaction',
      description: 'The foundational governance layer establishing user preferences and identity.',
      color: '#3b82f6',
      icon: '📋'
    },
    {
      id: 'otoi',
      path: '/otoi',
      name: 'OTOI',
      fullName: 'Orchestrated TOI',
      description: 'The coordination layer ensuring multi-agent honoring of the TOI.',
      color: '#6366f1',
      icon: '📋'
    },
    {
      id: 'rrt',
      path: '/rrt',
      name: 'RRT Advocate',
      fullName: 'Rapid Response Team',
      description: 'The protective layer for crisis detection and immediate safety protocols.',
      color: '#ef4444',
      icon: '🚨'
    },
    {
      id: 'sleepwalker',
      path: '/sleepwalker',
      name: 'Sleepwalker Protocol',
      fullName: 'Continuity Layer',
      description: 'The continuity layer managing emotional state across sessions.',
      color: '#a855f7',
      icon: '🌙'
    },
  ];

  return (
    <div style={{ fontFamily: 'system-ui, sans-serif', padding: '2rem', maxWidth: '1000px', margin: '0 auto', backgroundColor: '#f9fafb', minHeight: '100vh' }}>
      <header style={{ textAlign: 'center', marginBottom: '3rem' }}>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 'bold', color: '#111827', marginBottom: '1rem' }}>Solidarity Framework Learning Center</h1>
        <p style={{ fontSize: '1.25rem', color: '#4b5563', maxWidth: '700px', margin: '0 auto' }}>
          Explore the layers that sit between the model and the agent to ensure human safety, transparency, and emotional continuity.
        </p>
      </header>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '1.5rem' }}>
        {pillars.map((pillar) => (
          <a key={pillar.id} href={pillar.path} style={{ textDecoration: 'none', color: 'inherit' }}>
            <div style={{ 
              padding: '1.5rem', 
              borderRadius: '1rem', 
              backgroundColor: 'white', 
              boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1)', 
              border: '1px solid #e5e7eb',
              transition: 'transform 0.2s ease',
              cursor: 'pointer',
              borderTop: `4px solid ${pillar.color}`
            }}>
              <div style={{ fontSize: '2rem', marginBottom: '1rem' }}>{pillar.icon}</div>
              <h2 style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#111827', marginBottom: '0.5rem' }}>{pillar.name}</h2>
              <p style={{ fontSize: '0.875rem', fontWeight: '600', color: '#6b7280', marginBottom: '1rem' }}>{pillar.fullName}</p>
              <p style={{ fontSize: '1rem', color: '#374151', lineHeight: '1.5', marginBottom: '1.5rem' }}>{pillar.description}</p>
              <button style={{ 
                width: '100%', 
                padding: '0.5rem', 
                borderRadius: '0.5rem', 
                border: 'none', 
                backgroundColor: pillar.color, 
                color: 'white', 
                fontWeight: '600',
                cursor: 'pointer'
              }}>
                Learn More
              </button>
            </div>
          </a>
        ))}
      </div>

      <footer style={{ marginTop: '4rem', textAlign: 'center', color: '#9ca3af', fontSize: '0.875rem' }}>
        <p>NeuroLift Technologies • Governed by HAIEF</p>
      </footer>
    </div>
  );
}
