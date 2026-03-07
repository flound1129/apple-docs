# ToolbarSpacer

A standard space item in toolbars.

```swift
struct ToolbarSpacer
```

## Overview

A space item creates visual breaks in the toolbar between items. Spacers can have a standard fixed size or be flexible and push items apart.

Spacers can also be used in customizable toolbars:

```swift
ContentView()
    .toolbar(id: "main-toolbar") {
        ToolbarItem(id: "tag") {
           TagButton()
        }
        ToolbarItem(id: "share") {
           ShareButton()
        }
        ToolbarSpacer(.fixed)
        ToolbarItem(id: "more") {
           MoreButton()
        }
    }
```

Space items are customizable and can be added, removed, and rearranged by users. If a customizable toolbar supports a spacer of a given type, users can also add in multiple copies of that spacer from the customization panel.

### Initializers

- [init(_:placement:)](/documentation/swiftui/toolbarspacer/init(_:placement:)): Creates a toolbar spacer item with the specified sizing behavior and placement.

## See Also

### Populating a toolbar

- [toolbar(content:)](/documentation/swiftui/view/toolbar(content:)): Populates the toolbar or navigation bar with the specified items.
- [ToolbarItem](/documentation/swiftui/toolbaritem): A model that represents an item which can be placed in the toolbar or navigation bar.
- [ToolbarItemGroup](/documentation/swiftui/toolbaritemgroup): A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [ToolbarItemPlacement](/documentation/swiftui/toolbaritemplacement): A structure that defines the placement of a toolbar item.
- [ToolbarContent](/documentation/swiftui/toolbarcontent): Conforming types represent items that can be placed in various locations in a toolbar.
- [ToolbarContentBuilder](/documentation/swiftui/toolbarcontentbuilder): Constructs a toolbar item set from multi-expression closures.
- [DefaultToolbarItem](/documentation/swiftui/defaulttoolbaritem): A toolbar item that represents a system component.
