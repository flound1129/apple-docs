# VectorArithmetic

A type that can serve as the animatable data of an animatable type.

```swift
protocol VectorArithmetic : AdditiveArithmetic
```

## Overview

`VectorArithmetic` extends the `AdditiveArithmetic` protocol with scalar multiplication and a way to query the vector magnitude of the value. Use this type as the `animatableData` associated type of a type that conforms to the [Animatable](/documentation/swiftui/animatable) protocol.

### Manipulating values

- [magnitudeSquared](/documentation/swiftui/vectorarithmetic/magnitudesquared): Returns the dot-product of this vector arithmetic instance with itself.
- [scale(by:)](/documentation/swiftui/vectorarithmetic/scale(by:)): Multiplies each component of this value by the given value.
- [scaled(by:)](/documentation/swiftui/vectorarithmetic/scaled(by:)): Returns a value with each component of this value multiplied by the given value.
- [interpolate(towards:amount:)](/documentation/swiftui/vectorarithmetic/interpolate(towards:amount:)): Interpolates this value with `other` by the specified `amount`.
- [interpolated(towards:amount:)](/documentation/swiftui/vectorarithmetic/interpolated(towards:amount:)): Returns this value interpolated with `other` by the specified `amount`.

## See Also

### Making data animatable

- [Animatable](/documentation/swiftui/animatable): A type that describes how to animate a property of a view.
- [AnimatableValues](/documentation/swiftui/animatablevalues)
- [AnimatablePair](/documentation/swiftui/animatablepair): A pair of animatable values, which is itself animatable.
- [EmptyAnimatableData](/documentation/swiftui/emptyanimatabledata): An empty type for animatable data.
