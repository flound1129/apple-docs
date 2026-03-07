# HoverEffectGroup

Describes a grouping of effects that activate together.

```swift
struct HoverEffectGroup
```

## Overview

Use [HoverEffectGroup](/documentation/swiftui/hovereffectgroup) to apply effects to multiple views in concert.

### Structures

- [HoverEffectGroup.Behavior](/documentation/swiftui/hovereffectgroup/behavior): Describes the behavior of an effect in a group.

### Initializers

- [init(_:behavior:)](/documentation/swiftui/hovereffectgroup/init(_:behavior:)): Creates a new [HoverEffectGroup](/documentation/swiftui/hovereffectgroup) from a `Namespace.ID`.
- [init(id:in:behavior:)](/documentation/swiftui/hovereffectgroup/init(id:in:behavior:)): Creates a new [HoverEffectGroup](/documentation/swiftui/hovereffectgroup).

### Instance Methods

- [behavior(_:)](/documentation/swiftui/hovereffectgroup/behavior(_:)): Returns a new version of `self` with the given `behavior`.

### Type Properties

- [systemOverlays](/documentation/swiftui/hovereffectgroup/systemoverlays): A `HoverEffectGroup` that becomes active when system overlays are visible.

## See Also

### Changing view appearance for hover events

- [hoverEffect(_:)](/documentation/swiftui/view/hovereffect(_:)): Applies a hover effect to this view.
- [HoverEffect](/documentation/swiftui/hovereffect): An effect applied when the pointer hovers over a view.
- [hoverEffect(_:in:isEnabled:)](/documentation/swiftui/view/hovereffect(_:in:isenabled:)): Applies a hover effect to this view, optionally adding it to a [HoverEffectGroup](/documentation/swiftui/hovereffectgroup).
- [hoverEffect(in:isEnabled:body:)](/documentation/swiftui/view/hovereffect(in:isenabled:body:)): Applies a hover effect to this view described by the given closure.
- [CustomHoverEffect](/documentation/swiftui/customhovereffect): A type that represents how a view should change when a pointer hovers over a view, or when someone looks at the view.
- [ContentHoverEffect](/documentation/swiftui/contenthovereffect): A `CustomHoverEffect` that applies effects to a view on hover using a closure.
- [hoverEffectGroup()](/documentation/swiftui/view/hovereffectgroup()): Adds an implicit [HoverEffectGroup](/documentation/swiftui/hovereffectgroup) to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.
- [hoverEffectGroup(_:)](/documentation/swiftui/view/hovereffectgroup(_:)): Adds a [HoverEffectGroup](/documentation/swiftui/hovereffectgroup) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [hoverEffectGroup(id:in:behavior:)](/documentation/swiftui/view/hovereffectgroup(id:in:behavior:)): Adds a [HoverEffectGroup](/documentation/swiftui/hovereffectgroup) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [GroupHoverEffect](/documentation/swiftui/grouphovereffect): A `CustomHoverEffect` that activates a named group of effects.
- [HoverEffectContent](/documentation/swiftui/hovereffectcontent): A type that describes the effects of a view for a particular hover effect phase.
- [EmptyHoverEffectContent](/documentation/swiftui/emptyhovereffectcontent): An empty base effect that you use to build other effects.
- [handPointerBehavior(_:)](/documentation/swiftui/view/handpointerbehavior(_:)): Sets the behavior of the hand pointer while the user is interacting with the view.
- [HandPointerBehavior](/documentation/swiftui/handpointerbehavior): A behavior that can be applied to the hand pointer while the user is interacting with a view.
