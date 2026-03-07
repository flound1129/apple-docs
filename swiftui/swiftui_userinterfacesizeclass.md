# UserInterfaceSizeClass

A set of values that indicate the visual size available to the view.

```swift
enum UserInterfaceSizeClass
```

## Overview

You receive a size class value when you read either the [horizontalSizeClass](/documentation/swiftui/environmentvalues/horizontalsizeclass) or [verticalSizeClass](/documentation/swiftui/environmentvalues/verticalsizeclass) environment value. The value tells you about the amount of space available to your views in a given direction. You can read the size class like any other of the [EnvironmentValues](/documentation/swiftui/environmentvalues), by creating a property with the [Environment](/documentation/swiftui/environment) property wrapper:

```swift
@Environment(\.horizontalSizeClass) private var horizontalSizeClass
@Environment(\.verticalSizeClass) private var verticalSizeClass
```

SwiftUI sets the size class based on several factors, including:

- The current device type.
- The orientation of the device.
- The appearance of Slide Over and Split View on iPad.

Several built-in views change their behavior based on the size class. For example, a [NavigationView](/documentation/swiftui/navigationview) presents a multicolumn view when the horizontal size class is [UserInterfaceSizeClass.regular](/documentation/swiftui/userinterfacesizeclass/regular), but a single column otherwise. You can also adjust the appearance of custom views by reading the size class and conditioning your views. If you do, be prepared to handle size class changes while your app runs, because factors like device orientation can change at runtime.

### Getting size classes

- [UserInterfaceSizeClass.compact](/documentation/swiftui/userinterfacesizeclass/compact): The compact size class.
- [UserInterfaceSizeClass.regular](/documentation/swiftui/userinterfacesizeclass/regular): The regular size class.

### Creating a size class

- [init(_:)](/documentation/swiftui/userinterfacesizeclass/init(_:)): Creates a SwiftUI size class from the specified UIKit size class.

## See Also

### Reacting to interface characteristics

- [isLuminanceReduced](/documentation/swiftui/environmentvalues/isluminancereduced): A Boolean value that indicates whether the display or environment currently requires reduced luminance.
- [displayScale](/documentation/swiftui/environmentvalues/displayscale): The display scale of this environment.
- [pixelLength](/documentation/swiftui/environmentvalues/pixellength): The size of a pixel on the screen.
- [horizontalSizeClass](/documentation/swiftui/environmentvalues/horizontalsizeclass): The horizontal size class of this environment.
- [verticalSizeClass](/documentation/swiftui/environmentvalues/verticalsizeclass): The vertical size class of this environment.
