# UIApplicationDelegateAdaptor

A property wrapper type that you use to create a UIKit app delegate.

```swift
@MainActor @preconcurrency @propertyWrapper struct UIApplicationDelegateAdaptor<DelegateType> where DelegateType : NSObject, DelegateType : UIApplicationDelegate
```

## Overview

To handle app delegate callbacks in an app that uses the SwiftUI life cycle, define a type that conforms to the [UIApplicationDelegate](/documentation/UIKit/UIApplicationDelegate) protocol, and implement the delegate methods that you need. For example, you can implement the [application(_:didRegisterForRemoteNotificationsWithDeviceToken:)](/documentation/UIKit/UIApplicationDelegate/application(_:didRegisterForRemoteNotificationsWithDeviceToken:)) method to handle remote notification registration:

```swift
class MyAppDelegate: NSObject, UIApplicationDelegate, ObservableObject {
    func application(
        _ application: UIApplication,
        didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
    ) {
        // Record the device token.
    }
}
```

Then use the `UIApplicationDelegateAdaptor` property wrapper inside your [App](/documentation/swiftui/app) declaration to tell SwiftUI about the delegate type:

```swift
@main
struct MyApp: App {
    @UIApplicationDelegateAdaptor private var appDelegate: MyAppDelegate

    var body: some Scene { ... }
}
```

SwiftUI instantiates the delegate and calls the delegate’s methods in response to life cycle events. Define the delegate adaptor only in your [App](/documentation/swiftui/app) declaration, and only once for a given app. If you declare it more than once, SwiftUI generates a runtime error.

If your app delegate conforms to the [ObservableObject](/documentation/Combine/ObservableObject) protocol, as in the example above, then SwiftUI puts the delegate it creates into the [Environment](/documentation/swiftui/environment). You can access the delegate from any scene or view in your app using the [EnvironmentObject](/documentation/swiftui/environmentobject) property wrapper:

```swift
@EnvironmentObject private var appDelegate: MyAppDelegate
```

This enables you to use the dollar sign (`$`) prefix to get a binding to published properties that you declare in the delegate. For more information, see [projectedValue](/documentation/swiftui/uiapplicationdelegateadaptor/projectedvalue).

> **Important:**
> Manage an app’s life cycle events without using an app delegate whenever possible. For example, prefer to handle changes in [ScenePhase](/documentation/swiftui/scenephase) instead of relying on delegate callbacks, like [application(_:didFinishLaunchingWithOptions:)](/documentation/UIKit/UIApplicationDelegate/application(_:didFinishLaunchingWithOptions:)).
>

### Scene delegates

Some iOS apps define a [UIWindowSceneDelegate](/documentation/UIKit/UIWindowSceneDelegate) to handle scene-based events, like app shortcuts:

```swift
class MySceneDelegate: NSObject, UIWindowSceneDelegate, ObservableObject {
    func windowScene(
        _ windowScene: UIWindowScene,
        performActionFor shortcutItem: UIApplicationShortcutItem
    ) async -> Bool {
        // Do something with the shortcut...

        return true
    }
}
```

You can provide this kind of delegate to a SwiftUI app by returning the scene delegate’s type from the [application(_:configurationForConnecting:options:)](/documentation/UIKit/UIApplicationDelegate/application(_:configurationForConnecting:options:)) method inside your app delegate:

```swift
extension MyAppDelegate {
    func application(
        _ application: UIApplication,
        configurationForConnecting connectingSceneSession: UISceneSession,
        options: UIScene.ConnectionOptions
    ) -> UISceneConfiguration {

        let configuration = UISceneConfiguration(
                                name: nil,
                                sessionRole: connectingSceneSession.role)
        if connectingSceneSession.role == .windowApplication {
            configuration.delegateClass = MySceneDelegate.self
        }
        return configuration
    }
}
```

When you configure the [UISceneConfiguration](/documentation/UIKit/UISceneConfiguration) instance, you only need to indicate the delegate class, and not a scene class or storyboard. SwiftUI creates and manages the delegate instance, and sends it any relevant delegate callbacks.

As with the app delegate, if you make your scene delegate an observable object, SwiftUI automatically puts it in the [Environment](/documentation/swiftui/environment), from where you can access it with the [EnvironmentObject](/documentation/swiftui/environmentobject) property wrapper, and create bindings to its published properties.

### Creating a delegate adaptor

- [init(_:)](/documentation/swiftui/uiapplicationdelegateadaptor/init(_:)): Creates a UIKit app delegate adaptor using an observable delegate.

### Getting the delegate adaptor

- [projectedValue](/documentation/swiftui/uiapplicationdelegateadaptor/projectedvalue): A projection of the observed object that provides bindings to its properties.
- [wrappedValue](/documentation/swiftui/uiapplicationdelegateadaptor/wrappedvalue): The underlying app delegate.

## See Also

### Targeting iOS and iPadOS

- [UILaunchScreen](/documentation/BundleResources/Information-Property-List/UILaunchScreen): The user interface to show while an app launches.
- [UILaunchScreens](/documentation/BundleResources/Information-Property-List/UILaunchScreens): The user interfaces to show while an app launches in response to different URL schemes.
