# ImmersiveEnvironmentBehavior

The behavior of the system-provided immersive environments when a scene is opened by your app.

```swift
struct ImmersiveEnvironmentBehavior
```

## Overview

Use one of these values with the [immersiveEnvironmentBehavior(_:)](/documentation/swiftui/scene/immersiveenvironmentbehavior(_:)) scene modifier to indicate how the immersive environment should behave when your app opens a scene.

### Type Properties

- [automatic](/documentation/swiftui/immersiveenvironmentbehavior/automatic): A behavior that matches the system default behavior.
- [coexist](/documentation/swiftui/immersiveenvironmentbehavior/coexist): A behavior that keeps the system’s immersive environment as is when opening a scene.
- [replace](/documentation/swiftui/immersiveenvironmentbehavior/replace): A behavior that replaces any currently opened immersive environment with the new scene.

## See Also

### Creating an immersive space

- [ImmersiveSpace](/documentation/swiftui/immersivespace): A scene that presents its content in an unbounded space.
- [ImmersiveSpaceContentBuilder](/documentation/swiftui/immersivespacecontentbuilder): A result builder for composing a collection of immersive space elements.
- [immersionStyle(selection:in:)](/documentation/swiftui/scene/immersionstyle(selection:in:)): Sets the style for an immersive space.
- [ImmersionStyle](/documentation/swiftui/immersionstyle): The styles that an immersive space can have.
- [immersiveSpaceDisplacement](/documentation/swiftui/environmentvalues/immersivespacedisplacement): The displacement that the system applies to the immersive space when moving the space away from its default position, in meters.
- [ProgressiveImmersionAspectRatio](/documentation/swiftui/progressiveimmersionaspectratio)
