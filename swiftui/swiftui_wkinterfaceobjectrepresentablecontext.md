# WKInterfaceObjectRepresentableContext

Contextual information about the state of the system that you use to create and update your WatchKit interface object.

```swift
@MainActor @preconcurrency struct WKInterfaceObjectRepresentableContext<Representable> where Representable : WKInterfaceObjectRepresentable
```

## Overview

A [WKInterfaceObjectRepresentableContext](/documentation/swiftui/wkinterfaceobjectrepresentablecontext) structure contains details about the current state of the system. When creating and updating your interface objects, the system creates one of these structures and passes it to the appropriate method of your custom [WKInterfaceObjectRepresentable](/documentation/swiftui/wkinterfaceobjectrepresentable) instance. Use the information in this structure to configure your object. Don’t create this structure yourself.

### Coordinating interactions

- [coordinator](/documentation/swiftui/wkinterfaceobjectrepresentablecontext/coordinator): The view’s associated coordinator.
- [transaction](/documentation/swiftui/wkinterfaceobjectrepresentablecontext/transaction): The current transaction.

### Getting the current environment data

- [environment](/documentation/swiftui/wkinterfaceobjectrepresentablecontext/environment): The current environment.

## See Also

### Adding WatchKit views to SwiftUI view hierarchies

- [WKInterfaceObjectRepresentable](/documentation/swiftui/wkinterfaceobjectrepresentable): A view that represents a WatchKit interface object.
