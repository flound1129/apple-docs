# ScrollPhaseChangeContext

A type that provides you with more content when the phase of a scroll view changes.

```swift
struct ScrollPhaseChangeContext
```

## Overview

You don’t create this type directly. Instead, SwiftUI provides an instance of this type in the [onScrollPhaseChange(_:)](/documentation/swiftui/view/onscrollphasechange(_:)) modifier.

### Instance Properties

- [geometry](/documentation/swiftui/scrollphasechangecontext/geometry): The geometry of the scroll view at the time of the scroll phase change.
- [velocity](/documentation/swiftui/scrollphasechangecontext/velocity): The velocity of the scroll view at the time of the scroll phase change.

## See Also

### Responding to scroll view changes

- [onScrollGeometryChange(for:of:action:)](/documentation/swiftui/view/onscrollgeometrychange(for:of:action:)): Adds an action to be performed when a value, created from a scroll geometry, changes.
- [onScrollTargetVisibilityChange(idType:threshold:_:)](/documentation/swiftui/view/onscrolltargetvisibilitychange(idtype:threshold:_:)): Adds an action to be called with information about what views would be considered visible.
- [onScrollVisibilityChange(threshold:_:)](/documentation/swiftui/view/onscrollvisibilitychange(threshold:_:)): Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [onScrollPhaseChange(_:)](/documentation/swiftui/view/onscrollphasechange(_:)): Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [ScrollGeometry](/documentation/swiftui/scrollgeometry): A type that defines the geometry of a scroll view.
- [ScrollPhase](/documentation/swiftui/scrollphase): A type that describes the state of a scroll gesture of a scrollable view like a scroll view.
