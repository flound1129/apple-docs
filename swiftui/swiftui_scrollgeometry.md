# ScrollGeometry

A type that defines the geometry of a scroll view.

```swift
struct ScrollGeometry
```

## Overview

SwiftUI provides you values of this type when using modifiers like `View/onScrollGeometryChange(_:action:)` or [onScrollPhaseChange(_:)](/documentation/swiftui/view/onscrollphasechange(_:)).

### Initializers

- [init(contentOffset:contentSize:contentInsets:containerSize:)](/documentation/swiftui/scrollgeometry/init(contentoffset:contentsize:contentinsets:containersize:)): Creates a scroll geometry.

### Instance Properties

- [bounds](/documentation/swiftui/scrollgeometry/bounds): The bounds rect of the scroll view.
- [containerSize](/documentation/swiftui/scrollgeometry/containersize): The size of the container of the scroll view.
- [contentInsets](/documentation/swiftui/scrollgeometry/contentinsets): The content insets of the scroll view.
- [contentOffset](/documentation/swiftui/scrollgeometry/contentoffset): The content offset of the scroll view.
- [contentSize](/documentation/swiftui/scrollgeometry/contentsize): The size of the content of the scroll view.
- [visibleRect](/documentation/swiftui/scrollgeometry/visiblerect): The visible rect of the scroll view.

## See Also

### Responding to scroll view changes

- [onScrollGeometryChange(for:of:action:)](/documentation/swiftui/view/onscrollgeometrychange(for:of:action:)): Adds an action to be performed when a value, created from a scroll geometry, changes.
- [onScrollTargetVisibilityChange(idType:threshold:_:)](/documentation/swiftui/view/onscrolltargetvisibilitychange(idtype:threshold:_:)): Adds an action to be called with information about what views would be considered visible.
- [onScrollVisibilityChange(threshold:_:)](/documentation/swiftui/view/onscrollvisibilitychange(threshold:_:)): Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [onScrollPhaseChange(_:)](/documentation/swiftui/view/onscrollphasechange(_:)): Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [ScrollPhase](/documentation/swiftui/scrollphase): A type that describes the state of a scroll gesture of a scrollable view like a scroll view.
- [ScrollPhaseChangeContext](/documentation/swiftui/scrollphasechangecontext): A type that provides you with more content when the phase of a scroll view changes.
