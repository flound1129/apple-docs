# CompositorContent

```swift
@MainActor protocol CompositorContent
```

### Associated Types

- [Body](/documentation/swiftui/compositorcontent/body-swift.associatedtype)

### Instance Properties

- [body](/documentation/swiftui/compositorcontent/body-swift.property)

### Instance Methods

- [contentCaptureProtected(_:)](/documentation/swiftui/compositorcontent/contentcaptureprotected(_:)): Marks the view as a view that activates content protection during scene capture events, such as screenshots, screen recordings, screensharing, etc.
- [onAppear(perform:)](/documentation/swiftui/compositorcontent/onappear(perform:)): Adds an action to perform before this content appears.
- [onChange(of:initial:_:)](/documentation/swiftui/compositorcontent/onchange(of:initial:_:))
- [onDisappear(perform:)](/documentation/swiftui/compositorcontent/ondisappear(perform:)): Adds an action to perform after this content disappears.
- [onImmersionChange(initial:_:)](/documentation/swiftui/compositorcontent/onimmersionchange(initial:_:)): Performs an action when the immersion state of your app changes.
- [onWorldRecenter(action:)](/documentation/swiftui/compositorcontent/onworldrecenter(action:)): Adds an action to perform when recentering the view with the digital crown.
- [persistentSystemOverlays(_:)](/documentation/swiftui/compositorcontent/persistentsystemoverlays(_:)): Sets the preferred visibility of the non-transient system views overlaying the app.
- [preferredSurroundingsEffect(_:)](/documentation/swiftui/compositorcontent/preferredsurroundingseffect(_:)): Applies an effect to passthrough video.
- [upperLimbVisibility(_:)](/documentation/swiftui/compositorcontent/upperlimbvisibility(_:)): Sets the preferred visibility of the user’s upper limbs, while an [ImmersiveSpace](/documentation/swiftui/immersivespace) scene is presented.

## See Also

### Compositing views

- [blendMode(_:)](/documentation/swiftui/view/blendmode(_:)): Sets the blend mode for compositing this view with overlapping views.
- [compositingGroup()](/documentation/swiftui/view/compositinggroup()): Wraps this view in a compositing group.
- [drawingGroup(opaque:colorMode:)](/documentation/swiftui/view/drawinggroup(opaque:colormode:)): Composites this view’s contents into an offscreen image before final display.
- [BlendMode](/documentation/swiftui/blendmode): Modes for compositing a view with overlapping content.
- [ColorRenderingMode](/documentation/swiftui/colorrenderingmode): The set of possible working color spaces for color-compositing operations.
- [CompositorContentBuilder](/documentation/swiftui/compositorcontentbuilder): A result builder for composing a collection of [CompositorContent](/documentation/swiftui/compositorcontent) elements.
- [AnyCompositorContent](/documentation/swiftui/anycompositorcontent): Type erased compositor content.
