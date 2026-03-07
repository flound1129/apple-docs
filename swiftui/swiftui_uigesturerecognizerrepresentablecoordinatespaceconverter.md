# UIGestureRecognizerRepresentableCoordinateSpaceConverter

A proxy structure used to convert locations to/from coordinate spaces in the hierarchy of the SwiftUI view associated with a [UIGestureRecognizerRepresentable](/documentation/swiftui/uigesturerecognizerrepresentable).

```swift
struct UIGestureRecognizerRepresentableCoordinateSpaceConverter
```

### Instance Properties

- [localLocation](/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/locallocation): The represented gesture recognizer’s current location in the coordinate space of the SwiftUI view it’s attached to.
- [localTranslation](/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/localtranslation): The represented gesture recognizer’s current translation in the coordinate space of the SwiftUI view it’s attached to.
- [localVelocity](/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/localvelocity): The represented gesture recognizer’s current velocity in the coordinate space of the SwiftUI view it’s attached to.

### Instance Methods

- [convert(globalPoint:to:)](/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/convert(globalpoint:to:)): Converts a point in the global coordinate space to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.
- [location(in:)](/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/location(in:)): Converts the represented gesture recognizer’s current location to a SwiftUI coordinate space  of an ancestor of the view the gesture recognizer is attached to.
- [translation(in:)](/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/translation(in:)): Converts the represented gesture recognizer’s current translation to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.
- [velocity(in:)](/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/velocity(in:)): Converts the represented gesture recognizer’s current velocity to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.

## See Also

### Adding UIKit gesture recognizers into SwiftUI view hierarchies

- [UIGestureRecognizerRepresentable](/documentation/swiftui/uigesturerecognizerrepresentable): A wrapper for a `UIGestureRecognizer` that you use to integrate that gesture recognizer into your SwiftUI hierarchy.
- [UIGestureRecognizerRepresentableContext](/documentation/swiftui/uigesturerecognizerrepresentablecontext): Contextual information about the state of the system that you use to create and update a represented gesture recognizer.
