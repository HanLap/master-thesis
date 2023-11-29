export type SlideType = "default" | "title" | "hero";

type TransitionType = "none" | "fade" | "slide" | "convex" | "concave" | "zoom";

export type TransitionDefinition = `${TransitionType}` | `${TransitionType}-in ${TransitionType}-out`;
