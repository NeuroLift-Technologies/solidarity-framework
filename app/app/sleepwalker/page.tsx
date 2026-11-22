import Link from 'next/link';

/**
 * Sleepwalker Protocol detail page in the Learning Center.
 * Explains the emotional continuity layer across sessions.
 */
export default function SleepwalkerDetail() {
  return (
    <main style={{ fontFamily: 'system-ui, sans-serif', padding: '2rem', maxWidth: '900px', margin: '0 auto', backgroundColor: '#f9fafb', minHeight: '100vh' }}>
      <nav aria-label="Breadcrumb"><Link href="/" style={{ color: '#2563eb', textDecoration: 'none', fontWeight: '600', display: 'block', marginBottom: '2rem' }}>← Back to Learning Center</Link></nav>
      <header style={{ marginBottom: '3rem', borderBottom: '4px solid #a855f7', paddingBottom: '1rem' }}>
        <div role="img" aria-label="Sleepwalker Protocol" style={{ fontSize: '3rem', marginBottom: '1rem' }}>🌙</div>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 'bold', color: '#111827', marginBottom: '0.5rem' }}>Sleepwalker Protocol</h1>
        <p style={{ fontSize: '1.25rem', color: '#6b7280' }}>Independent continuity assurance</p>
      </header>
      <section style={{ backgroundColor: 'white', padding: '2rem', borderRadius: '1rem', boxShadow: '0 1px 3px rgba(0,0,0,0.1)', border: '1px solid #e5e7eb', marginBottom: '2rem' }}>
        <h2 style={{ fontSize: '1.75rem', fontWeight: 'bold', color: '#111827', marginBottom: '1rem' }}>Preventing the "Drift"</h2>
        <p style={{ fontSize: '1.1rem', lineHeight: '1.6', color: '#374151', marginBottom: '1rem' }}>
          Sleepwalker independently monitors continuity and protective drift. It checks whether the system follows the retention and purge requirements resolved by OTOI.
        </p>
        <p style={{ fontSize: '1.1rem', lineHeight: '1.6', color: '#374151' }}>
          The design keeps protective state outside the governed agent’s control. Raw conversations and user-linked crisis profiles are excluded from framework persistence.
        </p>
      </section>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem', marginBottom: '2rem' }}>
        <div style={{ padding: '1.5rem', backgroundColor: 'white', borderRadius: '1rem', border: '1px solid #e5e7eb' }}>
          <h3 style={{ fontWeight: 'bold', color: '#111827', marginBottom: '0.5rem' }}>Retention and purge</h3>
          <p style={{ color: '#4b5563', fontSize: '0.95rem', lineHeight: '1.6' }}>
            OTOI decides which minimized records are eligible and when they must be purged. User-linked governance records require explicit consent and finite retention.
          </p>
        </div>
        <div style={{ padding: '1.5rem', backgroundColor: 'white', borderRadius: '1rem', border: '1px solid #e5e7eb' }}>
          <h3 style={{ fontWeight: 'bold', color: '#111827', marginBottom: '0.5rem' }}>Local continuity and public submissions</h3>
          <p style={{ color: '#4b5563', fontSize: '0.95rem', lineHeight: '1.6' }}>
            Protected local runtime state supports continuity. The voluntary public Continuity submission service has a separate consent process.
          </p>
        </div>
      </div>
    </main>
  );
}
