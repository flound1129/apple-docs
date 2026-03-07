# Double

A double-precision (64-bit), floating-point value type.

```swift
@frozen struct Double
```

### Converting Integers

- [init(_:)](/documentation/swift/double/init(_:)-5blrp): Creates a new value, rounded to the closest possible representation.
- [init(_:)](/documentation/swift/double/init(_:)-84ohu): Creates a new value, rounded to the closest possible representation.

### Converting Strings

- [init(_:)](/documentation/swift/double/init(_:)-5wmm8): Creates a new instance from the given string.
- [init(_:)](/documentation/swift/double/init(_:)-15kej)

### Converting Floating-Point Values

- [init(_:)](/documentation/swift/double/init(_:)-1488d): Creates a new instance from the given value, rounded to the closest possible representation.
- [init(_:)](/documentation/swift/double/init(_:)-o1k9): Creates a new instance initialized to the given value.
- [init(_:)](/documentation/swift/double/init(_:)-5h7qh): Creates a new instance that approximates the given value.
- [init(_:)](/documentation/swift/double/init(_:)-aeox): Creates a new instance that approximates the given value.
- [init(_:)](/documentation/swift/double/init(_:)-9z7ob): Creates a new instance that approximates the given value.
- [init(_:)](/documentation/swift/double/init(_:)-7ag2w)
- [init(sign:exponent:significand:)](/documentation/swift/double/init(sign:exponent:significand:)): Creates a new value from the given sign, exponent, and significand.
- [init(signOf:magnitudeOf:)](/documentation/swift/double/init(signof:magnitudeof:)): Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init(_:)](/documentation/swift/double/init(_:)-1oh9r): Creates a new value, rounded to the closest possible representation.
- [init(truncating:)](/documentation/swift/double/init(truncating:))

### Converting with No Loss of Precision

- [init(exactly:)](/documentation/swift/double/init(exactly:)-8esra): Creates a new instance from the given value, if it can be represented exactly.
- [init(exactly:)](/documentation/swift/double/init(exactly:)-1h1oc): Creates a new value, if the given integer can be represented exactly.
- [init(exactly:)](/documentation/swift/double/init(exactly:)-2uexo): Creates a new value, if the given integer can be represented exactly.
- [init(exactly:)](/documentation/swift/double/init(exactly:)-2l6p1): Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](/documentation/swift/double/init(exactly:)-7cl0t): Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](/documentation/swift/double/init(exactly:)-50ofc): Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](/documentation/swift/double/init(exactly:)-63925): Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](/documentation/swift/double/init(exactly:)-8e00y)

### Creating a Random Value

- [random(in:)](/documentation/swift/double/random(in:)-6idef): Returns a random value within the specified range.
- [random(in:using:)](/documentation/swift/double/random(in:using:)-1m6gd): Returns a random value within the specified range, using the given generator as a source for randomness.
- [random(in:)](/documentation/swift/double/random(in:)-5o5ha): Returns a random value within the specified range.
- [random(in:using:)](/documentation/swift/double/random(in:using:)-613hz): Returns a random value within the specified range, using the given generator as a source for randomness.

### Performing Calculations

- [Floating-Point Operators for Double](/documentation/swift/floating-point-operators-for-double): Perform arithmetic and bitwise operations or compare values.
- [addingProduct(_:_:)](/documentation/swift/double/addingproduct(_:_:)): Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [addProduct(_:_:)](/documentation/swift/double/addproduct(_:_:)): Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [squareRoot()](/documentation/swift/double/squareroot()): Returns the square root of the value, rounded to a representable value.
- [formSquareRoot()](/documentation/swift/double/formsquareroot()): Replaces this value with its square root, rounded to a representable value.
- [remainder(dividingBy:)](/documentation/swift/double/remainder(dividingby:)): Returns the remainder of this value divided by the given value.
- [formRemainder(dividingBy:)](/documentation/swift/double/formremainder(dividingby:)): Replaces this value with the remainder of itself divided by the given value.
- [truncatingRemainder(dividingBy:)](/documentation/swift/double/truncatingremainder(dividingby:)): Returns the remainder of this value divided by the given value using truncating division.
- [formTruncatingRemainder(dividingBy:)](/documentation/swift/double/formtruncatingremainder(dividingby:)): Replaces this value with the remainder of itself divided by the given value using truncating division.
- [negate()](/documentation/swift/double/negate()): Replaces this value with its additive inverse.

