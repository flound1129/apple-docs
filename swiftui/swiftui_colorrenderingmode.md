# ColorRenderingMode

The set of possible working color spaces for color-compositing operations.

```swift
enum ColorRenderingMode
```

## Overview

Each color space guarantees the preservation of a particular range of color values.

### Getting rendering modes

- [ColorRenderingMode.extendedLinear](/documentation/swiftui/colorrenderingmode/extendedlinear): The extended linear sRGB working color space.
- [ColorRenderingMode.linear](/documentation/swiftui/colorrenderingmode/linear): The linear sRGB working color space.
- [ColorRenderingMode.nonLinear](/documentation/swiftui/colorrenderingmode/nonlinear): The non-linear sRGB working color space.

## See Also

### Compositing views

- [blendMode(_:)](/documentation/swiftui/view/blendmode(_:)): Sets the blend mode for compositing this view with overlapping views.
- [compositingGroup()](/documentation/swiftui/view/compositinggroup()): Wraps this view in a compositing group.
- [drawingGroup(opaque:colorMode:)](/documentation/swiftui/view/drawinggroup(opaque:colormode:)): Composites this view’s contents into an offscreen image before final display.
- [BlendMode](/documentation/swiftui/blendmode): Modes for compositing a view with overlapping content.
- [CompositorContent](/documentation/swiftui/compositorcontent)
- [CompositorContentBuilder](/documentation/swiftui/compositorcontentbuilder): A result builder for composing a collection of [CompositorContent](/documentation/swiftui/compositorcontent) elements.
- [AnyCompositorContent](/documentation/swiftui/anycompositorcontent): Type erased compositor content.
