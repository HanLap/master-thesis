<script>
  import xxLogo from "$assets/eXXcellent-solutions-Logo_blau_transBG_RGB.svg";
  import uniLogo from "$assets/logo_uulm_sw.png";
  import { fade } from "svelte/transition";
  import { slideState } from "./slide";
</script>

<div class="fixed top-0 left-0 right-0 z-50 flex justify-between">
  {#if slideState.slideType === "title"}
    <img class="w-96 mt-10 ml-20" src={xxLogo} alt="" transition:fade />
    <img class="h-24 mt-14 mr-20" src={uniLogo} alt="" transition:fade />
  {/if}
</div>
