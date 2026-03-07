# ScrollBounceBehavior

The ways that a scrollable view can bounce when it reaches the end of its content.

```swift
struct ScrollBounceBehavior
```

## Overview

Use the [scrollBounceBehavior(_:axes:)](/documentation/swiftui/view/scrollbouncebehavior(_:axes:)) view modifier to set a value of this type for a scrollable view, like a [ScrollView](/documentation/swiftui/scrollview) or a [List](/documentation/swiftui/list). The value configures the bounce behavior when people scroll to the end of the view’s content.

You can configure each scrollable axis to use a different bounce mode.

### Bounce behaviors

- [automatic](/documentation/swiftui/scrollbouncebehavior/automatic): The automatic behavior.
- [always](/documentation/swiftui/scrollbouncebehavior/always): The scrollable view always bounces.
- [basedOnSize](/documentation/swiftui/scrollbouncebehavior/basedonsize): The scrollable view bounces when its content is large enough to require scrolling.

## See Also

### Configuring scroll bounce behavior

- [scrollBounceBehavior(_:axes:)](/documentation/swiftui/view/scrollbouncebehavior(_:axes:)): Configures the bounce behavior of scrollable views along the specified axis.
- [horizontalScrollBounceBehavior](/documentation/swiftui/environmentvalues/horizontalscrollbouncebehavior): The scroll bounce mode for the horizontal axis of scrollable views.
- [verticalScrollBounceBehavior](/documentation/swiftui/environmentvalues/verticalscrollbouncebehavior): The scroll bounce mode for the vertical axis of scrollable views.
