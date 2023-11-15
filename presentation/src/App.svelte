<script>
  import "reveal.js/dist/reveal.css";

  import Reveal from "reveal.js";
  import { onMount, tick } from "svelte";
  import Presentation from "./Presentation.svelte";

  export let app;
  export let reveal;

  let deck;

  async function initializeReveal() {
    if (deck) deck.destroy();

    await tick();
    deck = Reveal(reveal);
    deck.initialize();
  }

  onMount(async () => {
    initializeReveal();
  });

  if (import.meta.hot) {
    import.meta.hot.on("vite:beforeUpdate", async (event) => {
      await new Promise((res) => setTimeout(res, 500));
      initializeReveal();
    });
  }
</script>

<svelte:head>
  <title>{app.name}</title>
</svelte:head>

<div class="reveal">
  <div class="slides">
    <Presentation />
  </div>
</div>
