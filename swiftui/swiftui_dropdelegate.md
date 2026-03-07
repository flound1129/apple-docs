# DropDelegate

An interface that you implement to interact with a drop operation in a view modified to accept drops.

```swift
@MainActor @preconcurrency protocol DropDelegate
```

## Overview

The [DropDelegate](/documentation/swiftui/dropdelegate) protocol provides a comprehensive and flexible way to interact with a drop operation. Specify a drop delegate when you modify a view to accept drops with the [onDrop(of:delegate:)](/documentation/swiftui/view/ondrop(of:delegate:)) method.

Alternatively, for simple drop cases that don’t require the full functionality of a drop delegate, you can modify a view to accept drops using the [onDrop(of:isTargeted:perform:)](/documentation/swiftui/view/ondrop(of:istargeted:perform:)) method. This method handles the drop using a closure you provide as part of the modifier.

### Receiving drop information

- [dropEntered(info:)](/documentation/swiftui/dropdelegate/dropentered(info:)): Tells the delegate a validated drop has entered the modified view.
- [dropExited(info:)](/documentation/swiftui/dropdelegate/dropexited(info:)): Tells the delegate a validated drop operation has exited the modified view.
- [dropUpdated(info:)](/documentation/swiftui/dropdelegate/dropupdated(info:)): Tells the delegate that a validated drop moved inside the modified view.
- [validateDrop(info:)](/documentation/swiftui/dropdelegate/validatedrop(info:)): Tells the delegate that a drop containing items conforming to one of the expected types entered a view that accepts drops.
- [performDrop(info:)](/documentation/swiftui/dropdelegate/performdrop(info:)): Tells the delegate it can request the item provider data from the given information.

## See Also

### Moving items using item providers

- [itemProvider(_:)](/documentation/swiftui/view/itemprovider(_:)): Provides a closure that vends the drag representation to be used for a particular data element.
- [onDrag(_:preview:)](/documentation/swiftui/view/ondrag(_:preview:)): Activates this view as the source of a drag and drop operation.
- [onDrag(_:)](/documentation/swiftui/view/ondrag(_:)): Activates this view as the source of a drag and drop operation.
- [onDrop(of:isTargeted:perform:)](/documentation/swiftui/view/ondrop(of:istargeted:perform:)): Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [onDrop(of:delegate:)](/documentation/swiftui/view/ondrop(of:delegate:)): Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [DropProposal](/documentation/swiftui/dropproposal): The behavior of a drop.
- [DropOperation](/documentation/swiftui/dropoperation): Operation types that determine how a drag and drop session resolves when the user drops a drag item.
- [DropInfo](/documentation/swiftui/dropinfo): The current state of a drop.
