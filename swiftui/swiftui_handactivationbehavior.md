# HandActivationBehavior

An activation behavior specific to hand-driven input.

```swift
struct HandActivationBehavior
```

## Overview

Hand activation behavior determines what hand input modes activate a gesture.

### Getting the behaviors

- [automatic](/documentation/swiftui/handactivationbehavior/automatic): The default activation behavior, including direct touch, direct pinch, and indirect pinch.
- [pinch](/documentation/swiftui/handactivationbehavior/pinch): Activation that requires a pinched hand.

## See Also

### Defining custom gestures

- [highPriorityGesture(_:including:)](/documentation/swiftui/view/highprioritygesture(_:including:)): Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:isEnabled:)](/documentation/swiftui/view/highprioritygesture(_:isenabled:)): Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:name:isEnabled:)](/documentation/swiftui/view/highprioritygesture(_:name:isenabled:)): Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [handGestureShortcut(_:isEnabled:)](/documentation/swiftui/view/handgestureshortcut(_:isenabled:)): Assigns a hand gesture shortcut to the modified control.
- [defersSystemGestures(on:)](/documentation/swiftui/view/deferssystemgestures(on:)): Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [Gesture](/documentation/swiftui/gesture): An instance that matches a sequence of events to a gesture, and returns a stream of values for each of its states.
- [AnyGesture](/documentation/swiftui/anygesture): A type-erased gesture.
- [HandGestureShortcut](/documentation/swiftui/handgestureshortcut): Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.
