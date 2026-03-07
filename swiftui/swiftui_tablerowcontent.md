# TableRowContent

A type used to represent table rows.

```swift
@MainActor @preconcurrency protocol TableRowContent<TableRowValue>
```

## Overview

Like with the [View](/documentation/swiftui/view) protocol, you can create custom table row content by declaring a type that conforms to the `TableRowContent` protocol and implementing the required [tableRowBody](/documentation/swiftui/tablerowcontent/tablerowbody-swift.property) property.

```swift
struct GroupOfPeopleRows: TableRowContent {
    @Binding var people: [Person]

    var tableRowBody: some TableRowContent<Person> {
        ForEach(people) { person in
            TableRow(person)
                .itemProvider { person.itemProvider }
        }
        .dropDestination(for: Person.self) { destination, newPeople in
            people.insert(contentsOf: newPeople, at: destination)
        }
    }
}
```

This example uses an opaque result type and specifies that the primary associated type `TableRowValue` for the `tableRowBody` property is a `Person`. From this, SwiftUI can infer `TableRowValue` for the `GroupOfPeopleRows` structure is also `Person`.

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

### Getting the row body

- [tableRowBody](/documentation/swiftui/tablerowcontent/tablerowbody-swift.property): The composition of content that comprise the table row content.
- [TableRowBody](/documentation/swiftui/tablerowcontent/tablerowbody-swift.associatedtype): The type of content representing the body of this table row content.

### Defining the row value

- [TableRowValue](/documentation/swiftui/tablerowcontent/tablerowvalue): The type of value represented by this table row content.

### Managing interaction

- [draggable(_:)](/documentation/swiftui/tablerowcontent/draggable(_:)): Activates this row as the source of a drag and drop operation.
- [dropDestination(for:action:)](/documentation/swiftui/tablerowcontent/dropdestination(for:action:)): Defines the entire row as a destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [onHover(perform:)](/documentation/swiftui/tablerowcontent/onhover(perform:)): Adds an action to perform when the pointer moves onto or away from the entire row.
- [itemProvider(_:)](/documentation/swiftui/tablerowcontent/itemprovider(_:)): Provides a closure that vends the drag representation for a particular data element.
- [ItemProviderTableRowModifier](/documentation/swiftui/itemprovidertablerowmodifier): A table row modifier that associates an item provider with some base row content.

### Adding a context menu to a row

- [contextMenu(menuItems:)](/documentation/swiftui/tablerowcontent/contextmenu(menuitems:)): Adds a context menu to a table row.
- [contextMenu(menuItems:preview:)](/documentation/swiftui/tablerowcontent/contextmenu(menuitems:preview:)): Adds a context menu with a preview to a table row.

### Instance Methods

- [selectionDisabled(_:)](/documentation/swiftui/tablerowcontent/selectiondisabled(_:)): Adds a condition that controls whether users can select this row.

## See Also

### Creating rows

- [TableRow](/documentation/swiftui/tablerow): A row that represents a data value in a table.
- [TableHeaderRowContent](/documentation/swiftui/tableheaderrowcontent): A table row that displays a single view instead of columned content.
- [TupleTableRowContent](/documentation/swiftui/tupletablerowcontent): A type of table column content that creates table rows created from a Swift tuple of table rows.
- [TableForEachContent](/documentation/swiftui/tableforeachcontent): A type of table row content that creates table rows created by iterating over a collection.
- [EmptyTableRowContent](/documentation/swiftui/emptytablerowcontent): A table row content that doesn’t produce any rows.
- [DynamicTableRowContent](/documentation/swiftui/dynamictablerowcontent): A type of table row content that generates table rows from an underlying collection of data.
- [TableRowBuilder](/documentation/swiftui/tablerowbuilder): A result builder that creates table row content from closures.
