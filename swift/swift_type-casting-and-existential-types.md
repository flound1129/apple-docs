# Type Casting and Existential Types

Perform casts between types or represent values of any type.

### Integer Value Casting

- [numericCast(_:)](/documentation/swift/numericcast(_:)): Returns the given integer as the equivalent value in a different integer type.

### Closure Casting

- [withoutActuallyEscaping(_:do:)](/documentation/swift/withoutactuallyescaping(_:do:)): Allows a nonescaping closure to temporarily be used as if it were allowed to escape.

### Instance Casting

- [unsafeDowncast(_:to:)](/documentation/swift/unsafedowncast(_:to:)): Returns the given instance cast unconditionally to the specified type.
- [unsafeBitCast(_:to:)](/documentation/swift/unsafebitcast(_:to:)): Returns the bits of the given instance, interpreted as having the specified type.

### Existential Types

- [AnyObject](/documentation/swift/anyobject): The protocol to which all classes implicitly conform.
- [AnyClass](/documentation/swift/anyclass): The protocol to which all class types implicitly conform.

### Comparing Identity

- [===(_:_:)](/documentation/swift/===(_:_:))
- [!==(_:_:)](/documentation/swift/!==(_:_:)): Returns a Boolean value indicating whether two references point to different object instances.

### Void Type

- [Void](/documentation/swift/void): The return type of functions that don’t explicitly specify a return type, that is, an empty tuple `()`.

## See Also

### Programming Tasks

- [Input and Output](/documentation/swift/input-and-output): Print values to the console, read from and write to text streams, and use command line arguments.
- [Debugging and Reflection](/documentation/swift/debugging-and-reflection): Fortify your code with runtime checks, and examine your values’ runtime representation.
- [Macros](/documentation/swift/macros): Generate boilerplate code and perform other compile-time operations.
- [Concurrency](/documentation/swift/concurrency): Perform asynchronous and parallel operations.
- [Key-Path Expressions](/documentation/swift/key-path-expressions): Use key-path expressions to access properties dynamically.
- [Manual Memory Management](/documentation/swift/manual-memory-management): Allocate and manage memory manually.
- [C Interoperability](/documentation/swift/c-interoperability): Use imported C types or call C variadic functions.
- [Operator Declarations](/documentation/swift/operator-declarations): Work with prefix, postfix, and infix operators.
