# UnevenRoundedRectangle

A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.

```swift
@frozen struct UnevenRoundedRectangle
```

### Creating an uneven rounded rectangle

- [init(cornerRadii:style:)](/documentation/swiftui/unevenroundedrectangle/init(cornerradii:style:)): Creates a new rounded rectangle shape with uneven corners.
- [init(topLeadingRadius:bottomLeadingRadius:bottomTrailingRadius:topTrailingRadius:style:)](/documentation/swiftui/unevenroundedrectangle/init(topleadingradius:bottomleadingradius:bottomtrailingradius:toptrailingradius:style:)): Creates a new rounded rectangle shape with uneven corners.

### Getting the shape’s characteristics

- [cornerRadii](/documentation/swiftui/unevenroundedrectangle/cornerradii): The radii of each corner of the rounded rectangle.
- [style](/documentation/swiftui/unevenroundedrectangle/style): The style of corners drawn by the rounded rectangle.

### Supporting types

- [animatableData](/documentation/swiftui/unevenroundedrectangle/animatabledata): The data to animate.

## See Also

### Creating rectangular shapes

- [Rectangle](/documentation/swiftui/rectangle): A rectangular shape aligned inside the frame of the view containing it.
- [RoundedRectangle](/documentation/swiftui/roundedrectangle): A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [RoundedCornerStyle](/documentation/swiftui/roundedcornerstyle): Defines the shape of a rounded rectangle’s corners.
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape): A protocol of [InsettableShape](/documentation/swiftui/insettableshape) that describes a rounded rectangular shape.
- [RoundedRectangularShapeCorners](/documentation/swiftui/roundedrectangularshapecorners): A type describing the corner styles of a [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape).
- [RectangleCornerRadii](/documentation/swiftui/rectanglecornerradii): Describes the corner radius values of a rounded rectangle with uneven corners.
- [RectangleCornerInsets](/documentation/swiftui/rectanglecornerinsets): The inset sizes for the corners of a rectangle.
- [ConcentricRectangle](/documentation/swiftui/concentricrectangle): A shape that is replaced by a concentric version of the current container shape. If the container shape is a rectangle derived shape with four corners, this shape could choose to respect corners individually.
