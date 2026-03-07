# TableRowBuilder

A result builder that creates table row content from closures.

```swift
@resultBuilder struct TableRowBuilder<Value> where Value : Identifiable
```

## Overview

The `buildBlock` methods in this type create [TableRowContent](/documentation/swiftui/tablerowcontent) instances based on the number and types of sources provided as parameters.

Don’t use this type directly; instead, SwiftUI annotates the `rows` parameter of the various [Table](/documentation/swiftui/table) initializers with the `@TableRowBuilder` annotation, implicitly calling this builder for you.

### Building a row from sources

- [buildBlock(_:)](/documentation/swiftui/tablerowbuilder/buildblock(_:)): Creates a single row result.
- [buildBlock(_:_:)](/documentation/swiftui/tablerowbuilder/buildblock(_:_:)): Creates a row result from two sources.
- [buildBlock(_:_:_:)](/documentation/swiftui/tablerowbuilder/buildblock(_:_:_:)): Creates a row result from three sources.
- [buildBlock(_:_:_:_:)](/documentation/swiftui/tablerowbuilder/buildblock(_:_:_:_:)): Creates a row result from four sources.
- [buildBlock(_:_:_:_:_:)](/documentation/swiftui/tablerowbuilder/buildblock(_:_:_:_:_:)): Creates a row result from five sources.
- [buildBlock(_:_:_:_:_:_:)](/documentation/swiftui/tablerowbuilder/buildblock(_:_:_:_:_:_:)): Creates a row result from six sources.
- [buildBlock(_:_:_:_:_:_:_:)](/documentation/swiftui/tablerowbuilder/buildblock(_:_:_:_:_:_:_:)): Creates a row result from seven sources.
- [buildBlock(_:_:_:_:_:_:_:_:)](/documentation/swiftui/tablerowbuilder/buildblock(_:_:_:_:_:_:_:_:)): Creates a row result from eight sources.
- [buildBlock(_:_:_:_:_:_:_:_:_:)](/documentation/swiftui/tablerowbuilder/buildblock(_:_:_:_:_:_:_:_:_:)): Creates a row result from nine sources.
- [buildBlock(_:_:_:_:_:_:_:_:_:_:)](/documentation/swiftui/tablerowbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:)): Creates a row result from ten sources.

### Building a row from conditionals

- [buildIf(_:)](/documentation/swiftui/tablerowbuilder/buildif(_:)): Creates a row result for conditional statements.
- [buildEither(first:)](/documentation/swiftui/tablerowbuilder/buildeither(first:)): Creates a row result for the first of two row content alternatives.
- [buildEither(second:)](/documentation/swiftui/tablerowbuilder/buildeither(second:)): Creates a row result for the second of two row content alternatives.
- [buildExpression(_:)](/documentation/swiftui/tablerowbuilder/buildexpression(_:)): Builds an expression within the builder.

## See Also

### Creating rows

- [TableRow](/documentation/swiftui/tablerow): A row that represents a data value in a table.
- [TableRowContent](/documentation/swiftui/tablerowcontent): A type used to represent table rows.
- [TableHeaderRowContent](/documentation/swiftui/tableheaderrowcontent): A table row that displays a single view instead of columned content.
- [TupleTableRowContent](/documentation/swiftui/tupletablerowcontent): A type of table column content that creates table rows created from a Swift tuple of table rows.
- [TableForEachContent](/documentation/swiftui/tableforeachcontent): A type of table row content that creates table rows created by iterating over a collection.
- [EmptyTableRowContent](/documentation/swiftui/emptytablerowcontent): A table row content that doesn’t produce any rows.
- [DynamicTableRowContent](/documentation/swiftui/dynamictablerowcontent): A type of table row content that generates table rows from an underlying collection of data.
