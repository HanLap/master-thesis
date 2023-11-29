import { getContext } from "svelte";
import { slideState } from "./slideState.svelte";

export const slideContextKey = "SlideContext";

/**
 * @param {HTMLElement} node
 * @param {String} subtitle
 * @return {import('svelte/action').ActionReturn}
 */
export function subtitle(node, subtitle) {
  const context = getContext(slideContextKey);

  function changeHandler(event) {
    if (event.currentSlide === node) {
      context.subtitle = subtitle;
    }
  }

  $effect(() => {
    if (slideState.reveal) {
      slideState.reveal.on("slidechanged", changeHandler);

      return () => {
        slideState.reveal.off("slidechanged", changeHandler);
      };
    }
  });

  return {
    destroy() {
      slideState.reveal?.on("slidechanged", changeHandler);
    },
  };
}
