# GeometryProxy3D

A proxy for access to the size and coordinate space of the container view.

```swift
struct GeometryProxy3D
```

## Overview

You can use a proxy for anchor resolution.

### Accessing geometry characteristics

- [frame(in:)](/documentation/swiftui/geometryproxy3d/frame(in:)): The container view’s bounds rectangle converted to a defined coordinate space.
- [size](/documentation/swiftui/geometryproxy3d/size): The size of the container view.
- [safeAreaInsets](/documentation/swiftui/geometryproxy3d/safeareainsets): The safe area inset of the container view.
- [subscript(_:)](/documentation/swiftui/geometryproxy3d/subscript(_:)): Resolves the value of an anchor to the container view.
- [transform(in:)](/documentation/swiftui/geometryproxy3d/transform(in:)): The container view’s 3D transform converted to a defined coordinate space.

### Instance Methods

- [coordinateSpace3D(for:)](/documentation/swiftui/geometryproxy3d/coordinatespace3d(for:)): Returns a value that can be used for `CoordinateSpace3D` based coordinate conversions.

## See Also

### Measuring a view

- [GeometryReader](/documentation/swiftui/geometryreader): A container view that defines its content as a function of its own size and coordinate space.
- [GeometryReader3D](/documentation/swiftui/geometryreader3d): A container view that defines its content as a function of its own size and coordinate space.
- [GeometryProxy](/documentation/swiftui/geometryproxy): A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
- [coordinateSpace(_:)](/documentation/swiftui/view/coordinatespace(_:)): Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [CoordinateSpace](/documentation/swiftui/coordinatespace): A resolved coordinate space created by the coordinate space protocol.
- [CoordinateSpaceProtocol](/documentation/swiftui/coordinatespaceprotocol): A frame of reference within the layout system.
- [PhysicalMetric](/documentation/swiftui/physicalmetric): Provides access to a value in points that corresponds to the specified physical measurement.
- [PhysicalMetricsConverter](/documentation/swiftui/physicalmetricsconverter): A physical metrics converter provides conversion between point values and their extent in 3D space, in the form of physical length measurements.
