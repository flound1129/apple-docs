# WKHostingController

A WatchKit interface controller that hosts a SwiftUI view hierarchy.

```swift
@MainActor @preconcurrency class WKHostingController<Body> where Body : View
```

## Overview

A [WKHostingController](/documentation/swiftui/wkhostingcontroller) presents and manages your app’s main interface using SwiftUI views. You must subclass [WKHostingController](/documentation/swiftui/wkhostingcontroller) and override the [body](/documentation/swiftui/wkhostingcontroller/body) property to provide the set of SwiftUI views you want to display. Display the content of your hosting controller as you would any other [WKInterfaceController](/documentation/WatchKit/WKInterfaceController) object. For example, you can include it as one of your app’s root interface controllers, or present it modally.

### Creating a hosting controller object

- [init()](/documentation/swiftui/wkhostingcontroller/init()): Creates a hosting controller object that you can use to implement your app’s main interface using SwiftUI views

### Getting the root view

- [body](/documentation/swiftui/wkhostingcontroller/body): The root view of the view hierarchy to display for your interface controller.

### Updating the root view

- [updateBodyIfNeeded()](/documentation/swiftui/wkhostingcontroller/updatebodyifneeded()): Updates the interface controller’s set of views immediately, if updates are pending.
- [setNeedsBodyUpdate()](/documentation/swiftui/wkhostingcontroller/setneedsbodyupdate()): Invalidates the current SwiftUI views and triggers an update during the next cycle.

## See Also

### Displaying SwiftUI views in WatchKit

- [WKUserNotificationHostingController](/documentation/swiftui/wkusernotificationhostingcontroller): A WatchKit user notification interface controller that hosts a SwiftUI view hierarchy.
