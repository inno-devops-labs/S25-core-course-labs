/// <reference types="vitest" />
/// <reference types="vite/client" />

import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';

// https://vite.dev/config/
export default defineConfig({
    plugins: [react()],
    preview: {
        port: 8080,
        strictPort: true,
        allowedHosts: ['app-typescript.local'],
    },
    server: {
        port: 8080,
        strictPort: true,
        host: true,
        origin: '0.0.0.0',
    },
    test: {
        environment: 'jsdom',
        setupFiles: ['./src/tests/setup.ts'],
        globals: true,
    },
});
