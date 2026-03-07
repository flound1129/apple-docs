# TableColumnBuilder

A result builder that creates table column content from closures.

```swift
@resultBuilder struct TableColumnBuilder<RowValue, Sort> where RowValue : Identifiable, Sort : SortComparator
```

## Overview

The `buildBlock` methods in this type create [TableColumnContent](/documentation/swiftui/tablecolumncontent) instances based on the number and types of sources provided as parameters.

Don’t use this type directly; instead, SwiftUI annotates the `columns` parameter of the various [Table](/documentation/swiftui/table) initializers with the `@TableColumnBuilder` annotation, implicitly calling this builder for you.

### Building a column

- [buildBlock(_:)](/documentation/swiftui/tablecolumnbuilder/buildblock(_:)): Creates a single, unsortable column result.
- [buildBlock(_:_:)](/documentation/swiftui/tablecolumnbuilder/buildblock(_:_:)): Creates an unsortable column result from two sources.
- [buildBlock(_:_:_:)](/documentation/swiftui/tablecolumnbuilder/buildblock(_:_:_:)): Creates an unsortable column result from three sources.
- [buildBlock(_:_:_:_:)](/documentation/swiftui/tablecolumnbuilder/buildblock(_:_:_:_:)): Creates an unsortable column result from four sources.
- [buildBlock(_:_:_:_:_:)](/documentation/swiftui/tablecolumnbuilder/buildblock(_:_:_:_:_:)): Creates an unsortable column result from five sources.
- [buildBlock(_:_:_:_:_:_:)](/documentation/swiftui/tablecolumnbuilder/buildblock(_:_:_:_:_:_:)): Creates an unsortable column result from six sources.
- [buildBlock(_:_:_:_:_:_:_:)](/documentation/swiftui/tablecolumnbuilder/buildblock(_:_:_:_:_:_:_:)): Creates an unsortable column result from seven sources.
- [buildBlock(_:_:_:_:_:_:_:_:)](/documentation/swiftui/tablecolumnbuilder/buildblock(_:_:_:_:_:_:_:_:)): Creates an unsortable column result from eight sources.
- [buildBlock(_:_:_:_:_:_:_:_:_:)](/documentation/swiftui/tablecolumnbuilder/buildblock(_:_:_:_:_:_:_:_:_:)): Creates an unsortable column result from nine sources.
- [buildBlock(_:_:_:_:_:_:_:_:_:_:)](/documentation/swiftui/tablecolumnbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:)): Creates an unsortable column result from ten sources.
- [buildExpression(_:)](/documentation/swiftui/tablecolumnbuilder/buildexpression(_:)): Creates a generic, unsortable single column expression.

### Supporting types

- [TupleTableColumnContent](/documentation/swiftui/tupletablecolumncontent): A type of table column content that creates table columns created from a Swift tuple of table columns.

### Type Methods

- [buildEither(first:)](/documentation/swiftui/tablecolumnbuilder/buildeither(first:)): Creates a column result for the first of two column content alternatives.
- [buildEither(second:)](/documentation/swiftui/tablecolumnbuilder/buildeither(second:)): Creates a row result for the second of two row content alternatives.
- [buildIf(_:)](/documentation/swiftui/tablecolumnbuilder/buildif(_:))
- [buildLimitedAvailability(_:)](/documentation/swiftui/tablecolumnbuilder/buildlimitedavailability(_:))

## See Also

### Creating columns

- [TableColumn](/documentation/swiftui/tablecolumn): A column that displays a view for each row in a table.
- [TableColumnContent](/documentation/swiftui/tablecolumncontent): A type used to represent columns within a table.
- [TableColumnAlignment](/documentation/swiftui/tablecolumnalignment): Describes the alignment of the content of a table column.
- [TableColumnForEach](/documentation/swiftui/tablecolumnforeach): A structure that computes columns on demand from an underlying collection of identified data.
