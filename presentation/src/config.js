import Highlight from "reveal.js/plugin/highlight/highlight";
import HighlightSvelte from "highlightjs-svelte";
import Markdown from "reveal.js/plugin/markdown/markdown";
import RevealNotes from "reveal.js/plugin/notes/notes";
import "@fontsource/overpass";

// Import theme
import "$lib/style/xx-theme.css";
import "$lib/style/code-theme.css";

export default {
  // App Config
  app: {
    name: "Case-study of SvelteKit for a Modern Business Application",
  },
  // Reveal Config
  /** @type {import('reveal.js').Options} */
  reveal: {
    width: 1280,
    height: 720,
    plugins: [Highlight, Markdown, RevealNotes],
    highlight: {
      beforeHighlight: (hljs) => HighlightSvelte(hljs),
    },
    hash: true,
  },
};
