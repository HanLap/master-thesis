<script>
  import "reveal.js/dist/reveal.css";

  import "./app.css";
  import Reveal from "reveal.js";
  import { mount, tick } from "svelte";
  import Presentation from "./Presentation.svelte";
  import Footer from "./lib/Footer.svelte";
  import { slideState } from "$lib/slide";
  import Header from "$lib/Header.svelte";

  let { app, reveal } = $props();

  let deck;

  $effect(() => {
    initializeReveal();
    mountStaticElements();
  });

  if (import.meta.hot) {
    // reinitialize Reveal after HMR, to rerender slides
    // using beforeUpdate and timeout because afterUpdater doesn't seem to work.
    import.meta.hot.on("vite:beforeUpdate", async (e) => {
      if (
        e.updates.reduce(
          (acc, a) => acc && !a.path.endsWith(".js|.svelte"),
          true
        )
      ) {
        return;
      }

      console.log(e);
      await new Promise((res) => setTimeout(res, 500));
      initializeReveal();
    });
  }

  async function initializeReveal() {
    if (deck) deck.destroy();

    await tick();
    deck = Reveal(reveal);
    deck.initialize();
    slideState.reveal = deck;
  }

  function mountStaticElements() {
    mount(Header, {
      target: document.querySelector("div.reveal"),
    });
    mount(Footer, {
      target: document.querySelector("div.reveal"),
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
