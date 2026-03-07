# Integer Operators

Perform arithmetic and bitwise operations or compare values.

### Arithmetic

- [+(_:_:)](/documentation/swift/int/+(_:_:)): Adds two values and produces their sum.
- [-(_:_:)](/documentation/swift/int/-(_:_:)): Subtracts one value from another and produces their difference.
- [*(_:_:)](/documentation/swift/int/*(_:_:)): Multiplies two values and produces their product.
- [/(_:_:)](/documentation/swift/int/_(_:_:)-7j9bj): Returns the quotient of dividing the first value by the second.

### Arithmetic with Assignment

- [+=(_:_:)](/documentation/swift/int/+=(_:_:)): Adds two values and stores the result in the left-hand-side variable.
- [*=(_:_:)](/documentation/swift/int/*=(_:_:)): Multiplies two values and stores the result in the left-hand-side variable.
- [/=(_:_:)](/documentation/swift/int/_=(_:_:)-9lzpe): Divides the first value by the second and stores the quotient in the left-hand-side variable.

### Masked Arithmetic

- [&+(_:_:)](/documentation/swift/int/&+(_:_:)): Returns the sum of the two given values, wrapping the result in case of any overflow.
- [&-(_:_:)](/documentation/swift/int/&-(_:_:)): Returns the difference of the two given values, wrapping the result in case of any overflow.
- [&*(_:_:)](/documentation/swift/int/&*(_:_:)): Returns the product of the two given values, wrapping the result in case of any overflow.
- [&+=(_:_:)](/documentation/swift/int/&+=(_:_:)): Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [&-=(_:_:)](/documentation/swift/int/&-=(_:_:)): Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [&*=(_:_:)](/documentation/swift/int/&*=(_:_:)): Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.

### Bitwise Operations

- [&(_:_:)](/documentation/swift/int/&(_:_:)): Returns the result of performing a bitwise AND operation on the two given values.
- [&=(_:_:)](/documentation/swift/int/&=(_:_:)): Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [~(_:)](/documentation/swift/int/~(_:)): Returns the inverse of the bits set in the argument.

### Negation

- [-(_:)](/documentation/swift/int/-(_:)): Returns the additive inverse of the specified value.
- [+(_:)](/documentation/swift/int/+(_:)): Returns the given number unchanged.

### Comparison

- [==(_:_:)](/documentation/swift/int/==(_:_:)): Returns a Boolean value indicating whether two values are equal.
- [==(_:_:)](/documentation/swift/int/==(_:_:)-1zalu): Returns a Boolean value indicating whether the two given values are equal.
- [!=(_:_:)](/documentation/swift/int/!=(_:_:)-1baz3): Returns a Boolean value indicating whether two values are not equal.
- [!=(_:_:)](/documentation/swift/int/!=(_:_:)-4jphg): Returns a Boolean value indicating whether the two given values are not equal.

### Range Expressions

- [...(_:_:)](/documentation/swift/int/'...(_:_:)): Returns a closed range that contains both of its bounds.
- [...(_:)](/documentation/swift/int/'...(_:)-6ct66): Returns a partial range extending upward from a lower bound.
- [...(_:)](/documentation/swift/int/'...(_:)-4mm5u): Returns a partial range up to, and including, its upper bound.

### Deprecated

- [-=(_:_:)](/documentation/swift/int/-=(_:_:)): Subtracts the second value from the first and stores the difference in the left-hand-side variable.

## See Also

### Performing Calculations

- [negate()](/documentation/swift/int/negate()): Replaces this value with its additive inverse.
- [quotientAndRemainder(dividingBy:)](/documentation/swift/int/quotientandremainder(dividingby:)): Returns the quotient and remainder of this value divided by the given value.
- [isMultiple(of:)](/documentation/swift/int/ismultiple(of:)): Returns `true` if this value is a multiple of the given value, and `false` otherwise.
