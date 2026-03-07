# DropInfo

The current state of a drop.

```swift
struct DropInfo
```

### Getting the drop location

- [location](/documentation/swiftui/dropinfo/location): The location of the drag in the coordinate space of the drop view.

### Checking for items

- [hasItemsConforming(to:)](/documentation/swiftui/dropinfo/hasitemsconforming(to:)-47irh): Indicates whether at least one item conforms to at least one of the specified uniform type identifiers.
- [itemProviders(for:)](/documentation/swiftui/dropinfo/itemproviders(for:)-93409): Finds item providers that conform to at least one of the specified uniform type identifiers.

### Deprecated symbols

- [hasItemsConforming(to:)](/documentation/swiftui/dropinfo/hasitemsconforming(to:)-4qeez): Returns whether at least one item conforms to at least one of the specified uniform type identifiers.
- [itemProviders(for:)](/documentation/swiftui/dropinfo/itemproviders(for:)-b6fo): Returns an array of items that each conform to at least one of the specified uniform type identifiers.

### Instance Methods

- [hasItemsConforming(to:)](/documentation/swiftui/dropinfo/hasitemsconforming(to:)): Indicates whether at least one item conforms to at least one of the specified uniform type identifiers.
- [itemProviders(for:)](/documentation/swiftui/dropinfo/itemproviders(for:)): Finds item providers that conform to at least one of the specified uniform type identifiers.

## See Also

### Moving items using item providers

- [itemProvider(_:)](/documentation/swiftui/view/itemprovider(_:)): Provides a closure that vends the drag representation to be used for a particular data element.
- [onDrag(_:preview:)](/documentation/swiftui/view/ondrag(_:preview:)): Activates this view as the source of a drag and drop operation.
- [onDrag(_:)](/documentation/swiftui/view/ondrag(_:)): Activates this view as the source of a drag and drop operation.
- [onDrop(of:isTargeted:perform:)](/documentation/swiftui/view/ondrop(of:istargeted:perform:)): Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [onDrop(of:delegate:)](/documentation/swiftui/view/ondrop(of:delegate:)): Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [DropDelegate](/documentation/swiftui/dropdelegate): An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [DropProposal](/documentation/swiftui/dropproposal): The behavior of a drop.
- [DropOperation](/documentation/swiftui/dropoperation): Operation types that determine how a drag and drop session resolves when the user drops a drag item.
