# ProgressViewStyle

A type that applies standard interaction behavior to all progress views within a view hierarchy.

```swift
@MainActor @preconcurrency protocol ProgressViewStyle
```

## Overview

To configure the current progress view style for a view hierarchy, use the [progressViewStyle(_:)](/documentation/swiftui/view/progressviewstyle(_:)) modifier.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

### Getting built-in progress view styles

- [automatic](/documentation/swiftui/progressviewstyle/automatic): The default progress view style in the current context of the view being styled.
- [circular](/documentation/swiftui/progressviewstyle/circular): The style of a progress view that uses a circular gauge to indicate the partial completion of an activity.
- [linear](/documentation/swiftui/progressviewstyle/linear): A progress view that visually indicates its progress using a horizontal bar.

### Creating custom progress view styles

- [makeBody(configuration:)](/documentation/swiftui/progressviewstyle/makebody(configuration:)): Creates a view representing the body of a progress view.
- [ProgressViewStyle.Configuration](/documentation/swiftui/progressviewstyle/configuration): A type alias for the properties of a progress view instance.
- [Body](/documentation/swiftui/progressviewstyle/body): A view representing the body of a progress view.

### Supporting types

- [DefaultProgressViewStyle](/documentation/swiftui/defaultprogressviewstyle): The default progress view style in the current context of the view being styled.
- [CircularProgressViewStyle](/documentation/swiftui/circularprogressviewstyle): A progress view that uses a circular gauge to indicate the partial completion of an activity.
- [LinearProgressViewStyle](/documentation/swiftui/linearprogressviewstyle): A progress view that visually indicates its progress using a horizontal bar.

## See Also

### Styling indicators

- [gaugeStyle(_:)](/documentation/swiftui/view/gaugestyle(_:)): Sets the style for gauges within this view.
- [GaugeStyle](/documentation/swiftui/gaugestyle): Defines the implementation of all gauge instances within a view hierarchy.
- [GaugeStyleConfiguration](/documentation/swiftui/gaugestyleconfiguration): The properties of a gauge instance.
- [progressViewStyle(_:)](/documentation/swiftui/view/progressviewstyle(_:)): Sets the style for progress views in this view.
- [ProgressViewStyleConfiguration](/documentation/swiftui/progressviewstyleconfiguration): The properties of a progress view instance.
