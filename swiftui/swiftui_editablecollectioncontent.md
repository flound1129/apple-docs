# EditableCollectionContent

An opaque wrapper view that adds editing capabilities to a row in a list.

```swift
struct EditableCollectionContent<Content, Data>
```

## Overview

You don’t use this type directly. Instead SwiftUI creates this type on your behalf.

## See Also

### Editing a list

- [moveDisabled(_:)](/documentation/swiftui/view/movedisabled(_:)): Adds a condition for whether the view’s view hierarchy is movable.
- [deleteDisabled(_:)](/documentation/swiftui/view/deletedisabled(_:)): Adds a condition for whether the view’s view hierarchy is deletable.
- [editMode](/documentation/swiftui/environmentvalues/editmode): An indication of whether the user can edit the contents of a view associated with this environment.
- [EditMode](/documentation/swiftui/editmode): A mode that indicates whether the user can edit a view’s content.
- [EditActions](/documentation/swiftui/editactions): A set of edit actions on a collection of data that a view can offer to a user.
- [IndexedIdentifierCollection](/documentation/swiftui/indexedidentifiercollection): A collection wrapper that iterates over the indices and identifiers of a collection together.
