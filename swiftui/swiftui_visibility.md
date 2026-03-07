# Visibility

The visibility of a UI element, chosen automatically based on the platform, current context, and other factors.

```swift
@frozen enum Visibility
```

## Overview

For example, the preferred visibility of list row separators can be configured using the [listRowSeparator(_:edges:)](/documentation/swiftui/view/listrowseparator(_:edges:)).

### Getting visibility options

- [Visibility.automatic](/documentation/swiftui/visibility/automatic): The element may be visible or hidden depending on the policies of the component accepting the visibility configuration.
- [Visibility.visible](/documentation/swiftui/visibility/visible): The element may be visible.
- [Visibility.hidden](/documentation/swiftui/visibility/hidden): The element may be hidden.

## See Also

### Hiding system elements

- [labelsHidden()](/documentation/swiftui/view/labelshidden()): Hides the labels of any controls contained within this view.
- [labelsVisibility(_:)](/documentation/swiftui/view/labelsvisibility(_:)): Controls the visibility of labels of any controls contained within this view.
- [labelsVisibility](/documentation/swiftui/environmentvalues/labelsvisibility): The labels visibility set by [labelsVisibility(_:)](/documentation/swiftui/view/labelsvisibility(_:)).
- [menuIndicator(_:)](/documentation/swiftui/view/menuindicator(_:)): Sets the menu indicator visibility for controls within this view.
- [statusBarHidden(_:)](/documentation/swiftui/view/statusbarhidden(_:)): Sets the visibility of the status bar.
- [persistentSystemOverlays(_:)](/documentation/swiftui/view/persistentsystemoverlays(_:)): Sets the preferred visibility of the non-transient system views overlaying the app.
