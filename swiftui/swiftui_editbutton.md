# EditButton

A button that toggles the edit mode environment value.

```swift
struct EditButton
```

## Overview

An edit button toggles the environment’s [editMode](/documentation/swiftui/environmentvalues/editmode) value for content within a container that supports edit mode. In the following example, an edit button placed inside a [NavigationView](/documentation/swiftui/navigationview) supports editing of a [List](/documentation/swiftui/list):

```swift
@State private var fruits = [
    "Apple",
    "Banana",
    "Papaya",
    "Mango"
]

var body: some View {
    NavigationView {
        List {
            ForEach(fruits, id: \.self) { fruit in
                Text(fruit)
            }
            .onDelete { fruits.remove(atOffsets: $0) }
            .onMove { fruits.move(fromOffsets: $0, toOffset: $1) }
        }
        .navigationTitle("Fruits")
        .toolbar {
            EditButton()
        }
    }
}
```

Because the [ForEach](/documentation/swiftui/foreach) in the above example defines behaviors for [onDelete(perform:)](/documentation/swiftui/dynamicviewcontent/ondelete(perform:)) and [onMove(perform:)](/documentation/swiftui/dynamicviewcontent/onmove(perform:)), the editable list displays the delete and move UI when the user taps Edit. Notice that the Edit button displays the title “Done” while edit mode is active:

![A screenshot of an app with an Edit button in the navigation bar.]

You can also create custom views that react to changes in the edit mode state, as described in [EditMode](/documentation/swiftui/editmode).

### Creating an edit button

- [init()](/documentation/swiftui/editbutton/init()): Creates an Edit button instance.

## See Also

### Creating special-purpose buttons

- [PasteButton](/documentation/swiftui/pastebutton): A system button that reads items from the pasteboard and delivers it to a closure.
- [RenameButton](/documentation/swiftui/renamebutton): A button that triggers a standard rename action.
