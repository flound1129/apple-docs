# SpatialEventCollection

A collection of spatial input events that target a specific view.

```swift
struct SpatialEventCollection
```

## Overview

You receive a structure of this type as an input to the [onChanged(_:)](/documentation/swiftui/gesture/onchanged(_:)) or [onEnded(_:)](/documentation/swiftui/gesture/onended(_:)) method of a [SpatialEventGesture](/documentation/swiftui/spatialeventgesture). The structure contains a collection of [SpatialEventCollection.Event](/documentation/swiftui/spatialeventcollection/event) values that correspond to ongoing input events. You can look up a specific event in the collection by its [id](/documentation/swiftui/spatialeventcollection/event/id-swift.property) value or iterate over all events in the collection to apply logic depending on the event’s state.

### Accessing the collection’s events

- [SpatialEventCollection.Event](/documentation/swiftui/spatialeventcollection/event): A spatial event generated from an input like a touch or click that can drive gestures in the system.
- [subscript(_:)](/documentation/swiftui/spatialeventcollection/subscript(_:)): Retrieves an event using its unique identifier.

### Iterating over events in the collection

- [makeIterator()](/documentation/swiftui/spatialeventcollection/makeiterator()): Makes an iterator over all events in the collection.
- [SpatialEventCollection.Iterator](/documentation/swiftui/spatialeventcollection/iterator): An iterator over all events in the collection.

## See Also

### Recognizing spatial events

- [SpatialEventGesture](/documentation/swiftui/spatialeventgesture): A gesture that provides information about ongoing spatial events like clicks and touches.
- [Chirality](/documentation/swiftui/chirality): The chirality, or handedness, of a pose.
