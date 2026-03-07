# AnyGesture

A type-erased gesture.

```swift
@frozen struct AnyGesture<Value>
```

### Implementing a custom gesture

- [init(_:)](/documentation/swiftui/anygesture/init(_:)): Creates an instance from another gesture.

## See Also

### Defining custom gestures

- [highPriorityGesture(_:including:)](/documentation/swiftui/view/highprioritygesture(_:including:)): Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:isEnabled:)](/documentation/swiftui/view/highprioritygesture(_:isenabled:)): Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:name:isEnabled:)](/documentation/swiftui/view/highprioritygesture(_:name:isenabled:)): Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [handGestureShortcut(_:isEnabled:)](/documentation/swiftui/view/handgestureshortcut(_:isenabled:)): Assigns a hand gesture shortcut to the modified control.
- [defersSystemGestures(on:)](/documentation/swiftui/view/deferssystemgestures(on:)): Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [Gesture](/documentation/swiftui/gesture): An instance that matches a sequence of events to a gesture, and returns a stream of values for each of its states.
- [HandActivationBehavior](/documentation/swiftui/handactivationbehavior): An activation behavior specific to hand-driven input.
- [HandGestureShortcut](/documentation/swiftui/handgestureshortcut): Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.
