# DropOperation

Operation types that determine how a drag and drop session resolves when the user drops a drag item.

```swift
enum DropOperation
```

### Getting operation types

- [DropOperation.cancel](/documentation/swiftui/dropoperation/cancel): Cancel the drag operation and transfer no data.
- [DropOperation.copy](/documentation/swiftui/dropoperation/copy): Copy the data to the modified view.
- [DropOperation.forbidden](/documentation/swiftui/dropoperation/forbidden): The drop activity is not allowed at this time or location.
- [DropOperation.move](/documentation/swiftui/dropoperation/move): Move the data represented by the drag items instead of copying it.

### Structures

- [DropOperation.Set](/documentation/swiftui/dropoperation/set): A set of drop operations, corresponding to matching cases in `DropOperation`.

### Enumeration Cases

- [DropOperation.alias](/documentation/swiftui/dropoperation/alias)
- [DropOperation.delete](/documentation/swiftui/dropoperation/delete): Delete the data. The item was dragged to Trash or to another destination that semantically represents deletion.

## See Also

### Moving items using item providers

- [itemProvider(_:)](/documentation/swiftui/view/itemprovider(_:)): Provides a closure that vends the drag representation to be used for a particular data element.
- [onDrag(_:preview:)](/documentation/swiftui/view/ondrag(_:preview:)): Activates this view as the source of a drag and drop operation.
- [onDrag(_:)](/documentation/swiftui/view/ondrag(_:)): Activates this view as the source of a drag and drop operation.
- [onDrop(of:isTargeted:perform:)](/documentation/swiftui/view/ondrop(of:istargeted:perform:)): Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [onDrop(of:delegate:)](/documentation/swiftui/view/ondrop(of:delegate:)): Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [DropDelegate](/documentation/swiftui/dropdelegate): An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [DropProposal](/documentation/swiftui/dropproposal): The behavior of a drop.
- [DropInfo](/documentation/swiftui/dropinfo): The current state of a drop.
