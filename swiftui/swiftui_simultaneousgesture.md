# SimultaneousGesture

A gesture containing two gestures that can happen at the same time with neither of them preceding the other.

```swift
@frozen struct SimultaneousGesture<First, Second> where First : Gesture, Second : Gesture
```

## Overview

A simultaneous gesture is a container-event handler that evaluates its two child gestures at the same time. Its value is a struct with two optional values, each representing the phases of one of the two gestures.

### Creating the gesture

- [init(_:_:)](/documentation/swiftui/simultaneousgesture/init(_:_:)): Creates a gesture with two gestures that can receive updates or succeed independently of each other.
- [first](/documentation/swiftui/simultaneousgesture/first): The first of two gestures that can happen simultaneously.
- [second](/documentation/swiftui/simultaneousgesture/second): The second of two gestures that can happen simultaneously.

### Getting the gesture’s values

- [SimultaneousGesture.Value](/documentation/swiftui/simultaneousgesture/value): The value of a simultaneous gesture that indicates which of its two gestures receives events.

## See Also

### Combining gestures

- [Composing SwiftUI gestures](/documentation/swiftui/composing-swiftui-gestures): Combine gestures to create complex interactions.
- [simultaneousGesture(_:including:)](/documentation/swiftui/view/simultaneousgesture(_:including:)): Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [simultaneousGesture(_:isEnabled:)](/documentation/swiftui/view/simultaneousgesture(_:isenabled:)): Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [simultaneousGesture(_:name:isEnabled:)](/documentation/swiftui/view/simultaneousgesture(_:name:isenabled:)): Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [SequenceGesture](/documentation/swiftui/sequencegesture): A gesture that’s a sequence of two gestures.
- [ExclusiveGesture](/documentation/swiftui/exclusivegesture): A gesture that consists of two gestures where only one of them can succeed.
