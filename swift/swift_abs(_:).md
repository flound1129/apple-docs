# abs(_:)

Returns the absolute value of the given number.

```swift
func abs<T>(_ x: T) -> T where T : Comparable, T : SignedNumeric
```

## Parameters

- **x**: A signed number.

## Return Value

The absolute value of `x`.

## Discussion

The absolute value of `x` must be representable in the same type. In particular, the absolute value of a signed, fixed-width integer type’s minimum cannot be represented.

```swift
let x = Int8.min
// x == -128
let y = abs(x)
// Overflow error
```

## See Also

### Finding the Sign and Magnitude

- [magnitude](/documentation/swift/int/magnitude-swift.property): The magnitude of this value.
- [Int.Magnitude](/documentation/swift/int/magnitude-swift.typealias): A type that can represent the absolute value of any possible value of this type.
- [signum()](/documentation/swift/int/signum()): Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
