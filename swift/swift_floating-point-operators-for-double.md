# Floating-Point Operators for Double

Perform arithmetic and bitwise operations or compare values.

### Arithmetic

- [+(_:_:)](/documentation/swift/double/+(_:_:)): Adds two values and produces their sum, rounded to a representable value.
- [-(_:_:)](/documentation/swift/double/-(_:_:)): Subtracts one value from another and produces their difference, rounded to a representable value.
- [*(_:_:)](/documentation/swift/double/*(_:_:)): Multiplies two values and produces their product, rounding to a representable value.
- [/(_:_:)](/documentation/swift/double/_(_:_:)): Returns the quotient of dividing the first value by the second, rounded to a representable value.

### Arithmetic with Assignment

- [+=(_:_:)](/documentation/swift/double/+=(_:_:)): Adds two values and stores the result in the left-hand-side variable, rounded to a representable value.
- [-=(_:_:)](/documentation/swift/double/-=(_:_:)): Subtracts the second value from the first and stores the difference in the left-hand-side variable, rounding to a representable value.
- [*=(_:_:)](/documentation/swift/double/*=(_:_:)): Multiplies two values and stores the result in the left-hand-side variable, rounding to a representable value.
- [/=(_:_:)](/documentation/swift/double/_=(_:_:)): Divides the first value by the second and stores the quotient in the left-hand-side variable, rounding to a representable value.

### Comparison

- [==(_:_:)](/documentation/swift/double/==(_:_:)-12hdv): Returns a Boolean value indicating whether two values are equal.
- [!=(_:_:)](/documentation/swift/double/!=(_:_:)): Returns a Boolean value indicating whether two values are not equal.

### Negation

- [-(_:)](/documentation/swift/double/-(_:)): Calculates the additive inverse of a value.
- [+(_:)](/documentation/swift/double/+(_:)): Returns the given number unchanged.

### Range Expressions

- [...(_:)](/documentation/swift/double/'...(_:)-4mm67): Returns a partial range up to, and including, its upper bound.
- [...(_:)](/documentation/swift/double/'...(_:)-6ct5v): Returns a partial range extending upward from a lower bound.

## See Also

### Performing Calculations

- [addingProduct(_:_:)](/documentation/swift/double/addingproduct(_:_:)): Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [addProduct(_:_:)](/documentation/swift/double/addproduct(_:_:)): Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [squareRoot()](/documentation/swift/double/squareroot()): Returns the square root of the value, rounded to a representable value.
- [formSquareRoot()](/documentation/swift/double/formsquareroot()): Replaces this value with its square root, rounded to a representable value.
- [remainder(dividingBy:)](/documentation/swift/double/remainder(dividingby:)): Returns the remainder of this value divided by the given value.
- [formRemainder(dividingBy:)](/documentation/swift/double/formremainder(dividingby:)): Replaces this value with the remainder of itself divided by the given value.
- [truncatingRemainder(dividingBy:)](/documentation/swift/double/truncatingremainder(dividingby:)): Returns the remainder of this value divided by the given value using truncating division.
- [formTruncatingRemainder(dividingBy:)](/documentation/swift/double/formtruncatingremainder(dividingby:)): Replaces this value with the remainder of itself divided by the given value using truncating division.
- [negate()](/documentation/swift/double/negate()): Replaces this value with its additive inverse.
