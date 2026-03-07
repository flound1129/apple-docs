# WindowManagerRole

Options for defining how a scene’s windows behave when used within a managed window context, such as full screen mode and Stage Manager.

```swift
struct WindowManagerRole
```

## Overview

Use values of this type in conjunction with the [windowManagerRole(_:)](/documentation/swiftui/scene/windowmanagerrole(_:)) modifier to override the default system behavior.

For example, you can specify that a secondary `Window` scene should use the principal role for full screen and Stage Manager:

```swift
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        Window("Organizer", id: "organizer") {
            OrganizerView()
        }
        .windowManagerRole(.principal)
    }
}
```

### Type Properties

- [associated](/documentation/swiftui/windowmanagerrole/associated): The associated role. Windows derived from this scene can be shown alongside windows with a `.principal` role in either full screen or Stage Manager, but do not participate in those modes on their own.
- [automatic](/documentation/swiftui/windowmanagerrole/automatic): The automatic role. The type and configuration of the scene will be used to determine how its windows behave in full screen and Stage Manager.
- [principal](/documentation/swiftui/windowmanagerrole/principal): The principal role. Windows derived from this scene will show in full screen, if enabled, or in Stage Manager.

## See Also

### Managing window behavior

- [windowManagerRole(_:)](/documentation/swiftui/scene/windowmanagerrole(_:)): Configures the role for windows derived from `self` when participating in a managed window context, such as full screen or Stage Manager.
- [WindowInteractionBehavior](/documentation/swiftui/windowinteractionbehavior): Options for enabling and disabling window interaction behaviors.
- [windowDismissBehavior(_:)](/documentation/swiftui/view/windowdismissbehavior(_:)): Configures the dismiss functionality for the window enclosing `self`.
- [windowFullScreenBehavior(_:)](/documentation/swiftui/view/windowfullscreenbehavior(_:)): Configures the full screen functionality for the window enclosing `self`.
- [windowMinimizeBehavior(_:)](/documentation/swiftui/view/windowminimizebehavior(_:)): Configures the minimize functionality for the window enclosing `self`.
- [windowResizeBehavior(_:)](/documentation/swiftui/view/windowresizebehavior(_:)): Configures the resize functionality for the window enclosing `self`.
- [windowBackgroundDragBehavior(_:)](/documentation/swiftui/scene/windowbackgrounddragbehavior(_:)): Configures the behavior of dragging a window by its background.
