# GeometryProxy

A proxy for access to the size and coordinate space (for anchor resolution) of the container view.

```swift
struct GeometryProxy
```

### Accessing geometry characteristics

- [bounds(of:)](/documentation/swiftui/geometryproxy/bounds(of:)): Returns the given coordinate space’s bounds rectangle, converted to the local coordinate space.
- [frame(in:)](/documentation/swiftui/geometryproxy/frame(in:)): Returns the container view’s bounds rectangle, converted to a defined coordinate space.
- [size](/documentation/swiftui/geometryproxy/size): The size of the container view.
- [safeAreaInsets](/documentation/swiftui/geometryproxy/safeareainsets): The safe area inset of the container view.
- [subscript(_:)](/documentation/swiftui/geometryproxy/subscript(_:)): Resolves the value of an anchor to the container view.
- [transform(in:)](/documentation/swiftui/geometryproxy/transform(in:)): The container view’s 3D transform converted to a defined coordinate space.

### Instance Properties

- [containerCornerInsets](/documentation/swiftui/geometryproxy/containercornerinsets): Returns the corner insets of the container view. Use this value to adjust the geometry of a view based on the overlapping corner insets of the container view. Corner insets may include pieces of system UI as well as the corner radii for windows and presentations.

## See Also

### Measuring a view

- [GeometryReader](/documentation/swiftui/geometryreader): A container view that defines its content as a function of its own size and coordinate space.
- [GeometryReader3D](/documentation/swiftui/geometryreader3d): A container view that defines its content as a function of its own size and coordinate space.
- [GeometryProxy3D](/documentation/swiftui/geometryproxy3d): A proxy for access to the size and coordinate space of the container view.
- [coordinateSpace(_:)](/documentation/swiftui/view/coordinatespace(_:)): Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [CoordinateSpace](/documentation/swiftui/coordinatespace): A resolved coordinate space created by the coordinate space protocol.
- [CoordinateSpaceProtocol](/documentation/swiftui/coordinatespaceprotocol): A frame of reference within the layout system.
- [PhysicalMetric](/documentation/swiftui/physicalmetric): Provides access to a value in points that corresponds to the specified physical measurement.
- [PhysicalMetricsConverter](/documentation/swiftui/physicalmetricsconverter): A physical metrics converter provides conversion between point values and their extent in 3D space, in the form of physical length measurements.
