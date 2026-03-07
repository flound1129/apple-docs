# UIHostingSceneDelegate

Extends `UIKit/UISceneDelegate` to bridge SwiftUI scenes.

```swift
protocol UIHostingSceneDelegate : UISceneDelegate
```

## Overview

Declare any SwiftUI scenes you wish to activate from UIKit in the static `rootScene` property of your conforming class:

```swift
class HostingSceneDelegate: UIHostingSceneDelegate {
    static var rootScene: some Scene {
        WindowGroup(id: "swiftui-window") {
            ContentView()
        }
    }

    // Add UISceneDelegate lifecycle callbacks here
}
```

Use a class conforming to [UIHostingSceneDelegate](/documentation/swiftui/uihostingscenedelegate) to  activate a scene by its ID or presented value with `UISceneSessionActivationRequest`:

```swift
if let requestWithID = UISceneSessionActivationRequest(
    hostingDelegateClass: HostingSceneDelegate.self,
    id: "swiftui-window"
) {
    UIApplication.shared.activateSceneSession(for: requestWithID)
}

if let requestWithData = UISceneSessionActivationRequest(
    hostingDelegateClass: HostingSceneDelegate.self,
    value: FavoriteNumber(13)
) {
    UIApplication.shared.activateSceneSession(for: requestWithData)
}
```

When a SwiftUI scene declared in your `rootScene` property is activated, an instance of your conforming class will be created by SwiftUI and receive window scene lifecycle callbacks.

Your `UIHostingSceneDelegate` class can be used with a `UISceneConfiguration` in your app delegate’s `application(_:configurationForConnecting:options:)`method to activate a SwiftUI scene in response to an external event:

```swift
class AppDelegate: UIApplicationDelegate {

    func application(
        _ app: UIApplication,
        configurationForConnecting sceneSession: UISceneSession,
        options: UIScene.ConnectionOptions
    ) -> UISceneConfiguration {
        let config = UISceneConfiguration(
            name: nil, sessionRole: sceneSession.role)
        config.delegateClass = HostingSceneDelegate.self
        return config
    }

}
```

### Associated Types

- [RootScene](/documentation/swiftui/uihostingscenedelegate/rootscene-swift.associatedtype)

### Type Properties

- [rootScene](/documentation/swiftui/uihostingscenedelegate/rootscene-swift.type.property)

## See Also

### Displaying SwiftUI views in UIKit

- [Using SwiftUI with UIKit](/documentation/UIKit/using-swiftui-with-uikit): Learn how to incorporate SwiftUI views into a UIKit app.
- [Unifying your app’s animations](/documentation/swiftui/unifying-your-app-s-animations): Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [UIHostingController](/documentation/swiftui/uihostingcontroller): A UIKit view controller that manages a SwiftUI view hierarchy.
- [UIHostingControllerSizingOptions](/documentation/swiftui/uihostingcontrollersizingoptions): Options for how a hosting controller tracks its content’s size.
- [UIHostingConfiguration](/documentation/swiftui/uihostingconfiguration): A content configuration suitable for hosting a hierarchy of SwiftUI views.
