# TableOutlineGroupContent

An opaque table row type created by a table’s hierarchical initializers.

```swift
struct TableOutlineGroupContent<Data> where Data : RandomAccessCollection, Data.Element : Identifiable
```

## Overview

This row content is created by `Table.init(_:,children:,...)` initializers as the table’s `Rows` generic type.

To explicitly create hierarchical rows, use [OutlineGroup](/documentation/swiftui/outlinegroup) instead.

## See Also

### Adding progressive disclosure

- [DisclosureTableRow](/documentation/swiftui/disclosuretablerow): A kind of table row that shows or hides additional rows based on the state of a disclosure control.
