import { render, screen } from '@testing-library/react';
import App from '../App.tsx';
import { describe, it, expect } from 'vitest';

describe('App component', () => {
    it('renders Vite and React logos with correct links', () => {
        render(<App />);

        const viteLogo = screen.getByRole('img', { name: /Vite logo/i });
        const reactLogo = screen.getByAltText('React logo');

        expect(viteLogo).toBeInTheDocument();
        expect(reactLogo).toBeInTheDocument();

        expect(viteLogo.closest('a')).toHaveAttribute(
            'href',
            'https://vite.dev',
        );
        expect(reactLogo.closest('a')).toHaveAttribute(
            'href',
            'https://react.dev',
        );
    });

    it('renders text content correctly', () => {
        render(<App />);

        const title = screen.getByText('Vite + React');
        const docsText = screen.getByText(
            'Click on the Vite and React logos to learn more',
        );

        expect(title).toBeInTheDocument();
        expect(docsText).toBeInTheDocument();
    });
});
