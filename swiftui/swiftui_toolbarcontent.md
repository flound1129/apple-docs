# ToolbarContent

Conforming types represent items that can be placed in various locations in a toolbar.

```swift
@MainActor @preconcurrency protocol ToolbarContent
```

## Overview

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

### Implementing toolbar content

- [body](/documentation/swiftui/toolbarcontent/body-swift.property): The composition of content that comprise the toolbar content.
- [Body](/documentation/swiftui/toolbarcontent/body-swift.associatedtype): The type of content representing the body of this toolbar content.

### Instance Methods

- [hidden(_:)](/documentation/swiftui/toolbarcontent/hidden(_:)): Hides a toolbar item within its toolbar.
- [matchedTransitionSource(id:in:)](/documentation/swiftui/toolbarcontent/matchedtransitionsource(id:in:)): Identifies this toolbar content as the source of a navigation transition, such as a zoom transition.
- [sharedBackgroundVisibility(_:)](/documentation/swiftui/toolbarcontent/sharedbackgroundvisibility(_:)): Controls the visibility of the glass background effect on items in the toolbar. In certain contexts, such as the navigation bar on iOS and the window toolbar on macOS, toolbar items will be given a glass background effect that is shared with other items in the same logical grouping.

## See Also

### Populating a toolbar

- [toolbar(content:)](/documentation/swiftui/view/toolbar(content:)): Populates the toolbar or navigation bar with the specified items.
- [ToolbarItem](/documentation/swiftui/toolbaritem): A model that represents an item which can be placed in the toolbar or navigation bar.
- [ToolbarItemGroup](/documentation/swiftui/toolbaritemgroup): A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [ToolbarItemPlacement](/documentation/swiftui/toolbaritemplacement): A structure that defines the placement of a toolbar item.
- [ToolbarContentBuilder](/documentation/swiftui/toolbarcontentbuilder): Constructs a toolbar item set from multi-expression closures.
- [ToolbarSpacer](/documentation/swiftui/toolbarspacer): A standard space item in toolbars.
- [DefaultToolbarItem](/documentation/swiftui/defaulttoolbaritem): A toolbar item that represents a system component.
