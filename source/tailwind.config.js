module.exports = {
	content: ['./dist/**/*.html'],
	theme: {
		fontFamily: {
			sans: 'Inter',
		},
		extend: {
			colors: {
				accent: {
					DEFAULT: '#07367C',
					100: '#86B2FF',
				},
			},
			container: {
				center: true,
				padding: '20px',
			},
			screens: {
				'2xl': 'none',
			},
		},
	},
	plugins: [],
};

// npx tailwindcss -i ./src/input.css -o ./dist/css/style.min.css --watch -m