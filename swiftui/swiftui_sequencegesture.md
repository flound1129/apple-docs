# SequenceGesture

A gesture that’s a sequence of two gestures.

```swift
@frozen struct SequenceGesture<First, Second> where First : Gesture, Second : Gesture
```

## Overview

Read [Composing SwiftUI gestures](/documentation/swiftui/composing-swiftui-gestures) to learn how you can create a sequence of two gestures.

### Creating the gesture

- [init(_:_:)](/documentation/swiftui/sequencegesture/init(_:_:)): Creates a sequence gesture with two gestures.
- [first](/documentation/swiftui/sequencegesture/first): The first gesture in a sequence of two gestures.
- [second](/documentation/swiftui/sequencegesture/second): The second gesture in a sequence of two gestures.

### Getting the gesture’s values

- [SequenceGesture.Value](/documentation/swiftui/sequencegesture/value): The value of a sequence gesture that helps to detect whether the first gesture succeeded, so the second gesture can start.

## See Also

### Combining gestures

- [Composing SwiftUI gestures](/documentation/swiftui/composing-swiftui-gestures): Combine gestures to create complex interactions.
- [simultaneousGesture(_:including:)](/documentation/swiftui/view/simultaneousgesture(_:including:)): Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [simultaneousGesture(_:isEnabled:)](/documentation/swiftui/view/simultaneousgesture(_:isenabled:)): Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [simultaneousGesture(_:name:isEnabled:)](/documentation/swiftui/view/simultaneousgesture(_:name:isenabled:)): Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [SimultaneousGesture](/documentation/swiftui/simultaneousgesture): A gesture containing two gestures that can happen at the same time with neither of them preceding the other.
- [ExclusiveGesture](/documentation/swiftui/exclusivegesture): A gesture that consists of two gestures where only one of them can succeed.
