# DynamicTableRowContent

A type of table row content that generates table rows from an underlying collection of data.

```swift
protocol DynamicTableRowContent : TableRowContent
```

## Overview

This table row content type provides drag-and-drop support for tables. Use the [onInsert(of:perform:)](/documentation/swiftui/dynamictablerowcontent/oninsert(of:perform:)) modifier to add an action to call when the table inserts new contents into its underlying collection.

### Getting row data

- [data](/documentation/swiftui/dynamictablerowcontent/data-swift.property): The collection of underlying data.
- [Data](/documentation/swiftui/dynamictablerowcontent/data-swift.associatedtype): The type of the underlying collection of data.

### Inserting rows

- [onInsert(of:perform:)](/documentation/swiftui/dynamictablerowcontent/oninsert(of:perform:)): Sets the insert action for the dynamic table rows.
- [OnInsertTableRowModifier](/documentation/swiftui/oninserttablerowmodifier): A table row modifier that adds the ability to insert data in some base row content.

### Supporting drag and drop

- [dropDestination(for:action:)](/documentation/swiftui/dynamictablerowcontent/dropdestination(for:action:)): Sets the insert action for the dynamic table rows.

## See Also

### Creating rows

- [TableRow](/documentation/swiftui/tablerow): A row that represents a data value in a table.
- [TableRowContent](/documentation/swiftui/tablerowcontent): A type used to represent table rows.
- [TableHeaderRowContent](/documentation/swiftui/tableheaderrowcontent): A table row that displays a single view instead of columned content.
- [TupleTableRowContent](/documentation/swiftui/tupletablerowcontent): A type of table column content that creates table rows created from a Swift tuple of table rows.
- [TableForEachContent](/documentation/swiftui/tableforeachcontent): A type of table row content that creates table rows created by iterating over a collection.
- [EmptyTableRowContent](/documentation/swiftui/emptytablerowcontent): A table row content that doesn’t produce any rows.
- [TableRowBuilder](/documentation/swiftui/tablerowbuilder): A result builder that creates table row content from closures.
