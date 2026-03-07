# SceneLaunchBehavior

The launch behavior for a scene.

```swift
struct SceneLaunchBehavior
```

## Overview

Use the [defaultLaunchBehavior(_:)](/documentation/swiftui/scene/defaultlaunchbehavior(_:)) modifier to apply a value of this type to a [Scene](/documentation/swiftui/scene) you specify in your [App](/documentation/swiftui/app). The value you specify determines how the system will present the scene in the absense of any previously restored scenes on launch of your application.

For example, you may wish to present a welcome window on launch of your app when there are no previous document windows being restored:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: MyDocument()) { configuration in
            DocumentEditor(configuration.$document)
        }

        Window("Welcome to My App", id: "welcome") {
            WelcomeView()
        }
        .defaultLaunchBehavior(.presented)
    }
}
```

### Type Properties

- [automatic](/documentation/swiftui/scenelaunchbehavior/automatic): The automatic behavior.
- [presented](/documentation/swiftui/scenelaunchbehavior/presented): The presented behavior. The scene will present itself in the absence of any previously restored scenes.
- [suppressed](/documentation/swiftui/scenelaunchbehavior/suppressed): The suppressed behavior. The scene will not present itself in the absence of any previously restored scenes.

## See Also

### Configuring window visibility

- [WindowVisibilityToggle](/documentation/swiftui/windowvisibilitytoggle): A specialized button for toggling the visibility of a window.
- [defaultLaunchBehavior(_:)](/documentation/swiftui/scene/defaultlaunchbehavior(_:)): Sets the default launch behavior for this scene.
- [restorationBehavior(_:)](/documentation/swiftui/scene/restorationbehavior(_:)): Sets the restoration behavior for this scene.
- [SceneRestorationBehavior](/documentation/swiftui/scenerestorationbehavior): The restoration behavior for a scene.
- [persistentSystemOverlays(_:)](/documentation/swiftui/scene/persistentsystemoverlays(_:)): Sets the preferred visibility of the non-transient system views overlaying the app.
- [windowToolbarFullScreenVisibility(_:)](/documentation/swiftui/view/windowtoolbarfullscreenvisibility(_:)): Configures the visibility of the window toolbar when the window enters full screen mode.
- [WindowToolbarFullScreenVisibility](/documentation/swiftui/windowtoolbarfullscreenvisibility): The visibility of the window toolbar with respect to full screen mode.
