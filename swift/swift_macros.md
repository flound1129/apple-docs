# Macros

Generate boilerplate code and perform other compile-time operations.

### Essentials

- [Applying Macros](/documentation/swift/applying-macros): Use macros to generate repetitive code at compile time.

### Getting Source Location Information

- [file()](/documentation/swift/file()): Produces the path to the file in which it appears.
- [fileID()](/documentation/swift/fileid()): Produces a unique identifier for the source file in which the macro appears.
- [filePath()](/documentation/swift/filepath()): Produces the complete path to the file in which the macro appears.
- [function()](/documentation/swift/function()): Produces the name of the declaration in which it appears.
- [line()](/documentation/swift/line()): Produces the line number on which it appears.
- [column()](/documentation/swift/column()): Produces the column number in which the macro begins.

### Generating Compile-Time Diagnostics

- [warning(_:)](/documentation/swift/warning(_:)): Produces the given warning message during compilation.
- [error(_:)](/documentation/swift/error(_:)): Emits the given message as a fatal error and terminates the compilation process.

### Writing Custom Macros

- [externalMacro(module:type:)](/documentation/swift/externalmacro(module:type:)): Specifies the module and type name for a macro’s implementation.

### Accessing the Dynamic Shared Object Handle

- [dsohandle()](/documentation/swift/dsohandle()): Produces the dynamic shared object (DSO) handle in use where the macro appears.

## See Also

### Programming Tasks

- [Input and Output](/documentation/swift/input-and-output): Print values to the console, read from and write to text streams, and use command line arguments.
- [Debugging and Reflection](/documentation/swift/debugging-and-reflection): Fortify your code with runtime checks, and examine your values’ runtime representation.
- [Concurrency](/documentation/swift/concurrency): Perform asynchronous and parallel operations.
- [Key-Path Expressions](/documentation/swift/key-path-expressions): Use key-path expressions to access properties dynamically.
- [Manual Memory Management](/documentation/swift/manual-memory-management): Allocate and manage memory manually.
- [Type Casting and Existential Types](/documentation/swift/type-casting-and-existential-types): Perform casts between types or represent values of any type.
- [C Interoperability](/documentation/swift/c-interoperability): Use imported C types or call C variadic functions.
- [Operator Declarations](/documentation/swift/operator-declarations): Work with prefix, postfix, and infix operators.
