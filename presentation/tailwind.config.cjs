/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{svelte,js}"],
  theme: {
    extend: {
      colors: {
        primary1: "var(--xx-primary1)",
        primary2: "var(--xx-primary2)",
        primary3: "var(--xx-primary3)",
        secondary1: "var(--xx-secondary1)",
        secondary2: "var(--xx-secondary2)",
        surface: "var(--xx-surface)",
        svelte1: "var(--svelte-color1)",
        svelte2: "var(--svelte-color2)",
        "svelte-text1": "var(--svelte-text1)",
        "svelte-text2": "var(--svelte-text2)",
      },
    },
  },
  plugins: [],
  important: true,
};
