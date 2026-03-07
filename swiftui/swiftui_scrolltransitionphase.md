# ScrollTransitionPhase

The phases that a view transitions between when it scrolls among other views.

```swift
@frozen enum ScrollTransitionPhase
```

## Overview

When a view with a scroll transition modifier applied is approaching the visible region of the containing scroll view or other container, the effect  will first be applied with the `topLeading` or `bottomTrailing` phase (depending on which edge the view is approaching), then will be moved to the `identity` phase as the view moves into the visible area. The timing and behavior that determines when a view is visible within the container is controlled by the configuration that is provided to the `scrollTransition` modifier.

In the `identity` phase, scroll transitions should generally not make any visual change to the view they are applied to, since the transition’s view modifications in the `identity` phase will be applied to the view as long as it is visible. In the `topLeading` and `bottomTrailing` phases, transitions should apply a change that will be animated to create the transition.

### Getting the phase

- [ScrollTransitionPhase.identity](/documentation/swiftui/scrolltransitionphase/identity): The scroll transition is being applied to a view that is in the visible area.
- [ScrollTransitionPhase.topLeading](/documentation/swiftui/scrolltransitionphase/topleading): The scroll transition is being applied to a view that is about to move into the visible area at the top edge of a vertical scroll view, or the leading edge of a horizont scroll view.
- [ScrollTransitionPhase.bottomTrailing](/documentation/swiftui/scrolltransitionphase/bottomtrailing): The scroll transition is being applied to a view that is about to move into the visible area at the bottom edge of a vertical scroll view, or the trailing edge of a horizontal scroll view.

### Accessing the phase state

- [isIdentity](/documentation/swiftui/scrolltransitionphase/isidentity)
- [value](/documentation/swiftui/scrolltransitionphase/value): A phase-derived value that can be used to scale or otherwise modify effects.

## See Also

### Animating scroll transitions

- [scrollTransition(_:axis:transition:)](/documentation/swiftui/view/scrolltransition(_:axis:transition:)): Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [scrollTransition(topLeading:bottomTrailing:axis:transition:)](/documentation/swiftui/view/scrolltransition(topleading:bottomtrailing:axis:transition:)): Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [ScrollTransitionConfiguration](/documentation/swiftui/scrolltransitionconfiguration): The configuration of a scroll transition that controls how a transition is applied as a view is scrolled through the visible region of a containing scroll view or other container.
