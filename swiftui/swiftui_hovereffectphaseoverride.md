# HoverEffectPhaseOverride

Options for overriding a hover effect’s current phase.

```swift
struct HoverEffectPhaseOverride
```

## Overview

By default hover effects transition between the active and inactive phases in response to hover events. Use `HoverEffectPhaseOverride` to cause a hover effect to transition between phases based on other criteria.

### Type Properties

- [active](/documentation/swiftui/hovereffectphaseoverride/active): Immediately transition to the active phase.
- [inactive](/documentation/swiftui/hovereffectphaseoverride/inactive): Immediately transition to the inactive phase.

### Type Methods

- [activeTemporarily(trigger:)](/documentation/swiftui/hovereffectphaseoverride/activetemporarily(trigger:)): Temporaily transitions to the active phase until all animations finish, and the transition is complete.
- [inactiveTemporarily(trigger:)](/documentation/swiftui/hovereffectphaseoverride/inactivetemporarily(trigger:)): Temporaily transitions to the inactve phase until all animations finish, and the transition is complete.
- [toggled(trigger:)](/documentation/swiftui/hovereffectphaseoverride/toggled(trigger:)): Immediately transition to the opposite of an effect’s current phase.
- [toggledTemporarily(trigger:)](/documentation/swiftui/hovereffectphaseoverride/toggledtemporarily(trigger:)): Temporaily transitions to the opposite of the effect’s current phase at the moment the override is applied.

## See Also

### Responding to hover events

- [onHover(perform:)](/documentation/swiftui/view/onhover(perform:)): Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [onContinuousHover(coordinateSpace:perform:)](/documentation/swiftui/view/oncontinuoushover(coordinatespace:perform:)): Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [hoverEffect(_:isEnabled:)](/documentation/swiftui/view/hovereffect(_:isenabled:)): Applies a hover effect to this view.
- [hoverEffectDisabled(_:)](/documentation/swiftui/view/hovereffectdisabled(_:)): Adds a condition that controls whether this view can display hover effects.
- [defaultHoverEffect(_:)](/documentation/swiftui/view/defaulthovereffect(_:)): Sets the default hover effect to use for views within this view.
- [isHoverEffectEnabled](/documentation/swiftui/environmentvalues/ishovereffectenabled): A Boolean value that indicates whether the view associated with this environment allows hover effects to be displayed.
- [HoverPhase](/documentation/swiftui/hoverphase): The current hovering state and value of the pointer.
- [OrnamentHoverContentEffect](/documentation/swiftui/ornamenthovercontenteffect): Presents an ornament on hover using a custom effect.
- [OrnamentHoverEffect](/documentation/swiftui/ornamenthovereffect): Presents an ornament on hover.
