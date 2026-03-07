# NSHostingController

An AppKit view controller that hosts SwiftUI view hierarchy.

```swift
@MainActor @preconcurrency class NSHostingController<Content> where Content : View
```

## Overview

Create an `NSHostingController` object when you want to integrate SwiftUI views into an AppKit view hierarchy. At creation time, specify the SwiftUI view you want to use as the root view for this view controller; you can change that view later using the [rootView](/documentation/swiftui/nshostingcontroller/rootview) property. Use the hosting controller like you would any other view controller, by presenting it or embedding it as a child view controller in your interface.

### Creating a hosting controller object

- [init(rootView:)](/documentation/swiftui/nshostingcontroller/init(rootview:)): Creates a hosting controller object that wraps the specified SwiftUI view.
- [init(coder:rootView:)](/documentation/swiftui/nshostingcontroller/init(coder:rootview:)): Creates a hosting controller object from an archive and the specified SwiftUI view.
- [init(coder:)](/documentation/swiftui/nshostingcontroller/init(coder:)): Creates a hosting controller object from the contents of the specified archive.

### Getting the root view

- [rootView](/documentation/swiftui/nshostingcontroller/rootview): The root view of the SwiftUI view hierarchy managed by this view controller.
- [identifier](/documentation/swiftui/nshostingcontroller/identifier)

### Configuring the controller

- [sizeThatFits(in:)](/documentation/swiftui/nshostingcontroller/sizethatfits(in:)): Calculates and returns the most appropriate size for the current view.
- [preferredContentSize](/documentation/swiftui/nshostingcontroller/preferredcontentsize)
- [sizingOptions](/documentation/swiftui/nshostingcontroller/sizingoptions): The options for how the hosting controller’s view creates and updates constraints based on the size of its SwiftUI content.
- [safeAreaRegions](/documentation/swiftui/nshostingcontroller/safearearegions): The safe area regions that this view controller adds to its view.
- [sceneBridgingOptions](/documentation/swiftui/nshostingcontroller/scenebridgingoptions): The options for which aspects of the window will be managed by this controller’s hosting view.

## See Also

### Displaying SwiftUI views in AppKit

- [Unifying your app’s animations](/documentation/swiftui/unifying-your-app-s-animations): Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [NSHostingView](/documentation/swiftui/nshostingview): An AppKit view that hosts a SwiftUI view hierarchy.
- [NSHostingMenu](/documentation/swiftui/nshostingmenu): An AppKit menu with menu items that are defined by a SwiftUI View.
- [NSHostingSizingOptions](/documentation/swiftui/nshostingsizingoptions): Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.
- [NSHostingSceneRepresentation](/documentation/swiftui/nshostingscenerepresentation): An AppKit type that hosts and can present SwiftUI scenes
- [NSHostingSceneBridgingOptions](/documentation/swiftui/nshostingscenebridgingoptions): Options for how hosting views and controllers manage aspects of the associated window.
