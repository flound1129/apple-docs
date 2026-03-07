# NSGestureRecognizerRepresentableCoordinateSpaceConverter

A structure used to convert locations to and from coordinate spaces in the hierarchy of the SwiftUI view associated with an [NSGestureRecognizerRepresentable](/documentation/swiftui/nsgesturerecognizerrepresentable).

```swift
struct NSGestureRecognizerRepresentableCoordinateSpaceConverter
```

### Instance Properties

- [localLocation](/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/locallocation): The represented gesture recognizer’s current location in the coordinate space of the SwiftUI view it’s attached to.
- [localTranslation](/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/localtranslation): The represented gesture recognizer’s current translation in the coordinate space of the SwiftUI view it’s attached to, or `nil` if the represented gesture recognizer doesn’t respond to `-translationInView:` selector.
- [localVelocity](/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/localvelocity): The represented gesture recognizer’s current velocity in the coordinate space of the SwiftUI view it’s attached to, or `nil` if the represented gesture recognizer doesn’t respond to `-velocityInView:` selector.

### Instance Methods

- [convert(globalPoint:to:)](/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/convert(globalpoint:to:)): Converts a point in the global coordinate space to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.
- [location(in:)](/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/location(in:)): Converts the represented gesture recognizer’s current location to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.
- [translation(in:)](/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/translation(in:)): Converts the represented gesture recognizer’s current translation to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.
- [velocity(in:)](/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/velocity(in:)): Converts the represented gesture recognizer’s current velocity to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.

## See Also

### Adding AppKit gesture recognizers into SwiftUI view hierarchies

- [NSGestureRecognizerRepresentable](/documentation/swiftui/nsgesturerecognizerrepresentable): A wrapper for an `NSGestureRecognizer` that you use to integrate that gesture recognizer into your SwiftUI hierarchy.
- [NSGestureRecognizerRepresentableContext](/documentation/swiftui/nsgesturerecognizerrepresentablecontext): Contextual information about the state of the system that you use to create and update a represented gesture recognizer.
