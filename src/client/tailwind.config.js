/** @type {import('tailwindcss').Config} */
export default {
  darkMode: ["class"],
  content: ["./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      borderRadius: {},
      colors: {},
    },
  },
  plugins: [require("tailwindcss-animate")],
};
