<script>
  import jsBenchmark from "$assets/js-benchmark.png";
  import stateOfJS from "$assets/stateofjs2022.png";
  import { Slide, SlideTitle, subtitle } from "$lib/slide";
</script>

<Slide>
  <SlideTitle title="Related Work" />

  <section use:subtitle={"State of JS"}>
    <div class="flex flex-col items-center">
      <img
        class="h-[500px] bg-[radial-gradient(ellipse_at_center,#999_40%,transparent,transparent)]"
        src={stateOfJS}
        alt=""
      />
    </div>
  </section>

  <section use:subtitle={"JS web frameworks Benchmark"}>
    <div class="flex justify-center">
      <img class="h-[520px]" src={jsBenchmark} alt="" />
    </div>
  </section>
</Slide>
