# Gradient

A color gradient represented as an array of color stops, each having a parametric location value.

```swift
@frozen struct Gradient
```

### Creating a gradient from colors

- [init(colors:)](/documentation/swiftui/gradient/init(colors:)): Creates a gradient from an array of colors.

### Creating a gradient from stops

- [init(stops:)](/documentation/swiftui/gradient/init(stops:)): Creates a gradient from an array of color stops.
- [stops](/documentation/swiftui/gradient/stops): The array of color stops.
- [Gradient.Stop](/documentation/swiftui/gradient/stop): One color stop in the gradient.

### Working with color spaces

- [colorSpace(_:)](/documentation/swiftui/gradient/colorspace(_:)): Returns a version of the gradient that will use a specified color space for interpolating between its colors.
- [Gradient.ColorSpace](/documentation/swiftui/gradient/colorspace): A method of interpolating between the colors in a gradient.

## See Also

### Styling content

- [border(_:width:)](/documentation/swiftui/view/border(_:width:)): Adds a border to this view with the specified style and width.
- [foregroundStyle(_:)](/documentation/swiftui/view/foregroundstyle(_:)): Sets a view’s foreground elements to use a given style.
- [foregroundStyle(_:_:)](/documentation/swiftui/view/foregroundstyle(_:_:)): Sets the primary and secondary levels of the foreground style in the child view.
- [foregroundStyle(_:_:_:)](/documentation/swiftui/view/foregroundstyle(_:_:_:)): Sets the primary, secondary, and tertiary levels of the foreground style.
- [backgroundStyle(_:)](/documentation/swiftui/view/backgroundstyle(_:)): Sets the specified style to render backgrounds within the view.
- [backgroundStyle](/documentation/swiftui/environmentvalues/backgroundstyle): An optional style that overrides the default system background style when set.
- [ShapeStyle](/documentation/swiftui/shapestyle): A color or pattern to use when rendering a shape.
- [AnyShapeStyle](/documentation/swiftui/anyshapestyle): A type-erased ShapeStyle value.
- [MeshGradient](/documentation/swiftui/meshgradient): A two-dimensional gradient defined by a 2D grid of positioned colors.
- [AnyGradient](/documentation/swiftui/anygradient): A color gradient.
- [ShadowStyle](/documentation/swiftui/shadowstyle): A style to use when rendering shadows.
- [Glass](/documentation/swiftui/glass): A structure that defines the configuration of the Liquid Glass material.
