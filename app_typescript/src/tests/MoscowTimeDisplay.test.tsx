import { render, screen } from '@testing-library/react';
import MoscowTimeDisplay from '../MoscowTimeDisplay';
import { vi, expect } from 'vitest';

vi.useFakeTimers();

describe('MoscowTimeDisplay component', () => {
    beforeEach(() => {
        vi.clearAllTimers();
    });

    it('renders the component correctly', () => {
        render(<MoscowTimeDisplay />);
        expect(screen.getByText(/Current time in Moscow/i)).toBeInTheDocument();
    });

    it('displays the correct initial Moscow time', () => {
        render(<MoscowTimeDisplay />);
        const now = new Date().toLocaleString('ru-RU', {
            timeZone: 'Europe/Moscow',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: false,
        });
        expect(screen.getByText(now)).toBeInTheDocument();
    });
});
