# WindowIdealSize

A type which defines the size a window should use when zooming.

```swift
struct WindowIdealSize
```

## Overview

Use this type in conjunction with the `Scene.windowIdealSize(_:)` modifier to override the default behavior for how windows behave when performing a zoom.

For example, you can define a window group where the window has an ideal width of 800 points and an ideal height of 600 points:

```swift
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .frame(idealWidth: 800, idealHeight: 600)
        }
        .windowIdealSize(.fitToContent)
    }
}
```

### Type Properties

- [automatic](/documentation/swiftui/windowidealsize/automatic): The automatic window ideal size. Windows will use the system behavior when determining the size to use when zooming.
- [fitToContent](/documentation/swiftui/windowidealsize/fittocontent): A window ideal size which uses the ideal size of the window’s contents.
- [maximum](/documentation/swiftui/windowidealsize/maximum): A window ideal size which uses the maximum size of the window’s contents.

## See Also

### Sizing a window

- [Positioning and sizing windows](/documentation/visionOS/positioning-and-sizing-windows): Influence the initial geometry of windows that your app presents.
- [defaultSize(_:)](/documentation/swiftui/scene/defaultsize(_:)): Sets a default size for a window.
- [defaultSize(width:height:)](/documentation/swiftui/scene/defaultsize(width:height:)): Sets a default width and height for a window.
- [defaultSize(width:height:depth:)](/documentation/swiftui/scene/defaultsize(width:height:depth:)): Sets a default size for a volumetric window.
- [defaultSize(_:in:)](/documentation/swiftui/scene/defaultsize(_:in:)): Sets a default size for a volumetric window.
- [defaultSize(width:height:depth:in:)](/documentation/swiftui/scene/defaultsize(width:height:depth:in:)): Sets a default size for a volumetric window.
- [windowResizability(_:)](/documentation/swiftui/scene/windowresizability(_:)): Sets the kind of resizability to use for a window.
- [WindowResizability](/documentation/swiftui/windowresizability): The resizability of a window.
- [windowIdealSize(_:)](/documentation/swiftui/scene/windowidealsize(_:)): Specifies how windows derived form this scene should determine their size when zooming.
