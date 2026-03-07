# ScrollTransitionConfiguration

The configuration of a scroll transition that controls how a transition is applied as a view is scrolled through the visible region of a containing scroll view or other container.

```swift
struct ScrollTransitionConfiguration
```

### Getting the configuration

- [identity](/documentation/swiftui/scrolltransitionconfiguration/identity): Creates a new configuration that does not change the appearance of the view.
- [animated](/documentation/swiftui/scrolltransitionconfiguration/animated): Creates a new configuration that discretely animates the transition when the view becomes visible.
- [animated(_:)](/documentation/swiftui/scrolltransitionconfiguration/animated(_:)): Creates a new configuration that discretely animates the transition when the view becomes visible.
- [interactive](/documentation/swiftui/scrolltransitionconfiguration/interactive): Creates a new configuration that interactively interpolates the transition’s effect as the view is scrolled into the visible region of the container.
- [interactive(timingCurve:)](/documentation/swiftui/scrolltransitionconfiguration/interactive(timingcurve:)): Creates a new configuration that interactively interpolates the transition’s effect as the view is scrolled into the visible region of the container.

### Accessing the configuration

- [animation(_:)](/documentation/swiftui/scrolltransitionconfiguration/animation(_:)): Sets the animation with which the transition will be applied.
- [threshold(_:)](/documentation/swiftui/scrolltransitionconfiguration/threshold(_:)): Sets the threshold at which the view will be considered fully visible.
- [ScrollTransitionConfiguration.Threshold](/documentation/swiftui/scrolltransitionconfiguration/threshold): Describes a specific point in the progression of a target view within a container from hidden (fully outside the container) to visible.

## See Also

### Animating scroll transitions

- [scrollTransition(_:axis:transition:)](/documentation/swiftui/view/scrolltransition(_:axis:transition:)): Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [scrollTransition(topLeading:bottomTrailing:axis:transition:)](/documentation/swiftui/view/scrolltransition(topleading:bottomtrailing:axis:transition:)): Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [ScrollTransitionPhase](/documentation/swiftui/scrolltransitionphase): The phases that a view transitions between when it scrolls among other views.
