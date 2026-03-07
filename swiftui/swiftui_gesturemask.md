# GestureMask

Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.

```swift
@frozen struct GestureMask
```

### Getting gesture options

- [all](/documentation/swiftui/gesturemask/all): Enable both the added gesture as well as all other gestures on the view and its subviews.
- [gesture](/documentation/swiftui/gesturemask/gesture): Enable the added gesture but disable all gestures in the subview hierarchy.
- [subviews](/documentation/swiftui/gesturemask/subviews): Enable all gestures in the subview hierarchy but disable the added gesture.
- [none](/documentation/swiftui/gesturemask/none): Disable all gestures in the subview hierarchy, including the added gesture.

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
- [RotateGesture3D](/documentation/swiftui/rotategesture3d): A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.
