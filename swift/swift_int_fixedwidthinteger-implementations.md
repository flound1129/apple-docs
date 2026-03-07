# FixedWidthInteger Implementations

### Operators

- [&*(_:_:)](/documentation/swift/int/&*(_:_:)): Returns the product of the two given values, wrapping the result in case of any overflow.
- [&*=(_:_:)](/documentation/swift/int/&*=(_:_:)): Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [&+(_:_:)](/documentation/swift/int/&+(_:_:)): Returns the sum of the two given values, wrapping the result in case of any overflow.
- [&+=(_:_:)](/documentation/swift/int/&+=(_:_:)): Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [&-(_:_:)](/documentation/swift/int/&-(_:_:)): Returns the difference of the two given values, wrapping the result in case of any overflow.
- [&-=(_:_:)](/documentation/swift/int/&-=(_:_:)): Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [&<<(_:_:)](/documentation/swift/int/&__(_:_:)-2kxph): Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [&>>(_:_:)](/documentation/swift/int/&__(_:_:)-35o0c): Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [&<<(_:_:)](/documentation/swift/int/&__(_:_:)-3euzz): Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [&>>(_:_:)](/documentation/swift/int/&__(_:_:)-5zh5j): Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [&>>(_:_:)](/documentation/swift/int/&__(_:_:)-76ndv): Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [&<<(_:_:)](/documentation/swift/int/&__(_:_:)-voti): Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [&<<=(_:_:)](/documentation/swift/int/&__=(_:_:)-13miv): Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [&>>=(_:_:)](/documentation/swift/int/&__=(_:_:)-704vj): Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.

### Initializers

- [init(_:)](/documentation/swift/int/init(_:)-2hmii): Creates a new integer value from the given string.
- [init(_:)](/documentation/swift/int/init(_:)-6gt9z)
- [init(_:radix:)](/documentation/swift/int/init(_:radix:)): Creates a new integer value from the given string and radix.
- [init(bigEndian:)](/documentation/swift/int/init(bigendian:)): Creates an integer from its big-endian representation, changing the byte order if necessary.
- [init(exactly:)](/documentation/swift/int/init(exactly:)-7yhn6)
- [init(littleEndian:)](/documentation/swift/int/init(littleendian:)): Creates an integer from its little-endian representation, changing the byte order if necessary.

### Instance Properties

- [bigEndian](/documentation/swift/int/bigendian): The big-endian representation of this integer.
- [littleEndian](/documentation/swift/int/littleendian): The little-endian representation of this integer.

### Type Methods

- [random(in:)](/documentation/swift/int/random(in:)-8zzqh): Returns a random value within the specified range.
- [random(in:)](/documentation/swift/int/random(in:)-9mjpw): Returns a random value within the specified range.
- [random(in:using:)](/documentation/swift/int/random(in:using:)-3dwv4): Returns a random value within the specified range, using the given generator as a source for randomness.
- [random(in:using:)](/documentation/swift/int/random(in:using:)-4lsb5): Returns a random value within the specified range, using the given generator as a source for randomness.
