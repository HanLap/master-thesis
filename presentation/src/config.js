import Highlight from "reveal.js/plugin/highlight/highlight";
import HighlightSvelte from "highlightjs-svelte";
import Markdown from "reveal.js/plugin/markdown/markdown";
import RevealNotes from "reveal.js/plugin/notes/notes";

// Import theme
import "reveal.js/dist/theme/white.css";

// Import CSS for plugins
import "reveal.js/plugin/highlight/zenburn.css";

export default {
  // App Config
  app: {
    name: "Reveal.js with Svelte and Vite",
  },
  // Reveal Config
  reveal: {
    plugins: [Highlight, Markdown, RevealNotes],
    highlight: {
      beforeHighlight: (hljs) => HighlightSvelte(hljs),
    },
    hash: true,
  },
};
