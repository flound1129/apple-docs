# WindowDragGesture

A gesture that recognizes the motion of and handles dragging a window.

```swift
struct WindowDragGesture
```

## Overview

To recognize a window drag gesture on a view, create and configure the gesture, and then add it to the view using the [gesture(_:isEnabled:)](/documentation/swiftui/view/gesture(_:isenabled:)) modifier. Consider also letting the gesture [allowsWindowActivationEvents(_:)](/documentation/SwiftUI/View/allowsWindowActivationEvents(_:)) so that dragging the containing window works even when it’s inactive.

To add a window drag gesture to a [Circle](/documentation/swiftui/circle) and change its color while a user performs the window drag gesture:

```swift
struct MyView: View {
    @GestureState var isDraggingWindow = false

    var dragWindow: some Gesture {
        WindowDragGesture()
            .updating($isDraggingWindow) { _, state, _ in
                state = true
            }
    }

    var body: some View {
        Circle()
            .fill(isDraggingWindow ? Color.green : .blue)
            .frame(width: 50, height: 50)
            .gesture(dragWindow)
            .allowsWindowActivationEvents()
    }
}
```

### Structures

- [WindowDragGesture.Value](/documentation/swiftui/windowdraggesture/value): The properties of a window drag gesture.

### Initializers

- [init()](/documentation/swiftui/windowdraggesture/init()): Creates a window drag gesture.

## See Also

### Recognizing gestures that change over time

- [gesture(_:)](/documentation/swiftui/view/gesture(_:)): Attaches an [NSGestureRecognizerRepresentable](/documentation/swiftui/nsgesturerecognizerrepresentable) to the view.
- [gesture(_:isEnabled:)](/documentation/swiftui/view/gesture(_:isenabled:)): Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:name:isEnabled:)](/documentation/swiftui/view/gesture(_:name:isenabled:)): Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:including:)](/documentation/swiftui/view/gesture(_:including:)): Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [DragGesture](/documentation/swiftui/draggesture): A dragging motion that invokes an action as the drag-event sequence changes.
- [MagnifyGesture](/documentation/swiftui/magnifygesture): A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [RotateGesture](/documentation/swiftui/rotategesture): A gesture that recognizes a rotation motion and tracks the angle of the rotation.
- [RotateGesture3D](/documentation/swiftui/rotategesture3d): A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.
- [GestureMask](/documentation/swiftui/gesturemask): Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.
