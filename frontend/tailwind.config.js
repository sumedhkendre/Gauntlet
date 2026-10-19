/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        cyber: {
          bg: '#080c14',
          surface: '#0f172a',
          card: '#111c2e',
          cardHover: '#16243b',
          border: '#1e293b',
          borderLight: '#334155',
          accent: '#00e5ff',
          accentHover: '#00c4db',
          accentGlow: 'rgba(0, 229, 255, 0.15)',
          detected: '#ef4444',
          detectedBg: 'rgba(239, 68, 68, 0.12)',
          detectedBorder: 'rgba(239, 68, 68, 0.3)',
          safe: '#10b981',
          safeBg: 'rgba(16, 185, 129, 0.12)',
          safeBorder: 'rgba(16, 185, 129, 0.3)',
          warning: '#f59e0b',
          warningBg: 'rgba(245, 158, 11, 0.12)',
          muted: '#94a3b8',
          text: '#f8fafc',
          textSecondary: '#cbd5e1'
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'Menlo', 'Consolas', 'monospace'],
      },
      boxShadow: {
        'cyber-sm': '0 2px 8px -2px rgba(0, 0, 0, 0.5), 0 1px 4px -1px rgba(0, 229, 255, 0.05)',
        'cyber-md': '0 4px 16px -4px rgba(0, 0, 0, 0.6), 0 2px 8px -2px rgba(0, 229, 255, 0.08)',
        'cyber-lg': '0 10px 25px -5px rgba(0, 0, 0, 0.7), 0 4px 12px -2px rgba(0, 229, 255, 0.12)',
        'cyber-glow': '0 0 15px rgba(0, 229, 255, 0.25)',
        'cyber-danger': '0 0 15px rgba(239, 68, 68, 0.25)',
      },
      animation: {
        'pulse-subtle': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'fade-in': 'fadeIn 0.25s ease-out forwards',
        'slide-up': 'slideUp 0.3s ease-out forwards',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { opacity: '0', transform: 'translateY(12px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        }
      }
    },
  },
  plugins: [],
}
