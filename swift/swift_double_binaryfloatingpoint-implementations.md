# BinaryFloatingPoint Implementations

### Initializers

- [init(_:)](/documentation/swift/double/init(_:)-1488d): Creates a new instance from the given value, rounded to the closest possible representation.
- [init(_:)](/documentation/swift/double/init(_:)-1oh9r): Creates a new value, rounded to the closest possible representation.
- [init(_:)](/documentation/swift/double/init(_:)-5h7qh): Creates a new instance that approximates the given value.
- [init(_:)](/documentation/swift/double/init(_:)-9z7ob): Creates a new instance that approximates the given value.
- [init(_:)](/documentation/swift/double/init(_:)-o1k9): Creates a new instance initialized to the given value.
- [init(exactly:)](/documentation/swift/double/init(exactly:)-1h1oc): Creates a new value, if the given integer can be represented exactly.
- [init(exactly:)](/documentation/swift/double/init(exactly:)-8esra): Creates a new instance from the given value, if it can be represented exactly.
- [init(sign:exponentBitPattern:significandBitPattern:)](/documentation/swift/double/init(sign:exponentbitpattern:significandbitpattern:)): Creates a new instance from the specified sign and bit patterns.

### Instance Properties

- [binade](/documentation/swift/double/binade): The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.
- [exponentBitPattern](/documentation/swift/double/exponentbitpattern): The raw encoding of the value’s exponent field.
- [significandBitPattern](/documentation/swift/double/significandbitpattern): The raw encoding of the value’s significand field.
- [significandWidth](/documentation/swift/double/significandwidth): The number of bits required to represent the value’s significand.

### Type Aliases

- [Double.RawExponent](/documentation/swift/double/rawexponent): A type that represents the encoded exponent of a value.
- [Double.RawSignificand](/documentation/swift/double/rawsignificand): A type that represents the encoded significand of a value.

### Type Properties

- [exponentBitCount](/documentation/swift/double/exponentbitcount): The number of bits used to represent the type’s exponent.
- [significandBitCount](/documentation/swift/double/significandbitcount): The available number of fractional significand bits.

### Type Methods

- [random(in:)](/documentation/swift/double/random(in:)-5o5ha): Returns a random value within the specified range.
- [random(in:)](/documentation/swift/double/random(in:)-6idef): Returns a random value within the specified range.
- [random(in:using:)](/documentation/swift/double/random(in:using:)-1m6gd): Returns a random value within the specified range, using the given generator as a source for randomness.
- [random(in:using:)](/documentation/swift/double/random(in:using:)-613hz): Returns a random value within the specified range, using the given generator as a source for randomness.
