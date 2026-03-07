# UIHostingControllerSizingOptions

Options for how a hosting controller tracks its content’s size.

```swift
struct UIHostingControllerSizingOptions
```

### Getting sizing options

- [intrinsicContentSize](/documentation/swiftui/uihostingcontrollersizingoptions/intrinsiccontentsize): The hosting controller’s view automatically invalidate its intrinsic content size when its ideal size changes.
- [preferredContentSize](/documentation/swiftui/uihostingcontrollersizingoptions/preferredcontentsize): The hosting controller tracks its content’s ideal size in its preferred content size.

### Creating a sizing option

- [init(rawValue:)](/documentation/swiftui/uihostingcontrollersizingoptions/init(rawvalue:)): Creates a new option set from a raw value.
- [rawValue](/documentation/swiftui/uihostingcontrollersizingoptions/rawvalue): The raw value.

## See Also

### Displaying SwiftUI views in UIKit

- [Using SwiftUI with UIKit](/documentation/UIKit/using-swiftui-with-uikit): Learn how to incorporate SwiftUI views into a UIKit app.
- [Unifying your app’s animations](/documentation/swiftui/unifying-your-app-s-animations): Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [UIHostingController](/documentation/swiftui/uihostingcontroller): A UIKit view controller that manages a SwiftUI view hierarchy.
- [UIHostingConfiguration](/documentation/swiftui/uihostingconfiguration): A content configuration suitable for hosting a hierarchy of SwiftUI views.
- [UIHostingSceneDelegate](/documentation/swiftui/uihostingscenedelegate): Extends `UIKit/UISceneDelegate` to bridge SwiftUI scenes.
