# UIViewRepresentableContext

Contextual information about the state of the system that you use to create and update your UIKit view.

```swift
@MainActor @preconcurrency struct UIViewRepresentableContext<Representable> where Representable : UIViewRepresentable
```

## Overview

A [UIViewRepresentableContext](/documentation/swiftui/uiviewrepresentablecontext) structure contains details about the current state of the system. When creating and updating your view, the system creates one of these structures and passes it to the appropriate method of your custom [UIViewRepresentable](/documentation/swiftui/uiviewrepresentable) instance. Use the information in this structure to configure your view. For example, use the provided environment values to configure the appearance of your view. Don’t create this structure yourself.

### Coordinating view-related interactions

- [coordinator](/documentation/swiftui/uiviewrepresentablecontext/coordinator): The view’s associated coordinator.
- [transaction](/documentation/swiftui/uiviewrepresentablecontext/transaction): The current transaction.

### Getting the current environment data

- [environment](/documentation/swiftui/uiviewrepresentablecontext/environment): The current environment.

### Instance Methods

- [animate(changes:completion:)](/documentation/swiftui/uiviewrepresentablecontext/animate(changes:completion:)): Animates changes using the animation in the current transaction.

## See Also

### Adding UIKit views to SwiftUI view hierarchies

- [UIViewRepresentable](/documentation/swiftui/uiviewrepresentable): A wrapper for a UIKit view that you use to integrate that view into your SwiftUI view hierarchy.
- [UIViewControllerRepresentable](/documentation/swiftui/uiviewcontrollerrepresentable): A view that represents a UIKit view controller.
- [UIViewControllerRepresentableContext](/documentation/swiftui/uiviewcontrollerrepresentablecontext): Contextual information about the state of the system that you use to create and update your UIKit view controller.
