# Namespace

A dynamic property type that allows access to a namespace defined by the persistent identity of the object containing the property (e.g. a view).

```swift
@frozen @propertyWrapper struct Namespace
```

### Creating a namespace

- [init()](/documentation/swiftui/namespace/init())

### Getting the namespace

- [wrappedValue](/documentation/swiftui/namespace/wrappedvalue)
- [Namespace.ID](/documentation/swiftui/namespace/id): A namespace defined by the persistent identity of an `@Namespace` dynamic property.

## See Also

### Synchronizing geometries

- [matchedGeometryEffect(id:in:properties:anchor:isSource:)](/documentation/swiftui/view/matchedgeometryeffect(id:in:properties:anchor:issource:)): Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [MatchedGeometryProperties](/documentation/swiftui/matchedgeometryproperties): A set of view properties that may be synchronized between views using the `View.matchedGeometryEffect()` function.
- [GeometryEffect](/documentation/swiftui/geometryeffect): An effect that changes the visual appearance of a view, largely without changing its ancestors or descendants.
- [geometryGroup()](/documentation/swiftui/view/geometrygroup()): Isolates the geometry (e.g. position and size) of the view from its parent view.
