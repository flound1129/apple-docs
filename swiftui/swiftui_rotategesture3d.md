# RotateGesture3D

A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.

```swift
struct RotateGesture3D
```

## Overview

You can constrain this gesture to recognize rotation about a specific 3D axis. For example, `RotateGesture3D(constrainedToAxis: .x)` creates a gesture that recognizes rotation only around the global X axis. The axis you provide will be normalized.

A rotation gesture tracks how a rotation event sequence changes. To recognize a rotation gesture on a view, create and configure the gesture, and then add it to the view using the [gesture(_:including:)](/documentation/swiftui/view/gesture(_:including:)) modifier.

### Creating the gesture

- [init(constrainedToAxis:minimumAngleDelta:)](/documentation/swiftui/rotategesture3d/init(constrainedtoaxis:minimumangledelta:)): Creates a rotation gesture with a minimum delta for the gesture to start and axis to constrain measurement of rotation.
- [minimumAngleDelta](/documentation/swiftui/rotategesture3d/minimumangledelta): The minimum angle delta before the gesture becomes active.
- [constrainedAxis](/documentation/swiftui/rotategesture3d/constrainedaxis): An axis around which the rotation is constrained.

## See Also

### Recognizing gestures that change over time

- [gesture(_:)](/documentation/swiftui/view/gesture(_:)): Attaches an [NSGestureRecognizerRepresentable](/documentation/swiftui/nsgesturerecognizerrepresentable) to the view.
- [gesture(_:isEnabled:)](/documentation/swiftui/view/gesture(_:isenabled:)): Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:name:isEnabled:)](/documentation/swiftui/view/gesture(_:name:isenabled:)): Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:including:)](/documentation/swiftui/view/gesture(_:including:)): Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [DragGesture](/documentation/swiftui/draggesture): A dragging motion that invokes an action as the drag-event sequence changes.
- [WindowDragGesture](/documentation/swiftui/windowdraggesture): A gesture that recognizes the motion of and handles dragging a window.
- [MagnifyGesture](/documentation/swiftui/magnifygesture): A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [RotateGesture](/documentation/swiftui/rotategesture): A gesture that recognizes a rotation motion and tracks the angle of the rotation.
- [GestureMask](/documentation/swiftui/gesturemask): Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.
