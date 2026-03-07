# ExclusiveGesture

A gesture that consists of two gestures where only one of them can succeed.

```swift
@frozen struct ExclusiveGesture<First, Second> where First : Gesture, Second : Gesture
```

## Overview

The `ExclusiveGesture` gives precedence to its first gesture.

### Creating the gesture

- [init(_:_:)](/documentation/swiftui/exclusivegesture/init(_:_:)): Creates a gesture from two gestures where only one of them succeeds.
- [first](/documentation/swiftui/exclusivegesture/first): The first of two gestures.
- [second](/documentation/swiftui/exclusivegesture/second): The second of two gestures.

### Supporting types

- [ExclusiveGesture.Value](/documentation/swiftui/exclusivegesture/value): The value of an exclusive gesture that indicates which of two gestures succeeded.

## See Also

### Combining gestures

- [Composing SwiftUI gestures](/documentation/swiftui/composing-swiftui-gestures): Combine gestures to create complex interactions.
- [simultaneousGesture(_:including:)](/documentation/swiftui/view/simultaneousgesture(_:including:)): Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [simultaneousGesture(_:isEnabled:)](/documentation/swiftui/view/simultaneousgesture(_:isenabled:)): Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [simultaneousGesture(_:name:isEnabled:)](/documentation/swiftui/view/simultaneousgesture(_:name:isenabled:)): Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [SequenceGesture](/documentation/swiftui/sequencegesture): A gesture that’s a sequence of two gestures.
- [SimultaneousGesture](/documentation/swiftui/simultaneousgesture): A gesture containing two gestures that can happen at the same time with neither of them preceding the other.
