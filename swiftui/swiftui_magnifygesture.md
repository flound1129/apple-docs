# MagnifyGesture

A gesture that recognizes a magnification motion and tracks the amount of magnification.

```swift
struct MagnifyGesture
```

## Overview

A magnify gesture tracks how a magnification event sequence changes. To recognize a magnify gesture on a view, create and configure the gesture, and then add it to the view using the [gesture(_:including:)](/documentation/swiftui/view/gesture(_:including:)) modifier.

Add a magnify gesture to a [Circle](/documentation/swiftui/circle) that changes its size while the user performs the gesture:

```swift
struct MagnifyGestureView: View {
    @GestureState private var magnifyBy = 1.0

    var magnification: some Gesture {
        MagnifyGesture()
            .updating($magnifyBy) { value, gestureState, transaction in
                gestureState = value.magnification
            }
    }

    var body: some View {
        Circle()
            .frame(width: 100, height: 100)
            .scaleEffect(magnifyBy)
            .gesture(magnification)
    }
}
```

### Creating the gesture

- [init(minimumScaleDelta:)](/documentation/swiftui/magnifygesture/init(minimumscaledelta:)): Creates a magnify gesture with a given minimum delta for the gesture to start.
- [minimumScaleDelta](/documentation/swiftui/magnifygesture/minimumscaledelta): The minimum required delta before the gesture starts.

## See Also

### Recognizing gestures that change over time

- [gesture(_:)](/documentation/swiftui/view/gesture(_:)): Attaches an [NSGestureRecognizerRepresentable](/documentation/swiftui/nsgesturerecognizerrepresentable) to the view.
- [gesture(_:isEnabled:)](/documentation/swiftui/view/gesture(_:isenabled:)): Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:name:isEnabled:)](/documentation/swiftui/view/gesture(_:name:isenabled:)): Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:including:)](/documentation/swiftui/view/gesture(_:including:)): Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [DragGesture](/documentation/swiftui/draggesture): A dragging motion that invokes an action as the drag-event sequence changes.
- [WindowDragGesture](/documentation/swiftui/windowdraggesture): A gesture that recognizes the motion of and handles dragging a window.
- [RotateGesture](/documentation/swiftui/rotategesture): A gesture that recognizes a rotation motion and tracks the angle of the rotation.
- [RotateGesture3D](/documentation/swiftui/rotategesture3d): A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.
- [GestureMask](/documentation/swiftui/gesturemask): Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.
