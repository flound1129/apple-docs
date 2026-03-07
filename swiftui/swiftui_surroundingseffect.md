# SurroundingsEffect

Effects that the system can apply to passthrough video.

```swift
struct SurroundingsEffect
```

## Overview

Use one of these values with the [preferredSurroundingsEffect(_:)](/documentation/swiftui/view/preferredsurroundingseffect(_:)) view modifier to indicate what effect to apply to passthrough video when the modified view is displayed.

### Getting the effect

- [systemDark](/documentation/swiftui/surroundingseffect/systemdark): An effect that dims passthrough video.

### Type Properties

- [dark](/documentation/swiftui/surroundingseffect/dark): An effect that dims passthrough video.
- [semiDark](/documentation/swiftui/surroundingseffect/semidark): An effect that dims passthrough video less than [dark](/documentation/swiftui/surroundingseffect/dark).
- [ultraDark](/documentation/swiftui/surroundingseffect/ultradark): An effect that dims passthrough video more than [dark](/documentation/swiftui/surroundingseffect/dark)

### Type Methods

- [colorMultiply(_:)](/documentation/swiftui/surroundingseffect/colormultiply(_:)): An effect that applies a custom tint to the passthrough video by multiplying the passthrough with a [Color](/documentation/swiftui/color).
- [dim(intensity:)](/documentation/swiftui/surroundingseffect/dim(intensity:)): An effect that dims the passthrough video a custom amount.

## See Also

### Configuring passthrough

- [preferredSurroundingsEffect(_:)](/documentation/swiftui/view/preferredsurroundingseffect(_:)): Applies an effect to passthrough video.
- [BreakthroughEffect](/documentation/swiftui/breakthrougheffect)
