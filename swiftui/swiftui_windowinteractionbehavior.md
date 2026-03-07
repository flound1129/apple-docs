# WindowInteractionBehavior

Options for enabling and disabling window interaction behaviors.

```swift
struct WindowInteractionBehavior
```

## Overview

Use values of this type in conjunction with the following view and scene modifiers to adjust the supported functionality for the window:

- [windowDismissBehavior(_:)](/documentation/swiftui/view/windowdismissbehavior(_:))
- [windowMinimizeBehavior(_:)](/documentation/swiftui/view/windowminimizebehavior(_:))
- [windowFullScreenBehavior(_:)](/documentation/swiftui/view/windowfullscreenbehavior(_:))
- [windowResizeBehavior(_:)](/documentation/swiftui/view/windowresizebehavior(_:))
- [windowBackgroundDragBehavior(_:)](/documentation/swiftui/scene/windowbackgrounddragbehavior(_:))

For example, you can create a custom “About” window which only allows for dismissal:

```swift
struct MyApp: App {
    var body: some Scene {
        ...
        Window("About MyApp", id: "about") {
            AboutView()
                .windowMinimizeBehavior(.disabled)
                .windowResizeBehavior(.disabled)
        }
        .windowResizability(.contentSize)
    }
}
```

### Type Properties

- [automatic](/documentation/swiftui/windowinteractionbehavior/automatic): The automatic behavior. The associated window behavior will be enabled or disabled depending on the configuration of the enclosing `Scene`.
- [disabled](/documentation/swiftui/windowinteractionbehavior/disabled): The disabled behavior. The associated window interaction behavior will be disabled.
- [enabled](/documentation/swiftui/windowinteractionbehavior/enabled): The enabled behavior. The associated window interaction behavior will be enabled.

## See Also

### Managing window behavior

- [WindowManagerRole](/documentation/swiftui/windowmanagerrole): Options for defining how a scene’s windows behave when used within a managed window context, such as full screen mode and Stage Manager.
- [windowManagerRole(_:)](/documentation/swiftui/scene/windowmanagerrole(_:)): Configures the role for windows derived from `self` when participating in a managed window context, such as full screen or Stage Manager.
- [windowDismissBehavior(_:)](/documentation/swiftui/view/windowdismissbehavior(_:)): Configures the dismiss functionality for the window enclosing `self`.
- [windowFullScreenBehavior(_:)](/documentation/swiftui/view/windowfullscreenbehavior(_:)): Configures the full screen functionality for the window enclosing `self`.
- [windowMinimizeBehavior(_:)](/documentation/swiftui/view/windowminimizebehavior(_:)): Configures the minimize functionality for the window enclosing `self`.
- [windowResizeBehavior(_:)](/documentation/swiftui/view/windowresizebehavior(_:)): Configures the resize functionality for the window enclosing `self`.
- [windowBackgroundDragBehavior(_:)](/documentation/swiftui/scene/windowbackgrounddragbehavior(_:)): Configures the behavior of dragging a window by its background.
