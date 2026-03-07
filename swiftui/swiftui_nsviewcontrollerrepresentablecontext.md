# NSViewControllerRepresentableContext

Contextual information about the state of the system that you use to create and update your AppKit view controller.

```swift
@MainActor @preconcurrency struct NSViewControllerRepresentableContext<ViewController> where ViewController : NSViewControllerRepresentable
```

## Overview

An [NSViewControllerRepresentableContext](/documentation/swiftui/nsviewcontrollerrepresentablecontext) structure contains details about the current state of the system. When creating and updating your view controller, the system creates one of these structures and passes it to the appropriate method of your custom [NSViewControllerRepresentable](/documentation/swiftui/nsviewcontrollerrepresentable) instance. Use the information in this structure to configure your view controller. For example, use the provided environment values to configure the appearance of your view controller and views. Don’t create this structure yourself.

### Coordinating view-related interactions

- [coordinator](/documentation/swiftui/nsviewcontrollerrepresentablecontext/coordinator): An object you use to communicate your AppKit view controller’s behavior and state out to SwiftUI objects.
- [transaction](/documentation/swiftui/nsviewcontrollerrepresentablecontext/transaction): The current transaction.

### Getting the current environment data

- [environment](/documentation/swiftui/nsviewcontrollerrepresentablecontext/environment): Environment data that describes the current state of the system.

### Instance Methods

- [animate(changes:completion:)](/documentation/swiftui/nsviewcontrollerrepresentablecontext/animate(changes:completion:)): Animates changes using the animation in the current transaction.

## See Also

### Adding AppKit views to SwiftUI view hierarchies

- [NSViewRepresentable](/documentation/swiftui/nsviewrepresentable): A wrapper that you use to integrate an AppKit view into your SwiftUI view hierarchy.
- [NSViewRepresentableContext](/documentation/swiftui/nsviewrepresentablecontext): Contextual information about the state of the system that you use to create and update your AppKit view.
- [NSViewControllerRepresentable](/documentation/swiftui/nsviewcontrollerrepresentable): A wrapper that you use to integrate an AppKit view controller into your SwiftUI interface.
