# HelpLink

A button with a standard appearance that opens app-specific help documentation.

```swift
struct HelpLink
```

## Overview

A help link opens documentation relevant to the context where they are used. Typically this is by opening to an anchor in an Apple Help book, but can also perform an arbitrary action such as opening a URL or opening a window.

```swift
HelpLink(anchor: "accountSetupHelp")

HelpLink {
    openURL(onlineHelpURL)
}
```

Help links have a standard appearance, as well as conventional placement within a view. When used within an alert or confirmation dialog’s actions, the help link will automatically be placed in the top trailing corner. Or when used in a sheet toolbar, the help link is automatically placed in the lower leading corner.

```swift
struct SheetContentView: View {
    var body: some View {
        Form {
             ...
        }
        .toolbar {
            ToolbarItem(.confirmationAction) {
                Button("Save") { ... }
            }
            ToolbarItem(.cancellationAction) {
                Button("Cancel") { ... }
            }
            ToolbarItem {
                HelpLink(anchor: "sheetHelp")
            }
         }
    }
}
```

### Creating a help link

- [init(action:)](/documentation/swiftui/helplink/init(action:)): Constructs a new help link with the specified action.
- [init(destination:)](/documentation/swiftui/helplink/init(destination:)): Constructs a new help link that opens the specified destination URL.
- [init(anchor:)](/documentation/swiftui/helplink/init(anchor:)): Constructs a new help link with the specified anchor in the main app bundle’s book.
- [init(anchor:book:)](/documentation/swiftui/helplink/init(anchor:book:)): Constructs a new help link with the specified anchor and book.

## See Also

### Linking to other content

- [Link](/documentation/swiftui/link): A control for navigating to a URL.
- [ShareLink](/documentation/swiftui/sharelink): A view that controls a sharing presentation.
- [SharePreview](/documentation/swiftui/sharepreview): A representation of a type to display in a share preview.
- [TextFieldLink](/documentation/swiftui/textfieldlink): A control that requests text input from the user when pressed.
