# CustomHoverEffect

A type that represents how a view should change when a pointer hovers over a view, or when someone looks at the view.

```swift
protocol CustomHoverEffect
```

## Overview

Custom hover effects apply their inactive values when the effect is inactive, and their active values when the effect is active. For example, the following effect causes a view to be partially transparent when inactive, but animate to fully opaque when active:

```swift
struct FadeInHoverEffect: CustomHoverEffect {
    func body(content: Content) -> some CustomHoverEffect {
        content.hoverEffect { effect, isActive, proxy in
            effect.animation(.easeOut) {
                $0.opacity(isActive ? 1 : 0.5)
            }
        }
    }
}
```

This effect can be applied to a view using the `hoverEffect(_:)` modifier:

```swift
Color.red
    .hoverEffect(FadeInHoverEffect())
```

Hover effects do not affect a view’s layout, and may be applied to a view out-of-process. Therefore an effect’s current phase may not be visible within your app.

### Getting built-in hover effects

- [automatic](/documentation/swiftui/customhovereffect/automatic): The default hover effect based on the surrounding context.
- [empty](/documentation/swiftui/customhovereffect/empty): An effect that applies no changes when hovered.
- [highlight](/documentation/swiftui/customhovereffect/highlight): A hover effect that highlights views using a light source to indicate position.
- [lift](/documentation/swiftui/customhovereffect/lift): A hover effect that slides the pointer under the view and disappears as the view scales up and gains a shadow.

### Creating custom hover effects

- [hoverEffect(_:in:isEnabled:)](/documentation/swiftui/customhovereffect/hovereffect(_:in:isenabled:)): Applies this effect in parallel with the given `effect`.
- [hoverEffect(in:isEnabled:body:)](/documentation/swiftui/customhovereffect/hovereffect(in:isenabled:body:)-swift.method): Applies a hover effect based on the current phase.
- [hoverEffectGroup(_:)](/documentation/swiftui/customhovereffect/hovereffectgroup(_:)-swift.method): Activates this effect as part of an effect group.
- [hoverEffectGroup(id:in:behavior:)](/documentation/swiftui/customhovereffect/hovereffectgroup(id:in:behavior:)-swift.method): Activates this effect as part of an effect group.
- [hoverEffectDisabled(_:)](/documentation/swiftui/customhovereffect/hovereffectdisabled(_:)): Disables this hover effect.

### Supporting types

- [AutomaticHoverEffect](/documentation/swiftui/automatichovereffect): The default hover effect based on the surrounding context.
- [EmptyHoverEffect](/documentation/swiftui/emptyhovereffect): A base hover effect used to build additional effects.
- [HighlightHoverEffect](/documentation/swiftui/highlighthovereffect): A hover effect that highlights views using a light source to indicate position.
- [LiftHoverEffect](/documentation/swiftui/lifthovereffect): A hover effect that slides the pointer under the view and disappears as the view scales up and gains a shadow.

### Associated Types

- [Body](/documentation/swiftui/customhovereffect/body): The type of effect representing the body of this effect. When you create a custom effect, Swift infers this type from your implementation of the required [body(content:)](/documentation/swiftui/customhovereffect/body(content:)) method.

### Instance Methods

- [body(content:)](/documentation/swiftui/customhovereffect/body(content:)): Defines the effect produced by this effect.
- [hoverEffectPhaseOverride(_:)](/documentation/swiftui/customhovereffect/hovereffectphaseoverride(_:)): Returns a new effect with the given `HoverEffectPhaseOverride` applied to this effect.

### Type Aliases

- [CustomHoverEffect.Content](/documentation/swiftui/customhovereffect/content): The content effect type passed to `body(content:)`.

### Type Methods

- [hoverEffect(in:isEnabled:body:)](/documentation/swiftui/customhovereffect/hovereffect(in:isenabled:body:)-swift.type.method): Creates a hover effect that applies effects to a view using the given closure.
- [hoverEffectGroup(_:)](/documentation/swiftui/customhovereffect/hovereffectgroup(_:)-swift.type.method): Creates an effect that activates a named group of effects.
- [hoverEffectGroup(id:in:behavior:)](/documentation/swiftui/customhovereffect/hovereffectgroup(id:in:behavior:)-swift.type.method): Creates an effect that activates a named group of effects.
- [ornament(attachmentAnchor:contentAlignment:ornament:)](/documentation/swiftui/customhovereffect/ornament(attachmentanchor:contentalignment:ornament:)): Presents an ornament on hover.
- [ornament(attachmentAnchor:contentAlignment:ornament:effect:)](/documentation/swiftui/customhovereffect/ornament(attachmentanchor:contentalignment:ornament:effect:)): Presents an ornament on hover.

## See Also

### Changing view appearance for hover events

- [hoverEffect(_:)](/documentation/swiftui/view/hovereffect(_:)): Applies a hover effect to this view.
- [HoverEffect](/documentation/swiftui/hovereffect): An effect applied when the pointer hovers over a view.
- [hoverEffect(_:in:isEnabled:)](/documentation/swiftui/view/hovereffect(_:in:isenabled:)): Applies a hover effect to this view, optionally adding it to a [HoverEffectGroup](/documentation/swiftui/hovereffectgroup).
- [hoverEffect(in:isEnabled:body:)](/documentation/swiftui/view/hovereffect(in:isenabled:body:)): Applies a hover effect to this view described by the given closure.
- [ContentHoverEffect](/documentation/swiftui/contenthovereffect): A `CustomHoverEffect` that applies effects to a view on hover using a closure.
- [HoverEffectGroup](/documentation/swiftui/hovereffectgroup): Describes a grouping of effects that activate together.
- [hoverEffectGroup()](/documentation/swiftui/view/hovereffectgroup()): Adds an implicit [HoverEffectGroup](/documentation/swiftui/hovereffectgroup) to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.
- [hoverEffectGroup(_:)](/documentation/swiftui/view/hovereffectgroup(_:)): Adds a [HoverEffectGroup](/documentation/swiftui/hovereffectgroup) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [hoverEffectGroup(id:in:behavior:)](/documentation/swiftui/view/hovereffectgroup(id:in:behavior:)): Adds a [HoverEffectGroup](/documentation/swiftui/hovereffectgroup) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [GroupHoverEffect](/documentation/swiftui/grouphovereffect): A `CustomHoverEffect` that activates a named group of effects.
- [HoverEffectContent](/documentation/swiftui/hovereffectcontent): A type that describes the effects of a view for a particular hover effect phase.
- [EmptyHoverEffectContent](/documentation/swiftui/emptyhovereffectcontent): An empty base effect that you use to build other effects.
- [handPointerBehavior(_:)](/documentation/swiftui/view/handpointerbehavior(_:)): Sets the behavior of the hand pointer while the user is interacting with the view.
- [HandPointerBehavior](/documentation/swiftui/handpointerbehavior): A behavior that can be applied to the hand pointer while the user is interacting with a view.
