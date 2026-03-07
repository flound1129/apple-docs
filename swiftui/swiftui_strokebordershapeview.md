# StrokeBorderShapeView

A shape provider that strokes the border of its shape.

```swift
@frozen struct StrokeBorderShapeView<Content, Style, Background> where Content : InsettableShape, Style : ShapeStyle, Background : View
```

## Overview

You don’t create this type directly; it’s the return type of `Shape.strokeBorder`.

### Creating a stroke border shape view

- [init(shape:style:strokeStyle:isAntialiased:background:)](/documentation/swiftui/strokebordershapeview/init(shape:style:strokestyle:isantialiased:background:)): Create a stroke border shape.

### Getting shape view properties

- [background](/documentation/swiftui/strokebordershapeview/background): The background shown beneath this view.
- [isAntialiased](/documentation/swiftui/strokebordershapeview/isantialiased): Whether this shape should be drawn antialiased.
- [shape](/documentation/swiftui/strokebordershapeview/shape): The shape that this type draws and provides for other drawing operations.
- [strokeStyle](/documentation/swiftui/strokebordershapeview/strokestyle): The stroke style used when stroking this view’s shape.
- [style](/documentation/swiftui/strokebordershapeview/style): The style that strokes the border of this view’s shape.

## See Also

### Defining shape behavior

- [ShapeView](/documentation/swiftui/shapeview): A view that provides a shape that you can use for drawing operations.
- [Shape](/documentation/swiftui/shape): A 2D shape that you can use when drawing a view.
- [AnyShape](/documentation/swiftui/anyshape): A type-erased shape value.
- [ShapeRole](/documentation/swiftui/shaperole): Ways of styling a shape.
- [StrokeStyle](/documentation/swiftui/strokestyle): The characteristics of a stroke that traces a path.
- [StrokeShapeView](/documentation/swiftui/strokeshapeview): A shape provider that strokes its shape.
- [FillStyle](/documentation/swiftui/fillstyle): A style for rasterizing vector shapes.
- [FillShapeView](/documentation/swiftui/fillshapeview): A shape provider that fills its shape.
