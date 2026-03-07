# GeometryEffect

An effect that changes the visual appearance of a view, largely without changing its ancestors or descendants.

```swift
protocol GeometryEffect : Animatable, ViewModifier, _RemoveGlobalActorIsolation where Self.Body == Never
```

## Overview

The only change the effect makes to the view’s ancestors and descendants is to change the coordinate transform to and from them.

### Applying effects

- [effectValue(size:)](/documentation/swiftui/geometryeffect/effectvalue(size:)): Returns the current value of the effect.
- [ignoredByLayout()](/documentation/swiftui/geometryeffect/ignoredbylayout()): Returns an effect that produces the same geometry transform as this effect, but only applies the transform while rendering its view.

## See Also

### Synchronizing geometries

- [matchedGeometryEffect(id:in:properties:anchor:isSource:)](/documentation/swiftui/view/matchedgeometryeffect(id:in:properties:anchor:issource:)): Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [MatchedGeometryProperties](/documentation/swiftui/matchedgeometryproperties): A set of view properties that may be synchronized between views using the `View.matchedGeometryEffect()` function.
- [Namespace](/documentation/swiftui/namespace): A dynamic property type that allows access to a namespace defined by the persistent identity of the object containing the property (e.g. a view).
- [geometryGroup()](/documentation/swiftui/view/geometrygroup()): Isolates the geometry (e.g. position and size) of the view from its parent view.
