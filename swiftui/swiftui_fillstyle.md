# FillStyle

A style for rasterizing vector shapes.

```swift
@frozen struct FillStyle
```

### Creating a fill style

- [init(eoFill:antialiased:)](/documentation/swiftui/fillstyle/init(eofill:antialiased:)): Creates a new fill style with the specified settings.

### Setting fill style properties

- [isEOFilled](/documentation/swiftui/fillstyle/iseofilled): A Boolean value that indicates whether to use the even-odd rule when rendering a shape.
- [isAntialiased](/documentation/swiftui/fillstyle/isantialiased): A Boolean value that indicates whether to apply antialiasing to the edges of a shape.

## See Also

### Defining shape behavior

- [ShapeView](/documentation/swiftui/shapeview): A view that provides a shape that you can use for drawing operations.
- [Shape](/documentation/swiftui/shape): A 2D shape that you can use when drawing a view.
- [AnyShape](/documentation/swiftui/anyshape): A type-erased shape value.
- [ShapeRole](/documentation/swiftui/shaperole): Ways of styling a shape.
- [StrokeStyle](/documentation/swiftui/strokestyle): The characteristics of a stroke that traces a path.
- [StrokeShapeView](/documentation/swiftui/strokeshapeview): A shape provider that strokes its shape.
- [StrokeBorderShapeView](/documentation/swiftui/strokebordershapeview): A shape provider that strokes the border of its shape.
- [FillShapeView](/documentation/swiftui/fillshapeview): A shape provider that fills its shape.
