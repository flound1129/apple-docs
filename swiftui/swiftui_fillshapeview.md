# FillShapeView

A shape provider that fills its shape.

```swift
@frozen struct FillShapeView<Content, Style, Background> where Content : Shape, Style : ShapeStyle, Background : View
```

## Overview

You do not create this type directly, it is the return type of `Shape.fill`.

### Creating a stroke shape view

- [init(shape:style:fillStyle:background:)](/documentation/swiftui/fillshapeview/init(shape:style:fillstyle:background:)): Create a FillShapeView.

### Getting shape view properties

- [background](/documentation/swiftui/fillshapeview/background): The background shown beneath this view.
- [fillStyle](/documentation/swiftui/fillshapeview/fillstyle): The fill style used when filling this view’s shape.
- [shape](/documentation/swiftui/fillshapeview/shape): The shape that this type draws and provides for other drawing operations.
- [style](/documentation/swiftui/fillshapeview/style): The style that fills this view’s shape.

## See Also

### Defining shape behavior

- [ShapeView](/documentation/swiftui/shapeview): A view that provides a shape that you can use for drawing operations.
- [Shape](/documentation/swiftui/shape): A 2D shape that you can use when drawing a view.
- [AnyShape](/documentation/swiftui/anyshape): A type-erased shape value.
- [ShapeRole](/documentation/swiftui/shaperole): Ways of styling a shape.
- [StrokeStyle](/documentation/swiftui/strokestyle): The characteristics of a stroke that traces a path.
- [StrokeShapeView](/documentation/swiftui/strokeshapeview): A shape provider that strokes its shape.
- [StrokeBorderShapeView](/documentation/swiftui/strokebordershapeview): A shape provider that strokes the border of its shape.
- [FillStyle](/documentation/swiftui/fillstyle): A style for rasterizing vector shapes.
