# Anchor

An opaque value derived from an anchor source and a particular view.

```swift
@frozen struct Anchor<Value>
```

## Overview

You can convert the anchor to a `Value` in the coordinate space of a target view by using a [GeometryProxy](/documentation/swiftui/geometryproxy) to specify the target view.

### Getting the anchor’s source

- [Anchor.Source](/documentation/swiftui/anchor/source): A type-erased geometry value that produces an anchored value of a given type.

## See Also

### Accessing geometric constructs

- [Axis](/documentation/swiftui/axis): The horizontal or vertical dimension in a 2D coordinate system.
- [Angle](/documentation/swiftui/angle): A geometric angle whose value you access in either radians or degrees.
- [UnitPoint](/documentation/swiftui/unitpoint): A normalized 2D point in a view’s coordinate space.
- [UnitPoint3D](/documentation/swiftui/unitpoint3d): A normalized 3D point in a view’s coordinate space.
- [DepthAlignmentID](/documentation/swiftui/depthalignmentid)
- [Alignment3D](/documentation/swiftui/alignment3d): An alignment in all three axes.
- [GeometryProxyCoordinateSpace3D](/documentation/swiftui/geometryproxycoordinatespace3d): A representation of a `GeometryProxy3D` which can be used for `CoordinateSpace3D` based conversions.
