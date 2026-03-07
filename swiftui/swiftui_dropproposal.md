# DropProposal

The behavior of a drop.

```swift
struct DropProposal
```

### Creating a drop proposal

- [init(operation:)](/documentation/swiftui/dropproposal/init(operation:))
- [operation](/documentation/swiftui/dropproposal/operation): The drop operation that the drop proposes to perform.

### Initializers

- [init(withinApplication:outsideApplication:)](/documentation/swiftui/dropproposal/init(withinapplication:outsideapplication:))

### Instance Properties

- [operationOutsideApplication](/documentation/swiftui/dropproposal/operationoutsideapplication): The drop operation for drops outside the source application.

## See Also

### Moving items using item providers

- [itemProvider(_:)](/documentation/swiftui/view/itemprovider(_:)): Provides a closure that vends the drag representation to be used for a particular data element.
- [onDrag(_:preview:)](/documentation/swiftui/view/ondrag(_:preview:)): Activates this view as the source of a drag and drop operation.
- [onDrag(_:)](/documentation/swiftui/view/ondrag(_:)): Activates this view as the source of a drag and drop operation.
- [onDrop(of:isTargeted:perform:)](/documentation/swiftui/view/ondrop(of:istargeted:perform:)): Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [onDrop(of:delegate:)](/documentation/swiftui/view/ondrop(of:delegate:)): Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [DropDelegate](/documentation/swiftui/dropdelegate): An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [DropOperation](/documentation/swiftui/dropoperation): Operation types that determine how a drag and drop session resolves when the user drops a drag item.
- [DropInfo](/documentation/swiftui/dropinfo): The current state of a drop.
