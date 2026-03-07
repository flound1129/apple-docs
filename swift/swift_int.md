# Int

A signed integer value type.

```swift
@frozen struct Int
```

## Overview

On 32-bit platforms, `Int` is the same size as `Int32`, and on 64-bit platforms, `Int` is the same size as `Int64`.

### Converting Integers

- [init(_:)](/documentation/swift/int/init(_:)-4ekvl): Creates a new instance from the given integer.
- [init(exactly:)](/documentation/swift/int/init(exactly:)-b1dy)
- [init(clamping:)](/documentation/swift/int/init(clamping:)): Creates a new instance with the representable value that’s closest to the given integer.
- [init(truncatingIfNeeded:)](/documentation/swift/int/init(truncatingifneeded:)): Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
- [init(bitPattern:)](/documentation/swift/int/init(bitpattern:)-72037): Creates a new instance with the same memory representation as the given value.
- [init(exactly:)](/documentation/swift/int/init(exactly:)-177ax)
- [init(truncating:)](/documentation/swift/int/init(truncating:))

### Converting Floating-Point Values

- [init(_:)](/documentation/swift/int/init(_:)-6gt9z)
- [init(_:)](/documentation/swift/int/init(_:)-8vbwo): Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](/documentation/swift/int/init(_:)-2oscb): Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](/documentation/swift/int/init(_:)-3huv0): Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](/documentation/swift/int/init(_:)-66i0w): Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](/documentation/swift/int/init(_:)-5q6q5)

### Converting with No Loss of Precision

- [init(exactly:)](/documentation/swift/int/init(exactly:)-7yhn6)
- [init(exactly:)](/documentation/swift/int/init(exactly:)-77kq8): Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](/documentation/swift/int/init(exactly:)-7qdwf): Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](/documentation/swift/int/init(exactly:)-5xh2s): Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](/documentation/swift/int/init(exactly:)-5kot1): Creates an integer from the given floating-point value, if it can be represented exactly.

### Converting Strings

- [init(_:)](/documentation/swift/int/init(_:)-2hmii): Creates a new integer value from the given string.
- [init(_:radix:)](/documentation/swift/int/init(_:radix:)): Creates a new integer value from the given string and radix.

### Creating a Random Integer

- [random(in:)](/documentation/swift/int/random(in:)-9mjpw): Returns a random value within the specified range.
- [random(in:using:)](/documentation/swift/int/random(in:using:)-4lsb5): Returns a random value within the specified range, using the given generator as a source for randomness.
- [random(in:)](/documentation/swift/int/random(in:)-8zzqh): Returns a random value within the specified range.
- [random(in:using:)](/documentation/swift/int/random(in:using:)-3dwv4): Returns a random value within the specified range, using the given generator as a source for randomness.

### Performing Calculations

- [Integer Operators](/documentation/swift/integer-operators): Perform arithmetic and bitwise operations or compare values.
- [negate()](/documentation/swift/int/negate()): Replaces this value with its additive inverse.
- [quotientAndRemainder(dividingBy:)](/documentation/swift/int/quotientandremainder(dividingby:)): Returns the quotient and remainder of this value divided by the given value.
- [isMultiple(of:)](/documentation/swift/int/ismultiple(of:)): Returns `true` if this value is a multiple of the given value, and `false` otherwise.

### Performing Calculations with Overflow

- [addingReportingOverflow(_:)](/documentation/swift/int/addingreportingoverflow(_:)): Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [subtractingReportingOverflow(_:)](/documentation/swift/int/subtractingreportingoverflow(_:)): Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.
- [multipliedReportingOverflow(by:)](/documentation/swift/int/multipliedreportingoverflow(by:)): Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividedReportingOverflow(by:)](/documentation/swift/int/dividedreportingoverflow(by:)): Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [remainderReportingOverflow(dividingBy:)](/documentation/swift/int/remainderreportingoverflow(dividingby:)): Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.

### Performing Double-Width Calculations

