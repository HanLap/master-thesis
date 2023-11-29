class SlideState {
  /** @type {import('reveal.js').Api | undefined} */
  #reveal = $state(undefined);

  config = $state({
    title: "Case-Study of SvelteKit in a Modern Business Application",
    shortTitle: "Case-Study of SvelteKit",
    presenter: "Hannah Lappe",
    date: "24.11.2023",
    confidentiality: "Masterarbeit",
  });

  /**
   * @type {number | undefined}
   */
  slideNumber = $state(undefined);

  /**
   * @type {import('./SlideTypes').SlideType}
   */
  slideType = $state("default");

  get reveal() {
    return this.#reveal;
  }

  /**
   * @param {import('reveal.js').Api} r
   */
  set reveal(r) {
    this.#reveal = r;
    if (r) {
      r.on("ready", (event) => this.#updateSlideInformation(event));
      r.on("slidechanged", (event) => this.#updateSlideInformation(event));
    }
  }

  #updateSlideInformation(event) {
    this.slideNumber = this.#reveal.getSlidePastCount() + 1;
    this.slideType = event.currentSlide.getAttribute("data-type") ?? undefined;
  }
}

export const slideState = new SlideState();
