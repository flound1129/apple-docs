# EditMode

A mode that indicates whether the user can edit a view’s content.

```swift
enum EditMode
```

## Overview

You receive an optional binding to the edit mode state when you read the [editMode](/documentation/swiftui/environmentvalues/editmode) environment value. The binding contains an `EditMode` value that indicates whether edit mode is active, and that you can use to change the mode. To learn how to read an environment value, see [EnvironmentValues](/documentation/swiftui/environmentvalues).

Certain built-in views automatically alter their appearance and behavior in edit mode. For example, a [List](/documentation/swiftui/list) with a [ForEach](/documentation/swiftui/foreach) that’s configured with the [onDelete(perform:)](/documentation/swiftui/dynamicviewcontent/ondelete(perform:)) or [onMove(perform:)](/documentation/swiftui/dynamicviewcontent/onmove(perform:)) modifier provides controls to delete or move list items while in edit mode. On devices without an attached keyboard and mouse or trackpad, people can make multiple selections in lists only when edit mode is active.

You can also customize your own views to react to edit mode. The following example replaces a read-only [Text](/documentation/swiftui/text) view with an editable [TextField](/documentation/swiftui/textfield), checking for edit mode by testing the wrapped value’s [isEditing](/documentation/swiftui/editmode/isediting) property:

```swift
@Environment(\.editMode) private var editMode
@State private var name = "Maria Ruiz"

var body: some View {
    Form {
        if editMode?.wrappedValue.isEditing == true {
            TextField("Name", text: $name)
        } else {
            Text(name)
        }
    }
    .animation(nil, value: editMode?.wrappedValue)
    .toolbar { // Assumes embedding this view in a NavigationView.
        EditButton()
    }
}
```

You can set the edit mode through the binding, or you can rely on an [EditButton](/documentation/swiftui/editbutton) to do that for you, as the example above demonstrates. The button activates edit mode when the user taps it, and disables the mode when the user taps again.

### Getting edit modes

- [EditMode.active](/documentation/swiftui/editmode/active): The user can edit the view content.
- [EditMode.inactive](/documentation/swiftui/editmode/inactive): The user can’t edit the view content.
- [EditMode.transient](/documentation/swiftui/editmode/transient): The view is in a temporary edit mode.

### Checking for editing mode

- [isEditing](/documentation/swiftui/editmode/isediting): Indicates whether a view is being edited.

## See Also

### Editing a list

- [moveDisabled(_:)](/documentation/swiftui/view/movedisabled(_:)): Adds a condition for whether the view’s view hierarchy is movable.
- [deleteDisabled(_:)](/documentation/swiftui/view/deletedisabled(_:)): Adds a condition for whether the view’s view hierarchy is deletable.
- [editMode](/documentation/swiftui/environmentvalues/editmode): An indication of whether the user can edit the contents of a view associated with this environment.
- [EditActions](/documentation/swiftui/editactions): A set of edit actions on a collection of data that a view can offer to a user.
- [EditableCollectionContent](/documentation/swiftui/editablecollectioncontent): An opaque wrapper view that adds editing capabilities to a row in a list.
- [IndexedIdentifierCollection](/documentation/swiftui/indexedidentifiercollection): A collection wrapper that iterates over the indices and identifiers of a collection together.
