# GlassBackgroundDisplayMode

The display mode of a glass background.

```swift
enum GlassBackgroundDisplayMode
```

## Overview

Use a value of this type to indicate when to display a glass background that you add to a view using a view modifier like [glassBackgroundEffect(displayMode:)](/documentation/swiftui/view/glassbackgroundeffect(displaymode:)).

### Getting the mode

- [GlassBackgroundDisplayMode.always](/documentation/swiftui/glassbackgrounddisplaymode/always): Always display the glass material.
- [GlassBackgroundDisplayMode.implicit](/documentation/swiftui/glassbackgrounddisplaymode/implicit): Display the glass material only when the view isn’t already contained in glass.
- [GlassBackgroundDisplayMode.never](/documentation/swiftui/glassbackgrounddisplaymode/never): Never display the glass material.

## See Also

### Adding a glass background on views in visionOS

- [glassBackgroundEffect(displayMode:)](/documentation/swiftui/view/glassbackgroundeffect(displaymode:)): Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [glassBackgroundEffect(in:displayMode:)](/documentation/swiftui/view/glassbackgroundeffect(in:displaymode:)): Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [GlassBackgroundEffect](/documentation/swiftui/glassbackgroundeffect): A specification for the appearance of a glass background.
- [AutomaticGlassBackgroundEffect](/documentation/swiftui/automaticglassbackgroundeffect): The automatic glass background effect.
- [GlassBackgroundEffectConfiguration](/documentation/swiftui/glassbackgroundeffectconfiguration): A configuration used to build a custom effect.
- [FeatheredGlassBackgroundEffect](/documentation/swiftui/featheredglassbackgroundeffect)
- [PlateGlassBackgroundEffect](/documentation/swiftui/plateglassbackgroundeffect): The plate glass background effect.
