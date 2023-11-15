<script>
  import Slide from "$lib/Slide.svelte";
  import Code from "$lib/Code.svelte";
  import SvelteLogo from "$assets/svelte-logo.svg";
  import RichHarris from "$assets/rich-harris.jpg";

  const codeSegments = [
    `<script>
        let name = 'Hannah';
    ${"<"}/script>

    `,
    `<div>Hello World!</div>
    `,
    `<div>Hello {name}!</div>
    `,
  ];
</script>

<Slide>
  <section class="hstack flex align-baseline justify-center gap-12">
    <img src={SvelteLogo} alt="" />
    <h2 class="self-center">Svelte</h2>
  </section>
</Slide>

<Slide>
  <section class="hstack flex items-start justify-center gap-12">
    <img class="w-40 aspect-square" src={RichHarris} alt="" />
    <div>
      <div class="flex gap-4 items-center">
        <img class="w-20 aspect-square" src={SvelteLogo} alt="" />
        <h2>Svelte</h2>
      </div>
      <ul>
        <li>Created: 2016</li>
        <li>Compiler-base approach</li>
      </ul>
    </div>
  </section>
</Slide>

<Slide>
  <section data-auto-animate>
    <Code id="code" class="hljs svelte" trim noescape lineNumbers>
      {codeSegments[1]}
    </Code>
  </section>

  <section data-auto-animate>
    <Code id="code" class="hljs svelte" trim noescape lineNumbers>
      {codeSegments[0] + codeSegments[1]}
    </Code>
  </section>

  <section data-auto-animate>
    <Code id="code" class="hljs svelte" trim noescape lineNumbers="5">
      {codeSegments[0] + codeSegments[2]}
    </Code>
  </section>
</Slide>
