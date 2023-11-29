<script>
  import { getContext } from "svelte";
  import { slideContextKey } from "./subtitleAction.svelte";
  
  /**
   * @type {{
   *  title: string,
   *  subtitle?: string,
   *  static?: boolean
   * }}
   */
  let { title, subtitle, static: stat = false } = $props();

  const context = getContext(slideContextKey);

  // $effect(() => {
  //   // check data-subtitle attribute if subtitle is not provided.
  //   if (!stat && !subtitle && slideState.reveal) {
  //     const changeHandler = (event) => {
  //       dynamicTitle =
  //         event.currentSlide?.getAttribute("data-subtitle") ?? undefined;
  //     };

  //     slideState.reveal.on("slidechanged", changeHandler);

  //     return () => {
  //       slideState.reveal.off("slidechanged", changeHandler);
  //     };
  //   }
  // });
</script>

<div class="flex flex-col items-start">
  <h2 class="mt-4 text-4xl leading-4">{title}</h2>
  {#if subtitle || context.subtitle}
    <h3 class="text-3xl leading-3 mt-2">
      {subtitle ?? context.subtitle}
    </h3>
  {/if}
  <span class="w-20 border-b-2 border-svelte2" />
</div>