- [multipliedFullWidth(by:)](/documentation/swift/int/multipliedfullwidth(by:)): Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [dividingFullWidth(_:)](/documentation/swift/int/dividingfullwidth(_:)): Returns a tuple containing the quotient and remainder of dividing the given value by this value.

### Finding the Sign and Magnitude

- [magnitude](/documentation/swift/int/magnitude-swift.property): The magnitude of this value.
- [Int.Magnitude](/documentation/swift/int/magnitude-swift.typealias): A type that can represent the absolute value of any possible value of this type.
- [abs(_:)](/documentation/swift/abs(_:)): Returns the absolute value of the given number.
- [signum()](/documentation/swift/int/signum()): Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.

### Accessing Numeric Constants

- [zero](/documentation/swift/int/zero): The zero value.
- [min](/documentation/swift/int/min): The minimum representable integer in this type.
- [max](/documentation/swift/int/max): The maximum representable integer in this type.
- [isSigned](/documentation/swift/int/issigned): A Boolean value indicating whether this type is a signed integer type.

### Working with Byte Order

- [byteSwapped](/documentation/swift/int/byteswapped): A representation of this integer with the byte order swapped.
- [littleEndian](/documentation/swift/int/littleendian): The little-endian representation of this integer.
- [bigEndian](/documentation/swift/int/bigendian): The big-endian representation of this integer.
- [init(littleEndian:)](/documentation/swift/int/init(littleendian:)): Creates an integer from its little-endian representation, changing the byte order if necessary.
- [init(bigEndian:)](/documentation/swift/int/init(bigendian:)): Creates an integer from its big-endian representation, changing the byte order if necessary.

### Working with Binary Representation

- [bitWidth](/documentation/swift/int/bitwidth): The number of bits used for the underlying binary representation of values of this type.
- [bitWidth](/documentation/swift/int/bitwidth-swift.property): The number of bits in the current binary representation of this value.
- [nonzeroBitCount](/documentation/swift/int/nonzerobitcount): The number of bits equal to 1 in this value’s binary representation.
- [leadingZeroBitCount](/documentation/swift/int/leadingzerobitcount): The number of leading zeros in this value’s binary representation.
- [trailingZeroBitCount](/documentation/swift/int/trailingzerobitcount): The number of trailing zeros in this value’s binary representation.
- [words](/documentation/swift/int/words-swift.property): A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
- [Int.Words](/documentation/swift/int/words-swift.struct): A type that represents the words of this integer.

### Working with Memory Addresses

- [init(bitPattern:)](/documentation/swift/int/init(bitpattern:)-2i0qy): Creates a new value with the bit pattern of the given pointer.
- [init(bitPattern:)](/documentation/swift/int/init(bitpattern:)-2o9co): Creates an integer that captures the full value of the given object identifier.
- [init(bitPattern:)](/documentation/swift/int/init(bitpattern:)-5qm7a): Creates a new value with the bit pattern of the given pointer.

### Encoding and Decoding Values

- [encode(to:)](/documentation/swift/int/encode(to:)): Encodes this value into the given encoder.
- [init(from:)](/documentation/swift/int/init(from:)): Creates a new instance by decoding from the given decoder.

### Describing an Integer

- [description](/documentation/swift/int/description): A textual representation of this value.
- [hash(into:)](/documentation/swift/int/hash(into:)): Hashes the essential components of this value by feeding them into the given hasher.
- [customMirror](/documentation/swift/int/custommirror): A mirror that reflects the `Int` instance.

### Infrequently Used Functionality

- [init()](/documentation/swift/int/init()): Creates a new value equal to zero.
- [init(integerLiteral:)](/documentation/swift/int/init(integerliteral:))
- [Int.IntegerLiteralType](/documentation/swift/int/integerliteraltype): A type that represents an integer literal.
- [distance(to:)](/documentation/swift/int/distance(to:)): Returns the distance from this value to the given value, expressed as a stride.
- [advanced(by:)](/documentation/swift/int/advanced(by:)): Returns a value that is offset the specified distance from this value.
- [Int.Stride](/documentation/swift/int/stride): A type that represents the distance between two values.
- [hashValue](/documentation/swift/int/hashvalue): The hash value.

