# WindowResizability

The resizability of a window.

```swift
struct WindowResizability
```

## Overview

Use the [windowResizability(_:)](/documentation/swiftui/scene/windowresizability(_:)) scene modifier to apply a value of this type to a [Scene](/documentation/swiftui/scene) that you define in your [App](/documentation/swiftui/app) declaration. The value that you specify indicates the strategy the system uses to place minimum and maximum size restrictions on windows that it creates from that scene.

For example, you can create a window group that people can resize to between 100 and 400 points in both dimensions by applying both a frame with those constraints to the scene’s content, and the [contentSize](/documentation/swiftui/windowresizability/contentsize) resizability to the scene:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .frame(
                    minWidth: 100, maxWidth: 400,
                    minHeight: 100, maxHeight: 400)
        }
        .windowResizability(.contentSize)
    }
}
```

The default value for all scenes if you don’t apply the modifier is [automatic](/documentation/swiftui/windowresizability/automatic). With that strategy, [Settings](/documentation/swiftui/settings) windows use the [contentSize](/documentation/swiftui/windowresizability/contentsize) strategy, while all others use [contentMinSize](/documentation/swiftui/windowresizability/contentminsize). Windows on visionOS with a window style of [volumetric](/documentation/swiftui/windowstyle/volumetric) also use the [contentSize](/documentation/swiftui/windowresizability/contentsize) strategy.

### Getting the resizability

- [automatic](/documentation/swiftui/windowresizability/automatic): The automatic window resizability.
- [contentMinSize](/documentation/swiftui/windowresizability/contentminsize): A window resizability that’s partially derived from the window’s content.
- [contentSize](/documentation/swiftui/windowresizability/contentsize): A window resizability that’s derived from the window’s content.

## See Also

### Sizing a window

- [Positioning and sizing windows](/documentation/visionOS/positioning-and-sizing-windows): Influence the initial geometry of windows that your app presents.
- [defaultSize(_:)](/documentation/swiftui/scene/defaultsize(_:)): Sets a default size for a window.
- [defaultSize(width:height:)](/documentation/swiftui/scene/defaultsize(width:height:)): Sets a default width and height for a window.
- [defaultSize(width:height:depth:)](/documentation/swiftui/scene/defaultsize(width:height:depth:)): Sets a default size for a volumetric window.
- [defaultSize(_:in:)](/documentation/swiftui/scene/defaultsize(_:in:)): Sets a default size for a volumetric window.
- [defaultSize(width:height:depth:in:)](/documentation/swiftui/scene/defaultsize(width:height:depth:in:)): Sets a default size for a volumetric window.
- [windowResizability(_:)](/documentation/swiftui/scene/windowresizability(_:)): Sets the kind of resizability to use for a window.
- [windowIdealSize(_:)](/documentation/swiftui/scene/windowidealsize(_:)): Specifies how windows derived form this scene should determine their size when zooming.
- [WindowIdealSize](/documentation/swiftui/windowidealsize): A type which defines the size a window should use when zooming.
