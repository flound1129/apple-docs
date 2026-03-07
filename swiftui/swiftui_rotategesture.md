# RotateGesture

A gesture that recognizes a rotation motion and tracks the angle of the rotation.

```swift
struct RotateGesture
```

## Overview

A rotate gesture tracks how a rotation event sequence changes. To recognize a rotate gesture on a view, create and configure the gesture, and then add it to the view using the [gesture(_:including:)](/documentation/swiftui/view/gesture(_:including:)) modifier.

Add a rotate gesture to a [Rectangle](/documentation/swiftui/rectangle) and apply a rotation effect:

```swift
struct RotateGestureView: View {
    @State private var angle = Angle(degrees: 0.0)

    var rotation: some Gesture {
        RotateGesture()
            .onChanged { value in
                angle = value.rotation
            }
    }

    var body: some View {
        Rectangle()
            .frame(width: 200, height: 200, alignment: .center)
            .rotationEffect(angle)
            .gesture(rotation)
    }
}
```

### Creating the gesture

- [init(minimumAngleDelta:)](/documentation/swiftui/rotategesture/init(minimumangledelta:)): Creates a rotation gesture with a minimum delta for the gesture to start.
- [minimumAngleDelta](/documentation/swiftui/rotategesture/minimumangledelta): The minimum delta required before the gesture succeeds.

## See Also

### Recognizing gestures that change over time

- [gesture(_:)](/documentation/swiftui/view/gesture(_:)): Attaches an [NSGestureRecognizerRepresentable](/documentation/swiftui/nsgesturerecognizerrepresentable) to the view.
- [gesture(_:isEnabled:)](/documentation/swiftui/view/gesture(_:isenabled:)): Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:name:isEnabled:)](/documentation/swiftui/view/gesture(_:name:isenabled:)): Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:including:)](/documentation/swiftui/view/gesture(_:including:)): Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [DragGesture](/documentation/swiftui/draggesture): A dragging motion that invokes an action as the drag-event sequence changes.
- [WindowDragGesture](/documentation/swiftui/windowdraggesture): A gesture that recognizes the motion of and handles dragging a window.
- [MagnifyGesture](/documentation/swiftui/magnifygesture): A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [RotateGesture3D](/documentation/swiftui/rotategesture3d): A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.
- [GestureMask](/documentation/swiftui/gesturemask): Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.
