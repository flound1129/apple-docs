# MeshGradient

A two-dimensional gradient defined by a 2D grid of positioned colors.

```swift
struct MeshGradient
```

## Overview

Each vertex has a position, a color and four surrounding Bezier control points (leading, top, trailing, bottom) that define the tangents connecting the vertex with its four neighboring vertices. (Vertices on the corners or edges of the mesh have less than four neighbors, they ignore their extra control points.) Control points may either be specified explicitly or implicitly.

When rendering, a tessellated sequence of Bezier patches are created, and vertex colors are interpolated across each patch, either linearly, or via another set of cubic curves derived from how the colors change between neighbors – the latter typically gives smoother color transitions.

```swift
MeshGradient(width: 3, height: 3, points: [
    .init(0, 0), .init(0.5, 0), .init(1, 0),
    .init(0, 0.5), .init(0.5, 0.5), .init(1, 0.5),
    .init(0, 1), .init(0.5, 1), .init(1, 1)
], colors: [
    .red, .purple, .indigo,
    .orange, .white, .blue,
    .yellow, .green, .mint
])
```

### Structures

- [MeshGradient.BezierPoint](/documentation/swiftui/meshgradient/bezierpoint): One location in a gradient mesh, along with the four Bezier control points surrounding it.

### Initializers

- [init(width:height:bezierPoints:colors:background:smoothsColors:colorSpace:)](/documentation/swiftui/meshgradient/init(width:height:bezierpoints:colors:background:smoothscolors:colorspace:)): Creates a new gradient mesh specified as a 2D grid of colored points, specifying the Bezier control points explicitly.
- [init(width:height:bezierPoints:resolvedColors:background:smoothsColors:colorSpace:)](/documentation/swiftui/meshgradient/init(width:height:bezierpoints:resolvedcolors:background:smoothscolors:colorspace:)): Creates a new gradient mesh specified as a 2D grid of colored points, specifying the Bezier control points explicitly, with already-resolved sRGB colors.
- [init(width:height:locations:colors:background:smoothsColors:colorSpace:)](/documentation/swiftui/meshgradient/init(width:height:locations:colors:background:smoothscolors:colorspace:)): Creates a new gradient mesh specified as a 2D grid of colored vertices.
- [init(width:height:points:colors:background:smoothsColors:colorSpace:)](/documentation/swiftui/meshgradient/init(width:height:points:colors:background:smoothscolors:colorspace:)): Creates a new gradient mesh specified as a 2D grid of colored points.
- [init(width:height:points:resolvedColors:background:smoothsColors:colorSpace:)](/documentation/swiftui/meshgradient/init(width:height:points:resolvedcolors:background:smoothscolors:colorspace:)): Creates a new gradient mesh specified as a 2D grid of colored points, with already-resolved sRGB colors.

### Instance Properties

- [background](/documentation/swiftui/meshgradient/background): The background color, this fills any points outside the defined vertex mesh.
- [colorSpace](/documentation/swiftui/meshgradient/colorspace): The color space in which to interpolate vertex colors.
- [colors](/documentation/swiftui/meshgradient/colors-swift.property): The array of colors. Must contain `width x height` elements.
- [height](/documentation/swiftui/meshgradient/height): The height of the mesh, i.e. the number of vertices per column.
- [locations](/documentation/swiftui/meshgradient/locations-swift.property): The array of locations. Must contain `width x height` elements.
- [smoothsColors](/documentation/swiftui/meshgradient/smoothscolors): Whether cubic (smooth) interpolation should be used for the colors in the mesh (rather than only for the shape of the mesh).
- [width](/documentation/swiftui/meshgradient/width): The width of the mesh, i.e. the number of vertices per row.

### Enumerations

- [MeshGradient.Colors](/documentation/swiftui/meshgradient/colors-swift.enum): An array of colors.
- [MeshGradient.Locations](/documentation/swiftui/meshgradient/locations-swift.enum): An array of 2D locations and their control points.

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
- [AnyGradient](/documentation/swiftui/anygradient): A color gradient.
- [ShadowStyle](/documentation/swiftui/shadowstyle): A style to use when rendering shadows.
- [Glass](/documentation/swiftui/glass): A structure that defines the configuration of the Liquid Glass material.
