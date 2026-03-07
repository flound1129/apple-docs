# ToolbarItem

A model that represents an item which can be placed in the toolbar or navigation bar.

```swift
struct ToolbarItem<ID, Content> where Content : View
```

### Creating a toolbar item

- [init(placement:content:)](/documentation/swiftui/toolbaritem/init(placement:content:)): Creates a toolbar item with the specified placement and content.
- [init(id:placement:content:)](/documentation/swiftui/toolbaritem/init(id:placement:content:)): Creates a toolbar item with the specified placement and content, which allows for user customization.
- [init(id:placement:showsByDefault:content:)](/documentation/swiftui/toolbaritem/init(id:placement:showsbydefault:content:)): Creates a toolbar item with the specified placement and content, which allows for user customization.

## See Also

### Populating a toolbar

- [toolbar(content:)](/documentation/swiftui/view/toolbar(content:)): Populates the toolbar or navigation bar with the specified items.
- [ToolbarItemGroup](/documentation/swiftui/toolbaritemgroup): A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [ToolbarItemPlacement](/documentation/swiftui/toolbaritemplacement): A structure that defines the placement of a toolbar item.
- [ToolbarContent](/documentation/swiftui/toolbarcontent): Conforming types represent items that can be placed in various locations in a toolbar.
- [ToolbarContentBuilder](/documentation/swiftui/toolbarcontentbuilder): Constructs a toolbar item set from multi-expression closures.
- [ToolbarSpacer](/documentation/swiftui/toolbarspacer): A standard space item in toolbars.
- [DefaultToolbarItem](/documentation/swiftui/defaulttoolbaritem): A toolbar item that represents a system component.
