# GeometryReader

A container view that defines its content as a function of its own size and coordinate space.

```swift
@frozen struct GeometryReader<Content> where Content : View
```

## Overview

This view returns a flexible preferred size to its parent layout.

### Creating a geometry reader

- [init(content:)](/documentation/swiftui/geometryreader/init(content:))
- [content](/documentation/swiftui/geometryreader/content)

## See Also

### Measuring a view

- [GeometryReader3D](/documentation/swiftui/geometryreader3d): A container view that defines its content as a function of its own size and coordinate space.
- [GeometryProxy](/documentation/swiftui/geometryproxy): A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
- [GeometryProxy3D](/documentation/swiftui/geometryproxy3d): A proxy for access to the size and coordinate space of the container view.
- [coordinateSpace(_:)](/documentation/swiftui/view/coordinatespace(_:)): Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [CoordinateSpace](/documentation/swiftui/coordinatespace): A resolved coordinate space created by the coordinate space protocol.
- [CoordinateSpaceProtocol](/documentation/swiftui/coordinatespaceprotocol): A frame of reference within the layout system.
- [PhysicalMetric](/documentation/swiftui/physicalmetric): Provides access to a value in points that corresponds to the specified physical measurement.
- [PhysicalMetricsConverter](/documentation/swiftui/physicalmetricsconverter): A physical metrics converter provides conversion between point values and their extent in 3D space, in the form of physical length measurements.
