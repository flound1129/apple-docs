# NSHostingSceneRepresentation

An AppKit type that hosts and can present SwiftUI scenes

```swift
@MainActor class NSHostingSceneRepresentation<Content> where Content : Scene
```

## Overview

Use instances of this type with `NSApplication.addSceneRepresentation(_:)` to include SwiftUI scene functionality in an app which uses the AppKit app lifecycle.

For example, you can add a `Settings` scene to your app and present it when the corresponding menu item is selected:

```swift
import AppKit
import SwiftUI

@main
class ApplicationDelegate: NSApplicationDelegate {
    let settingsScene = NSHostingSceneRepresentation {
        Settings {
            SettingsView()
        }
    }

    func applicationWillFinishLaunching(_ notification: Notification) {
        NSApplication.shared.addSceneRepresentation(settingsScene)
    }

    @IBAction func showAppSettings(_ sender: NSMenuItem) {
        settingsScene.environment.openSettings()
    }
}
```

### Initializers

- [init(rootScene:)](/documentation/swiftui/nshostingscenerepresentation/init(rootscene:)): Creates a new hosting scene representation for the specified scene(s).

### Instance Properties

- [environment](/documentation/swiftui/nshostingscenerepresentation/environment): The environment for any scene(s) being represented by `self`.

## See Also

### Displaying SwiftUI views in AppKit

- [Unifying your app’s animations](/documentation/swiftui/unifying-your-app-s-animations): Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [NSHostingController](/documentation/swiftui/nshostingcontroller): An AppKit view controller that hosts SwiftUI view hierarchy.
- [NSHostingView](/documentation/swiftui/nshostingview): An AppKit view that hosts a SwiftUI view hierarchy.
- [NSHostingMenu](/documentation/swiftui/nshostingmenu): An AppKit menu with menu items that are defined by a SwiftUI View.
- [NSHostingSizingOptions](/documentation/swiftui/nshostingsizingoptions): Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.
- [NSHostingSceneBridgingOptions](/documentation/swiftui/nshostingscenebridgingoptions): Options for how hosting views and controllers manage aspects of the associated window.
