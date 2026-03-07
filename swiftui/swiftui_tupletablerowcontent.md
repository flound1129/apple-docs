# TupleTableRowContent

A type of table column content that creates table rows created from a Swift tuple of table rows.

```swift
@frozen struct TupleTableRowContent<Value, T> where Value : Identifiable
```

## Overview

Don’t use this type directly; instead, SwiftUI uses this type as the return value from the various `buildBlock` methods in [TableRowBuilder](/documentation/swiftui/tablerowbuilder). The size of the tuple corresponds to how many columns you create in the `rows` closure you provide to the [Table](/documentation/swiftui/table) initializer.

### Accessing the value

- [value](/documentation/swiftui/tupletablerowcontent/value)

## See Also

### Creating rows

- [TableRow](/documentation/swiftui/tablerow): A row that represents a data value in a table.
- [TableRowContent](/documentation/swiftui/tablerowcontent): A type used to represent table rows.
- [TableHeaderRowContent](/documentation/swiftui/tableheaderrowcontent): A table row that displays a single view instead of columned content.
- [TableForEachContent](/documentation/swiftui/tableforeachcontent): A type of table row content that creates table rows created by iterating over a collection.
- [EmptyTableRowContent](/documentation/swiftui/emptytablerowcontent): A table row content that doesn’t produce any rows.
- [DynamicTableRowContent](/documentation/swiftui/dynamictablerowcontent): A type of table row content that generates table rows from an underlying collection of data.
- [TableRowBuilder](/documentation/swiftui/tablerowbuilder): A result builder that creates table row content from closures.
