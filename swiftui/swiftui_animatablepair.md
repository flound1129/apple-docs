# AnimatablePair

A pair of animatable values, which is itself animatable.

```swift
@frozen struct AnimatablePair<First, Second> where First : VectorArithmetic, Second : VectorArithmetic
```

### Creating an animatable pair

- [init(_:_:)](/documentation/swiftui/animatablepair/init(_:_:)): Creates an animated pair with the provided values.

### Getting the constituent animations

- [first](/documentation/swiftui/animatablepair/first): The first value.
- [second](/documentation/swiftui/animatablepair/second): The second value.

### Manipulating values

- [magnitudeSquared](/documentation/swiftui/animatablepair/magnitudesquared): The dot-product of this animated pair with itself.

## See Also

### Making data animatable

- [Animatable](/documentation/swiftui/animatable): A type that describes how to animate a property of a view.
- [AnimatableValues](/documentation/swiftui/animatablevalues)
- [VectorArithmetic](/documentation/swiftui/vectorarithmetic): A type that can serve as the animatable data of an animatable type.
- [EmptyAnimatableData](/documentation/swiftui/emptyanimatabledata): An empty type for animatable data.
