<script>
  import architectureDswfd from "$assets/dswfd-architecture.png";
  import architetureFrontend from "$assets/dswfd-architecture-frontend.png";
  import architetureFullstack from "$assets/dswfd-architecture-fullstack.png";
  import architetureSpa from "$assets/dswfd-architecture-spa.png";
  import bwFuhrpark from "$assets/bwfuhrparkService_freistehend.jpg";
  import { Slide, SlideTitle, subtitle } from "$lib/slide";
  import Notes from "$lib/Notes.svelte";
</script>

<Slide type="hero" transition="slide-in zoom-out">
  <h2 class="uppercase">Procedure</h2>

  <Notes>
    <ul>
      <li>Actually write Software</li>
    </ul>
  </Notes>
</Slide>

<Slide transition="zoom-in slide-out">
  <SlideTitle title="Implementation" />
  <section
    class="flex flex-col justify-center items-center"
    use:subtitle={"BwFuhrpark"}
  >
    <img class="w-1/2" src={bwFuhrpark} alt="" />
    <h2 class="fragment">DSW-Fahrdienst</h2>
  </section>

  <section
    class="flex justify-center mt-8"
    use:subtitle={"Existing Implementation"}
  >
    <img class="h-[420px]" src={architectureDswfd} alt="" />
  </section>

  <section use:subtitle={"SvelteKit Implementations"}>
    <div class="grid grid-cols-[30%,40%,30%]">
      <div class="fragment flex flex-col items-start">
        <h5 class="text-4xl">SvelteKit Fullstack</h5>
        <img class="h-48" src={architetureFullstack} alt="" />
      </div>
      <div class="fragment flex flex-col items-start">
        <h5 class="text-4xl">SvelteKit Frontend</h5>
        <img class="h-48" src={architetureFrontend} alt="" />
      </div>
      <div class="fragment flex flex-col items-start">
        <h5 class="text-4xl">SvelteKit SPA</h5>
        <img class="h-48" src={architetureSpa} alt="" />
      </div>
    </div>
  </section>
</Slide>
