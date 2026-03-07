# AlertScene

A scene that renders itself as a standalone alert dialog.

```swift
struct AlertScene<Actions, Message> where Actions : View, Message : View
```

## Overview

Alert scenes are not attached to any particular window, and present themselves in the center of the current display. The dialog must be dismissed before any further interaction with the app is permitted.

```swift
@main
struct MyApp: App {
    @State var showLoginAlert = true
    @State var loggedIn = false

    var body: some Scene {
        Window("Welcome User Window", id:"WelcomeWindow") {
            ...
        }
        .defaultLaunchBehavior(loggedIn ? .presented : .suppressed)

        AlertScene("Login Required", isPresented: $showLoginAlert) {
            Button("OK") {
                ...
            }
        }
    }
}
```

All actions present in the ViewBuilder will dismiss the alert. Like the alert modifier, you can determine the role of the buttons with `.cancel` or `.destructive`. If no actions are present, we will automatically include an OK button for dismissal.

### Initializers

- [init(_:isPresented:actions:)](/documentation/swiftui/alertscene/init(_:ispresented:actions:)): Creates an alert scene with a title and a set of actions.
- [init(_:isPresented:actions:message:)](/documentation/swiftui/alertscene/init(_:ispresented:actions:message:)): Creates an alert scene with a title, a set of actions, and a message.
- [init(_:isPresented:presenting:actions:)](/documentation/swiftui/alertscene/init(_:ispresented:presenting:actions:)): Creates an alert scene, using the given data to produce the alert’s content with a title, and a set of actions. Note that this creates a text view on your behalf.
- [init(_:isPresented:presenting:actions:message:)](/documentation/swiftui/alertscene/init(_:ispresented:presenting:actions:message:)): Creates an alert scene, using the given data to produce the alert’s content with a title, a set of actions, and a message. Note that this creates a text view on your behalf.

## See Also

### Presenting an alert

- [alert(_:isPresented:actions:)](/documentation/swiftui/view/alert(_:ispresented:actions:)): Presents an alert when a given condition is true, using a text view for the title.
- [alert(_:isPresented:presenting:actions:)](/documentation/swiftui/view/alert(_:ispresented:presenting:actions:)): Presents an alert using the given data to produce the alert’s content and a text view as a title.
- [alert(isPresented:error:actions:)](/documentation/swiftui/view/alert(ispresented:error:actions:)): Presents an alert when an error is present.
- [alert(_:isPresented:actions:message:)](/documentation/swiftui/view/alert(_:ispresented:actions:message:)): Presents an alert with a message when a given condition is true using a text view as a title.
- [alert(_:isPresented:presenting:actions:message:)](/documentation/swiftui/view/alert(_:ispresented:presenting:actions:message:)): Presents an alert with a message using the given data to produce the alert’s content and a text view for a title.
- [alert(isPresented:error:actions:message:)](/documentation/swiftui/view/alert(ispresented:error:actions:message:)): Presents an alert with a message when an error is present.
