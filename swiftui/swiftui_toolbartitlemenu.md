# ToolbarTitleMenu

The title menu of a toolbar.

```swift
struct ToolbarTitleMenu<Content> where Content : View
```

## Overview

A title menu represents common functionality that can be done on the content represented by your app’s toolbar or navigation title. This menu may be populated from your app’s commands like [saveItem](/documentation/swiftui/commandgroupplacement/saveitem) or [printItem](/documentation/swiftui/commandgroupplacement/printitem).

```swift
ContentView()
    .toolbar {
        ToolbarTitleMenu()
    }
```

You can provide your own set of actions to override this behavior.

```swift
ContentView()
    .toolbar {
        ToolbarTitleMenu {
            DuplicateButton()
            PrintButton()
        }
    }
```

In iOS and iPadOS, this will construct a menu that can be presented by tapping the navigation title in the app’s navigation bar.

### Creating a toolbar title menu

- [init()](/documentation/swiftui/toolbartitlemenu/init()): Creates a toolbar title menu where actions are inferred from your apps commands.
- [init(content:)](/documentation/swiftui/toolbartitlemenu/init(content:)): Creates a toolbar title menu.

## See Also

### Setting the toolbar title menu

- [toolbarTitleMenu(content:)](/documentation/swiftui/view/toolbartitlemenu(content:)): Configure the title menu of a toolbar.
