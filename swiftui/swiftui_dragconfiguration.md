# DragConfiguration

The behavior of the drag, proposed by the dragging source.

```swift
struct DragConfiguration
```

### Structures

- [DragConfiguration.OperationsOutsideApp](/documentation/swiftui/dragconfiguration/operationsoutsideapp-swift.struct): Describes the suggested drag operations to other applications.
- [DragConfiguration.OperationsWithinApp](/documentation/swiftui/dragconfiguration/operationswithinapp-swift.struct): Describes the drag operations suggested to destinations within the app.

### Initializers

- [init(allowMove:)](/documentation/swiftui/dragconfiguration/init(allowmove:)): Creates a drag configuration that can support drag-to-move in addition to drag-to-copy.
- [init(allowMove:allowDelete:)](/documentation/swiftui/dragconfiguration/init(allowmove:allowdelete:)): Creates a drag configuration that can support drag-to-move and drag-to-delete in addition to drag-to-copy.
- [init(operationsWithinApp:operationsOutsideApp:)](/documentation/swiftui/dragconfiguration/init(operationswithinapp:operationsoutsideapp:)): Creates a default drag configuration with operation `.copy` support for drags within the application and to other applications.

### Instance Properties

- [operationsOutsideApp](/documentation/swiftui/dragconfiguration/operationsoutsideapp-swift.property): The operations suggested by the drag source for drags to other applications.
- [operationsWithinApp](/documentation/swiftui/dragconfiguration/operationswithinapp-swift.property): The operations suggested by the drag source for drags within the application.

## See Also

### Configuring drag and drop behavior

- [DropConfiguration](/documentation/swiftui/dropconfiguration): Describes the behavior of the drop.
