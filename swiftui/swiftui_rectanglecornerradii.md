# RectangleCornerRadii

Describes the corner radius values of a rounded rectangle with uneven corners.

```swift
@frozen struct RectangleCornerRadii
```

### Creating a set of radii

- [init(topLeading:bottomLeading:bottomTrailing:topTrailing:)](/documentation/swiftui/rectanglecornerradii/init(topleading:bottomleading:bottomtrailing:toptrailing:)): Creates a new set of corner radii for a rounded rectangle with uneven corners.

### Getting values for specific corners

- [topLeading](/documentation/swiftui/rectanglecornerradii/topleading): The radius of the top-leading corner.
- [topTrailing](/documentation/swiftui/rectanglecornerradii/toptrailing): The radius of the top-trailing corner.
- [bottomLeading](/documentation/swiftui/rectanglecornerradii/bottomleading): The radius of the bottom-leading corner.
- [bottomTrailing](/documentation/swiftui/rectanglecornerradii/bottomtrailing): The radius of the bottom-trailing corner.

### Subscripts

- [subscript(_:)](/documentation/swiftui/rectanglecornerradii/subscript(_:)): Returns the corner radius for a certain corner.

## See Also

### Creating rectangular shapes

- [Rectangle](/documentation/swiftui/rectangle): A rectangular shape aligned inside the frame of the view containing it.
- [RoundedRectangle](/documentation/swiftui/roundedrectangle): A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [RoundedCornerStyle](/documentation/swiftui/roundedcornerstyle): Defines the shape of a rounded rectangle’s corners.
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape): A protocol of [InsettableShape](/documentation/swiftui/insettableshape) that describes a rounded rectangular shape.
- [RoundedRectangularShapeCorners](/documentation/swiftui/roundedrectangularshapecorners): A type describing the corner styles of a [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape).
- [UnevenRoundedRectangle](/documentation/swiftui/unevenroundedrectangle): A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [RectangleCornerInsets](/documentation/swiftui/rectanglecornerinsets): The inset sizes for the corners of a rectangle.
- [ConcentricRectangle](/documentation/swiftui/concentricrectangle): A shape that is replaced by a concentric version of the current container shape. If the container shape is a rectangle derived shape with four corners, this shape could choose to respect corners individually.