### Deprecated

- [customPlaygroundQuickLook](/documentation/swift/int/customplaygroundquicklook): A custom playground Quick Look for the `Int` instance.
- [init(_:)](/documentation/swift/int/init(_:)-3mb3q)

### SIMD-Supporting Types

- [Int.SIMDMaskScalar](/documentation/swift/int/simdmaskscalar)
- [Int.SIMD2Storage](/documentation/swift/int/simd2storage): Storage for a vector of two integers.
- [Int.SIMD4Storage](/documentation/swift/int/simd4storage): Storage for a vector of four integers.
- [Int.SIMD8Storage](/documentation/swift/int/simd8storage): Storage for a vector of eight integers.
- [Int.SIMD16Storage](/documentation/swift/int/simd16storage): Storage for a vector of 16 integers.
- [Int.SIMD32Storage](/documentation/swift/int/simd32storage): Storage for a vector of 32 integers.
- [Int.SIMD64Storage](/documentation/swift/int/simd64storage): Storage for a vector of 64 integers.

### Operators

- [!=(_:_:)](/documentation/swift/int/!=(_:_:))
- [&>>=(_:_:)](/documentation/swift/int/&__=(_:_:)-2i06i): Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [&<<=(_:_:)](/documentation/swift/int/&__=(_:_:)-58orm): Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [<(_:_:)](/documentation/swift/int/_(_:_:)-3wpum): Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [^=(_:_:)](/documentation/swift/int/_=(_:_:)-1ypi9): Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [%=(_:_:)](/documentation/swift/int/_=(_:_:)-30t77): Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [|=(_:_:)](/documentation/swift/int/_=(_:_:)-4b29i): Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.

### Type Aliases

- [Int.Specification](/documentation/swift/int/specification)
- [Int.UnwrappedType](/documentation/swift/int/unwrappedtype)
- [Int.ValueType](/documentation/swift/int/valuetype)

### Type Properties

- [defaultResolverSpecification](/documentation/swift/int/defaultresolverspecification)

### Default Implementations

- [AdditiveArithmetic Implementations](/documentation/swift/int/additivearithmetic-implementations)
- [AtomicRepresentable Implementations](/documentation/swift/int/atomicrepresentable-implementations)
- [BinaryInteger Implementations](/documentation/swift/int/binaryinteger-implementations)
- [CodingKeyRepresentable Implementations](/documentation/swift/int/codingkeyrepresentable-implementations)
- [Comparable Implementations](/documentation/swift/int/comparable-implementations)
- [CustomReflectable Implementations](/documentation/swift/int/customreflectable-implementations)
- [Decodable Implementations](/documentation/swift/int/decodable-implementations)
- [Encodable Implementations](/documentation/swift/int/encodable-implementations)
- [Equatable Implementations](/documentation/swift/int/equatable-implementations)
- [ExpressibleByIntegerLiteral Implementations](/documentation/swift/int/expressiblebyintegerliteral-implementations)
- [FixedWidthInteger Implementations](/documentation/swift/int/fixedwidthinteger-implementations)
- [Hashable Implementations](/documentation/swift/int/hashable-implementations)
- [SIMDScalar Implementations](/documentation/swift/int/simdscalar-implementations)
- [SignedInteger Implementations](/documentation/swift/int/signedinteger-implementations)
- [SignedNumeric Implementations](/documentation/swift/int/signednumeric-implementations)
- [Strideable Implementations](/documentation/swift/int/strideable-implementations)

## See Also

### Standard Library

- [Double](/documentation/swift/double): A double-precision (64-bit), floating-point value type.
- [String](/documentation/swift/string): A Unicode string value that is a collection of characters.
- [Array](/documentation/swift/array): An ordered, random-access collection.
- [Dictionary](/documentation/swift/dictionary): A collection whose elements are key-value pairs.
- [Swift Standard Library](/documentation/swift/swift-standard-library): Solve complex problems and write high-performance, readable code.
