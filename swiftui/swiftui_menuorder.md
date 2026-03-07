# MenuOrder

The order in which a menu presents its content.

```swift
struct MenuOrder
```

## Overview

You can configure the preferred menu order using the [menuOrder(_:)](/documentation/swiftui/view/menuorder(_:)) view modifier.

### Getting menu orders

- [automatic](/documentation/swiftui/menuorder/automatic): The ordering of the menu chosen by the system for the current context.
- [fixed](/documentation/swiftui/menuorder/fixed): Order items from top to bottom.
- [priority](/documentation/swiftui/menuorder/priority): Keep the first items closest to user’s interaction point.

## See Also

### Setting a preferred order

- [menuOrder(_:)](/documentation/swiftui/view/menuorder(_:)): Sets the preferred order of items for menus presented from this view.
- [menuOrder](/documentation/swiftui/environmentvalues/menuorder): The preferred order of items for menus presented from this view.
