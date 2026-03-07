# ShapeView

A view that provides a shape that you can use for drawing operations.

```swift
protocol ShapeView<Content> : View, _RemoveGlobalActorIsolation
```

## Overview

Use this type with the drawing methods on [Shape](/documentation/swiftui/shape) to apply multiple fills and/or strokes to a shape. For example, the following code applies a fill and stroke to a capsule shape:

```swift
Capsule()
    .fill(.yellow)
    .stroke(.blue, lineWidth: 8)
```

### Getting the shape

- [shape](/documentation/swiftui/shapeview/shape): The shape that this type draws and provides for other drawing operations.
- [Content](/documentation/swiftui/shapeview/content): The type of shape this can provide.

### Modify the shape

- [fill(_:style:)](/documentation/swiftui/shapeview/fill(_:style:)): Fills this shape with a color or gradient.
- [stroke(_:style:antialiased:)](/documentation/swiftui/shapeview/stroke(_:style:antialiased:)): Traces the outline of this shape with a color or gradient.
- [stroke(_:lineWidth:antialiased:)](/documentation/swiftui/shapeview/stroke(_:linewidth:antialiased:)): Traces the outline of this shape with a color or gradient.
- [strokeBorder(_:style:antialiased:)](/documentation/swiftui/shapeview/strokeborder(_:style:antialiased:)): Returns a view that’s the result of insetting this view by half of its style’s line width.
- [strokeBorder(_:lineWidth:antialiased:)](/documentation/swiftui/shapeview/strokeborder(_:linewidth:antialiased:)): Returns a view that’s the result of filling an inner stroke of this view with the content you supply.

## See Also

### Defining shape behavior

- [Shape](/documentation/swiftui/shape): A 2D shape that you can use when drawing a view.
- [AnyShape](/documentation/swiftui/anyshape): A type-erased shape value.
- [ShapeRole](/documentation/swiftui/shaperole): Ways of styling a shape.
- [StrokeStyle](/documentation/swiftui/strokestyle): The characteristics of a stroke that traces a path.
- [StrokeShapeView](/documentation/swiftui/strokeshapeview): A shape provider that strokes its shape.
- [StrokeBorderShapeView](/documentation/swiftui/strokebordershapeview): A shape provider that strokes the border of its shape.
- [FillStyle](/documentation/swiftui/fillstyle): A style for rasterizing vector shapes.
- [FillShapeView](/documentation/swiftui/fillshapeview): A shape provider that fills its shape.
