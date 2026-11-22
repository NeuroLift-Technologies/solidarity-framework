import Link from 'next/link';

/**
 * OTOI detail page in the Learning Center.
 * Explains the Orchestrated Terms of Interaction layer and multi-agent coordination.
 */
export default function OTOIDetail() {
  return (
    <main style={{ fontFamily: 'system-ui, sans-serif', padding: '2rem', maxWidth: '900px', margin: '0 auto', backgroundColor: '#f9fafb', minHeight: '100vh' }}>
      <nav aria-label="Breadcrumb"><Link href="/" style={{ color: '#2563eb', textDecoration: 'none', fontWeight: '600', display: 'block', marginBottom: '2rem' }}>← Back to Learning Center</Link></nav>
      <header style={{ marginBottom: '3rem', borderBottom: '4px solid #6366f1', paddingBottom: '1rem' }}>
        <div role="img" aria-label="OTOI" style={{ fontSize: '3rem', marginBottom: '1rem' }}>📋</div>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 'bold', color: '#111827', marginBottom: '0.5rem' }}>OTOI</h1>
        <p style={{ fontSize: '1.25rem', color: '#6b7280' }}>Orchestrated Terms of Interaction</p>
      </header>
      <section style={{ backgroundColor: 'white', padding: '2rem', borderRadius: '1rem', boxShadow: '0 1px 3px rgba(0,0,0,0.1)', border: '1px solid #e5e7eb', marginBottom: '2rem' }}>
        <h2 style={{ fontSize: '1.75rem', fontWeight: 'bold', color: '#111827', marginBottom: '1rem' }}>The Orchestration Layer</h2>
        <p style={{ fontSize: '1.1rem', lineHeight: '1.6', color: '#374151', marginBottom: '1rem' }}>
          OTOI resolves the authority of trusted Terms of Interaction. It applies mandatory guardrails and decides what an agent may do, delegate or share.
        </p>
        <p style={{ fontSize: '1.1rem', lineHeight: '1.6', color: '#374151' }}>
          The ASFDK Harness applies those decisions where the runtime can intercept the operation. Coverage depends on the adapter and operation.
        </p>
      </section>
      <div style={{ padding: '2rem', backgroundColor: 'white', borderRadius: '1rem', border: '1px solid #e5e7eb', marginBottom: '2rem' }}>
        <h3 style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#111827', marginBottom: '1.5rem', textAlign: 'center' }}>What OTOI decides</h3>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1.5rem' }}>
          <div style={{ textAlign: 'center', padding: '1rem', border: '1px solid #e5e7eb', borderRadius: '0.5rem' }}>
            <div style={{ fontWeight: 'bold', color: '#6366f1', marginBottom: '0.5rem' }}>Authority</div>
            <p style={{ fontSize: '0.9rem', color: '#4b5563' }}>Resolves TOI at runtime and checks whether its signing key is trusted.</p>
          </div>
          <div style={{ textAlign: 'center', padding: '1rem', border: '1px solid #e5e7eb', borderRadius: '0.5rem' }}>
            <div style={{ fontWeight: 'bold', color: '#6366f1', marginBottom: '0.5rem' }}>Delegation and sharing</div>
            <p style={{ fontSize: '0.9rem', color: '#4b5563' }}>Scopes grants and decides what information can be released.</p>
          </div>
          <div style={{ textAlign: 'center', padding: '1rem', border: '1px solid #e5e7eb', borderRadius: '0.5rem' }}>
            <div style={{ fontWeight: 'bold', color: '#6366f1', marginBottom: '0.5rem' }}>Retention and notices</div>
            <p style={{ fontSize: '0.9rem', color: '#4b5563' }}>Decides retention and purge requirements and issues notices for direct delivery to the person.</p>
          </div>
        </div>
      </div>
    </main>
  );
}
