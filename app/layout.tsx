import type { Metadata } from 'next';
import type { ReactNode } from 'react';

export const metadata: Metadata = {
  title: 'Solidarity Framework — Learning Center',
  description: 'Learn about the Solidarity Framework: TOI, OTOI, RRT AIdvocAIte, and the Sleepwalker Protocol.',
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
