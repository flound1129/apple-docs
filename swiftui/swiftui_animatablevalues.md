# AnimatableValues

```swift
@frozen struct AnimatableValues<each Value> where repeat each Value : VectorArithmetic
```

### Initializers

- [init(_:)](/documentation/swiftui/animatablevalues/init(_:)): Creates a tuple of animatable values.

### Instance Properties

- [magnitudeSquared](/documentation/swiftui/animatablevalues/magnitudesquared): The dot-product of the tuple of animatable values with itself.
- [value](/documentation/swiftui/animatablevalues/value): The tuple of values.

## See Also

### Making data animatable

- [Animatable](/documentation/swiftui/animatable): A type that describes how to animate a property of a view.
- [AnimatablePair](/documentation/swiftui/animatablepair): A pair of animatable values, which is itself animatable.
- [VectorArithmetic](/documentation/swiftui/vectorarithmetic): A type that can serve as the animatable data of an animatable type.
- [EmptyAnimatableData](/documentation/swiftui/emptyanimatabledata): An empty type for animatable data.
