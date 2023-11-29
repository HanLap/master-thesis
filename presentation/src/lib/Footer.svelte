<script>
  import { fade } from "svelte/transition";
  import { slideState } from "./slide";

  const config = $derived(slideState.config);

  let isSpeakerView = $state(false);

  $effect(() => {
    if (window.self !== window.top) {
      // The page is inside an iframe
      isSpeakerView = true;
    } else {
      // The page is not inside an iframe
      isSpeakerView = false;
    }
  });

  // $effect(() => {
  //   if (slideState.slideType === "title") {
  //     const elems = document.querySelectorAll(".controls-arrow");

  //     elems.forEach((e) => e.classList.add("text-surface"));

  //     return () => {
  //       elems.forEach((e) => e.classList.remove("text-surface"));
  //     };
  //   }
  // });
</script>

{#if !isSpeakerView && slideState.slideType !== "title"}
  <small
    class="footer absolute bottom-4 left-8 flex items-center text-xl text-gray-400 z-20"
    transition:fade
  >
    <div class="w-16 pr-6 text-4xl text-right">{slideState.slideNumber}</div>
    <div
      class="animate border-l-2 border-gray-300 pl-4 flex flex-col items-start"
    >
      <div>{config.shortTitle}</div>
      <div>{config.date} | {config.confidentiality} | {config.presenter}</div>
    </div>
  </small>
{/if}
