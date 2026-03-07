# WindowToolbarFullScreenVisibility

The visibility of the window toolbar with respect to full screen mode.

```swift
struct WindowToolbarFullScreenVisibility
```

## Overview

Use values of this type in conjunction with the [windowToolbarFullScreenVisibility(_:)](/documentation/swiftui/view/windowtoolbarfullscreenvisibility(_:)) modifier to configure how the window toolbar displays itself when the window enters full screen mode.

For example, you can specify that the window toolbar should be hidden by default, and only show when the mouse moves into the area occupied by the menu bar:

```swift
struct RootView: View {
    var body: some View {
        ContentView()
            .toolbar {
                ...
            }
            .windowToolbarFullScreenVisibility(.onHover)
    }
}
```

### Type Properties

- [automatic](/documentation/swiftui/windowtoolbarfullscreenvisibility/automatic): The window toolbar visibility will be defined by the system default behavior.
- [onHover](/documentation/swiftui/windowtoolbarfullscreenvisibility/onhover): Hide the window toolbar in full screen mode by default. It will reveal itself when the mouse moves into the area occupied by the menu bar.
- [visible](/documentation/swiftui/windowtoolbarfullscreenvisibility/visible): Prefer to show window toolbar when the window is in full screen mode.

## See Also

### Configuring window visibility

- [WindowVisibilityToggle](/documentation/swiftui/windowvisibilitytoggle): A specialized button for toggling the visibility of a window.
- [defaultLaunchBehavior(_:)](/documentation/swiftui/scene/defaultlaunchbehavior(_:)): Sets the default launch behavior for this scene.
- [restorationBehavior(_:)](/documentation/swiftui/scene/restorationbehavior(_:)): Sets the restoration behavior for this scene.
- [SceneLaunchBehavior](/documentation/swiftui/scenelaunchbehavior): The launch behavior for a scene.
- [SceneRestorationBehavior](/documentation/swiftui/scenerestorationbehavior): The restoration behavior for a scene.
- [persistentSystemOverlays(_:)](/documentation/swiftui/scene/persistentsystemoverlays(_:)): Sets the preferred visibility of the non-transient system views overlaying the app.
- [windowToolbarFullScreenVisibility(_:)](/documentation/swiftui/view/windowtoolbarfullscreenvisibility(_:)): Configures the visibility of the window toolbar when the window enters full screen mode.
