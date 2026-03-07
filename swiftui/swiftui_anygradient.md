# AnyGradient

A color gradient.

```swift
@frozen struct AnyGradient
```

## Overview

When used as a [ShapeStyle](/documentation/swiftui/shapestyle), this type draws a linear gradient with start-point [0.5, 0] and end-point [0.5, 1].

### Creating a gradient

- [init(_:)](/documentation/swiftui/anygradient/init(_:)): Creates a new instance from the specified gradient.

### Working with color spaces

- [colorSpace(_:)](/documentation/swiftui/anygradient/colorspace(_:)): Returns a version of the gradient that will use a specified color space for interpolating between its colors.

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
- [Gradient](/documentation/swiftui/gradient): A color gradient represented as an array of color stops, each having a parametric location value.
- [MeshGradient](/documentation/swiftui/meshgradient): A two-dimensional gradient defined by a 2D grid of positioned colors.
- [ShadowStyle](/documentation/swiftui/shadowstyle): A style to use when rendering shadows.
- [Glass](/documentation/swiftui/glass): A structure that defines the configuration of the Liquid Glass material.
