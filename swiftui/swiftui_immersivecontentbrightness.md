# ImmersiveContentBrightness

The content brightness of an immersive space.

```swift
struct ImmersiveContentBrightness
```

## Overview

Use a value of this type as an input to the [immersiveContentBrightness(_:)](/documentation/swiftui/scene/immersivecontentbrightness(_:)) scene modifier to indicate the ambient content brightness of an [ImmersiveSpace](/documentation/swiftui/immersivespace).

When you do this to create an environment that’s suitable for video playback, use one of the standard brightness values like [bright](/documentation/swiftui/immersivecontentbrightness/bright), [dim](/documentation/swiftui/immersivecontentbrightness/dim), or [dark](/documentation/swiftui/immersivecontentbrightness/dark) to provide good results for most use cases. To optimize further, you can create a custom brightness using a normalized value that expresses the linear brightness ratio between a standard dynamic range white video frame and the background that surrounds the player window.

### Getting brightness levels

- [automatic](/documentation/swiftui/immersivecontentbrightness/automatic): The default content brightness.
- [dark](/documentation/swiftui/immersivecontentbrightness/dark): A dark content brightness.
- [dim](/documentation/swiftui/immersivecontentbrightness/dim): A dimmed content brightness.
- [bright](/documentation/swiftui/immersivecontentbrightness/bright): A bright content brightness.
- [custom(_:)](/documentation/swiftui/immersivecontentbrightness/custom(_:)): Creates a content brightness with a custom value.

## See Also

### Adjusting content brightness

- [immersiveContentBrightness(_:)](/documentation/swiftui/scene/immersivecontentbrightness(_:)): Sets the content brightness of an immersive space.
