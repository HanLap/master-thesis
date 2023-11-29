<script>
  import richHarris from "$assets/rich-harris.jpg";
  import svelteLogo from "$assets/svelte-logo.svg";
  import Code from "$lib/Code.svelte";
  import Counter from "$lib/Counter.svelte";
  import Notes from "$lib/Notes.svelte";
  import { Slide, SlideTitle, subtitle } from "$lib/slide";
  import SveltekitLogo from "$lib/SveltekitLogo.svelte";
  import SvelteLogo from "$lib/SvelteLogo.svelte";

  const codeSegments = [
    `<script>
  let count = 2;
${"<"}/script>

`,
    `<div>Hello world!</div>
`,
    `<div>count: {count}!</div>
`,
    `<button on:click={() => count++}>
  click me!
</button>
`,
    `<script>
  let count = 1;

  $: doubled = count * 2;
${"<"}/script>

`,
    `<div>{count} * 2 = {doubled}</div>
`,
  ];

  let count = 1;
</script>

<Slide type="hero" transition="slide-in zoom-out">
  <div class="h-[720px] flex justify-center items-center">
    <div class="flex items-center justify-center gap-12">
      <img src={svelteLogo} alt="" />
      <SvelteLogo class="h-20" />
    </div>
  </div>

  <Notes>
    <ul>
      <li>Language to develop UIs</li>
      <li>e.g.: React, Vue</li>
    </ul>
  </Notes>
</Slide>

<Slide transition="zoom-in slide-out">
  <SlideTitle title="Svelte" />

  <section
    class="hstack flex items-start justify-center gap-12"
    use:subtitle={"What is Svelte"}
  >
    <img class="w-40 aspect-square" src={richHarris} alt="" />
    <div>
      <div class="flex gap-4 items-center">
        <img class="w-20 aspect-square" src={svelteLogo} alt="" />
        <SvelteLogo class="h-12" />
      </div>
      <ul>
        <li>Author: Rich Harris</li>
        <li>Created: 2016</li>
        <li>Compiler-based approach</li>
      </ul>
    </div>

    <Notes>
      <ul>
        <li>Alleinstellungsmerkmal Compiler</li>
        <li>hat Compile-schritt zur zwischenverarbeitung</li>
      </ul>
    </Notes>
  </section>

  <section use:subtitle={"Svelte Example"} data-auto-animate>
    <div class="grid grid-cols-2">
      <Code id="code" class="hljs svelte" trim noescape lineNumbers>
        {codeSegments[1]}
      </Code>
      <div class="flex flex-col justify-center items-center">
        <Counter step={0} />
      </div>
    </div>
  </section>

  <section use:subtitle={"Svelte Example"} data-auto-animate>
    <div class="grid grid-cols-2">
      <Code id="code" class="hljs svelte" trim noescape lineNumbers>
        {codeSegments[0] + codeSegments[1]}
      </Code>
      <div class="flex flex-col justify-center items-center">
        <Counter step={1} />
      </div>
    </div>
  </section>

  <section use:subtitle={"Svelte Example"} data-auto-animate>
    <div class="grid grid-cols-2">
      <Code id="code" class="hljs svelte" trim noescape lineNumbers="5">
        {codeSegments[0] + codeSegments[2]}
      </Code>
      <div class="flex flex-col justify-center items-center">
        <Counter step={2} />
      </div>
    </div>
  </section>

  <section use:subtitle={"Svelte Example"} data-auto-animate>
    <div class="grid grid-cols-2">
      <Code id="code" class="hljs svelte" trim noescape lineNumbers="6-8">
        {codeSegments[0] + codeSegments[2] + codeSegments[3]}
      </Code>

      <div class="flex flex-col justify-center items-center">
        <Counter step={3} />
      </div>
    </div>
  </section>

  <section use:subtitle={"Svelte Example"} data-auto-animate>
    <div class="grid grid-cols-2">
      <Code id="code" class="hljs svelte" trim noescape lineNumbers="4,11">
        {codeSegments[4] + codeSegments[2] + codeSegments[3] + codeSegments[5]}
      </Code>

      <div class="flex flex-col justify-center items-center">
        <Counter step={4} />
      </div>
    </div>
  </section>
</Slide>

<Slide type="hero" transition="slide-in zoom-out">
  <div class="h-[720px] flex justify-center items-center">
    <div class="flex items-center justify-center gap-12">
      <img src={svelteLogo} alt="" />
      <SveltekitLogo class="h-20" />
    </div>
  </div>

  <Notes>
    <ul>
      <li>Full stack framework</li>
      <li>can be used for FE and BE</li>
    </ul>
  </Notes>
</Slide>

<Slide transition="zoom-in slide-out">
  <SlideTitle title="SvelteKit" />

  <section
    class="hstack flex items-start justify-center gap-12"
    use:subtitle={"What is SvelteKit"}
  >
    <div>
      <div class="flex gap-4 items-center">
        <img class="w-20 aspect-square" src={svelteLogo} alt="" />
        <SveltekitLogo class="h-12" />
      </div>
      <ul>
        <li>Framework for Svelte</li>
        <li>Release: December 2022</li>
      </ul>
    </div>

    <Notes>
      <ul>
        <li>Fullstack Framework</li>
        <li>explain</li>
      </ul>
    </Notes>
  </section>

  <section use:subtitle={"SvelteKit Features"}>
    <h3>Key Features:</h3>
    <ul>
      <li class="fragment">Routing</li>
      <li class="fragment">Configurable Rendering</li>
      <li class="fragment">Data Preloading</li>
      <li class="fragment">Progressive Enhancement</li>
    </ul>
  </section>

  <section use:subtitle={"Rendering"}>
    <div class="grid grid-cols-3 h-[400px] gap-12">
      <div
        class="fragment flex flex-col items-start p-4 [background:var(--svelte-gradient)]"
      >
        <h4 class="text-4xl">Client Side Rendering</h4>
        <ul class="text-2xl">
          <li>App rendered in browser</li>
        </ul>
      </div>

      <div
        class="fragment flex flex-col items-start p-4 [background:var(--svelte-gradient)]"
      >
        <h4 class="text-4xl">Server Side Rendering</h4>
        <ul class="text-2xl">
          <li>Rendered on server once</li>
          <li class="mt-8">Hydration in browser</li>
          <li class="mt-8">browser takes over</li>
        </ul>
      </div>

      <div
        class="fragment flex flex-col items-start p-4 [background:var(--svelte-gradient)]"
      >
        <h4 class="text-4xl">Static Site Generation</h4>
        <ul class="text-2xl">
          <li>Rendered at build time</li>
          <li class="mt-8">Server sends rendered resources</li>
        </ul>
      </div>
    </div>

    <Notes>
      <li>SvelteKit 3 rendering modi</li>
      <li>SvelteKit can switch in one app</li>
    </Notes>
  </section>
</Slide>
