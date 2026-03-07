# NSHostingSceneBridgingOptions

Options for how hosting views and controllers manage aspects of the associated window.

```swift
struct NSHostingSceneBridgingOptions
```

### Geting bridging options

- [all](/documentation/swiftui/nshostingscenebridgingoptions/all): The hosting view’s associated window will have both its title bars and toolbars populated with values from their respective modifiers.
- [title](/documentation/swiftui/nshostingscenebridgingoptions/title): The hosting view’s associated window will have its title and subtitle populated with the values provided to the `navigationTitle(_:)` and `navigationSubtitle(_:)` modifiers, respectively.
- [toolbars](/documentation/swiftui/nshostingscenebridgingoptions/toolbars): The hosting view’s associated window will have its toolbar populated with any items provided to the `toolbar(content:)` modifier.

### Creating a bridging options

- [init(rawValue:)](/documentation/swiftui/nshostingscenebridgingoptions/init(rawvalue:)): Creates a new set from a raw value.
- [rawValue](/documentation/swiftui/nshostingscenebridgingoptions/rawvalue): The raw value.

## See Also

### Displaying SwiftUI views in AppKit

- [Unifying your app’s animations](/documentation/swiftui/unifying-your-app-s-animations): Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [NSHostingController](/documentation/swiftui/nshostingcontroller): An AppKit view controller that hosts SwiftUI view hierarchy.
- [NSHostingView](/documentation/swiftui/nshostingview): An AppKit view that hosts a SwiftUI view hierarchy.
- [NSHostingMenu](/documentation/swiftui/nshostingmenu): An AppKit menu with menu items that are defined by a SwiftUI View.
- [NSHostingSizingOptions](/documentation/swiftui/nshostingsizingoptions): Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.
- [NSHostingSceneRepresentation](/documentation/swiftui/nshostingscenerepresentation): An AppKit type that hosts and can present SwiftUI scenes
