# ScrollPhase

A type that describes the state of a scroll gesture of a scrollable view like a scroll view.

```swift
@frozen enum ScrollPhase
```

## Overview

A scroll gesture can be in one of four phases: - idle: No active scroll is occurring. - panning: An active scroll being driven by the user is occurring. - decelerating: The user has stopped driving a scroll and the scroll view is decelerating to its final target. - animating: The system is animating to a final target as a result of a programmatic animated scroll from using a [ScrollViewReader](/documentation/swiftui/scrollviewreader) or [scrollPosition(id:anchor:)](/documentation/swiftui/view/scrollposition(id:anchor:)) modifier.

SwiftUI provides you a value of this type when using the [onScrollPhaseChange(_:)](/documentation/swiftui/view/onscrollphasechange(_:)) modifier.

### Getting scroll gesture states

- [ScrollPhase.animating](/documentation/swiftui/scrollphase/animating): The animating phase where the scroll view is animating towards a final target.
- [ScrollPhase.decelerating](/documentation/swiftui/scrollphase/decelerating): The decelerating phase where the user use has stopped interacting with the scroll view and the scroll view is decelerating towards its final target.
- [ScrollPhase.idle](/documentation/swiftui/scrollphase/idle): The idle phase where no kind of scrolling is occurring.
- [ScrollPhase.interacting](/documentation/swiftui/scrollphase/interacting): The interacting phase where the user is interacting with the scroll view.
- [ScrollPhase.tracking](/documentation/swiftui/scrollphase/tracking): The tracking phase where the scroll view is tracking a potential scroll by the user but the user hasn’t started a scroll.

### Checking for active scrolling

- [isScrolling](/documentation/swiftui/scrollphase/isscrolling): Whether the scroll view is actively scrolling.

## See Also

### Responding to scroll view changes

- [onScrollGeometryChange(for:of:action:)](/documentation/swiftui/view/onscrollgeometrychange(for:of:action:)): Adds an action to be performed when a value, created from a scroll geometry, changes.
- [onScrollTargetVisibilityChange(idType:threshold:_:)](/documentation/swiftui/view/onscrolltargetvisibilitychange(idtype:threshold:_:)): Adds an action to be called with information about what views would be considered visible.
- [onScrollVisibilityChange(threshold:_:)](/documentation/swiftui/view/onscrollvisibilitychange(threshold:_:)): Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [onScrollPhaseChange(_:)](/documentation/swiftui/view/onscrollphasechange(_:)): Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [ScrollGeometry](/documentation/swiftui/scrollgeometry): A type that defines the geometry of a scroll view.
- [ScrollPhaseChangeContext](/documentation/swiftui/scrollphasechangecontext): A type that provides you with more content when the phase of a scroll view changes.
