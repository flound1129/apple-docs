# FeatheredGlassBackgroundEffect

```swift
struct FeatheredGlassBackgroundEffect
```

### Overview

You can also use [feathered](/documentation/swiftui/glassbackgroundeffect/feathered) to construct this effect.

The layout size of a view with feathered glass background is based on the content size instead of the glass background size. When the glass background is clipped by an outer container, such as VStack or HStack, it can be resolved by increasing content size, such as content padding, or reducing the feathered glass background size with its padding parameter.

### Initializers

- [init()](/documentation/swiftui/featheredglassbackgroundeffect/init()): Creates a feathered glass background effect.
- [init(padding:softEdgeRadius:)](/documentation/swiftui/featheredglassbackgroundeffect/init(padding:softedgeradius:)): Creates a feathered glass background effect.

## See Also

### Adding a glass background on views in visionOS

- [glassBackgroundEffect(displayMode:)](/documentation/swiftui/view/glassbackgroundeffect(displaymode:)): Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [glassBackgroundEffect(in:displayMode:)](/documentation/swiftui/view/glassbackgroundeffect(in:displaymode:)): Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [GlassBackgroundDisplayMode](/documentation/swiftui/glassbackgrounddisplaymode): The display mode of a glass background.
- [GlassBackgroundEffect](/documentation/swiftui/glassbackgroundeffect): A specification for the appearance of a glass background.
- [AutomaticGlassBackgroundEffect](/documentation/swiftui/automaticglassbackgroundeffect): The automatic glass background effect.
- [GlassBackgroundEffectConfiguration](/documentation/swiftui/glassbackgroundeffectconfiguration): A configuration used to build a custom effect.
- [PlateGlassBackgroundEffect](/documentation/swiftui/plateglassbackgroundeffect): The plate glass background effect.
