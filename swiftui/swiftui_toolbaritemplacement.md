# ToolbarItemPlacement

A structure that defines the placement of a toolbar item.

```swift
struct ToolbarItemPlacement
```

## Overview

There are two types of placements:

- Semantic placements, such as [principal](/documentation/swiftui/toolbaritemplacement/principal) and [navigation](/documentation/swiftui/toolbaritemplacement/navigation), denote the intent of the item being added. SwiftUI determines the appropriate placement for the item based on this intent and its surrounding context, like the current platform.
- Positional placements, such as [navigationBarLeading](/documentation/swiftui/toolbaritemplacement/navigationbarleading), denote a precise placement for the item, usually for a particular platform.

In iOS, iPadOS, and macOS, the system uses the space available to the toolbar when determining how many items to render in the toolbar. If not all items fit in the available space, an overflow menu may be created and remaining items placed in that menu.

### Getting semantic placement

- [automatic](/documentation/swiftui/toolbaritemplacement/automatic): The system places the item automatically, depending on many factors including the platform, size class, or presence of other items.
- [principal](/documentation/swiftui/toolbaritemplacement/principal): The system places the item in the principal item section.
- [status](/documentation/swiftui/toolbaritemplacement/status): The item represents a change in status for the current context.

### Getting placement for specific actions

- [primaryAction](/documentation/swiftui/toolbaritemplacement/primaryaction): The item represents a primary action.
- [secondaryAction](/documentation/swiftui/toolbaritemplacement/secondaryaction): The item represents a secondary action.
- [confirmationAction](/documentation/swiftui/toolbaritemplacement/confirmationaction): The item represents a confirmation action for a modal interface.
- [cancellationAction](/documentation/swiftui/toolbaritemplacement/cancellationaction): The item represents a cancellation action for a modal interface.
- [destructiveAction](/documentation/swiftui/toolbaritemplacement/destructiveaction): The item represents a destructive action for a modal interface.
- [navigation](/documentation/swiftui/toolbaritemplacement/navigation): The item represents a navigation action.

### Getting explicit placement

- [topBarLeading](/documentation/swiftui/toolbaritemplacement/topbarleading): Places the item in the leading edge of the top bar.
- [topBarTrailing](/documentation/swiftui/toolbaritemplacement/topbartrailing): Places the item in the trailing edge of the top bar.
- [bottomBar](/documentation/swiftui/toolbaritemplacement/bottombar): Places the item in the bottom toolbar.
- [bottomOrnament](/documentation/swiftui/toolbaritemplacement/bottomornament): Places the item in an ornament under the window.
- [keyboard](/documentation/swiftui/toolbaritemplacement/keyboard): The item is placed in the keyboard section.
- [accessoryBar(id:)](/documentation/swiftui/toolbaritemplacement/accessorybar(id:)): Creates a unique accessory bar placement.

### Deprecated symbols

- [init(id:)](/documentation/swiftui/toolbaritemplacement/init(id:)): Creates a custom accessory bar item placement.
- [navigationBarLeading](/documentation/swiftui/toolbaritemplacement/navigationbarleading): Places the item in the leading edge of the navigation bar.
- [navigationBarTrailing](/documentation/swiftui/toolbaritemplacement/navigationbartrailing): Places the item in the trailing edge of the navigation bar.

### Type Properties

- [largeSubtitle](/documentation/swiftui/toolbaritemplacement/largesubtitle): Places the item in the subtitle area of the navigation bar.
- [largeTitle](/documentation/swiftui/toolbaritemplacement/largetitle): Places the item in the title area of the navigation bar.
- [subtitle](/documentation/swiftui/toolbaritemplacement/subtitle): Places the item in the subtitle area of the navigation bar.
- [title](/documentation/swiftui/toolbaritemplacement/title): Places the item in the title area of the navigation bar.

## See Also

### Populating a toolbar

- [toolbar(content:)](/documentation/swiftui/view/toolbar(content:)): Populates the toolbar or navigation bar with the specified items.
- [ToolbarItem](/documentation/swiftui/toolbaritem): A model that represents an item which can be placed in the toolbar or navigation bar.
- [ToolbarItemGroup](/documentation/swiftui/toolbaritemgroup): A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [ToolbarContent](/documentation/swiftui/toolbarcontent): Conforming types represent items that can be placed in various locations in a toolbar.
- [ToolbarContentBuilder](/documentation/swiftui/toolbarcontentbuilder): Constructs a toolbar item set from multi-expression closures.
- [ToolbarSpacer](/documentation/swiftui/toolbarspacer): A standard space item in toolbars.
- [DefaultToolbarItem](/documentation/swiftui/defaulttoolbaritem): A toolbar item that represents a system component.
