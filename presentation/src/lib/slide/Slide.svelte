<script>
  import { setContext } from 'svelte';
  import { slideContextKey } from './subtitleAction.svelte';

  /** @type {{
   * bgColor?: string,
   * bgGradient?: string,
   * bgImage?: string,
   * bgSize?: string,
   * bgPosition?: string,
   * bgRepeat?: string,
   * bgOpacity?: string,
   * bgVideo?: string,
   * bgVideoLoop?: boolean,
   * bgVideoMuted?: boolean, 
   * bgIframe?: string,
   * bgInteractive?: boolean,
   * class?: string,
   * children?: any
   * transition?: import('./SlideTypes').TransitionDefinition,
   * type?: import('./SlideTypes').SlideType
   * }}
   */
  let {
    bgColor = undefined,
    bgGradient = undefined,
    bgImage = undefined,
    bgSize = undefined,
    bgPosition = undefined,
    bgRepeat = undefined,
    bgOpacity = undefined,
    bgVideo = undefined,
    bgVideoLoop = undefined,
    bgVideoMuted = undefined,
    bgIframe = undefined,
    bgInteractive = undefined,
    transition = undefined,
    class: clazz = "",
    children,
    type = "default",
  } = $props();

  const gradient = $derived(
    type === 'title' ? "linear-gradient(white 200px, transparent 200px), var(--svelte-gradient)"
  : type === 'hero' ? "linear-gradient(transparent 85%, white 85%), var(--svelte-gradient)"
  : bgGradient
  )


  class SlideContext {
    subtitle = $state(undefined);
  }

  setContext(slideContextKey, new SlideContext())

</script>

<section
  data-background-color={bgColor}
  data-background-gradient={gradient}
  data-background-image={bgImage}
  data-background-size={bgSize}
  data-background-position={bgPosition}
  data-background-repeat={bgRepeat}
  data-background-opacity={bgOpacity}
  data-background-video={bgVideo}
  data-background-video-loop={bgVideoLoop}
  data-background-video-muted={bgVideoMuted}
  data-background-iframe={bgIframe}
  data-background-interactive={bgInteractive}
  data-transition={transition}
  data-type={type}
  class={clazz}
>
  {@render children()}
</section>
