# AtomicRepresentable Implementations

### Type Aliases

- [Double.AtomicRepresentation](/documentation/swift/double/atomicrepresentation): The storage representation type that `Self` encodes to and decodes from which is a suitable type when used in atomic operations.

### Type Methods

- [decodeAtomicRepresentation(_:)](/documentation/swift/double/decodeatomicrepresentation(_:)): Recovers the logical atomic type `Self` by destroying some `AtomicRepresentation` storage instance returned from an atomic operation.
- [encodeAtomicRepresentation(_:)](/documentation/swift/double/encodeatomicrepresentation(_:)): Destroys a value of `Self` and prepares an `AtomicRepresentation` storage type to be used for atomic operations.
