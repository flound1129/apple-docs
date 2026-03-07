# Manual Memory Management

Allocate and manage memory manually.

### First Steps

- [Calling Functions With Pointer Parameters](/documentation/swift/calling-functions-with-pointer-parameters): Use implicit pointer casting or bridging when calling functions that takes pointers as parameters.

### Safe Memory Access

- [Span](/documentation/swift/span): `Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [RawSpan](/documentation/swift/rawspan): `RawSpan` represents a contiguous region of memory which contains initialized bytes.
- [OutputSpan](/documentation/swift/outputspan)
- [OutputRawSpan](/documentation/swift/outputrawspan)
- [UTF8Span](/documentation/swift/utf8span): A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.
- [MutableSpan](/documentation/swift/mutablespan)
- [MutableRawSpan](/documentation/swift/mutablerawspan)

### Typed Pointers

- [UnsafePointer](/documentation/swift/unsafepointer): A pointer for accessing data of a specific type.
- [UnsafeMutablePointer](/documentation/swift/unsafemutablepointer): A pointer for accessing and manipulating data of a specific type.
- [UnsafeBufferPointer](/documentation/swift/unsafebufferpointer): A nonowning collection interface to a buffer of elements stored contiguously in memory.
- [UnsafeMutableBufferPointer](/documentation/swift/unsafemutablebufferpointer): A nonowning collection interface to a buffer of mutable elements stored contiguously in memory.

### Raw Pointers

- [UnsafeRawPointer](/documentation/swift/unsaferawpointer): A raw pointer for accessing untyped data.
- [UnsafeMutableRawPointer](/documentation/swift/unsafemutablerawpointer): A raw pointer for accessing and manipulating untyped data.
- [UnsafeRawBufferPointer](/documentation/swift/unsaferawbufferpointer): A  nonowning collection interface to the bytes in a region of memory.
- [UnsafeMutableRawBufferPointer](/documentation/swift/unsafemutablerawbufferpointer): A mutable nonowning collection interface to the bytes in a region of memory.

### Memory Access

- [withUnsafePointer(to:_:)](/documentation/swift/withunsafepointer(to:_:)-9fjn6): Invokes the given closure with a pointer to the given argument.
- [withUnsafePointer(to:_:)](/documentation/swift/withunsafepointer(to:_:)-35wrn): Invokes the given closure with a pointer to the given argument.
- [withUnsafeMutablePointer(to:_:)](/documentation/swift/withunsafemutablepointer(to:_:)): Calls the given closure with a mutable pointer to the given argument.
- [withUnsafeBytes(of:_:)](/documentation/swift/withunsafebytes(of:_:)-5zxtl): Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [withUnsafeBytes(of:_:)](/documentation/swift/withunsafebytes(of:_:)-5gesg): Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [withUnsafeMutableBytes(of:_:)](/documentation/swift/withunsafemutablebytes(of:_:)): Invokes the given closure with a mutable buffer pointer covering the raw bytes of the given argument.
- [withUnsafeTemporaryAllocation(of:capacity:_:)](/documentation/swift/withunsafetemporaryallocation(of:capacity:_:)): Provides scoped access to a buffer pointer to memory of the specified type and with the specified capacity.
- [withUnsafeTemporaryAllocation(byteCount:alignment:_:)](/documentation/swift/withunsafetemporaryallocation(bytecount:alignment:_:)): Provides scoped access to a raw buffer pointer with the specified byte count and alignment.
- [swap(_:_:)](/documentation/swift/swap(_:_:)): Exchanges the values of the two arguments.
- [exchange(_:with:)](/documentation/swift/exchange(_:with:)): Replaces the value of a mutable value with the supplied new value, returning the original.

### Memory Layout

- [MemoryLayout](/documentation/swift/memorylayout): The memory layout of a type, describing its size, stride, and alignment.

### Reference Counting

- [Unmanaged](/documentation/swift/unmanaged): A type for propagating an unmanaged object reference.
- [withExtendedLifetime(_:_:)](/documentation/swift/withextendedlifetime(_:_:)-4mmpv): Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.
- [withExtendedLifetime(_:_:)](/documentation/swift/withextendedlifetime(_:_:)-59dz3): Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.
- [extendLifetime(_:)](/documentation/swift/extendlifetime(_:)): Extends the lifetime of the given instance.

## See Also

### Programming Tasks

- [Input and Output](/documentation/swift/input-and-output): Print values to the console, read from and write to text streams, and use command line arguments.
- [Debugging and Reflection](/documentation/swift/debugging-and-reflection): Fortify your code with runtime checks, and examine your values’ runtime representation.
- [Macros](/documentation/swift/macros): Generate boilerplate code and perform other compile-time operations.
- [Concurrency](/documentation/swift/concurrency): Perform asynchronous and parallel operations.
- [Key-Path Expressions](/documentation/swift/key-path-expressions): Use key-path expressions to access properties dynamically.
- [Type Casting and Existential Types](/documentation/swift/type-casting-and-existential-types): Perform casts between types or represent values of any type.
- [C Interoperability](/documentation/swift/c-interoperability): Use imported C types or call C variadic functions.
- [Operator Declarations](/documentation/swift/operator-declarations): Work with prefix, postfix, and infix operators.
