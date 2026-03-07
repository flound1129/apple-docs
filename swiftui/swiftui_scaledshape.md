# ScaledShape

A shape with a scale transform applied to it.

```swift
@frozen struct ScaledShape<Content> where Content : Shape
```

### Creating a scaled shape

- [init(shape:scale:anchor:)](/documentation/swiftui/scaledshape/init(shape:scale:anchor:))

### Getting the shape’s characteristics

- [anchor](/documentation/swiftui/scaledshape/anchor)
- [scale](/documentation/swiftui/scaledshape/scale)
- [shape](/documentation/swiftui/scaledshape/shape)

### Supporting types

- [animatableData](/documentation/swiftui/scaledshape/animatabledata): The data to animate.

## See Also

### Transforming a shape

- [RotatedShape](/documentation/swiftui/rotatedshape): A shape with a rotation transform applied to it.
- [OffsetShape](/documentation/swiftui/offsetshape): A shape with a translation offset transform applied to it.
- [TransformedShape](/documentation/swiftui/transformedshape): A shape with an affine transform applied to it.
