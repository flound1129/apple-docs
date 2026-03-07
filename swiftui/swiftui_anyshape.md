# AnyShape

A type-erased shape value.

```swift
@frozen struct AnyShape
```

## Overview

You can use this type to dynamically switch between shape types:

```swift
struct MyClippedView: View {
    var isCircular: Bool

    var body: some View {
        OtherView().clipShape(isCircular ?
            AnyShape(Circle()) : AnyShape(Capsule()))
    }
}
```

### Creating a shape

- [init(_:)](/documentation/swiftui/anyshape/init(_:)): Create an any shape instance from a shape.

## See Also

### Defining shape behavior

- [ShapeView](/documentation/swiftui/shapeview): A view that provides a shape that you can use for drawing operations.
- [Shape](/documentation/swiftui/shape): A 2D shape that you can use when drawing a view.
- [ShapeRole](/documentation/swiftui/shaperole): Ways of styling a shape.
- [StrokeStyle](/documentation/swiftui/strokestyle): The characteristics of a stroke that traces a path.
- [StrokeShapeView](/documentation/swiftui/strokeshapeview): A shape provider that strokes its shape.
- [StrokeBorderShapeView](/documentation/swiftui/strokebordershapeview): A shape provider that strokes the border of its shape.
- [FillStyle](/documentation/swiftui/fillstyle): A style for rasterizing vector shapes.
- [FillShapeView](/documentation/swiftui/fillshapeview): A shape provider that fills its shape.
