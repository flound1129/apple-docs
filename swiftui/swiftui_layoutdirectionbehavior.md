# LayoutDirectionBehavior

A description of what should happen when the layout direction changes.

```swift
enum LayoutDirectionBehavior
```

## Overview

A `LayoutDirectionBehavior` can be used with the `layoutDirectionBehavior` view modifier or the `layoutDirectionBehavior` property of `Shape`.

### Getting behaviors

- [LayoutDirectionBehavior.fixed](/documentation/swiftui/layoutdirectionbehavior/fixed): A behavior that doesn’t mirror when the layout direction changes.
- [mirrors](/documentation/swiftui/layoutdirectionbehavior/mirrors): A behavior that mirrors when the layout direction is right-to-left.
- [LayoutDirectionBehavior.mirrors(in:)](/documentation/swiftui/layoutdirectionbehavior/mirrors(in:)): A behavior that mirrors when the layout direction has the specified value.

## See Also

### Setting a layout direction

- [layoutDirectionBehavior(_:)](/documentation/swiftui/view/layoutdirectionbehavior(_:)): Sets the behavior of this view for different layout directions.
- [layoutDirection](/documentation/swiftui/environmentvalues/layoutdirection): The layout direction associated with the current environment.
- [LayoutDirection](/documentation/swiftui/layoutdirection): A direction in which SwiftUI can lay out content.
- [LayoutRotationUnaryLayout](/documentation/swiftui/layoutrotationunarylayout)
