# UIKit integration

Add UIKit views to your SwiftUI app, or use SwiftUI views in your UIKit app.

## Overview

Integrate SwiftUI with your app’s existing content using hosting controllers to add SwiftUI views into UIKit interfaces. A hosting controller wraps a set of SwiftUI views in a form that you can then add to your storyboard-based app.

![None]

You can also add UIKit views and view controllers to your SwiftUI interfaces. A representable object wraps the designated view or view controller, and facilitates communication between the wrapped object and your SwiftUI views.

For design guidance, see the following sections in the Human Interface Guidelines:

- [Designing for iOS](/design/Human-Interface-Guidelines/designing-for-ios)
- [Designing for iPadOS](/design/Human-Interface-Guidelines/designing-for-ipados)
- [Designing for tvOS](/design/Human-Interface-Guidelines/designing-for-tvos)

### Displaying SwiftUI views in UIKit

- [Using SwiftUI with UIKit](/documentation/UIKit/using-swiftui-with-uikit): Learn how to incorporate SwiftUI views into a UIKit app.
- [Unifying your app’s animations](/documentation/swiftui/unifying-your-app-s-animations): Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [UIHostingController](/documentation/swiftui/uihostingcontroller): A UIKit view controller that manages a SwiftUI view hierarchy.
- [UIHostingControllerSizingOptions](/documentation/swiftui/uihostingcontrollersizingoptions): Options for how a hosting controller tracks its content’s size.
- [UIHostingConfiguration](/documentation/swiftui/uihostingconfiguration): A content configuration suitable for hosting a hierarchy of SwiftUI views.
- [UIHostingSceneDelegate](/documentation/swiftui/uihostingscenedelegate): Extends `UIKit/UISceneDelegate` to bridge SwiftUI scenes.

### Adding UIKit views to SwiftUI view hierarchies

- [UIViewRepresentable](/documentation/swiftui/uiviewrepresentable): A wrapper for a UIKit view that you use to integrate that view into your SwiftUI view hierarchy.
- [UIViewRepresentableContext](/documentation/swiftui/uiviewrepresentablecontext): Contextual information about the state of the system that you use to create and update your UIKit view.
- [UIViewControllerRepresentable](/documentation/swiftui/uiviewcontrollerrepresentable): A view that represents a UIKit view controller.
- [UIViewControllerRepresentableContext](/documentation/swiftui/uiviewcontrollerrepresentablecontext): Contextual information about the state of the system that you use to create and update your UIKit view controller.

### Adding UIKit gesture recognizers into SwiftUI view hierarchies

- [UIGestureRecognizerRepresentable](/documentation/swiftui/uigesturerecognizerrepresentable): A wrapper for a `UIGestureRecognizer` that you use to integrate that gesture recognizer into your SwiftUI hierarchy.
- [UIGestureRecognizerRepresentableContext](/documentation/swiftui/uigesturerecognizerrepresentablecontext): Contextual information about the state of the system that you use to create and update a represented gesture recognizer.
- [UIGestureRecognizerRepresentableCoordinateSpaceConverter](/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter): A proxy structure used to convert locations to/from coordinate spaces in the hierarchy of the SwiftUI view associated with a [UIGestureRecognizerRepresentable](/documentation/swiftui/uigesturerecognizerrepresentable).

### Sharing configuration information

- [UITraitBridgedEnvironmentKey](/documentation/swiftui/uitraitbridgedenvironmentkey)

### Hosting an ornament in UIKit

- [UIHostingOrnament](/documentation/swiftui/uihostingornament): A model that represents an ornament suitable for being hosted in UIKit.
- [UIOrnament](/documentation/swiftui/uiornament): The abstract base class that represents an ornament.

## See Also

### Framework integration

- [AppKit integration](/documentation/swiftui/appkit-integration): Add AppKit views to your SwiftUI app, or use SwiftUI views in your AppKit app.
- [WatchKit integration](/documentation/swiftui/watchkit-integration): Add WatchKit views to your SwiftUI app, or use SwiftUI views in your WatchKit app.
- [Technology-specific views](/documentation/swiftui/technology-specific-views): Use SwiftUI views that other Apple frameworks provide.
