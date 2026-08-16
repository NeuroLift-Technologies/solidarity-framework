import type { Metadata } from 'next';
import type { ReactNode } from 'react';

export const metadata: Metadata = {
  title: 'Solidarity Framework — Learning Center',
  description: 'Learn about the Solidarity Framework: TOI, OTOI, RRT Advocate, and the Sleepwalker Protocol.',
};

/**
 * Root layout for the Learning Center app.
 * Renders the document shell (html/body) around page children.
 */
export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
