# TableRow

A row that represents a data value in a table.

```swift
struct TableRow<Value> where Value : Identifiable
```

## Overview

Create instances of [TableRow](/documentation/swiftui/tablerow) in the closure you provide to the `rows` parameter in [Table](/documentation/swiftui/table) initializers that take columns and rows. The table provides the value of a row to each column of a table, which produces the cells for each row in the column.

### Creating a row

- [init(_:)](/documentation/swiftui/tablerow/init(_:)): Creates a table row for the given value.

## See Also

### Creating rows

- [TableRowContent](/documentation/swiftui/tablerowcontent): A type used to represent table rows.
- [TableHeaderRowContent](/documentation/swiftui/tableheaderrowcontent): A table row that displays a single view instead of columned content.
- [TupleTableRowContent](/documentation/swiftui/tupletablerowcontent): A type of table column content that creates table rows created from a Swift tuple of table rows.
- [TableForEachContent](/documentation/swiftui/tableforeachcontent): A type of table row content that creates table rows created by iterating over a collection.
- [EmptyTableRowContent](/documentation/swiftui/emptytablerowcontent): A table row content that doesn’t produce any rows.
- [DynamicTableRowContent](/documentation/swiftui/dynamictablerowcontent): A type of table row content that generates table rows from an underlying collection of data.
- [TableRowBuilder](/documentation/swiftui/tablerowbuilder): A result builder that creates table row content from closures.
