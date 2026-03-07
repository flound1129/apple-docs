# DynamicViewContent

A type of view that generates views from an underlying collection of data.

```swift
protocol DynamicViewContent<Data> : View
```

### Managing the data

- [data](/documentation/swiftui/dynamicviewcontent/data-swift.property): The collection of underlying data.
- [Data](/documentation/swiftui/dynamicviewcontent/data-swift.associatedtype): The type of the underlying collection of data.

### Responding to updates

- [onDelete(perform:)](/documentation/swiftui/dynamicviewcontent/ondelete(perform:)): Sets the deletion action for the dynamic view. You must delete the corresponding item within `action`, as it will be called after the row has already been removed from the [List](/documentation/swiftui/list).
- [onInsert(of:perform:)](/documentation/swiftui/dynamicviewcontent/oninsert(of:perform:)-418bq): Sets the insert action for the dynamic view.
- [onMove(perform:)](/documentation/swiftui/dynamicviewcontent/onmove(perform:)): Sets the move action for the dynamic view.
- [dropDestination(for:action:)](/documentation/swiftui/dynamicviewcontent/dropdestination(for:action:)): Sets the insert action for the dynamic view.

### Deprecated symbols

- [onInsert(of:perform:)](/documentation/swiftui/dynamicviewcontent/oninsert(of:perform:)-40hwa): Sets the insert action for the dynamic view.

### Instance Methods

- [onInsert(of:perform:)](/documentation/swiftui/dynamicviewcontent/oninsert(of:perform:)): Sets the insert action for the dynamic view.

## See Also

### Iterating over dynamic data

- [ForEach](/documentation/swiftui/foreach): A structure that computes views on demand from an underlying collection of identified data.
- [ForEachSectionCollection](/documentation/swiftui/foreachsectioncollection): A collection which allows a view to be treated as a collection of its sections in a for each loop.
- [ForEachSubviewCollection](/documentation/swiftui/foreachsubviewcollection): A collection which allows a view to be treated as a collection of its subviews in a for each loop.
