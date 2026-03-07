# Gesture

An instance that matches a sequence of events to a gesture, and returns a stream of values for each of its states.

```swift
@MainActor @preconcurrency protocol Gesture<Value>
```

## Overview

Create custom gestures by declaring types that conform to the `Gesture` protocol.

### Implementing a custom gesture

- [body](/documentation/swiftui/gesture/body-swift.property): The content and behavior of the gesture.
- [Body](/documentation/swiftui/gesture/body-swift.associatedtype): The type of gesture representing the body of `Self`.

### Performing the gesture

- [updating(_:body:)](/documentation/swiftui/gesture/updating(_:body:)): Updates the provided gesture state property as the gesture’s value changes.
- [onChanged(_:)](/documentation/swiftui/gesture/onchanged(_:)): Adds an action to perform when the gesture’s value changes.
- [onEnded(_:)](/documentation/swiftui/gesture/onended(_:)): Adds an action to perform when the gesture ends.
- [Value](/documentation/swiftui/gesture/value): The type representing the gesture’s value.

### Composing gestures

- [simultaneously(with:)](/documentation/swiftui/gesture/simultaneously(with:)): Combines a gesture with another gesture to create a new gesture that recognizes both gestures at the same time.
- [sequenced(before:)](/documentation/swiftui/gesture/sequenced(before:)): Sequences a gesture with another one to create a new gesture, which results in the second gesture only receiving events after the first gesture succeeds.
- [exclusively(before:)](/documentation/swiftui/gesture/exclusively(before:)): Combines two gestures exclusively to create a new gesture where only one gesture succeeds, giving precedence to the first gesture.

### Adding modifier keys to a gesture

- [modifiers(_:)](/documentation/swiftui/gesture/modifiers(_:)): Combines a gesture with keyboard modifiers.

### Transforming a gesture

- [map(_:)](/documentation/swiftui/gesture/map(_:)): Returns a gesture that uses the given closure to map over this gesture’s value.

### Customizing gesture activation

- [handActivationBehavior(_:)](/documentation/swiftui/gesture/handactivationbehavior(_:)): Customizes the activation behavior for a gesture when driven by hand or hand-like input.

### Using a gesture with a RealityKit entity

- [targetedToAnyEntity()](/documentation/swiftui/gesture/targetedtoanyentity()): Requires this gesture to target an entity.
- [targetedToEntity(_:)](/documentation/swiftui/gesture/targetedtoentity(_:)): Requires this gesture to target an entity or a descendant of entity.
- [targetedToEntity(where:)](/documentation/swiftui/gesture/targetedtoentity(where:)): Requires this gesture to target an entity that can be found in the results of the query.

## See Also

### Defining custom gestures

- [highPriorityGesture(_:including:)](/documentation/swiftui/view/highprioritygesture(_:including:)): Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:isEnabled:)](/documentation/swiftui/view/highprioritygesture(_:isenabled:)): Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:name:isEnabled:)](/documentation/swiftui/view/highprioritygesture(_:name:isenabled:)): Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [handGestureShortcut(_:isEnabled:)](/documentation/swiftui/view/handgestureshortcut(_:isenabled:)): Assigns a hand gesture shortcut to the modified control.
- [defersSystemGestures(on:)](/documentation/swiftui/view/deferssystemgestures(on:)): Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [AnyGesture](/documentation/swiftui/anygesture): A type-erased gesture.
- [HandActivationBehavior](/documentation/swiftui/handactivationbehavior): An activation behavior specific to hand-driven input.
- [HandGestureShortcut](/documentation/swiftui/handgestureshortcut): Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.
