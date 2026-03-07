# UIGestureRecognizerRepresentableContext

Contextual information about the state of the system that you use to create and update a represented gesture recognizer.

```swift
struct UIGestureRecognizerRepresentableContext<Representable> where Representable : UIGestureRecognizerRepresentable
```

### Instance Properties

- [converter](/documentation/swiftui/uigesturerecognizerrepresentablecontext/converter): A structure used to convert locations to/from coordinate spaces in the hierarchy of the associated SwiftUI view.
- [coordinator](/documentation/swiftui/uigesturerecognizerrepresentablecontext/coordinator): The custom object that you use to communicate state changes from your gesture recognizer to other parts of your SwiftUI interface.

## See Also

### Adding UIKit gesture recognizers into SwiftUI view hierarchies

- [UIGestureRecognizerRepresentable](/documentation/swiftui/uigesturerecognizerrepresentable): A wrapper for a `UIGestureRecognizer` that you use to integrate that gesture recognizer into your SwiftUI hierarchy.
- [UIGestureRecognizerRepresentableCoordinateSpaceConverter](/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter): A proxy structure used to convert locations to/from coordinate spaces in the hierarchy of the SwiftUI view associated with a [UIGestureRecognizerRepresentable](/documentation/swiftui/uigesturerecognizerrepresentable).
