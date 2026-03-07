# NSHostingSizingOptions

Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.

```swift
struct NSHostingSizingOptions
```

### Geting sizing options

- [intrinsicContentSize](/documentation/swiftui/nshostingsizingoptions/intrinsiccontentsize): The hosting view creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting view’s `intrinsicContentSize`.
- [maxSize](/documentation/swiftui/nshostingsizingoptions/maxsize): The hosting view creates and updates constraints that represent its content’s maximum size.
- [minSize](/documentation/swiftui/nshostingsizingoptions/minsize): The hosting view creates and updates constraints that represent its content’s minimum size.
- [preferredContentSize](/documentation/swiftui/nshostingsizingoptions/preferredcontentsize): The hosting controller creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting controller’s `preferredContentSize`.
- [standardBounds](/documentation/swiftui/nshostingsizingoptions/standardbounds): The hosting view creates constraints for its minimum, ideal, and maximum sizes.

### Creating a sizing option

- [init(rawValue:)](/documentation/swiftui/nshostingsizingoptions/init(rawvalue:)): Creates a new options from a raw value.
- [rawValue](/documentation/swiftui/nshostingsizingoptions/rawvalue): The raw value.

## See Also

### Displaying SwiftUI views in AppKit

- [Unifying your app’s animations](/documentation/swiftui/unifying-your-app-s-animations): Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [NSHostingController](/documentation/swiftui/nshostingcontroller): An AppKit view controller that hosts SwiftUI view hierarchy.
- [NSHostingView](/documentation/swiftui/nshostingview): An AppKit view that hosts a SwiftUI view hierarchy.
- [NSHostingMenu](/documentation/swiftui/nshostingmenu): An AppKit menu with menu items that are defined by a SwiftUI View.
- [NSHostingSceneRepresentation](/documentation/swiftui/nshostingscenerepresentation): An AppKit type that hosts and can present SwiftUI scenes
- [NSHostingSceneBridgingOptions](/documentation/swiftui/nshostingscenebridgingoptions): Options for how hosting views and controllers manage aspects of the associated window.
