<script>
  import Slide from "$lib/Slide.svelte";
  import stateOfJS from "$assets/stateofjs2022.png";
  import feExperienceRanking from "$assets/front_end_frameworks_experience_ranking.png";
  import renderingExperienceRanking from "$assets/rendering_frameworks_experience_ranking.png";
</script>

<Slide>
  <div class="flex flex-col items-center">
    <img
      class="bg-[radial-gradient(ellipse_at_center,#999_40%,white,white)]"
      src={stateOfJS}
      alt=""
    />
  </div>
</Slide>

<Slide>
  <div class="flex justify-center">
    <img class="w-[80%] h-[470px] object-cover object-[50%_36%]" src={feExperienceRanking} alt="" />
  </div>
</Slide>

<Slide>
  <div class="flex justify-center">
    <img class="w-[80%] h-[350px] object-cover object-[50%_36%]" src={renderingExperienceRanking} alt="" />
  </div>
</Slide>
