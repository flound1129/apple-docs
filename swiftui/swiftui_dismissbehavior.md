# DismissBehavior

Programmatic window dismissal behaviors.

```swift
struct DismissBehavior
```

## Overview

Use values of this type to control window dismissal during the current transaction.

For example, to dismiss windows showing a modal presentation that would otherwise prohibit dismissal, use the [destructive](/documentation/swiftui/dismissbehavior/destructive) behavior:

```swift
struct DismissWindowButton: View {
    @Environment(\.dismissWindow) private var dismissWindow

    var body: some View {
        Button("Close Auxiliary Window") {
            withTransaction(\.dismissBehavior, .destructive) {
                dismissWindow(id: "auxiliary")
            }
        }
    }
}
```

### Getting behaviors

- [destructive](/documentation/swiftui/dismissbehavior/destructive): The destructive dismiss behavior.
- [interactive](/documentation/swiftui/dismissbehavior/interactive): The interactive dismiss behavior.

## See Also

### Closing windows

- [dismissWindow](/documentation/swiftui/environmentvalues/dismisswindow): A window dismissal action stored in a view’s environment.
- [DismissWindowAction](/documentation/swiftui/dismisswindowaction): An action that dismisses a window associated to a particular scene.
- [dismiss](/documentation/swiftui/environmentvalues/dismiss): An action that dismisses the current presentation.
- [DismissAction](/documentation/swiftui/dismissaction): An action that dismisses a presentation.
