# CoordinateSpace

A resolved coordinate space created by the coordinate space protocol.

```swift
enum CoordinateSpace
```

## Overview

You don’t typically use `CoordinateSpace` directly. Instead, use the static properties and functions of `CoordinateSpaceProtocol` such as `.global`, `.local`, and `.named(_:)`.

### Getting coordinate spaces

- [CoordinateSpace.global](/documentation/swiftui/coordinatespace/global): The global coordinate space at the root of the view hierarchy.
- [CoordinateSpace.local](/documentation/swiftui/coordinatespace/local): The local coordinate space of the current view.
- [CoordinateSpace.named(_:)](/documentation/swiftui/coordinatespace/named(_:)): A named reference to a view’s local coordinate space.

### Testing a space

- [isGlobal](/documentation/swiftui/coordinatespace/isglobal)
- [isLocal](/documentation/swiftui/coordinatespace/islocal)

## See Also

### Measuring a view

- [GeometryReader](/documentation/swiftui/geometryreader): A container view that defines its content as a function of its own size and coordinate space.
- [GeometryReader3D](/documentation/swiftui/geometryreader3d): A container view that defines its content as a function of its own size and coordinate space.
- [GeometryProxy](/documentation/swiftui/geometryproxy): A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
- [GeometryProxy3D](/documentation/swiftui/geometryproxy3d): A proxy for access to the size and coordinate space of the container view.
- [coordinateSpace(_:)](/documentation/swiftui/view/coordinatespace(_:)): Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [CoordinateSpaceProtocol](/documentation/swiftui/coordinatespaceprotocol): A frame of reference within the layout system.
- [PhysicalMetric](/documentation/swiftui/physicalmetric): Provides access to a value in points that corresponds to the specified physical measurement.
- [PhysicalMetricsConverter](/documentation/swiftui/physicalmetricsconverter): A physical metrics converter provides conversion between point values and their extent in 3D space, in the form of physical length measurements.