### Rounding Values

- [rounded()](/documentation/swift/double/rounded())
- [rounded(_:)](/documentation/swift/double/rounded(_:)): Returns this value rounded to an integral value using the specified rounding rule.
- [round()](/documentation/swift/double/round())
- [round(_:)](/documentation/swift/double/round(_:)): Rounds the value to an integral value using the specified rounding rule.

### Comparing Values

- [Floating-Point Operators for Double](/documentation/swift/floating-point-operators-for-double): Perform arithmetic and bitwise operations or compare values.
- [isEqual(to:)](/documentation/swift/double/isequal(to:)): Returns a Boolean value indicating whether this instance is equal to the given value.
- [isLess(than:)](/documentation/swift/double/isless(than:)): Returns a Boolean value indicating whether this instance is less than the given value.
- [isLessThanOrEqualTo(_:)](/documentation/swift/double/islessthanorequalto(_:)): Returns a Boolean value indicating whether this instance is less than or equal to the given value.
- [isTotallyOrdered(belowOrEqualTo:)](/documentation/swift/double/istotallyordered(beloworequalto:)): Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.
- [minimum(_:_:)](/documentation/swift/double/minimum(_:_:)): Returns the lesser of the two given values.
- [minimumMagnitude(_:_:)](/documentation/swift/double/minimummagnitude(_:_:)): Returns the value with lesser magnitude.
- [maximum(_:_:)](/documentation/swift/double/maximum(_:_:)): Returns the greater of the two given values.
- [maximumMagnitude(_:_:)](/documentation/swift/double/maximummagnitude(_:_:)): Returns the value with greater magnitude.

### Finding the Sign and Magnitude

- [magnitude](/documentation/swift/double/magnitude-swift.property): The magnitude of this value.
- [sign](/documentation/swift/double/sign): The sign of the floating-point value.
- [Double.Magnitude](/documentation/swift/double/magnitude-swift.typealias): A type that can represent the absolute value of any possible value of the conforming type.

### Querying a Double

- [ulp](/documentation/swift/double/ulp): The unit in the last place of this value.
- [significand](/documentation/swift/double/significand): The significand of the floating-point value.
- [exponent](/documentation/swift/double/exponent-swift.property): The exponent of the floating-point value.
- [nextUp](/documentation/swift/double/nextup): The least representable value that compares greater than this value.
- [nextDown](/documentation/swift/double/nextdown): The greatest representable value that compares less than this value.
- [binade](/documentation/swift/double/binade): The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.

### Accessing Numeric Constants

- [pi](/documentation/swift/double/pi): The mathematical constant pi (π), approximately equal to 3.14159.
- [infinity](/documentation/swift/double/infinity): Positive infinity.
- [greatestFiniteMagnitude](/documentation/swift/double/greatestfinitemagnitude): The greatest finite number representable by this type.
- [nan](/documentation/swift/double/nan): A quiet NaN (“not a number”).
- [signalingNaN](/documentation/swift/double/signalingnan): A signaling NaN (“not a number”).
- [ulpOfOne](/documentation/swift/double/ulpofone): The unit in the last place of 1.0.
- [leastNonzeroMagnitude](/documentation/swift/double/leastnonzeromagnitude): The least positive number.
- [leastNormalMagnitude](/documentation/swift/double/leastnormalmagnitude): The least positive normal number.
- [zero](/documentation/swift/double/zero): The zero value.

### Working with Binary Representation

