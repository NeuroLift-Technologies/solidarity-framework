import Link from 'next/link';

/**
 * Landing page for the Learning Center.
 * Renders the narrative hero and pillar navigation cards for the four Solidarity Framework components.
 */
export default function SolidarityNarrativeHome() {
  const pillars = [
    { id: 'toi', path: '/toi', name: 'TOI', fullName: 'Terms of Interaction', icon: '📋', color: '#3b82f6', desc: 'Establishing user identity and boundaries.' },
    { id: 'otoi', path: '/otoi', name: 'OTOI', fullName: 'Orchestrated Terms of Interaction', icon: '📋', color: '#6366f1', desc: 'Ensuring multi-agent coordination and honoring user boundaries.' },
    { id: 'rrt', path: '/rrt', name: 'RRT Advocate', fullName: 'Rapid Response Team', icon: '🚨', color: '#ef4444', desc: 'Crisis detection and immediate safety protocols.' },
    { id: 'sleepwalker', path: '/sleepwalker', name: 'Sleepwalker Protocol', fullName: 'Continuity Layer', icon: '🌙', color: '#a855f7', desc: 'Maintaining emotional state across sessions.' },
  ];

  return (
    <main style={{ fontFamily: 'system-ui, sans-serif', backgroundColor: '#fff', color: '#111827', lineHeight: '1.6' }}>
      <style>{`a:focus-visible { outline: 3px solid #6366f1; outline-offset: 2px; border-radius: 0.5rem; }`}</style>
      {/* Hero Section */}
      <section style={{ padding: '6rem 2rem', textAlign: 'center', backgroundColor: '#f9fafb', borderBottom: '1px solid #e5e7eb' }}>
        <h1 style={{ fontSize: '3.5rem', fontWeight: 'bold', marginBottom: '1.5rem', letterSpacing: '-0.02em' }}>
          The Solidarity Framework
        </h1>
        <p style={{ fontSize: '1.5rem', color: '#4b5563', maxWidth: '800px', margin: '0 auto', lineHeight: '1.4' }}>
          From a concrete need for neurodivergent support to a universal layer between model and agent.
        </p>
      </section>

      {/* The Story Section */}
      <section style={{ padding: '4rem 2rem', maxWidth: '800px', margin: '0 auto' }}>
        <div style={{ marginBottom: '4rem' }}>
          <h2 style={{ fontSize: '2rem', fontWeight: 'bold', marginBottom: '1.5rem' }}>Where this began</h2>
          <p style={{ fontSize: '1.2rem', color: '#374151', marginBottom: '1.5rem' }}>
            NeuroLift Technologies started with a specific mission: build intelligent, adaptive support that worked for neurodivergent minds first. 
            We focused on ADHD, autism spectrum, and thinking patterns that mainstream tools often ignore.
          </p>
          <p style={{ fontSize: '1.2rem', color: '#374151' }}>
            This journey taught us hard lessons about crisis response, shame-resistant design, and the absolute necessity of privacy-first state.
          </p>
        </div>

        <div style={{ marginBottom: '4rem', padding: '2rem', backgroundColor: '#eff6ff', borderRadius: '1rem', borderLeft: '4px solid #3b82f6' }}>
          <h2 style={{ fontSize: '2rem', fontWeight: 'bold', marginBottom: '1rem' }}>The Realization</h2>
          <p style={{ fontSize: '1.2rem', color: '#1e40af' }}>
            What we discovered is that these needs aren't niche. They are the baseline expectations for <strong>humane AI assistance</strong>.
          </p>
        </div>

        <div style={{ marginBottom: '4rem' }}>
          <h2 style={{ fontSize: '2rem', fontWeight: 'bold', marginBottom: '1.5rem' }}>The Universal Layer</h2>
          <p style={{ fontSize: '1.2rem', color: '#374151', marginBottom: '1.5rem' }}>
            The Solidarity Framework is the result of this evolution. It is the source of truth for the principles and components that sit 
            <strong>between the model and the agent</strong>. It ensures that no matter the tool, the interaction is governed by safety, transparency, and human agency.
          </p>
        </div>
      </section>

      {/* The Pillars Section */}
      <section style={{ padding: '4rem 2rem', backgroundColor: '#111827', color: 'white' }}>
        <div style={{ maxWidth: '1000px', margin: '0 auto' }}>
          <h2 style={{ fontSize: '2.5rem', fontWeight: 'bold', textAlign: 'center', marginBottom: '0.5rem' }}>Tools of Solidarity</h2>
          <p style={{ fontSize: '1.25rem', color: '#9ca3af', textAlign: 'center', marginBottom: '3rem' }}>The Learning Center</p>
          
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '2rem' }}>
            {pillars.map((pillar) => (
              <Link key={pillar.id} href={pillar.path} style={{ textDecoration: 'none', color: 'inherit' }}>
                <div style={{ 
                  padding: '2rem', 
                  borderRadius: '1rem', 
                  backgroundColor: '#1f2937', 
                  border: '1px solid #374151',
                  transition: 'all 0.2s ease',
                  cursor: 'pointer',
                  borderTop: `4px solid ${pillar.color}`
                }}>
                  <div role="img" aria-label={pillar.name} style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>{pillar.icon}</div>
                  <h3 style={{ fontSize: '1.5rem', fontWeight: 'bold', marginBottom: '0.5rem' }}>{pillar.name}</h3>
                  <p style={{ fontSize: '0.875rem', color: '#9ca3af', marginBottom: '1rem' }}>{pillar.fullName}</p>
                  <p style={{ fontSize: '1rem', color: '#d1d5db', marginBottom: '1.5rem' }}>{pillar.desc}</p>
                  <span style={{ color: pillar.color, fontWeight: '600' }}>Learn More →</span>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Looking Ahead */}
      <section style={{ padding: '4rem 2rem', textAlign: 'center', maxWidth: '800px', margin: '0 auto' }}>
        <h2 style={{ fontSize: '2rem', fontWeight: 'bold', marginBottom: '1.5rem' }}>Looking Ahead</h2>
        <p style={{ fontSize: '1.2rem', color: '#4b5563' }}>
          From healthcare and education to the workplace and beyond, we are extending these core principles—transparency, minimal footprint, 
          and escalation culture—to every product we build. The framework is the contract; the future is built on top of it.
        </p>
      </section>

      <footer style={{ padding: '2rem', textAlign: 'center', color: '#9ca3af', fontSize: '0.875rem', borderTop: '1px solid #e5e7eb' }}>
        <p>NeuroLift Technologies • Governed by HAIEF</p>
      </footer>
    </main>
  );
}
