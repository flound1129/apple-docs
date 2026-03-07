# SpatialTapGesture

A gesture that recognizes one or more taps and reports their location.

```swift
struct SpatialTapGesture
```

## Overview

To recognize a tap gesture on a view, create and configure the gesture, and then add it to the view using the [gesture(_:including:)](/documentation/swiftui/view/gesture(_:including:)) modifier. The following code adds a tap gesture to a [Circle](/documentation/swiftui/circle) that toggles the color of the circle based on the tap location:

```swift
struct TapGestureView: View {
    @State private var location: CGPoint = .zero

    var tap: some Gesture {
        SpatialTapGesture()
            .onEnded { event in
                self.location = event.location
             }
    }

    var body: some View {
        Circle()
            .fill(self.location.y > 50 ? Color.blue : Color.red)
            .frame(width: 100, height: 100, alignment: .center)
            .gesture(tap)
    }
}
```

### Creating a spatial tap gesture

- [init(count:coordinateSpace:)](/documentation/swiftui/spatialtapgesture/init(count:coordinatespace:)-75s7q): Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [coordinateSpace](/documentation/swiftui/spatialtapgesture/coordinatespace): The coordinate space in which to receive location values.
- [count](/documentation/swiftui/spatialtapgesture/count): The required number of tap events.

### Getting the gesture’s value

- [SpatialTapGesture.Value](/documentation/swiftui/spatialtapgesture/value): The attributes of a tap gesture.

### Deprecated initializers

- [init(count:coordinateSpace:)](/documentation/swiftui/spatialtapgesture/init(count:coordinatespace:)-1b85g): Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.

### Initializers

- [init(count:coordinateSpace3D:)](/documentation/swiftui/spatialtapgesture/init(count:coordinatespace3d:)): Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count:coordinateSpace:)](/documentation/swiftui/spatialtapgesture/init(count:coordinatespace:)): Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.

## See Also

### Recognizing tap gestures

- [onTapGesture(count:perform:)](/documentation/swiftui/view/ontapgesture(count:perform:)): Adds an action to perform when this view recognizes a tap gesture.
- [onTapGesture(count:coordinateSpace:perform:)](/documentation/swiftui/view/ontapgesture(count:coordinatespace:perform:)): Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [TapGesture](/documentation/swiftui/tapgesture): A gesture that recognizes one or more taps.
