# ToolbarItemGroup

A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.

```swift
struct ToolbarItemGroup<Content> where Content : View
```

### Creating a toolbar item group

- [init(placement:content:)](/documentation/swiftui/toolbaritemgroup/init(placement:content:)): Creates a toolbar item group with a specified placement and content.
- [init(placement:content:label:)](/documentation/swiftui/toolbaritemgroup/init(placement:content:label:)): Creates a toolbar item group with the specified placement, content, and a label describing that content.

### Supporting types

- [LabeledToolbarItemGroupContent](/documentation/swiftui/labeledtoolbaritemgroupcontent): A view that represents the view of a toolbar item group with a specified label.

## See Also

### Populating a toolbar

- [toolbar(content:)](/documentation/swiftui/view/toolbar(content:)): Populates the toolbar or navigation bar with the specified items.
- [ToolbarItem](/documentation/swiftui/toolbaritem): A model that represents an item which can be placed in the toolbar or navigation bar.
- [ToolbarItemPlacement](/documentation/swiftui/toolbaritemplacement): A structure that defines the placement of a toolbar item.
- [ToolbarContent](/documentation/swiftui/toolbarcontent): Conforming types represent items that can be placed in various locations in a toolbar.
- [ToolbarContentBuilder](/documentation/swiftui/toolbarcontentbuilder): Constructs a toolbar item set from multi-expression closures.
- [ToolbarSpacer](/documentation/swiftui/toolbarspacer): A standard space item in toolbars.
- [DefaultToolbarItem](/documentation/swiftui/defaulttoolbaritem): A toolbar item that represents a system component.