- [bitPattern](/documentation/swift/double/bitpattern): The bit pattern of the value’s encoding.
- [significandBitPattern](/documentation/swift/double/significandbitpattern): The raw encoding of the value’s significand field.
- [significandWidth](/documentation/swift/double/significandwidth): The number of bits required to represent the value’s significand.
- [exponentBitPattern](/documentation/swift/double/exponentbitpattern): The raw encoding of the value’s exponent field.
- [significandBitCount](/documentation/swift/double/significandbitcount): The available number of fractional significand bits.
- [exponentBitCount](/documentation/swift/double/exponentbitcount): The number of bits used to represent the type’s exponent.
- [radix](/documentation/swift/double/radix): The radix, or base of exponentiation, for a floating-point type.
- [init(bitPattern:)](/documentation/swift/double/init(bitpattern:)): Creates a new value with the given bit pattern.
- [init(sign:exponentBitPattern:significandBitPattern:)](/documentation/swift/double/init(sign:exponentbitpattern:significandbitpattern:)): Creates a new instance from the specified sign and bit patterns.
- [init(nan:signaling:)](/documentation/swift/double/init(nan:signaling:)): Creates a NaN (“not a number”) value with the specified payload.
- [Double.Exponent](/documentation/swift/double/exponent-swift.typealias): A type that can represent any written exponent.
- [Double.RawSignificand](/documentation/swift/double/rawsignificand): A type that represents the encoded significand of a value.
- [Double.RawExponent](/documentation/swift/double/rawexponent): A type that represents the encoded exponent of a value.

### Querying a Double’s State

- [isZero](/documentation/swift/double/iszero): A Boolean value indicating whether the instance is equal to zero.
- [isFinite](/documentation/swift/double/isfinite): A Boolean value indicating whether this instance is finite.
- [isInfinite](/documentation/swift/double/isinfinite): A Boolean value indicating whether the instance is infinite.
- [isNaN](/documentation/swift/double/isnan): A Boolean value indicating whether the instance is NaN (“not a number”).
- [isSignalingNaN](/documentation/swift/double/issignalingnan): A Boolean value indicating whether the instance is a signaling NaN.
- [isNormal](/documentation/swift/double/isnormal): A Boolean value indicating whether this instance is normal.
- [isSubnormal](/documentation/swift/double/issubnormal): A Boolean value indicating whether the instance is subnormal.
- [isCanonical](/documentation/swift/double/iscanonical): A Boolean value indicating whether the instance’s representation is in its canonical form.
- [floatingPointClass](/documentation/swift/double/floatingpointclass): The classification of this value.

### Encoding and Decoding Values

- [encode(to:)](/documentation/swift/double/encode(to:)): Encodes this value into the given encoder.
- [init(from:)](/documentation/swift/double/init(from:)): Creates a new instance by decoding from the given decoder.

### Creating a Range

