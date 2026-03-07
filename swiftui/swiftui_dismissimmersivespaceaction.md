# DismissImmersiveSpaceAction

An action that dismisses an immersive space.

```swift
@MainActor struct DismissImmersiveSpaceAction
```

## Overview

Use the [dismissImmersiveSpace](/documentation/swiftui/environmentvalues/dismissimmersivespace) environment value to get an instance of this type for a given [Environment](/documentation/swiftui/environment). Then call the instance to dismiss a space. You call the instance directly because it defines a [callAsFunction()](/documentation/swiftui/dismissimmersivespaceaction/callasfunction()) method that Swift calls when you call the instance.

On macOS, this may be used to dismiss a remote immersive space declared with [RemoteImmersiveSpace](/documentation/swiftui/remoteimmersivespace).

For example, you can define a button that dismisses an immersive space:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            DismissImmersiveSpaceButton()
        }
        ImmersiveSpace(id: "solarSystem") {
            SolarSystemView()
        }
    }
}

struct DismissImmersiveSpaceButton: View {
    @Environment(\.dismissImmersiveSpace) private var dismissImmersiveSpace

    var body: some View {
        Button("Dismiss") {
            Task {
                await dismissImmersiveSpace()
            }
        }
    }
}
```

The asynchronous call returns after the system finishes dismissing the space. Unlike the call to [openImmersiveSpace](/documentation/swiftui/environmentvalues/openimmersivespace) that you use to open the space — which requires an identifier, a value, or both to specify which space to open — the dismiss action requires no parameters because there can be only one immersive space open at a time. The call closes the space that is currently open, if any.

### Calling the action

- [callAsFunction()](/documentation/swiftui/dismissimmersivespaceaction/callasfunction()): Dismisses the currently opened immersive space.

## See Also

### Closing the immersive space

- [dismissImmersiveSpace](/documentation/swiftui/environmentvalues/dismissimmersivespace): An immersive space dismissal action stored in a view’s environment.
