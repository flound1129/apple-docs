# Animatable

A type that describes how to animate a property of a view.

```swift
protocol Animatable
```

### Animating data

- [Animatable()](/documentation/swiftui/animatable()): A member and extension macro that, when applied to a struct, class or enum declaration, synthesizes the conformance to `Animatable` and its requirement, the `animatableData` property using the existing animatable properties of the type this macro is applied to.
- [AnimatableIgnored()](/documentation/swiftui/animatableignored()): An accessor macro that marks a property of a type to be excluded from the `animatableData` synthesis:
- [animatableData](/documentation/swiftui/animatable/animatabledata-6nydg): The data to animate.
- [AnimatableData](/documentation/swiftui/animatable/animatabledata-swift.associatedtype): The type defining the data to animate.

## See Also

### Making data animatable

- [AnimatableValues](/documentation/swiftui/animatablevalues)
- [AnimatablePair](/documentation/swiftui/animatablepair): A pair of animatable values, which is itself animatable.
- [VectorArithmetic](/documentation/swiftui/vectorarithmetic): A type that can serve as the animatable data of an animatable type.
- [EmptyAnimatableData](/documentation/swiftui/emptyanimatabledata): An empty type for animatable data.
