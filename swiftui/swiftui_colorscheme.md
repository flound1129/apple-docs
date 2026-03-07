# ColorScheme

The possible color schemes, corresponding to the light and dark appearances.

```swift
enum ColorScheme
```

## Overview

You receive a color scheme value when you read the [colorScheme](/documentation/swiftui/environmentvalues/colorscheme) environment value. The value tells you if a light or dark appearance currently applies to the view. SwiftUI updates the value whenever the appearance changes, and redraws views that depend on the value. For example, the following [Text](/documentation/swiftui/text) view automatically updates when the user enables Dark Mode:

```swift
@Environment(\.colorScheme) private var colorScheme

var body: some View {
    Text(colorScheme == .dark ? "Dark" : "Light")
}
```

Set a preferred appearance for a particular view hierarchy to override the user’s Dark Mode setting using the [preferredColorScheme(_:)](/documentation/swiftui/view/preferredcolorscheme(_:)) view modifier.

### Getting color schemes

- [ColorScheme.light](/documentation/swiftui/colorscheme/light): The color scheme that corresponds to a light appearance.
- [ColorScheme.dark](/documentation/swiftui/colorscheme/dark): The color scheme that corresponds to a dark appearance.

### Creating a color scheme

- [init(_:)](/documentation/swiftui/colorscheme/init(_:)): Creates a color scheme from its user interface style equivalent.

### Supporting types

- [PreferredColorSchemeKey](/documentation/swiftui/preferredcolorschemekey): A key for specifying the preferred color scheme.

## See Also

### Detecting and requesting the light or dark appearance

- [preferredColorScheme(_:)](/documentation/swiftui/view/preferredcolorscheme(_:)): Sets the preferred color scheme for this presentation.
- [colorScheme](/documentation/swiftui/environmentvalues/colorscheme): The color scheme of this environment.
