# RoundedRectangularShape

A protocol of [InsettableShape](/documentation/swiftui/insettableshape) that describes a rounded rectangular shape.

```swift
protocol RoundedRectangularShape : InsettableShape
```

## Overview

Conform your [InsettableShape](/documentation/swiftui/insettableshape) type to [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape) when your shape is a rounded rectangular with four corners and you want to expose information about the corners. For example, a custom triangle [Shape](/documentation/swiftui/shape) is not fit for such conformance, while a custom rectangle [Shape](/documentation/swiftui/shape) could benefit from providing the implementation, especially when the shape is used as a container shape in [containerShape(_:)](/documentation/swiftui/view/containershape(_:)-3br47) to achieve concentricity.

System shapes like [Rectangle](/documentation/swiftui/rectangle), [RoundedRectangle](/documentation/swiftui/roundedrectangle), [UnevenRoundedRectangle](/documentation/swiftui/unevenroundedrectangle), [Capsule](/documentation/swiftui/capsule), and [Circle](/documentation/swiftui/circle) already provide default implementation for this protocol.

### Instance Methods

- [corners(in:)](/documentation/swiftui/roundedrectangularshape/corners(in:)): Resolved corners given a size. If the corner style of a shape is size-dependent, read the provided size and return values accordingly. This function could be called with a nil size when the size hasn’t been determined. In that case, return the best approximated value. For example, for a capsule shape, its corner radius is determined by the size. If size is not available, return `.fixed(.infinity)` to indicate that the corner should be as round as it could be.

### Type Aliases

- [RoundedRectangularShape.Corners](/documentation/swiftui/roundedrectangularshape/corners)

## See Also

### Creating rectangular shapes

- [Rectangle](/documentation/swiftui/rectangle): A rectangular shape aligned inside the frame of the view containing it.
- [RoundedRectangle](/documentation/swiftui/roundedrectangle): A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [RoundedCornerStyle](/documentation/swiftui/roundedcornerstyle): Defines the shape of a rounded rectangle’s corners.
- [RoundedRectangularShapeCorners](/documentation/swiftui/roundedrectangularshapecorners): A type describing the corner styles of a [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape).
- [UnevenRoundedRectangle](/documentation/swiftui/unevenroundedrectangle): A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [RectangleCornerRadii](/documentation/swiftui/rectanglecornerradii): Describes the corner radius values of a rounded rectangle with uneven corners.
- [RectangleCornerInsets](/documentation/swiftui/rectanglecornerinsets): The inset sizes for the corners of a rectangle.
- [ConcentricRectangle](/documentation/swiftui/concentricrectangle): A shape that is replaced by a concentric version of the current container shape. If the container shape is a rectangle derived shape with four corners, this shape could choose to respect corners individually.
