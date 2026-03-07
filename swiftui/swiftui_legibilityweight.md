# LegibilityWeight

The Accessibility Bold Text user setting options.

```swift
enum LegibilityWeight
```

## Overview

The app can’t override the user’s choice before iOS 16, tvOS 16 or watchOS 9.0.

### Getting weights

- [LegibilityWeight.regular](/documentation/swiftui/legibilityweight/regular): Use regular font weight (no Accessibility Bold).
- [LegibilityWeight.bold](/documentation/swiftui/legibilityweight/bold): Use heavier font weight (force Accessibility Bold).

### Creating a weight

- [init(_:)](/documentation/swiftui/legibilityweight/init(_:)): Creates a legibility weight from its UILegibilityWeight equivalent.

## See Also

### Improving legibility

- [accessibilityShowButtonShapes](/documentation/swiftui/environmentvalues/accessibilityshowbuttonshapes): Whether the system preference for Show Button Shapes is enabled.
- [accessibilityReduceTransparency](/documentation/swiftui/environmentvalues/accessibilityreducetransparency): Whether the system preference for Reduce Transparency is enabled.
- [legibilityWeight](/documentation/swiftui/environmentvalues/legibilityweight): The font weight to apply to text.
