# Initialization with Literals

Allow values of your type to be expressed using different kinds of literals.

### Collection Literals

- [ExpressibleByArrayLiteral](/documentation/swift/expressiblebyarrayliteral): A type that can be initialized using an array literal.
- [ExpressibleByDictionaryLiteral](/documentation/swift/expressiblebydictionaryliteral): A type that can be initialized using a dictionary literal.

### Value Literals

- [ExpressibleByIntegerLiteral](/documentation/swift/expressiblebyintegerliteral): A type that can be initialized with an integer literal.
- [ExpressibleByFloatLiteral](/documentation/swift/expressiblebyfloatliteral): A type that can be initialized with a floating-point literal.
- [ExpressibleByBooleanLiteral](/documentation/swift/expressiblebybooleanliteral): A type that can be initialized with the Boolean literals `true` and `false`.
- [ExpressibleByNilLiteral](/documentation/swift/expressiblebynilliteral): A type that can be initialized using the nil literal, `nil`.
- [StaticBigInt](/documentation/swift/staticbigint): An immutable arbitrary-precision signed integer.

### String Literals

- [ExpressibleByStringLiteral](/documentation/swift/expressiblebystringliteral): A type that can be initialized with a string literal.
- [ExpressibleByExtendedGraphemeClusterLiteral](/documentation/swift/expressiblebyextendedgraphemeclusterliteral): A type that can be initialized with a string literal containing a single extended grapheme cluster.
- [ExpressibleByUnicodeScalarLiteral](/documentation/swift/expressiblebyunicodescalarliteral): A type that can be initialized with a string literal containing a single Unicode scalar value.
- [ExpressibleByStringInterpolation](/documentation/swift/expressiblebystringinterpolation): A type that can be initialized by string interpolation with a string literal that includes expressions.
- [StringInterpolationProtocol](/documentation/swift/stringinterpolationprotocol): Represents the contents of a string literal with interpolations while it’s being built up.
- [DefaultStringInterpolation](/documentation/swift/defaultstringinterpolation): Represents a string literal with interpolations while it’s being built up.

### Default Types for Literals

- [Default Literal Types](/documentation/swift/default-literal-types): Type aliases representing the concrete type that a literal takes when no other type information is provided.

## See Also

### Tools for Your Types

- [Basic Behaviors](/documentation/swift/basic-behaviors): Use your custom types in operations that depend on testing for equality or order and as members of sets and dictionaries.
- [Encoding, Decoding, and Serialization](/documentation/swift/encoding-decoding-and-serialization): Serialize and deserialize instances of your types with implicit or customized encoding.
