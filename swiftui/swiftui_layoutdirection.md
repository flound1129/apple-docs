# LayoutDirection

A direction in which SwiftUI can lay out content.

```swift
enum LayoutDirection
```

## Overview

SwiftUI supports both left-to-right and right-to-left directions for laying out content to support different languages and locales. The system sets the value based on the user’s locale, but you can also use the [environment(_:_:)](/documentation/swiftui/view/environment(_:_:)) modifier to override the direction for a view and its child views:

```swift
MyView()
    .environment(\.layoutDirection, .rightToLeft)
```

You can also read the [layoutDirection](/documentation/swiftui/environmentvalues/layoutdirection) environment value to find out which direction applies to a particular environment. However, in many cases, you don’t need to take any action based on this value. SwiftUI horizontally flips the x position of each view within its parent, so layout calculations automatically produce the desired effect for both modes without any changes.

### Getting layout directions

- [LayoutDirection.leftToRight](/documentation/swiftui/layoutdirection/lefttoright): A left-to-right layout direction.
- [LayoutDirection.rightToLeft](/documentation/swiftui/layoutdirection/righttoleft): A right-to-left layout direction.

### Creating a layout direction

- [init(_:)](/documentation/swiftui/layoutdirection/init(_:)): Create a direction from its UITraitEnvironmentLayoutDirection equivalent.

## See Also

### Setting a layout direction

- [layoutDirectionBehavior(_:)](/documentation/swiftui/view/layoutdirectionbehavior(_:)): Sets the behavior of this view for different layout directions.
- [LayoutDirectionBehavior](/documentation/swiftui/layoutdirectionbehavior): A description of what should happen when the layout direction changes.
- [layoutDirection](/documentation/swiftui/environmentvalues/layoutdirection): The layout direction associated with the current environment.
- [LayoutRotationUnaryLayout](/documentation/swiftui/layoutrotationunarylayout)
