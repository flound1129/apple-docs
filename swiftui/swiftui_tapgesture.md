# TapGesture

A gesture that recognizes one or more taps.

```swift
struct TapGesture
```

## Overview

To recognize a tap gesture on a view, create and configure the gesture, and then add it to the view using the [gesture(_:including:)](/documentation/swiftui/view/gesture(_:including:)) modifier. The following code adds a tap gesture to a [Circle](/documentation/swiftui/circle) that toggles the color of the circle:

```swift
struct TapGestureView: View {
    @State private var tapped = false

    var tap: some Gesture {
        TapGesture(count: 1)
            .onEnded { _ in self.tapped = !self.tapped }
    }

    var body: some View {
        Circle()
            .fill(self.tapped ? Color.blue : Color.red)
            .frame(width: 100, height: 100, alignment: .center)
            .gesture(tap)
    }
}
```

### Creating a tap gesture

- [init(count:)](/documentation/swiftui/tapgesture/init(count:)): Creates a tap gesture with the number of required taps.
- [count](/documentation/swiftui/tapgesture/count): The required number of tap events.

## See Also

### Recognizing tap gestures

- [onTapGesture(count:perform:)](/documentation/swiftui/view/ontapgesture(count:perform:)): Adds an action to perform when this view recognizes a tap gesture.
- [onTapGesture(count:coordinateSpace:perform:)](/documentation/swiftui/view/ontapgesture(count:coordinatespace:perform:)): Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [SpatialTapGesture](/documentation/swiftui/spatialtapgesture): A gesture that recognizes one or more taps and reports their location.
