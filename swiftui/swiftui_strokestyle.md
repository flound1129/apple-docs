# StrokeStyle

The characteristics of a stroke that traces a path.

```swift
@frozen struct StrokeStyle
```

### Creating a stroke style

- [init(lineWidth:lineCap:lineJoin:miterLimit:dash:dashPhase:)](/documentation/swiftui/strokestyle/init(linewidth:linecap:linejoin:miterlimit:dash:dashphase:)): Creates a new stroke style from the given components.

### Setting stroke style properties

- [lineWidth](/documentation/swiftui/strokestyle/linewidth): The width of the stroked path.
- [lineCap](/documentation/swiftui/strokestyle/linecap): The endpoint style of a line.
- [lineJoin](/documentation/swiftui/strokestyle/linejoin): The join type of a line.
- [miterLimit](/documentation/swiftui/strokestyle/miterlimit): A threshold used to determine whether to use a bevel instead of a miter at a join.
- [dash](/documentation/swiftui/strokestyle/dash): The lengths of painted and unpainted segments used to make a dashed line.
- [dashPhase](/documentation/swiftui/strokestyle/dashphase): How far into the dash pattern the line starts.

## See Also

### Defining shape behavior

- [ShapeView](/documentation/swiftui/shapeview): A view that provides a shape that you can use for drawing operations.
- [Shape](/documentation/swiftui/shape): A 2D shape that you can use when drawing a view.
- [AnyShape](/documentation/swiftui/anyshape): A type-erased shape value.
- [ShapeRole](/documentation/swiftui/shaperole): Ways of styling a shape.
- [StrokeShapeView](/documentation/swiftui/strokeshapeview): A shape provider that strokes its shape.
- [StrokeBorderShapeView](/documentation/swiftui/strokebordershapeview): A shape provider that strokes the border of its shape.
- [FillStyle](/documentation/swiftui/fillstyle): A style for rasterizing vector shapes.
- [FillShapeView](/documentation/swiftui/fillshapeview): A shape provider that fills its shape.
