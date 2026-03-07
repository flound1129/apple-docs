# GlassBackgroundEffect

A specification for the appearance of a glass background.

```swift
protocol GlassBackgroundEffect
```

### Associated Types

- [Body](/documentation/swiftui/glassbackgroundeffect/body): The type of effect representing the body of this effect. When you create a custom effect, Swift infers this type from your implementation of the required [makeBody(configuration:)](/documentation/swiftui/glassbackgroundeffect/makebody(configuration:)) method.

### Instance Methods

- [makeBody(configuration:)](/documentation/swiftui/glassbackgroundeffect/makebody(configuration:)): Defines the effect produced by this effect.

### Type Aliases

- [GlassBackgroundEffect.Configuration](/documentation/swiftui/glassbackgroundeffect/configuration): The configuration type passed to `makeBody(configuration:)`.

### Type Properties

- [automatic](/documentation/swiftui/glassbackgroundeffect/automatic): The default glass background effect, based on the glass’s context.
- [feathered](/documentation/swiftui/glassbackgroundeffect/feathered): A feathered background effect with default padding amount and default soft edge radial size.
- [plate](/documentation/swiftui/glassbackgroundeffect/plate): A plate glass background effect.

### Type Methods

- [feathered(padding:softEdgeRadius:)](/documentation/swiftui/glassbackgroundeffect/feathered(padding:softedgeradius:)): A feathered background effect with custom padding and soft edge radius.

## See Also

### Adding a glass background on views in visionOS

- [glassBackgroundEffect(displayMode:)](/documentation/swiftui/view/glassbackgroundeffect(displaymode:)): Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [glassBackgroundEffect(in:displayMode:)](/documentation/swiftui/view/glassbackgroundeffect(in:displaymode:)): Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [GlassBackgroundDisplayMode](/documentation/swiftui/glassbackgrounddisplaymode): The display mode of a glass background.
- [AutomaticGlassBackgroundEffect](/documentation/swiftui/automaticglassbackgroundeffect): The automatic glass background effect.
- [GlassBackgroundEffectConfiguration](/documentation/swiftui/glassbackgroundeffectconfiguration): A configuration used to build a custom effect.
- [FeatheredGlassBackgroundEffect](/documentation/swiftui/featheredglassbackgroundeffect)
- [PlateGlassBackgroundEffect](/documentation/swiftui/plateglassbackgroundeffect): The plate glass background effect.
