# ToolbarDefaultItemKind

A kind of toolbar item a `View` adds by default.

```swift
struct ToolbarDefaultItemKind
```

## Overview

`View`s can add toolbar items clients may wish to remove or customize. A default item kind can be passed to the [toolbar(removing:)](/documentation/swiftui/view/toolbar(removing:)) modifier to remove the item. Documentation on the `View` placing the default item should reference the `ToolbarDefaultItemKind` used to remove the item.

### Getting the default item types

- [sidebarToggle](/documentation/swiftui/toolbardefaultitemkind/sidebartoggle): The sidebar toggle toolbar item a `NavigationSplitView` adds by default.

### Type Properties

- [search](/documentation/swiftui/toolbardefaultitemkind/search): The search item added by a `View/searchable(text:isPresented:placement:prompt)` modifier.
- [title](/documentation/swiftui/toolbardefaultitemkind/title): The title and subtitle shown in title bar / navigation bar.

## See Also

### Removing default items

- [toolbar(removing:)](/documentation/swiftui/view/toolbar(removing:)): Remove a toolbar item present by default
