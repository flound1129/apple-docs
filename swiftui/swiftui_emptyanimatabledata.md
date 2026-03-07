# EmptyAnimatableData

An empty type for animatable data.

```swift
@frozen struct EmptyAnimatableData
```

## Overview

This type is suitable for use as the `animatableData` property of types that do not have any animatable properties.

### Creating the data

- [init()](/documentation/swiftui/emptyanimatabledata/init())

### Manipulating the data

- [magnitudeSquared](/documentation/swiftui/emptyanimatabledata/magnitudesquared): The dot-product of this animatable data instance with itself.

## See Also

### Making data animatable

- [Animatable](/documentation/swiftui/animatable): A type that describes how to animate a property of a view.
- [AnimatableValues](/documentation/swiftui/animatablevalues)
- [AnimatablePair](/documentation/swiftui/animatablepair): A pair of animatable values, which is itself animatable.
- [VectorArithmetic](/documentation/swiftui/vectorarithmetic): A type that can serve as the animatable data of an animatable type.
