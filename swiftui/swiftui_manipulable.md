# Manipulable

A namespace for various manipulable related types.

```swift
enum Manipulable
```

### Structures

- [Manipulable.Event](/documentation/swiftui/manipulable/event): Describes an event generated during a manipulation gesture.
- [Manipulable.GestureState](/documentation/swiftui/manipulable/gesturestate): Describes the state of a manipulation gesture.
- [Manipulable.Inertia](/documentation/swiftui/manipulable/inertia): Describes inertia of a view that defines how much a view resists being manipulated.
- [Manipulable.InputDevice](/documentation/swiftui/manipulable/inputdevice): Describes an input device like a hand or a trackpad.
- [Manipulable.Operation](/documentation/swiftui/manipulable/operation): Describes an operation applied to a view when a person is manipulating a view.

## See Also

### Modifying a view

- [Configuring views](/documentation/swiftui/configuring-views): Adjust the characteristics of a view by applying view modifiers.
- [Reducing view modifier maintenance](/documentation/swiftui/reducing-view-modifier-maintenance): Bundle view modifiers that you regularly reuse into a custom view modifier.
- [modifier(_:)](/documentation/swiftui/view/modifier(_:)): Applies a modifier to a view and returns a new view.
- [ViewModifier](/documentation/swiftui/viewmodifier): A modifier that you apply to a view or another view modifier, producing a different version of the original value.
- [EmptyModifier](/documentation/swiftui/emptymodifier): An empty, or identity, modifier, used during development to switch modifiers at compile time.
- [ModifiedContent](/documentation/swiftui/modifiedcontent): A value with a modifier applied to it.
- [EnvironmentalModifier](/documentation/swiftui/environmentalmodifier): A modifier that must resolve to a concrete modifier in an environment before use.
- [ManipulableModifier](/documentation/swiftui/manipulablemodifier)
- [ManipulableResponderModifier](/documentation/swiftui/manipulablerespondermodifier)
- [ManipulableTransformBindingModifier](/documentation/swiftui/manipulabletransformbindingmodifier)
- [ManipulationGeometryModifier](/documentation/swiftui/manipulationgeometrymodifier)
- [ManipulationGestureModifier](/documentation/swiftui/manipulationgesturemodifier)
- [ManipulationUsingGestureStateModifier](/documentation/swiftui/manipulationusinggesturestatemodifier)
