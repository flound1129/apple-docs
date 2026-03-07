# ImmersionStyle

The styles that an immersive space can have.

```swift
protocol ImmersionStyle
```

## Overview

Configure the appearance and behavior of an [ImmersiveSpace](/documentation/swiftui/immersivespace) by adding the [immersionStyle(selection:in:)](/documentation/swiftui/scene/immersionstyle(selection:in:)) scene modifier to the space and specifying a style that conforms to this protocol, like [mixed](/documentation/swiftui/immersionstyle/mixed) or [full](/documentation/swiftui/immersionstyle/full). For example, the following app defines a solar system scene that uses full immersion:

```swift
@main
struct SolarSystemApp: App {
    @State private var style: ImmersionStyle = .full

    var body: some Scene {
        ImmersiveSpace {
            SolarSystem()
        }
        .immersionStyle(selection: $style, in: .full)
    }
}
```

### Getting built-in styles

- [automatic](/documentation/swiftui/immersionstyle/automatic): The default immersion style.
- [full](/documentation/swiftui/immersionstyle/full): An immersion style that displays unbounded content that completely replaces passthrough video.
- [mixed](/documentation/swiftui/immersionstyle/mixed): An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.
- [progressive](/documentation/swiftui/immersionstyle/progressive): An immersion style that displays unbounded content that partially replaces passthrough video.

### Supporting types

- [AutomaticImmersionStyle](/documentation/swiftui/automaticimmersionstyle): The default style of immersive spaces.
- [FullImmersionStyle](/documentation/swiftui/fullimmersionstyle): An immersion style that displays unbounded content that completely replaces passthrough video.
- [MixedImmersionStyle](/documentation/swiftui/mixedimmersionstyle): An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.
- [ProgressiveImmersionStyle](/documentation/swiftui/progressiveimmersionstyle): An immersion style that displays unbounded content that partially replaces passthrough video.

### Type Methods

- [progressive(_:initialAmount:)](/documentation/swiftui/immersionstyle/progressive(_:initialamount:)): An immersion style that displays unbounded content that partially replaces passthrough video.
- [progressive(_:initialAmount:aspectRatio:)](/documentation/swiftui/immersionstyle/progressive(_:initialamount:aspectratio:)): An immersion style that displays unbounded content that partially replaces passthrough video.
- [progressive(aspectRatio:)](/documentation/swiftui/immersionstyle/progressive(aspectratio:)): An immersion style that displays unbounded content that partially replaces passthrough video.

## See Also

### Creating an immersive space

- [ImmersiveSpace](/documentation/swiftui/immersivespace): A scene that presents its content in an unbounded space.
- [ImmersiveSpaceContentBuilder](/documentation/swiftui/immersivespacecontentbuilder): A result builder for composing a collection of immersive space elements.
- [immersionStyle(selection:in:)](/documentation/swiftui/scene/immersionstyle(selection:in:)): Sets the style for an immersive space.
- [immersiveSpaceDisplacement](/documentation/swiftui/environmentvalues/immersivespacedisplacement): The displacement that the system applies to the immersive space when moving the space away from its default position, in meters.
- [ImmersiveEnvironmentBehavior](/documentation/swiftui/immersiveenvironmentbehavior): The behavior of the system-provided immersive environments when a scene is opened by your app.
- [ProgressiveImmersionAspectRatio](/documentation/swiftui/progressiveimmersionaspectratio)
