# Basic Behaviors

Use your custom types in operations that depend on testing for equality or order and as members of sets and dictionaries.

### Equality and Ordering

- [Equatable](/documentation/swift/equatable): A type that can be compared for value equality.
- [Comparable](/documentation/swift/comparable): A type that can be compared using the relational operators `<`, `<=`, `>=`, and `>`.
- [Identifiable](/documentation/swift/identifiable): A class of types whose instances hold the value of an entity with stable identity.

### Copying

- [Copyable](/documentation/swift/copyable): A type whose values can be implicitly or explicitly copied.
- [BitwiseCopyable](/documentation/swift/bitwisecopyable)
- [Escapable](/documentation/swift/escapable): A type whose values can persist beyond their immediate local scope.

### Sets and Dictionaries

- [Hashable](/documentation/swift/hashable): A type that can be hashed into a `Hasher` to produce an integer hash value.
- [Hasher](/documentation/swift/hasher): The universal hash function used by `Set` and `Dictionary`.

### String Representation

- [CustomStringConvertible](/documentation/swift/customstringconvertible): A type with a customized textual representation.
- [LosslessStringConvertible](/documentation/swift/losslessstringconvertible): A type that can be represented as a string in a lossless, unambiguous way.
- [CustomDebugStringConvertible](/documentation/swift/customdebugstringconvertible): A type with a customized textual representation suitable for debugging purposes.

### Raw Representation

- [CaseIterable](/documentation/swift/caseiterable): A type that provides a collection of all of its values.
- [RawRepresentable](/documentation/swift/rawrepresentable): A type that can be converted to and from an associated raw value.

## See Also

### Tools for Your Types

- [Encoding, Decoding, and Serialization](/documentation/swift/encoding-decoding-and-serialization): Serialize and deserialize instances of your types with implicit or customized encoding.
- [Initialization with Literals](/documentation/swift/initialization-with-literals): Allow values of your type to be expressed using different kinds of literals.
