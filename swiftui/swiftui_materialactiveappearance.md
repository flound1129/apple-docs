# MaterialActiveAppearance

The behavior for how materials appear active and inactive.

```swift
struct MaterialActiveAppearance
```

## Overview

On macOS, materials have active and inactive appearances that can reinforce the active appearance of the window they are in:

- Materials used as a `window` container background and `bar` materials will appear inactive when their containing window is inactive.
- All other materials will always appear active by default.

An explicit active appearance can be set to override a material’s default behavior. For example, materials used as the `window` container background can be made to always appear active by setting the active appearance behavior to be always active:

```swift
Text("Hello, World!")
    .containerBackground(
        Material.regular.materialActiveAppearance(.active),
        for: .window)
```

### Type Properties

- [active](/documentation/swiftui/materialactiveappearance/active): Materials will always appear active.
- [automatic](/documentation/swiftui/materialactiveappearance/automatic): Materials will automatically appear active or inactive based on context and platform convention.
- [inactive](/documentation/swiftui/materialactiveappearance/inactive): Materials will always appear inactive.
- [matchWindow](/documentation/swiftui/materialactiveappearance/matchwindow): Materials will have an active or inactive appearance based on the active appearance of their window.

## See Also

### Transforming colors

- [brightness(_:)](/documentation/swiftui/view/brightness(_:)): Brightens this view by the specified amount.
- [contrast(_:)](/documentation/swiftui/view/contrast(_:)): Sets the contrast and separation between similar colors in this view.
- [colorInvert()](/documentation/swiftui/view/colorinvert()): Inverts the colors in this view.
- [colorMultiply(_:)](/documentation/swiftui/view/colormultiply(_:)): Adds a color multiplication effect to this view.
- [saturation(_:)](/documentation/swiftui/view/saturation(_:)): Adjusts the color saturation of this view.
- [grayscale(_:)](/documentation/swiftui/view/grayscale(_:)): Adds a grayscale effect to this view.
- [hueRotation(_:)](/documentation/swiftui/view/huerotation(_:)): Applies a hue rotation effect to this view.
- [luminanceToAlpha()](/documentation/swiftui/view/luminancetoalpha()): Adds a luminance to alpha effect to this view.
- [materialActiveAppearance(_:)](/documentation/swiftui/view/materialactiveappearance(_:)): Sets an explicit active appearance for materials in this view.
- [materialActiveAppearance](/documentation/swiftui/environmentvalues/materialactiveappearance): The behavior materials should use for their active state, defaulting to `automatic`.