- [...(_:_:)](/documentation/swift/double/'...(_:_:)): Returns a closed range that contains both of its bounds.

### Describing a Double

- [description](/documentation/swift/double/description): A textual representation of the value.
- [debugDescription](/documentation/swift/double/debugdescription): A textual representation of the value, suitable for debugging.
- [customMirror](/documentation/swift/double/custommirror): A mirror that reflects the `Double` instance.
- [hash(into:)](/documentation/swift/double/hash(into:)): Hashes the essential components of this value by feeding them into the given hasher.

### Infrequently Used Functionality

- [init()](/documentation/swift/double/init())
- [init(floatLiteral:)](/documentation/swift/double/init(floatliteral:)): Creates an instance initialized to the specified floating-point value.
- [init(integerLiteral:)](/documentation/swift/double/init(integerliteral:)): Creates an instance initialized to the specified integer value.
- [init(integerLiteral:)](/documentation/swift/double/init(integerliteral:)-6hc7j)
- [Double.FloatLiteralType](/documentation/swift/double/floatliteraltype): A type that represents a floating-point literal.
- [Double.IntegerLiteralType](/documentation/swift/double/integerliteraltype): A type that represents an integer literal.
- [advanced(by:)](/documentation/swift/double/advanced(by:)): Returns a value that is offset the specified distance from this value.
- [distance(to:)](/documentation/swift/double/distance(to:)): Returns the distance from this value to the given value, expressed as a stride.
- [Double.Stride](/documentation/swift/double/stride): A type that represents the distance between two values.
- [write(to:)](/documentation/swift/double/write(to:)): Writes a textual representation of this instance into the given output stream.
- [hashValue](/documentation/swift/double/hashvalue): The hash value.

### SIMD-Supporting Types

- [Double.SIMDMaskScalar](/documentation/swift/double/simdmaskscalar)
- [Double.SIMD2Storage](/documentation/swift/double/simd2storage): Storage for a vector of two floating-point values.
- [Double.SIMD4Storage](/documentation/swift/double/simd4storage): Storage for a vector of four floating-point values.
- [Double.SIMD8Storage](/documentation/swift/double/simd8storage): Storage for a vector of eight floating-point values.
- [Double.SIMD16Storage](/documentation/swift/double/simd16storage): Storage for a vector of 16 floating-point values.
- [Double.SIMD32Storage](/documentation/swift/double/simd32storage): Storage for a vector of 32 floating-point values.
- [Double.SIMD64Storage](/documentation/swift/double/simd64storage): Storage for a vector of 64 floating-point values.

### Deprecated

- [customPlaygroundQuickLook](/documentation/swift/double/customplaygroundquicklook): A custom playground Quick Look for the `Double` instance.
- [init(_:)](/documentation/swift/double/init(_:)-8kme5)

### Type Aliases

- [Double.Specification](/documentation/swift/double/specification)
- [Double.UnwrappedType](/documentation/swift/double/unwrappedtype)
- [Double.ValueType](/documentation/swift/double/valuetype)

### Type Properties

- [defaultResolverSpecification](/documentation/swift/double/defaultresolverspecification)
- [mlMultiArrayDataType](/documentation/swift/double/mlmultiarraydatatype)

### Default Implementations

- [AdditiveArithmetic Implementations](/documentation/swift/double/additivearithmetic-implementations)
- [AtomicRepresentable Implementations](/documentation/swift/double/atomicrepresentable-implementations)
- [BinaryFloatingPoint Implementations](/documentation/swift/double/binaryfloatingpoint-implementations)
- [Comparable Implementations](/documentation/swift/double/comparable-implementations)
- [CustomDebugStringConvertible Implementations](/documentation/swift/double/customdebugstringconvertible-implementations)
- [CustomReflectable Implementations](/documentation/swift/double/customreflectable-implementations)
- [CustomStringConvertible Implementations](/documentation/swift/double/customstringconvertible-implementations)
- [Decodable Implementations](/documentation/swift/double/decodable-implementations)
- [Encodable Implementations](/documentation/swift/double/encodable-implementations)
- [Equatable Implementations](/documentation/swift/double/equatable-implementations)
- [ExpressibleByFloatLiteral Implementations](/documentation/swift/double/expressiblebyfloatliteral-implementations)
- [ExpressibleByIntegerLiteral Implementations](/documentation/swift/double/expressiblebyintegerliteral-implementations)
- [FloatingPoint Implementations](/documentation/swift/double/floatingpoint-implementations)
- [Hashable Implementations](/documentation/swift/double/hashable-implementations)
- [LosslessStringConvertible Implementations](/documentation/swift/double/losslessstringconvertible-implementations)
- [Numeric Implementations](/documentation/swift/double/numeric-implementations)
- [SIMDScalar Implementations](/documentation/swift/double/simdscalar-implementations)
- [SignedNumeric Implementations](/documentation/swift/double/signednumeric-implementations)
- [Strideable Implementations](/documentation/swift/double/strideable-implementations)
- [TextOutputStreamable Implementations](/documentation/swift/double/textoutputstreamable-implementations)

## See Also

### Standard Library

- [Int](/documentation/swift/int): A signed integer value type.
- [String](/documentation/swift/string): A Unicode string value that is a collection of characters.
- [Array](/documentation/swift/array): An ordered, random-access collection.
- [Dictionary](/documentation/swift/dictionary): A collection whose elements are key-value pairs.
- [Swift Standard Library](/documentation/swift/swift-standard-library): Solve complex problems and write high-performance, readable code.
