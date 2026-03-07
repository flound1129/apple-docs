# MatchedGeometryProperties

A set of view properties that may be synchronized between views using the `View.matchedGeometryEffect()` function.

```swift
@frozen struct MatchedGeometryProperties
```

### Matching properties

- [frame](/documentation/swiftui/matchedgeometryproperties/frame): Both the `position` and `size` properties.
- [position](/documentation/swiftui/matchedgeometryproperties/position): The view’s position, in window coordinates.
- [size](/documentation/swiftui/matchedgeometryproperties/size): The view’s size, in local coordinates.

## See Also

### Synchronizing geometries

- [matchedGeometryEffect(id:in:properties:anchor:isSource:)](/documentation/swiftui/view/matchedgeometryeffect(id:in:properties:anchor:issource:)): Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [GeometryEffect](/documentation/swiftui/geometryeffect): An effect that changes the visual appearance of a view, largely without changing its ancestors or descendants.
- [Namespace](/documentation/swiftui/namespace): A dynamic property type that allows access to a namespace defined by the persistent identity of the object containing the property (e.g. a view).
- [geometryGroup()](/documentation/swiftui/view/geometrygroup()): Isolates the geometry (e.g. position and size) of the view from its parent view.
