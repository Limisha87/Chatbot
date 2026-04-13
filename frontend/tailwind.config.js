export default {
    content: [
        "./index.html",
        "./src/**/*.{js,jsx,ts,tsx}"
    ],
    theme: {
        extend: {
            fontFamily: {
                primary: ['Poppins', 'sans-serif'],
                secondary: ['Roboto', 'sans-serif'],
            },
            colors: {
                primary: '#FF7043',
                'primary-hover': '#F4511E',
                'text-strong': '#263238',
                'text-default': '#546E7A',
                'text-muted': '#6b7281',
                'text-subtle': '#9ca3af',
                'bg-app': '#FFFDF9',
                'bg-surface': '#FFFFFF',
                'bg-surface-alt': '#FAF3EB',
                'bg-surface-glass': 'rgba(255, 255, 255, 0.7)',
                'bg-interactive-subtle': '#f3f4f6',
                'border-default': '#ECEFF1',
                'border-hover': 'rgba(255, 112, 67, 0.5)',
                'border-focus': '#FF7043',
            },
        },
    },
    plugins: [],
};