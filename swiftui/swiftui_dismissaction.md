# DismissAction

An action that dismisses a presentation.

```swift
@MainActor @preconcurrency struct DismissAction
```

## Overview

Use the [dismiss](/documentation/swiftui/environmentvalues/dismiss) environment value to get the instance of this structure for a given [Environment](/documentation/swiftui/environment). Then call the instance to perform the dismissal. You call the instance directly because it defines a [callAsFunction()](/documentation/swiftui/dismissaction/callasfunction()) method that Swift calls when you call the instance.

You can use this action to:

- Dismiss a modal presentation, like a sheet or a popover.
- Pop the current view from a [NavigationStack](/documentation/swiftui/navigationstack).

On apps targeting iOS 18 and aligned releases, you also use the dismiss action to pop the implicit stack of a collapsed [NavigationSplitView](/documentation/swiftui/navigationsplitview), or clear the equivalent state in an expanded split view.

The specific behavior of the action depends on where you call it from. For example, you can create a button that calls the [DismissAction](/documentation/swiftui/dismissaction) inside a view that acts as a sheet:

```swift
private struct SheetContents: View {
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        Button("Done") {
            dismiss()
        }
    }
}
```

When you present the `SheetContents` view, someone can dismiss the sheet by tapping or clicking the sheet’s button:

```swift
private struct DetailView: View {
    @State private var isSheetPresented = false

    var body: some View {
        Button("Show Sheet") {
            isSheetPresented = true
        }
        .sheet(isPresented: $isSheetPresented) {
            SheetContents()
        }
    }
}
```

Be sure that you define the action in the appropriate environment. For example, don’t reorganize the `DetailView` in the example above so that it creates the `dismiss` property and calls it from the [sheet(item:onDismiss:content:)](/documentation/swiftui/view/sheet(item:ondismiss:content:)) view modifier’s `content` closure:

```swift
private struct DetailView: View {
    @State private var isSheetPresented = false
    @Environment(\.dismiss) private var dismiss // Applies to DetailView.

    var body: some View {
        Button("Show Sheet") {
            isSheetPresented = true
        }
        .sheet(isPresented: $isSheetPresented) {
            Button("Done") {
                dismiss() // Fails to dismiss the sheet.
            }
        }
    }
}
```

If you do this, the sheet fails to dismiss because the action applies to the environment where you declared it, which is that of the detail view, rather than the sheet. In fact, in macOS and iPadOS, if the `DetailView` is the root view of a window, the dismiss action closes the window instead.

The dismiss action has no effect on a view that isn’t currently presented. If you need to query whether SwiftUI is currently presenting a view, read the [isPresented](/documentation/swiftui/environmentvalues/ispresented) environment value.

> **Note:**
> While the dismiss action can be used to a close window that you create with [WindowGroup](/documentation/swiftui/windowgroup) or [Window](/documentation/swiftui/window), prefer [DismissWindowAction](/documentation/swiftui/dismisswindowaction) for that use case instead.
>

### Calling the action

- [callAsFunction()](/documentation/swiftui/dismissaction/callasfunction()): Dismisses the view if it is currently presented.

## See Also

### Dismissing a presentation

- [isPresented](/documentation/swiftui/environmentvalues/ispresented): A Boolean value that indicates whether the view associated with this environment is currently presented.
- [dismiss](/documentation/swiftui/environmentvalues/dismiss): An action that dismisses the current presentation.
- [interactiveDismissDisabled(_:)](/documentation/swiftui/view/interactivedismissdisabled(_:)): Conditionally prevents interactive dismissal of presentations like popovers, sheets, and inspectors.
