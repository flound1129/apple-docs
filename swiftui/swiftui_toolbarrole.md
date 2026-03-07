# ToolbarRole

The purpose of content that populates the toolbar.

```swift
struct ToolbarRole
```

## Overview

A toolbar role provides a description of the purpose of content that populates the toolbar. The purpose of the content influences how a toolbar renders its content. For example, a [browser](/documentation/swiftui/toolbarrole/browser) will automatically leading align the title of a toolbar in iPadOS.

Provide this type to the [toolbarRole(_:)](/documentation/swiftui/view/toolbarrole(_:)) modifier:

```swift
ContentView()
    .navigationTitle("Browser")
    .toolbarRole(.browser)
    .toolbar {
        ToolbarItem(placement: .primaryAction) {
            AddButton()
        }
     }
```

### Behavior-specific roles

- [browser](/documentation/swiftui/toolbarrole/browser): The browser role.
- [editor](/documentation/swiftui/toolbarrole/editor): The editor role.
- [navigationStack](/documentation/swiftui/toolbarrole/navigationstack): The navigationStack role.

### Automatic roles

- [automatic](/documentation/swiftui/toolbarrole/automatic): The automatic role.

## See Also

### Specifying the role of toolbar content

- [toolbarRole(_:)](/documentation/swiftui/view/toolbarrole(_:)): Configures the semantic role for the content populating the toolbar.
