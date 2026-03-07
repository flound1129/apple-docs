# RenameButton

A button that triggers a standard rename action.

```swift
struct RenameButton<Label> where Label : View
```

## Overview

A rename button receives its action from the environment. Use the [renameAction(_:)](/documentation/swiftui/view/renameaction(_:)) modifier to set the action. The system disables the button if you don’t define an action.

```swift
struct RowView: View {
    @State private var text = ""
    @FocusState private var isFocused: Bool

    var body: some View {
        TextField(text: $item.name) {
            Text("Prompt")
        }
        .focused($isFocused)
        .contextMenu {
            RenameButton()
            // ... your own custom actions
        }
        .renameAction { $isFocused = true }
}
```

When someone taps the rename button in the context menu, the rename action focuses the text field by setting the `isFocused` property to true.

You can use this button inside of a navigation title menu and the navigation title modifier automatically configures the environment with the appropriate rename action.

```swift
ContentView()
    .navigationTitle($contentTitle) {
        // ... your own custom actions
        RenameButton()
    }
```

### Creating an rename button

- [init()](/documentation/swiftui/renamebutton/init()): Creates a rename button.

## See Also

### Creating special-purpose buttons

- [EditButton](/documentation/swiftui/editbutton): A button that toggles the edit mode environment value.
- [PasteButton](/documentation/swiftui/pastebutton): A system button that reads items from the pasteboard and delivers it to a closure.
