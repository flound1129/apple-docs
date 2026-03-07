# TableForEachContent

A type of table row content that creates table rows created by iterating over a collection.

```swift
struct TableForEachContent<Data> where Data : RandomAccessCollection, Data.Element : Identifiable
```

## Overview

You don’t use this type directly. The various `Table.init(_:,...)` initializers create this type as the table’s `Rows` generic type.

To explicitly create dynamic collection-based rows, use [ForEach](/documentation/swiftui/foreach) instead.

## See Also

### Creating rows

- [TableRow](/documentation/swiftui/tablerow): A row that represents a data value in a table.
- [TableRowContent](/documentation/swiftui/tablerowcontent): A type used to represent table rows.
- [TableHeaderRowContent](/documentation/swiftui/tableheaderrowcontent): A table row that displays a single view instead of columned content.
- [TupleTableRowContent](/documentation/swiftui/tupletablerowcontent): A type of table column content that creates table rows created from a Swift tuple of table rows.
- [EmptyTableRowContent](/documentation/swiftui/emptytablerowcontent): A table row content that doesn’t produce any rows.
- [DynamicTableRowContent](/documentation/swiftui/dynamictablerowcontent): A type of table row content that generates table rows from an underlying collection of data.
- [TableRowBuilder](/documentation/swiftui/tablerowbuilder): A result builder that creates table row content from closures.
