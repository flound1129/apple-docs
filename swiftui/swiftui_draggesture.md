# DragGesture

A dragging motion that invokes an action as the drag-event sequence changes.

```swift
struct DragGesture
```

## Overview

To recognize a drag gesture on a view, create and configure the gesture, and then add it to the view using the [gesture(_:including:)](/documentation/swiftui/view/gesture(_:including:)) modifier.

Add a drag gesture to a [Circle](/documentation/swiftui/circle) and change its color while the user performs the drag gesture:

```swift
struct DragGestureView: View {
    @State private var isDragging = false

    var drag: some Gesture {
        DragGesture()
            .onChanged { _ in self.isDragging = true }
            .onEnded { _ in self.isDragging = false }
    }

    var body: some View {
        Circle()
            .fill(self.isDragging ? Color.red : Color.blue)
            .frame(width: 100, height: 100, alignment: .center)
            .gesture(drag)
    }
}
```

### Creating a drag gesture

- [init(minimumDistance:coordinateSpace:)](/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace:)-8ffe5): Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [minimumDistance](/documentation/swiftui/draggesture/minimumdistance): The minimum dragging distance before the gesture succeeds.
- [coordinateSpace](/documentation/swiftui/draggesture/coordinatespace): The coordinate space in which to receive location values.

### Deprecated initializers

- [init(minimumDistance:coordinateSpace:)](/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace:)-3804h): Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.

### Structures

- [DragGesture.Value](/documentation/swiftui/draggesture/value): The attributes of a drag gesture.

### Initializers

- [init(minimumDistance:coordinateSpace3D:)](/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace3d:)): Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance:coordinateSpace:)](/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace:)): Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.

## See Also

### Recognizing gestures that change over time

- [gesture(_:)](/documentation/swiftui/view/gesture(_:)): Attaches an [NSGestureRecognizerRepresentable](/documentation/swiftui/nsgesturerecognizerrepresentable) to the view.
- [gesture(_:isEnabled:)](/documentation/swiftui/view/gesture(_:isenabled:)): Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:name:isEnabled:)](/documentation/swiftui/view/gesture(_:name:isenabled:)): Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:including:)](/documentation/swiftui/view/gesture(_:including:)): Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [WindowDragGesture](/documentation/swiftui/windowdraggesture): A gesture that recognizes the motion of and handles dragging a window.
- [MagnifyGesture](/documentation/swiftui/magnifygesture): A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [RotateGesture](/documentation/swiftui/rotategesture): A gesture that recognizes a rotation motion and tracks the angle of the rotation.
- [RotateGesture3D](/documentation/swiftui/rotategesture3d): A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.
- [GestureMask](/documentation/swiftui/gesturemask): Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.
