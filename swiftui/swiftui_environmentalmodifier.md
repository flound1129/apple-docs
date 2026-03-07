# EnvironmentalModifier

A modifier that must resolve to a concrete modifier in an environment before use.

```swift
protocol EnvironmentalModifier : ViewModifier where Self.Body == Never
```

### Resolving a modifier

- [resolve(in:)](/documentation/swiftui/environmentalmodifier/resolve(in:)): Resolve to a concrete modifier in the given `environment`.
- [ResolvedModifier](/documentation/swiftui/environmentalmodifier/resolvedmodifier): The type of modifier to use after being resolved.

## See Also

### Modifying a view

- [Configuring views](/documentation/swiftui/configuring-views): Adjust the characteristics of a view by applying view modifiers.
- [Reducing view modifier maintenance](/documentation/swiftui/reducing-view-modifier-maintenance): Bundle view modifiers that you regularly reuse into a custom view modifier.
- [modifier(_:)](/documentation/swiftui/view/modifier(_:)): Applies a modifier to a view and returns a new view.
- [ViewModifier](/documentation/swiftui/viewmodifier): A modifier that you apply to a view or another view modifier, producing a different version of the original value.
- [EmptyModifier](/documentation/swiftui/emptymodifier): An empty, or identity, modifier, used during development to switch modifiers at compile time.
- [ModifiedContent](/documentation/swiftui/modifiedcontent): A value with a modifier applied to it.
- [ManipulableModifier](/documentation/swiftui/manipulablemodifier)
- [ManipulableResponderModifier](/documentation/swiftui/manipulablerespondermodifier)
- [ManipulableTransformBindingModifier](/documentation/swiftui/manipulabletransformbindingmodifier)
- [ManipulationGeometryModifier](/documentation/swiftui/manipulationgeometrymodifier)
- [ManipulationGestureModifier](/documentation/swiftui/manipulationgesturemodifier)
- [ManipulationUsingGestureStateModifier](/documentation/swiftui/manipulationusinggesturestatemodifier)
- [Manipulable](/documentation/swiftui/manipulable): A namespace for various manipulable related types.
