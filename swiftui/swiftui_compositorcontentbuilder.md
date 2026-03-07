# CompositorContentBuilder

A result builder for composing a collection of [CompositorContent](/documentation/swiftui/compositorcontent) elements.

```swift
@resultBuilder struct CompositorContentBuilder
```

### Structures

- [CompositorContentBuilder.Content](/documentation/swiftui/compositorcontentbuilder/content): A representation of the content of a compositor content builder.

### Type Methods

- [buildBlock(_:)](/documentation/swiftui/compositorcontentbuilder/buildblock(_:))
- [buildEither(first:)](/documentation/swiftui/compositorcontentbuilder/buildeither(first:)): Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [buildEither(second:)](/documentation/swiftui/compositorcontentbuilder/buildeither(second:)): Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [buildExpression(_:)](/documentation/swiftui/compositorcontentbuilder/buildexpression(_:))
- [buildLimitedAvailability(_:)](/documentation/swiftui/compositorcontentbuilder/buildlimitedavailability(_:)): Processes scene content for a conditional compiler-control statement that performs an availability check.

## See Also

### Compositing views

- [blendMode(_:)](/documentation/swiftui/view/blendmode(_:)): Sets the blend mode for compositing this view with overlapping views.
- [compositingGroup()](/documentation/swiftui/view/compositinggroup()): Wraps this view in a compositing group.
- [drawingGroup(opaque:colorMode:)](/documentation/swiftui/view/drawinggroup(opaque:colormode:)): Composites this view’s contents into an offscreen image before final display.
- [BlendMode](/documentation/swiftui/blendmode): Modes for compositing a view with overlapping content.
- [ColorRenderingMode](/documentation/swiftui/colorrenderingmode): The set of possible working color spaces for color-compositing operations.
- [CompositorContent](/documentation/swiftui/compositorcontent)
- [AnyCompositorContent](/documentation/swiftui/anycompositorcontent): Type erased compositor content.
