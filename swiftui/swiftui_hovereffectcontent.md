# HoverEffectContent

A type that describes the effects of a view for a particular hover effect phase.

```swift
protocol HoverEffectContent
```

## Overview

```swift
Color.red
    .hoverEffect { effect, isActive, proxy in
        effect.opacity(isActive ? 1 : 0.5)
    }
```

You don’t conform to this protocol yourself. Instead, effects are described by calling modifier functions on other effects, like the `opacity(_:)` modifier used in the example above.

### Instance Methods

- [animation(_:body:)](/documentation/swiftui/hovereffectcontent/animation(_:body:)): Applies the given [Animation](/documentation/swiftui/animation) to all effects within the `body` closure.
- [clipShape(_:style:)](/documentation/swiftui/hovereffectcontent/clipshape(_:style:)): Sets a clipping shape for the view.
- [offset(_:)](/documentation/swiftui/hovereffectcontent/offset(_:)): Offsets the view by the horizontal and vertical amount specified in the offset parameter.
- [offset(x:y:)](/documentation/swiftui/hovereffectcontent/offset(x:y:)): Offsets the view by the specified horizontal and vertical distances.
- [opacity(_:)](/documentation/swiftui/hovereffectcontent/opacity(_:)): Sets the transparency of the view.
- [rotationEffect(_:anchor:)](/documentation/swiftui/hovereffectcontent/rotationeffect(_:anchor:)): Rotates content in two dimensions around the specified point.
- [scaleEffect(_:anchor:)](/documentation/swiftui/hovereffectcontent/scaleeffect(_:anchor:)): Scales the view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.
- [scaleEffect(x:y:anchor:)](/documentation/swiftui/hovereffectcontent/scaleeffect(x:y:anchor:)): Scales the view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [transformEffect(_:)](/documentation/swiftui/hovereffectcontent/transformeffect(_:)): Applies an affine transformation to the view’s rendered output.

## See Also

### Changing view appearance for hover events

- [hoverEffect(_:)](/documentation/swiftui/view/hovereffect(_:)): Applies a hover effect to this view.
- [HoverEffect](/documentation/swiftui/hovereffect): An effect applied when the pointer hovers over a view.
- [hoverEffect(_:in:isEnabled:)](/documentation/swiftui/view/hovereffect(_:in:isenabled:)): Applies a hover effect to this view, optionally adding it to a [HoverEffectGroup](/documentation/swiftui/hovereffectgroup).
- [hoverEffect(in:isEnabled:body:)](/documentation/swiftui/view/hovereffect(in:isenabled:body:)): Applies a hover effect to this view described by the given closure.
- [CustomHoverEffect](/documentation/swiftui/customhovereffect): A type that represents how a view should change when a pointer hovers over a view, or when someone looks at the view.
- [ContentHoverEffect](/documentation/swiftui/contenthovereffect): A `CustomHoverEffect` that applies effects to a view on hover using a closure.
- [HoverEffectGroup](/documentation/swiftui/hovereffectgroup): Describes a grouping of effects that activate together.
- [hoverEffectGroup()](/documentation/swiftui/view/hovereffectgroup()): Adds an implicit [HoverEffectGroup](/documentation/swiftui/hovereffectgroup) to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.
- [hoverEffectGroup(_:)](/documentation/swiftui/view/hovereffectgroup(_:)): Adds a [HoverEffectGroup](/documentation/swiftui/hovereffectgroup) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [hoverEffectGroup(id:in:behavior:)](/documentation/swiftui/view/hovereffectgroup(id:in:behavior:)): Adds a [HoverEffectGroup](/documentation/swiftui/hovereffectgroup) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [GroupHoverEffect](/documentation/swiftui/grouphovereffect): A `CustomHoverEffect` that activates a named group of effects.
- [EmptyHoverEffectContent](/documentation/swiftui/emptyhovereffectcontent): An empty base effect that you use to build other effects.
- [handPointerBehavior(_:)](/documentation/swiftui/view/handpointerbehavior(_:)): Sets the behavior of the hand pointer while the user is interacting with the view.
- [HandPointerBehavior](/documentation/swiftui/handpointerbehavior): A behavior that can be applied to the hand pointer while the user is interacting with a view.
