import Link from 'next/link';

/**
 * TOI detail page in the Learning Center.
 * Explains the Terms of Interaction declarative schema and its reserved $ keys.
 */
export default function TOIDetail() {
  return (
    <main style={{ fontFamily: 'system-ui, sans-serif', padding: '2rem', maxWidth: '900px', margin: '0 auto', backgroundColor: '#f9fafb', minHeight: '100vh' }}>
      <nav aria-label="Breadcrumb"><Link href="/" style={{ color: '#2563eb', textDecoration: 'none', fontWeight: '600', display: 'block', marginBottom: '2rem' }}>← Back to Learning Center</Link></nav>
      <header style={{ marginBottom: '3rem', borderBottom: '4px solid #3b82f6', paddingBottom: '1rem' }}>
        <div role="img" aria-label="TOI" style={{ fontSize: '3rem', marginBottom: '1rem' }}>📋</div>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 'bold', color: '#111827', marginBottom: '0.5rem' }}>TOI</h1>
        <p style={{ fontSize: '1.25rem', color: '#6b7280' }}>Terms of Interaction</p>
      </header>
      <section style={{ backgroundColor: 'white', padding: '2rem', borderRadius: '1rem', boxShadow: '0 1px 3px rgba(0,0,0,0.1)', border: '1px solid #e5e7eb', marginBottom: '2rem' }}>
        <h2 style={{ fontSize: '1.75rem', fontWeight: 'bold', color: '#111827', marginBottom: '1rem' }}>The Declaration of Dignity</h2>
        <p style={{ fontSize: '1.1rem', lineHeight: '1.6', color: '#374151', marginBottom: '1rem' }}>
          TOI gives a person a portable way to declare interaction preferences, boundaries and authority constraints. The TOI project defines the canonical format, generator and signing primitives.
        </p>
        <p style={{ fontSize: '1.1rem', lineHeight: '1.6', color: '#374151' }}>
          A signature verifies integrity against a key. OTOI must establish that the key is trusted and bound to the person before using the declaration as authority.
        </p>
      </section>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem', marginBottom: '2rem' }}>
        <div style={{ padding: '1.5rem', backgroundColor: 'white', borderRadius: '1rem', border: '1px solid #e5e7eb' }}>
          <h3 style={{ fontWeight: 'bold', color: '#111827', marginBottom: '0.5rem' }}>Technical Rigor</h3>
          <ul style={{ color: '#4b5563', lineHeight: '1.6', fontSize: '0.95rem' }}>
            <li><strong>Canonical format:</strong> Defines the bytes that signing and verification use.</li>
            <li><strong>Signing:</strong> Binds document integrity to the signing key.</li>
            <li><strong>Strict Schema:</strong> reserved `$` keys for format evolution (e.g., `$toi`, `$tier`, `$created`, `$updated`, `$signature`).</li>
          </ul>
        </div>
        <div style={{ padding: '1.5rem', backgroundColor: 'white', borderRadius: '1rem', border: '1px solid #e5e7eb' }}>
          <h3 style={{ fontWeight: 'bold', color: '#111827', marginBottom: '0.5rem' }}>Core Sections</h3>
          <ul style={{ color: '#4b5563', lineHeight: '1.6', fontSize: '0.95rem' }}>
            <li><strong>Identity:</strong> Who is the author?</li>
            <li><strong>Cognitive Profile:</strong> How does the user think?</li>
            <li><strong>Privacy:</strong> Where are the boundaries?</li>
            <li><strong>Agency:</strong> How is control preserved?</li>
          </ul>
        </div>
      </div>
    </main>
  );
}
