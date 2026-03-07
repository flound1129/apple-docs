# TableHeaderRowContent

A table row that displays a single view instead of columned content.

```swift
struct TableHeaderRowContent<Value, Content> where Value : Identifiable, Content : View
```

## Overview

You do not create this type directly. The framework creates it on your behalf.

## See Also

### Creating rows

- [TableRow](/documentation/swiftui/tablerow): A row that represents a data value in a table.
- [TableRowContent](/documentation/swiftui/tablerowcontent): A type used to represent table rows.
- [TupleTableRowContent](/documentation/swiftui/tupletablerowcontent): A type of table column content that creates table rows created from a Swift tuple of table rows.
- [TableForEachContent](/documentation/swiftui/tableforeachcontent): A type of table row content that creates table rows created by iterating over a collection.
- [EmptyTableRowContent](/documentation/swiftui/emptytablerowcontent): A table row content that doesn’t produce any rows.
- [DynamicTableRowContent](/documentation/swiftui/dynamictablerowcontent): A type of table row content that generates table rows from an underlying collection of data.
- [TableRowBuilder](/documentation/swiftui/tablerowbuilder): A result builder that creates table row content from closures.
