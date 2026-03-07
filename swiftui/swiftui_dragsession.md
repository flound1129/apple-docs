# DragSession

Describes the ongoing dragging session.

```swift
struct DragSession
```

### Structures

- [DragSession.ID](/documentation/swiftui/dragsession/id-swift.struct): The identifier of a drag session.

### Instance Properties

- [draggedItemIndex](/documentation/swiftui/dragsession/draggeditemindex): The index of the dragged item under the cursor.
- [id](/documentation/swiftui/dragsession/id-swift.property): The identifier of the drag session.
- [location](/documentation/swiftui/dragsession/location): Location of the drag session in the local coordinate space.
- [phase](/documentation/swiftui/dragsession/phase-swift.property): The current phase of the drag session.

### Instance Methods

- [draggedItemIDs(for:)](/documentation/swiftui/dragsession/draggeditemids(for:)): Provides an array of identifiers of the currently dragged items in a case when the items conform to the `Identifiable` protocol, or identifiers were provided to SwiftUI separately.

### Enumerations

- [DragSession.Phase](/documentation/swiftui/dragsession/phase-swift.enum): The phase of the current drag session

## See Also

### Moving items

- [DropSession](/documentation/swiftui/dropsession)
