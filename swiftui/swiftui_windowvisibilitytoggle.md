# WindowVisibilityToggle

A specialized button for toggling the visibility of a window.

```swift
struct WindowVisibilityToggle<Label> where Label : View
```

## Overview

This is most commonly used in the main menu, where it can toggle the visibility of `Window` and `UtilityWindow` windows. The default label uses the title of the window in the format of “Show ” and “Hide ” depending on the current visibility of the window.

A keyboard shortcut can be assigned to this button.

The below example demonstrates how a main menu can be constructed with visibility buttons, replacing the default commands added by `Window` and `Utility Window`:

```swift
 struct PhotoEditor: App {
     var body: some Scene {
         WindowGroup {
             PhotoEditor()
         }
         .commands {
            CommandGroup(before: .textFormatting) {
                Section {
                    WindowVisibilityToggle(windowID: "formatting")
                        .keyboardShortcut("t", modifiers: [.command, .shift])

                    // other custom/image formatting controls
                }
            }
            CommandGroup(before: .sidebar) {
                Section {
                    WindowVisibilityToggle(windowID: "photo-library")

                    // other controls for showing/hiding UI
                }
            }
         }

         UtilityWindow("Formatting Style", id: "formatting") {
             TextAndImageFormatForm()
         }
         .commandsRemoved()

         Window("Photo Library", id: "photo-library") {
             PhotoInfoViewer()
         }
         .commandsRemoved()
     }
 }
```

### Creating a window visibility toggle

- [init(windowID:)](/documentation/swiftui/windowvisibilitytoggle/init(windowid:)): Create a window visibility toggle to alter the visibility of a specific window.

### Supporting types

- [DefaultWindowVisibilityToggleLabel](/documentation/swiftui/defaultwindowvisibilitytogglelabel): The default label of a window visibility toggle.

## See Also

### Configuring window visibility

- [defaultLaunchBehavior(_:)](/documentation/swiftui/scene/defaultlaunchbehavior(_:)): Sets the default launch behavior for this scene.
- [restorationBehavior(_:)](/documentation/swiftui/scene/restorationbehavior(_:)): Sets the restoration behavior for this scene.
- [SceneLaunchBehavior](/documentation/swiftui/scenelaunchbehavior): The launch behavior for a scene.
- [SceneRestorationBehavior](/documentation/swiftui/scenerestorationbehavior): The restoration behavior for a scene.
- [persistentSystemOverlays(_:)](/documentation/swiftui/scene/persistentsystemoverlays(_:)): Sets the preferred visibility of the non-transient system views overlaying the app.
- [windowToolbarFullScreenVisibility(_:)](/documentation/swiftui/view/windowtoolbarfullscreenvisibility(_:)): Configures the visibility of the window toolbar when the window enters full screen mode.
- [WindowToolbarFullScreenVisibility](/documentation/swiftui/windowtoolbarfullscreenvisibility): The visibility of the window toolbar with respect to full screen mode.
