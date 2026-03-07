# ToolbarPlacement

The placement of a toolbar.

```swift
struct ToolbarPlacement
```

## Overview

Use this type in conjunction with modifiers like [toolbarBackground(_:for:)](/documentation/swiftui/view/toolbarbackground(_:for:)) and [toolbar(_:for:)](/documentation/swiftui/view/toolbar(_:for:)) to customize the appearance of different bars managed by SwiftUI. Not all bars support all types of customizations.

See [ToolbarItemPlacement](/documentation/swiftui/toolbaritemplacement) to learn about the different regions of these toolbars that you can place your own controls into.

### Getting placements

- [automatic](/documentation/swiftui/toolbarplacement/automatic): The primary toolbar.
- [accessoryBar(id:)](/documentation/swiftui/toolbarplacement/accessorybar(id:)): Creates a unique accessory bar placement.
- [bottomBar](/documentation/swiftui/toolbarplacement/bottombar): The bottom toolbar of an app.
- [bottomOrnament](/documentation/swiftui/toolbarplacement/bottomornament): The bottom ornament of an app.
- [navigationBar](/documentation/swiftui/toolbarplacement/navigationbar): The navigation bar of an app.
- [tabBar](/documentation/swiftui/toolbarplacement/tabbar): The tab bar of an app.
- [windowToolbar](/documentation/swiftui/toolbarplacement/windowtoolbar): The placement for the containing window’s toolbar, sometimes referred to as the titlebar.

### Deprecated symbols

- [init(id:)](/documentation/swiftui/toolbarplacement/init(id:)): Creates a custom accessory bar placement.

## See Also

### Setting toolbar visibility

- [toolbar(_:for:)](/documentation/swiftui/view/toolbar(_:for:)): Specifies the visibility of a bar managed by SwiftUI.
- [toolbarVisibility(_:for:)](/documentation/swiftui/view/toolbarvisibility(_:for:)): Specifies the visibility of a bar managed by SwiftUI.
- [toolbarBackgroundVisibility(_:for:)](/documentation/swiftui/view/toolbarbackgroundvisibility(_:for:)): Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [ContentToolbarPlacement](/documentation/swiftui/contenttoolbarplacement)
