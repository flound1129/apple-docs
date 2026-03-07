# AnyCompositorContent

Type erased compositor content.

```swift
struct AnyCompositorContent
```

### Initializers

- [init(_:)](/documentation/swiftui/anycompositorcontent/init(_:)): Create an instance that type-erases `CompositorContent`.
- [init(erasing:)](/documentation/swiftui/anycompositorcontent/init(erasing:))

## See Also

### Compositing views

- [blendMode(_:)](/documentation/swiftui/view/blendmode(_:)): Sets the blend mode for compositing this view with overlapping views.
- [compositingGroup()](/documentation/swiftui/view/compositinggroup()): Wraps this view in a compositing group.
- [drawingGroup(opaque:colorMode:)](/documentation/swiftui/view/drawinggroup(opaque:colormode:)): Composites this view’s contents into an offscreen image before final display.
- [BlendMode](/documentation/swiftui/blendmode): Modes for compositing a view with overlapping content.
- [ColorRenderingMode](/documentation/swiftui/colorrenderingmode): The set of possible working color spaces for color-compositing operations.
- [CompositorContent](/documentation/swiftui/compositorcontent)
- [CompositorContentBuilder](/documentation/swiftui/compositorcontentbuilder): A result builder for composing a collection of [CompositorContent](/documentation/swiftui/compositorcontent) elements.
