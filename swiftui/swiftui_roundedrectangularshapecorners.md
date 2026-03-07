# RoundedRectangularShapeCorners

A type describing the corner styles of a [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape).

```swift
struct RoundedRectangularShapeCorners
```

### Initializers

- [init(all:)](/documentation/swiftui/roundedrectangularshapecorners/init(all:)): Create corner styles with all corner having the same style.
- [init(topLeading:topTrailing:bottomLeading:bottomTrailing:)](/documentation/swiftui/roundedrectangularshapecorners/init(topleading:toptrailing:bottomleading:bottomtrailing:)): Create corner styles with per-corner styles.

### Instance Properties

- [bottomLeading](/documentation/swiftui/roundedrectangularshapecorners/bottomleading): The bottom leading corner style.
- [bottomTrailing](/documentation/swiftui/roundedrectangularshapecorners/bottomtrailing): The bottom trailing corner style
- [topLeading](/documentation/swiftui/roundedrectangularshapecorners/topleading): The top leading corner style.
- [topTrailing](/documentation/swiftui/roundedrectangularshapecorners/toptrailing): The top trailing corner style.

### Subscripts

- [subscript(_:)](/documentation/swiftui/roundedrectangularshapecorners/subscript(_:)): Returns the corner style for a provided corner.

### Type Properties

- [concentric](/documentation/swiftui/roundedrectangularshapecorners/concentric): Corner styles will be concentric with its container, varying the radius as needed in all four corners.

### Type Methods

- [concentric(minimum:)](/documentation/swiftui/roundedrectangularshapecorners/concentric(minimum:)): Corner styles will be concentric with its container, varying the radius as needed in all four corners but never going below zero, or the provided minimum corner style, if provided.
- [fixed(_:)](/documentation/swiftui/roundedrectangularshapecorners/fixed(_:)): Corner styles with fixed radius in all four corners.

## See Also

### Creating rectangular shapes

- [Rectangle](/documentation/swiftui/rectangle): A rectangular shape aligned inside the frame of the view containing it.
- [RoundedRectangle](/documentation/swiftui/roundedrectangle): A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [RoundedCornerStyle](/documentation/swiftui/roundedcornerstyle): Defines the shape of a rounded rectangle’s corners.
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape): A protocol of [InsettableShape](/documentation/swiftui/insettableshape) that describes a rounded rectangular shape.
- [UnevenRoundedRectangle](/documentation/swiftui/unevenroundedrectangle): A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [RectangleCornerRadii](/documentation/swiftui/rectanglecornerradii): Describes the corner radius values of a rounded rectangle with uneven corners.
- [RectangleCornerInsets](/documentation/swiftui/rectanglecornerinsets): The inset sizes for the corners of a rectangle.
- [ConcentricRectangle](/documentation/swiftui/concentricrectangle): A shape that is replaced by a concentric version of the current container shape. If the container shape is a rectangle derived shape with four corners, this shape could choose to respect corners individually.
