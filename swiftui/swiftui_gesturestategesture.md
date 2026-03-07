# GestureStateGesture

A gesture that updates the state provided by a gesture’s updating callback.

```swift
@frozen struct GestureStateGesture<Base, State> where Base : Gesture
```

## Overview

A gesture’s [updating(_:body:)](/documentation/swiftui/gesture/updating(_:body:)) callback returns a `GestureStateGesture` instance for updating a transient state property that’s annotated with the [GestureState](/documentation/swiftui/gesturestate) property wrapper.

### Creating an in-progress gesture

- [init(base:state:body:)](/documentation/swiftui/gesturestategesture/init(base:state:body:)): Creates a new gesture that’s the result of an ongoing gesture.
- [base](/documentation/swiftui/gesturestategesture/base): The originating gesture.
- [state](/documentation/swiftui/gesturestategesture/state): A value that changes as the user performs the gesture.

### Supporting types

- [body](/documentation/swiftui/gesturestategesture/body): The updating gesture containing the originating gesture’s value, the updated state of the gesture, and a transaction.

## See Also

### Managing gesture state

- [GestureState](/documentation/swiftui/gesturestate): A property wrapper type that updates a property while the user performs a gesture and resets the property back to its initial state when the gesture ends.
