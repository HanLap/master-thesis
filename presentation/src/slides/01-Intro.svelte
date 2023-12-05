<script>
  import stackoverflowSurveyLogo from "$assets/stackoverflow-survey-logo.svg?raw";
  import stateOfJS from "$assets/stateofjs2022.png";
  import feExperienceRanking from "$assets/front_end_frameworks_experience_ranking.png";
  import renderingExperienceRanking from "$assets/rendering_frameworks_experience_ranking.png";
  import stackoverflowSurvey from "$assets/stackoverflow-survery.png";
  import gatsbyLogo from "$assets/gatsby-logo.svg";
  import nextLogo from "$assets/next-logo.svg";
  import nuxtLogo from "$assets/nuxt-logo.svg";
  import svelteLogo from "$assets/svelte-logo.svg";
  import Notes from "$lib/Notes.svelte";
  import { Slide, SlideTitle, slideState, subtitle } from "$lib/slide";
  import SveltekitLogo from "$lib/SveltekitLogo.svelte";
  import StackoverflowSurveyLogo from "$lib/StackoverflowSurveyLogo.svelte";
</script>

<Slide
  type="title"
  bgSize="200px"
  bgPosition="225% 75%"
  class="h-full pt-60 pb-20"
>
  <!-- <img src={SvelteLogo} alt="" /> -->

  <div class="z-10 h-full flex flex-col items-start">
    <h3 class="">Masterarbeit</h3>
    <h5 class="text-left">
      {slideState.config.title}
    </h5>

    <div class="flex-1" />
    <small class="text-svelte-text2">{slideState.config.presenter}</small>
    <small class="text-svelte-text2">December 2023</small>
  </div>
  <!-- <div class="top-0 left-0 fixed h-full w-screen -z-10 bg-gradient-to-tr from-primary1 to-primary2"></div> -->

  <Notes>
    <ul>
      <li>talking about MA</li>

      <li>what is Svelte(Kit)</li>
      <li>Procedure</li>
      <li>Evaluation</li>
    </ul>
  </Notes>
</Slide>

<Slide>
  <SlideTitle title="Motivation" />
  
  <section class="flex justify-center">
    <div class="absolute right-0 -top-8 p-8 bg-white rounded-full drop-shadow">
      <StackoverflowSurveyLogo class="drop-shadow-2xl" />
    </div>
    <img
      class="mt-12 w-[80%] h-[550px] object-cover object-[50%_9%]"
      src={stackoverflowSurvey}
      alt=""
    />
  </section>

  <!-- <section use:subtitle={"Web Development"}>
    <div class="w-full h-[520px] flex justify-center items-center relative">
      <h2>Web Development</h2>

      <small class="fragment absolute top-14 left-14">
        Server Side Rendering
      </small>
      <small class="fragment absolute bottom-36 right-28">
        Build Optimization
      </small>
      <small class="fragment absolute top-32 left-auto ml-12">Routing</small>
      <small class="fragment absolute bottom-40 left-40">
        Offline Support
      </small>
    </div>

    <Notes>
      <ul>
        <li>Web Dev hart</li>
        <li>Many requirements</li>
        <li>server-client Communication</li>
        <li>Server Side rendering</li>
        <li>Routing</li>
        <li>Preloading</li>
        <li>etc...</li>
      </ul>
    </Notes>
  </section> -->

  <!-- <section use:subtitle={"Meta Frameworks"}>
    <div
      class="w-full h-[520px] p-12 pt-40 grid grid-cols-2 grid-rows-2 px-40 justify-center items-center gap-12"
    >
      <img class="w-96 mx-auto" src={nextLogo} alt="" />
      <img class="w-96 mx-auto" src={nuxtLogo} alt="" />
      <img class="w-96 col-span-2 mx-auto" src={gatsbyLogo} alt="" />
      <div
        class="fragment h-60 flex gap-4 items-center absolute right-1/4 my-auto -rotate-[30deg] [background:radial-gradient(white,transparent)]"
      >
        <img src={svelteLogo} alt="" />
        <SveltekitLogo class="h-20" />
      </div>
    </div>

    <Notes>
      <ul>
        <li>Meta Frameworks try to fix this</li>
        <li>Popular ones like...</li>
        <li>We look at SvelteKit</li>
      </ul>
    </Notes>
  </section> -->

  <!-- <section use:subtitle={"Framework Popularity"}>
    <div class="h-[150px] z-1 absolute left-1/3 -top-20 bg-black rounded-full px-4 overflow-hidden">
      <img class="w-[250px] h-[200px] -mt-1 object-cover object-[50%_0%]" src={stateOfJS} alt="" />
    </div>
    <div class="w-full pt-12 flex flex-col items-center">
      <img
        class="w-[60%] h-[150px] object-cover object-[50%_20%]"
        src={renderingExperienceRanking}
        alt=""
      />
      <img
        class="fragment w-[60%] h-[150px] object-cover object-[50%_17%]"
        src={feExperienceRanking}
        alt=""
      />
    </div>
  </section>

  <section use:subtitle={"Question"}>
    <h3>SvelteKit for Business Applications</h3>
    <ul>
      <li>Pros</li>
      <li>Cons</li>
    </ul>
  </section> -->
</Slide>
