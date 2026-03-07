# Migrating to the SwiftUI life cycle

Use a scene-based life cycle in SwiftUI while keeping your existing codebase.

## Overview

Take advantage of the declarative syntax in SwiftUI and its compatibility with spatial frameworks by moving your app to the SwiftUI life cycle.

Moving to the SwiftUI life cycle requires several steps, including changing your app’s entry point, configuring the launch of your app, and monitoring life-cycle changes with the methods that SwiftUI provides.

### Change your app’s entry point

The [UIKit](/documentation/UIKit) framework defines the `AppDelegate` file as the entry point of your app with the annotation `@main`. For more information on `@main`, see the [Attributes](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes/#main) section in The Swift Programming Language. To indicate the entry of a SwiftUI app, you’ll need to create a new file that defines your app’s structure.

1. Open your project in Xcode.
2. Choose File > New > File > Swift file.
3. Name the file `<YourAppName>App.swift`.
4. Add `import SwiftUI` at the top of the file.
5. Annotate the app structure with the `@main` attribute to indicate the entry point of the SwiftUI app, as shown in the code snippet below.

> **Important:**
> Remove the `@main` or `@UIApplicationMain` attribute in your app delegate.
>

Use following code to create the SwiftUI app structure. To learn more about this structure, see [App](/documentation/swiftui/app).

```swift
import SwiftUI

@main
struct MyExampleApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

### Support app delegate methods

To continue using methods in your app delegate, use the [UIApplicationDelegateAdaptor](/documentation/swiftui/uiapplicationdelegateadaptor) property wrapper. To tell SwiftUI about a delegate that conforms to the [UIApplicationDelegate](/documentation/UIKit/UIApplicationDelegate) protocol, place this property wrapper inside your [App](/documentation/swiftui/app) declaration:

```swift
@main
struct MyExampleApp: App {
    @UIApplicationDelegateAdaptor private var appDelegate: MyAppDelegate
    var body: some Scene { ... }
}
```

This example marks a custom app delegate named `MyAppDelegate` as the delegate adaptor. Be sure to implement any necessary delegate methods in that type.

> **Note:**
> For AppKit support, use [NSApplicationDelegateAdaptor](/documentation/swiftui/nsapplicationdelegateadaptor). For WatchKit support, use [WKApplicationDelegateAdaptor](/documentation/swiftui/wkapplicationdelegateadaptor).
>

### Configure the launch of your app

If you’re migrating an app that contains storyboards to SwiftUI, make sure to remove them when they’re no longer needed.

1. Open your project in Xcode.
2. Remove `Main.storyboard` from the project navigator.
3. Choose your app’s target.
4. Open the `Info.plist` file.
5. Remove the [UIMainStoryboardFile](/documentation/BundleResources/Information-Property-List/UIMainStoryboardFile) key.
6. Remove the [UISceneStoryboardFile](/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UISceneConfigurations/UIWindowSceneSessionRoleApplication/UISceneStoryboardFile) key in the [UIApplicationSceneManifest](/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest) > [UISceneConfigurations](/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UISceneConfigurations) > [UIWindowSceneSessionRoleApplication](/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UISceneConfigurations/UIWindowSceneSessionRoleApplication) > `Item 0 (Default Configuration)` dictionary.

This figure shows the structure of the `Info.plist` file before removing these keys.

![A screenshot of the Info.plist file in Xcode, with all of the keys expanded.]

The scene delegate continues to be called after removing the keys from the `Info.plist` file, so you can still handle other scene-based life cycle changes in this file. If you were previously launching your app in your scene delegate, remove the [scene(_:willConnectTo:options:)](/documentation/UIKit/UISceneDelegate/scene(_:willConnectTo:options:)) method from your scene delegate.

If you didn’t previously support scenes in your app and rely on your app delegate to respond to the launch of your app, ensure you’re no longer setting a root view controller in [application(_:didFinishLaunchingWithOptions:)](/documentation/UIKit/UIApplicationDelegate/application(_:didFinishLaunchingWithOptions:)). Instead, return `true`.

### Monitor life cycle changes

You will no longer be able to monitor life-cycle changes in your app delegate due to the scene-based nature of SwiftUI (see [Scene](/documentation/swiftui/scene)). Prefer to handle these changes in [ScenePhase](/documentation/swiftui/scenephase), the life cycle enumeration that SwiftUI provides to monitor the phases of a scene. Observe the [Environment](/documentation/swiftui/environment) value to initiate actions when the phase changes.

```swift
@Environment(\.scenePhase) private var scenePhase
```

Interpret the value differently based on where you read it from. If you read the phase from inside a [View](/documentation/swiftui/view) instance, the value reflects the phase of the scene that contains the view. If you read the phase from within an `App` instance, the value reflects an aggregation of the phases of all of the scenes in your app.

To handle scene-based events with a scene delegate, provide your scene delegate to your SwiftUI app inside your app delegate. For more information, see the “Scene delegates” section of [UIApplicationDelegateAdaptor](/documentation/swiftui/uiapplicationdelegateadaptor).

For more information on handling scene-based life cycle events, see [Managing your app’s life cycle](/documentation/UIKit/managing-your-app-s-life-cycle).

## See Also

### Creating an app

- [Destination Video](/documentation/visionOS/destination-video): Leverage SwiftUI to build an immersive media experience in a multiplatform app.
- [Hello World](/documentation/visionOS/World): Use windows, volumes, and immersive spaces to teach people about the Earth.
- [Backyard Birds: Building an app with SwiftData and widgets](/documentation/swiftui/backyard-birds-sample): Create an app with persistent data, interactive widgets, and an all new in-app purchase experience.
- [Food Truck: Building a SwiftUI multiplatform app](/documentation/swiftui/food-truck-building-a-swiftui-multiplatform-app): Create a single codebase and app target for Mac, iPad, and iPhone.
- [Fruta: Building a feature-rich app with SwiftUI](/documentation/AppClip/fruta-building-a-feature-rich-app-with-swiftui): Create a shared codebase to build a multiplatform app that offers widgets and an App Clip.
- [App](/documentation/swiftui/app): A type that represents the structure and behavior of an app.
