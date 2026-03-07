# UIViewControllerRepresentableContext

Contextual information about the state of the system that you use to create and update your UIKit view controller.

```swift
@MainActor @preconcurrency struct UIViewControllerRepresentableContext<Representable> where Representable : UIViewControllerRepresentable
```

## Overview

A [UIViewControllerRepresentableContext](/documentation/swiftui/uiviewcontrollerrepresentablecontext) structure contains details about the current state of the system. When creating and updating your view controller, the system creates one of these structures and passes it to the appropriate method of your custom [UIViewControllerRepresentable](/documentation/swiftui/uiviewcontrollerrepresentable) instance. Use the information in this structure to configure your view controller. For example, use the provided environment values to configure the appearance of your view controller and views. Don’t create this structure yourself.

### Coordinating view controller interactions

- [coordinator](/documentation/swiftui/uiviewcontrollerrepresentablecontext/coordinator): The view’s associated coordinator.
- [transaction](/documentation/swiftui/uiviewcontrollerrepresentablecontext/transaction): The current transaction.

### Getting the environment data

- [environment](/documentation/swiftui/uiviewcontrollerrepresentablecontext/environment): Environment values that describe the current state of the system.

### Instance Methods

- [animate(changes:completion:)](/documentation/swiftui/uiviewcontrollerrepresentablecontext/animate(changes:completion:)): Animates changes using the animation in the current transaction.

## See Also

### Adding UIKit views to SwiftUI view hierarchies

- [UIViewRepresentable](/documentation/swiftui/uiviewrepresentable): A wrapper for a UIKit view that you use to integrate that view into your SwiftUI view hierarchy.
- [UIViewRepresentableContext](/documentation/swiftui/uiviewrepresentablecontext): Contextual information about the state of the system that you use to create and update your UIKit view.
- [UIViewControllerRepresentable](/documentation/swiftui/uiviewcontrollerrepresentable): A view that represents a UIKit view controller.
