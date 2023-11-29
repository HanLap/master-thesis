<script>
  import { onMount } from "svelte";

  export let step;

  let count = 2;

  $: doubled = count * 2;

  let ref;

  onMount(() => {
    ref?.addEventListener("click", () => count++);
  });
</script>

{#if step in [0, 1]}
  <div>Hello world!</div>
{/if}
{#if step >= 2}
  <div>count: {count}</div>
{/if}
{#if step >= 3}
  <button
    bind:this={ref}
    class="border rounded-xl border-gray-600 bg-gray-200 p-2 active:brightness-90"
  >
    click me!
  </button>
{/if}
{#if step >= 4}
  <div class="mt-4">{count} * 2 = {doubled}</div>
{/if}
