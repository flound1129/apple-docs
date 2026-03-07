# NSViewRepresentableContext

Contextual information about the state of the system that you use to create and update your AppKit view.

```swift
@MainActor @preconcurrency struct NSViewRepresentableContext<View> where View : NSViewRepresentable
```

## Overview

An [NSViewRepresentableContext](/documentation/swiftui/nsviewrepresentablecontext) structure contains details about the current state of the system. When creating and updating your view, the system creates one of these structures and passes it to the appropriate method of your custom [NSViewRepresentable](/documentation/swiftui/nsviewrepresentable) instance. Use the information in this structure to configure your view. For example, use the provided environment values to configure the appearance of your view. Don’t create this structure yourself.

### Coordinating view-related interactions

- [coordinator](/documentation/swiftui/nsviewrepresentablecontext/coordinator): An instance you use to communicate your AppKit view’s behavior and state out to SwiftUI objects.
- [transaction](/documentation/swiftui/nsviewrepresentablecontext/transaction): The current transaction.

### Getting the current environment data

- [environment](/documentation/swiftui/nsviewrepresentablecontext/environment): Environment data that describes the current state of the system.

### Instance Methods

- [animate(changes:completion:)](/documentation/swiftui/nsviewrepresentablecontext/animate(changes:completion:)): Animates changes using the animation in the current transaction.

## See Also

### Adding AppKit views to SwiftUI view hierarchies

- [NSViewRepresentable](/documentation/swiftui/nsviewrepresentable): A wrapper that you use to integrate an AppKit view into your SwiftUI view hierarchy.
- [NSViewControllerRepresentable](/documentation/swiftui/nsviewcontrollerrepresentable): A wrapper that you use to integrate an AppKit view controller into your SwiftUI interface.
- [NSViewControllerRepresentableContext](/documentation/swiftui/nsviewcontrollerrepresentablecontext): Contextual information about the state of the system that you use to create and update your AppKit view controller.
