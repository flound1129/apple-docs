# ConcentricRectangle

A shape that is replaced by a concentric version of the current container shape. If the container shape is a rectangle derived shape with four corners, this shape could choose to respect corners individually.

```swift
struct ConcentricRectangle
```

## Overview

To use [ConcentricRectangle](/documentation/swiftui/concentricrectangle), first make sure the ancestor view hierarchy provides the container shape. Some container shapes are provided by platform kits, but you could provide your own by writing the [containerShape(_:)](/documentation/swiftui/view/containershape(_:)-3br47) modifier with a shape. Then, either call one of the initializers of [ConcentricRectangle](/documentation/swiftui/concentricrectangle) or use the static [Shape](/documentation/swiftui/shape) convenience to create the concentric shape.

```swift
    ZStack {
        Color.cyan
            .fill(.rect(corners: .concentric(minimum: 12), isUniform: false))
            .padding(.all, padding)
    }
    .containerShape(.rect(cornerRadius: 24))
```

The above example will generate a shape that is inset by `padding` on all sides. It will stay concentric to its container shape which has a 24 pts corner radius, so the shape will have a smaller radius with more padding. However, since here we provided a minimum value, the radius will be at least 12 pts, ensuring the shape to never have a square corner.

[ConcentricRectangle](/documentation/swiftui/concentricrectangle) also provides per-corner control with the initializers that take different styles for each corner.

```swift
ConcentricRectangle(
    topLeadingCorner: 0,
    topTrailingCorner: 28,
    bottomLeadingCorner: .concentric,
    bottomTrailingCorner: .concentric(minimum: 12)
)
```

The above example will have the top leading corner as square, the top trailing corner as constant 28 pts radius, the bottom leading as concentric to container shape, and bottom trailing as concentric with a minimum radius.

If you wish [ConcentricRectangle](/documentation/swiftui/concentricrectangle) to be symmetric on two corners, create the shape with initializers that takes an uniform corner style for any two corners on the rectangle. [ConcentricRectangle](/documentation/swiftui/concentricrectangle) will still resolves corner radius individually, but use the maximum value out of the corners as the final, shared corner radius of the uniform corners.

When the container shape provided is not a [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape) compatible shape, [ConcentricRectangle](/documentation/swiftui/concentricrectangle) will not be able to resolve corner radius based on concentricity. In those cases, it will fallback to be a [ContainerRelativeShape](/documentation/swiftui/containerrelativeshape), which is an inset version of the container shape.

> **See Also:**
> [ContainerRelativeShape](/documentation/swiftui/containerrelativeshape).
>

> **See Also:**
> `Shape/rect(corners:isUniform:))`, [rect(uniformTopCorners:uniformBottomCorners:)](/documentation/swiftui/shape/rect(uniformtopcorners:uniformbottomcorners:)), [rect(uniformLeadingCorners:uniformTrailingCorners:)](/documentation/swiftui/shape/rect(uniformleadingcorners:uniformtrailingcorners:)), [rect(uniformTopCorners:bottomLeadingCorner:bottomTrailingCorner:)](/documentation/swiftui/shape/rect(uniformtopcorners:bottomleadingcorner:bottomtrailingcorner:)), [rect(uniformBottomCorners:topLeadingCorner:topTrailingCorner:)](/documentation/swiftui/shape/rect(uniformbottomcorners:topleadingcorner:toptrailingcorner:)), [rect(uniformLeadingCorners:topTrailingCorner:bottomTrailingCorner:)](/documentation/swiftui/shape/rect(uniformleadingcorners:toptrailingcorner:bottomtrailingcorner:)), [rect(uniformTrailingCorners:topLeadingCorner:bottomLeadingCorner:)](/documentation/swiftui/shape/rect(uniformtrailingcorners:topleadingcorner:bottomleadingcorner:)).
>

### Initializers

- [init()](/documentation/swiftui/concentricrectangle/init()): Create a concentric rectangle with each corner being concentric individually to the container shape.
- [init(corners:isUniform:)](/documentation/swiftui/concentricrectangle/init(corners:isuniform:)): Create a rectangle with the same corner style set on four corners.
- [init(topLeadingCorner:topTrailingCorner:bottomLeadingCorner:bottomTrailingCorner:)](/documentation/swiftui/concentricrectangle/init(topleadingcorner:toptrailingcorner:bottomleadingcorner:bottomtrailingcorner:)): Create a rectangle with individual styles of four corners.
- [init(uniformBottomCorners:topLeadingCorner:topTrailingCorner:)](/documentation/swiftui/concentricrectangle/init(uniformbottomcorners:topleadingcorner:toptrailingcorner:)): Create a rectangle with a corner style set on the top two corners uniformly, and two other styles for the bottom two corners respectively.
- [init(uniformLeadingCorners:topTrailingCorner:bottomTrailingCorner:)](/documentation/swiftui/concentricrectangle/init(uniformleadingcorners:toptrailingcorner:bottomtrailingcorner:)): Create a rectangle with a corner style set on the leading two corners uniformly, and two other styles for the trailing two corners respectively.
- [init(uniformLeadingCorners:uniformTrailingCorners:)](/documentation/swiftui/concentricrectangle/init(uniformleadingcorners:uniformtrailingcorners:)): Create a rectangle with a corner style set on the leading two corners uniformly, and another style set on the trailing two corners uniformly.
- [init(uniformTopCorners:bottomLeadingCorner:bottomTrailingCorner:)](/documentation/swiftui/concentricrectangle/init(uniformtopcorners:bottomleadingcorner:bottomtrailingcorner:)): Create a rectangle with a corner style set on the top two corners uniformly, and two other styles for the bottom two corners respectively.
- [init(uniformTopCorners:uniformBottomCorners:)](/documentation/swiftui/concentricrectangle/init(uniformtopcorners:uniformbottomcorners:)): Create a rectangle with a corner style set on the top two corners uniformly, and another style set on the bottom two corners uniformly.
- [init(uniformTrailingCorners:topLeadingCorner:bottomLeadingCorner:)](/documentation/swiftui/concentricrectangle/init(uniformtrailingcorners:topleadingcorner:bottomleadingcorner:)): Create a rectangle with a corner style set on the trailing two corners uniformly, and two other styles for the leading two corners respectively.

## See Also

### Creating rectangular shapes

- [Rectangle](/documentation/swiftui/rectangle): A rectangular shape aligned inside the frame of the view containing it.
- [RoundedRectangle](/documentation/swiftui/roundedrectangle): A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [RoundedCornerStyle](/documentation/swiftui/roundedcornerstyle): Defines the shape of a rounded rectangle’s corners.
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape): A protocol of [InsettableShape](/documentation/swiftui/insettableshape) that describes a rounded rectangular shape.
- [RoundedRectangularShapeCorners](/documentation/swiftui/roundedrectangularshapecorners): A type describing the corner styles of a [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape).
- [UnevenRoundedRectangle](/documentation/swiftui/unevenroundedrectangle): A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [RectangleCornerRadii](/documentation/swiftui/rectanglecornerradii): Describes the corner radius values of a rounded rectangle with uneven corners.
- [RectangleCornerInsets](/documentation/swiftui/rectanglecornerinsets): The inset sizes for the corners of a rectangle.
