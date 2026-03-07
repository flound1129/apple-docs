# ColorSchemeContrast

The contrast between the app’s foreground and background colors.

```swift
enum ColorSchemeContrast
```

## Overview

You receive a contrast value when you read the [colorSchemeContrast](/documentation/swiftui/environmentvalues/colorschemecontrast) environment value. The value tells you if a standard or increased contrast currently applies to the view. SwiftUI updates the value whenever the contrast changes, and redraws views that depend on the value. For example, the following [Text](/documentation/swiftui/text) view automatically updates when the user enables increased contrast:

```swift
@Environment(\.colorSchemeContrast) private var colorSchemeContrast

var body: some View {
    Text(colorSchemeContrast == .standard ? "Standard" : "Increased")
}
```

The user sets the contrast by selecting the Increase Contrast option in Accessibility > Display in System Preferences on macOS, or Accessibility > Display & Text Size in the Settings app on iOS. Your app can’t override the user’s choice. For information about using color and contrast in your app, see [Accessibility](/design/Human-Interface-Guidelines/accessibility#Color-and-effects) in the Human Interface Guidelines.

### Getting contrast options

- [ColorSchemeContrast.standard](/documentation/swiftui/colorschemecontrast/standard): SwiftUI displays views with standard contrast between the app’s foreground and background colors.
- [ColorSchemeContrast.increased](/documentation/swiftui/colorschemecontrast/increased): SwiftUI displays views with increased contrast between the app’s foreground and background colors.

### Creating a color scheme contrast

- [init(_:)](/documentation/swiftui/colorschemecontrast/init(_:)): Creates a contrast from its accessibility contrast equivalent.

## See Also

### Getting the color scheme contrast

- [colorSchemeContrast](/documentation/swiftui/environmentvalues/colorschemecontrast): The contrast associated with the color scheme of this environment.
