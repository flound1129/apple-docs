# BlendMode

Modes for compositing a view with overlapping content.

```swift
enum BlendMode
```

### Getting the default

- [BlendMode.normal](/documentation/swiftui/blendmode/normal)

### Darkening

- [BlendMode.darken](/documentation/swiftui/blendmode/darken)
- [BlendMode.multiply](/documentation/swiftui/blendmode/multiply)
- [BlendMode.colorBurn](/documentation/swiftui/blendmode/colorburn)
- [BlendMode.plusDarker](/documentation/swiftui/blendmode/plusdarker)

### Lightening

- [BlendMode.lighten](/documentation/swiftui/blendmode/lighten)
- [BlendMode.screen](/documentation/swiftui/blendmode/screen)
- [BlendMode.colorDodge](/documentation/swiftui/blendmode/colordodge)
- [BlendMode.plusLighter](/documentation/swiftui/blendmode/pluslighter)

### Adding contrast

- [BlendMode.overlay](/documentation/swiftui/blendmode/overlay)
- [BlendMode.softLight](/documentation/swiftui/blendmode/softlight)
- [BlendMode.hardLight](/documentation/swiftui/blendmode/hardlight)

### Inverting

- [BlendMode.difference](/documentation/swiftui/blendmode/difference)
- [BlendMode.exclusion](/documentation/swiftui/blendmode/exclusion)

### Mixing color components

- [BlendMode.hue](/documentation/swiftui/blendmode/hue)
- [BlendMode.saturation](/documentation/swiftui/blendmode/saturation)
- [BlendMode.color](/documentation/swiftui/blendmode/color)
- [BlendMode.luminosity](/documentation/swiftui/blendmode/luminosity)

### Accessing porter-duff modes

- [BlendMode.sourceAtop](/documentation/swiftui/blendmode/sourceatop)
- [BlendMode.destinationOver](/documentation/swiftui/blendmode/destinationover)
- [BlendMode.destinationOut](/documentation/swiftui/blendmode/destinationout)

## See Also

### Compositing views

- [blendMode(_:)](/documentation/swiftui/view/blendmode(_:)): Sets the blend mode for compositing this view with overlapping views.
- [compositingGroup()](/documentation/swiftui/view/compositinggroup()): Wraps this view in a compositing group.
- [drawingGroup(opaque:colorMode:)](/documentation/swiftui/view/drawinggroup(opaque:colormode:)): Composites this view’s contents into an offscreen image before final display.
- [ColorRenderingMode](/documentation/swiftui/colorrenderingmode): The set of possible working color spaces for color-compositing operations.
- [CompositorContent](/documentation/swiftui/compositorcontent)
- [CompositorContentBuilder](/documentation/swiftui/compositorcontentbuilder): A result builder for composing a collection of [CompositorContent](/documentation/swiftui/compositorcontent) elements.
- [AnyCompositorContent](/documentation/swiftui/anycompositorcontent): Type erased compositor content.
