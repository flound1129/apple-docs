# InsettableShape

A shape type that is able to inset itself to produce another shape.

```swift
protocol InsettableShape : Shape
```

### Setting the stroke border characteristics

- [strokeBorder(_:lineWidth:antialiased:)](/documentation/swiftui/insettableshape/strokeborder(_:linewidth:antialiased:)): Returns a view that is the result of filling the `lineWidth`-sized border (aka inner stroke) of `self` with `content`. This is equivalent to insetting `self` by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the line-width.
- [strokeBorder(lineWidth:antialiased:)](/documentation/swiftui/insettableshape/strokeborder(linewidth:antialiased:)): Returns a view that is the result of filling the `lineWidth`-sized border (aka inner stroke) of `self` with the foreground color. This is equivalent to insetting `self` by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the line-width.
- [strokeBorder(_:style:antialiased:)](/documentation/swiftui/insettableshape/strokeborder(_:style:antialiased:)): Returns a view that is the result of insetting `self` by `style.lineWidth / 2`, stroking the resulting shape with `style`, and then filling with `content`.
- [strokeBorder(style:antialiased:)](/documentation/swiftui/insettableshape/strokeborder(style:antialiased:)): Returns a view that is the result of insetting `self` by `style.lineWidth / 2`, stroking the resulting shape with `style`, and then filling with the foreground color.

### Setting the inset

- [inset(by:)](/documentation/swiftui/insettableshape/inset(by:)): Returns `self` inset by `amount`.
- [InsetShape](/documentation/swiftui/insettableshape/insetshape): The type of the inset shape.

## See Also

### Setting a container shape

- [containerShape(_:)](/documentation/swiftui/view/containershape(_:)): Sets the container shape to use for any container relative shape or concentric rectangle within this view.
- [ContainerRelativeShape](/documentation/swiftui/containerrelativeshape): A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.
