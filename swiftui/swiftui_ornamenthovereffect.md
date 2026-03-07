# OrnamentHoverEffect

Presents an ornament on hover.

```swift
struct OrnamentHoverEffect<OrnamentView> where OrnamentView : View
```

## Overview

You don’t use this directly. Use `CustomHoverEffect.ornament` to create ornament effects instead.

## See Also

### Responding to hover events

- [onHover(perform:)](/documentation/swiftui/view/onhover(perform:)): Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [onContinuousHover(coordinateSpace:perform:)](/documentation/swiftui/view/oncontinuoushover(coordinatespace:perform:)): Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [hoverEffect(_:isEnabled:)](/documentation/swiftui/view/hovereffect(_:isenabled:)): Applies a hover effect to this view.
- [hoverEffectDisabled(_:)](/documentation/swiftui/view/hovereffectdisabled(_:)): Adds a condition that controls whether this view can display hover effects.
- [defaultHoverEffect(_:)](/documentation/swiftui/view/defaulthovereffect(_:)): Sets the default hover effect to use for views within this view.
- [isHoverEffectEnabled](/documentation/swiftui/environmentvalues/ishovereffectenabled): A Boolean value that indicates whether the view associated with this environment allows hover effects to be displayed.
- [HoverPhase](/documentation/swiftui/hoverphase): The current hovering state and value of the pointer.
- [HoverEffectPhaseOverride](/documentation/swiftui/hovereffectphaseoverride): Options for overriding a hover effect’s current phase.
- [OrnamentHoverContentEffect](/documentation/swiftui/ornamenthovercontenteffect): Presents an ornament on hover using a custom effect.
