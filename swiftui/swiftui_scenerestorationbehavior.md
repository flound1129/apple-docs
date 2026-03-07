# SceneRestorationBehavior

The restoration behavior for a scene.

```swift
struct SceneRestorationBehavior
```

## Overview

Use the [restorationBehavior(_:)](/documentation/swiftui/scene/restorationbehavior(_:)) scene modifier to apply a value of this type to a [Scene](/documentation/swiftui/scene) you define in your [App](/documentation/swiftui/app) declaration. The value you specify determines how the system will restore windows from a previous run of your application.

For example, you may have a scene that you do not wish to be restored on launch:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        Window(id: "network-test", "Network Connection Test") {
            NetworkTestView()
        }
        .restorationBehavior(.disabled)
    }
}
```

### Type Properties

- [automatic](/documentation/swiftui/scenerestorationbehavior/automatic): The automatic behavior. The scene’s windows will be restored as defined by the underlying platform.
- [disabled](/documentation/swiftui/scenerestorationbehavior/disabled): The disabled behavior. The scene’s windows will not be restored.

## See Also

### Configuring window visibility

- [WindowVisibilityToggle](/documentation/swiftui/windowvisibilitytoggle): A specialized button for toggling the visibility of a window.
- [defaultLaunchBehavior(_:)](/documentation/swiftui/scene/defaultlaunchbehavior(_:)): Sets the default launch behavior for this scene.
- [restorationBehavior(_:)](/documentation/swiftui/scene/restorationbehavior(_:)): Sets the restoration behavior for this scene.
- [SceneLaunchBehavior](/documentation/swiftui/scenelaunchbehavior): The launch behavior for a scene.
- [persistentSystemOverlays(_:)](/documentation/swiftui/scene/persistentsystemoverlays(_:)): Sets the preferred visibility of the non-transient system views overlaying the app.
- [windowToolbarFullScreenVisibility(_:)](/documentation/swiftui/view/windowtoolbarfullscreenvisibility(_:)): Configures the visibility of the window toolbar when the window enters full screen mode.
- [WindowToolbarFullScreenVisibility](/documentation/swiftui/windowtoolbarfullscreenvisibility): The visibility of the window toolbar with respect to full screen mode.
