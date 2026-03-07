# ScrollAnchorRole

A type defining the role of a scroll anchor.

```swift
struct ScrollAnchorRole
```

## Overview

You can associate a [UnitPoint](/documentation/swiftui/unitpoint) to a [ScrollView](/documentation/swiftui/scrollview) using the [defaultScrollAnchor(_:)](/documentation/swiftui/view/defaultscrollanchor(_:)) modifier. By default, the system uses this point for different kinds of behaviors including:

- Where the scroll view should initially be scrolled
- How the scroll view should handle content size or container size changes
- How the scroll view should align content smaller than its container size

You can further customize this behavior by assigning different unit points for these different roles.

### Type Properties

- [alignment](/documentation/swiftui/scrollanchorrole/alignment): The role that influences how a scroll view should align its content when the size of its content is smaller than the container size of the scroll view.
- [initialOffset](/documentation/swiftui/scrollanchorrole/initialoffset): The role that influences where a scroll view should be initially scrolled.
- [sizeChanges](/documentation/swiftui/scrollanchorrole/sizechanges): The role that influences how a scroll view should adjust its content offset when the scroll view’s content or container size changes.

## See Also

### Managing scroll position

- [scrollPosition(_:anchor:)](/documentation/swiftui/view/scrollposition(_:anchor:)): Associates a binding to a scroll position with a scroll view within this view.
- [scrollPosition(id:anchor:)](/documentation/swiftui/view/scrollposition(id:anchor:)): Associates a binding to be updated when a scroll view within this view scrolls.
- [defaultScrollAnchor(_:)](/documentation/swiftui/view/defaultscrollanchor(_:)): Associates an anchor to control which part of the scroll view’s content should be rendered by default.
- [defaultScrollAnchor(_:for:)](/documentation/swiftui/view/defaultscrollanchor(_:for:)): Associates an anchor to control the position of a scroll view in a particular circumstance.
- [ScrollPosition](/documentation/swiftui/scrollposition): A type that defines the semantic position of where a scroll view is scrolled within its content.
