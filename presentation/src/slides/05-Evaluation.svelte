<script>
  import Code from "$lib/Code.svelte";
  import benchmarkResults from "$assets/benchmark-results.png";
  import svelteLogo from "$assets/svelte-logo.svg";
  import svelteRunes from "$assets/svelte-runes.jpg";
  import ui5Logo from "$assets/ui5-logo.png";
  import Notes from "$lib/Notes.svelte";
  import { Slide, SlideTitle, subtitle } from "$lib/slide";
</script>

<Slide type="hero" transition="slide-in zoom-out">
  <h2 class="uppercase">Evaluation</h2>

  <Notes>
    <ul>
      <li>Performance, Development Effort</li>
    </ul>
  </Notes>
</Slide>

<Slide transition="zoom-in slide-out">
  <SlideTitle title="Evaluation" />

  <section use:subtitle={"Pageload Speed"}>
    <div class="flex justify-center">
      <img class="h-[420px]" src={benchmarkResults} alt="" />
    </div>

    <Notes>
      <ul>
        <li>Expected Results</li>
        <li>TTFB, FCP, LCP, Nav</li>
        <li>TTFB: expected</li>
        <li>FCP: SK-SPA is weird</li>
        <li>LCP: SK Better</li>
        <li>Nav: SK Better</li>
      </ul>
    </Notes>
  </section>

  <!-- <section use:subtitle={"JS web frameworks Benchmark"}>
    <div class="flex justify-center">
      <img class="ml-40 h-[620px]" src={jsBenchmark} alt="" />
    </div>
  </section> -->

  <section use:subtitle={"Development Comparison"}>
    <h3>Development Comparison</h3>
    <div class="flex justify-center items-center gap-12">
      <img class="h-40" src={svelteLogo} alt="" />
      <h2>VS.</h2>
      <img class="h-40" src={ui5Logo} alt="" />
    </div>

    <Notes>
      <ul>
        <li>had to develop UI Component library</li>
        <li>easier to grasp than react</li>
      </ul>
    </Notes>
  </section>

  <!-- <section use:subtitle={"Development Comparison"}>
    <div class="grid grid-cols-2">
      <div>
        <Code lineNumbers trim noescape class="text-sm">
          {`<script>
  export let text;

  function onShowAlert() {
    alert(text);
  }
${"<"}/script>

<button on:click={onShowAlert}>Show Alert</button>
`}
        </Code>
      </div>
      <div>
        <Code lineNumbers trim noescape class="text-sm">
          {`<core:FragmentDefinition 
    xmlns="sap.m" 
    xmlns:core="sap.ui.core" 
    xmlns:layout="sap.ui.layout">
  <Button text="Show Alert" press="onShowAlert" />
</core:FragmentDefinition>
`}
        </Code>

        <Code lineNumbers trim noescape class="text-sm">
          {`sap.ui.define(
  ['sap/ui/core/XMLComposite'], 
  (XMLComposite) => {
  "use strict";

  return XMLComposite.extend("ui5.example.control.AlertButton", {
    metadata: {
      properties: { text: {type : "string" } }
    },

    onShowAlert() {
      alert(this.getText());
    },
  });
});
`}
        </Code>
      </div>
    </div>

    <Notes>
      <ul>
        <li>Svelte smaller</li>
        <li>But UI5 implementation better</li>
      </ul>
    </Notes>
  </section> -->

  <!-- <section use:subtitle={"UI Components"}>
    <div class="grid grid-cols-2">
      <img class="h-[420px]" src={currentAuftragDetails} alt="" />

      <div class="flex flex-col items-center justify-around">
        <div class="relative">
          <img class="fragment h-32" src={ui5Logo} alt="" />
        </div>

        <img
          class="fragment"
          src="https://media.tenor.com/vCqpL7x4sPUAAAAC/thanos-fine-ill-do-it-myself.gif"
          alt=""
        />
      </div>
    </div>
  </section> -->

  <section use:subtitle={"Findings"}>
    <h3>Findings</h3>

    <ul>
      <li class="fragment">Good for custom UI components</li>
      <li class="fragment">Immature ecosystem</li>
      <li class="fragment">Fast moving</li>
    </ul>

    <Notes>
      <ul>
        <li>Close to Webstandards</li>
        <li>SvelteKit very young</li>
        <li>Authentication</li>
      </ul>
    </Notes>
  </section>

  <!-- <section use:subtitle={"Future of Svelte"}>
    <h3>Future of Svelte</h3>
    <ul>
      <li>Large Community</li>
      <li>may require Migrations sometimes</li>
    </ul>
    <div class="text-orange-500">Mockup Slide</div>
  </section> -->

  <section use:subtitle={"Runes"}>
    <div class="relative h-[720px]">
      <img class="absolute h-[500px] mt-32 ml-12" src={svelteRunes} alt="" />

      <div class="absolute right-14 bottom-14 w-[650px]">
        <Code id="code" class="hljs svelte" trim noescape lineNumbers>
          {`<script>
  let count = $state(0);

  const doubled = $derived(count * 2);
${"<"}/script>

<div>{count}</div>
`}
        </Code>
      </div>
    </div>
  </section>
</Slide>

<style>
  #cross {
    width: 100px;
    height: 100px;
    position: relative;
    transform: rotate(45deg);
    -ms-transform: rotate(45deg); /* IE 9 */
    -webkit-transform: rotate(45deg); /* Safari and Chrome */
  }

  #cross:before,
  #cross:after {
    content: "";
    position: absolute;
    z-index: -1;
    background: #d00;
  }

  #cross:before {
    left: 50%;
    width: 30%;
    margin-left: -15%;
    height: 100%;
  }

  #cross:after {
    top: 50%;
    height: 30%;
    margin-top: -15%;
    width: 100%;
  }
</style>
