# C Interoperability

Use imported C types or call C variadic functions.

### C and Objective-C Pointers

- [OpaquePointer](/documentation/swift/opaquepointer): A wrapper around an opaque C pointer.
- [AutoreleasingUnsafeMutablePointer](/documentation/swift/autoreleasingunsafemutablepointer): A mutable pointer addressing an Objective-C reference that doesn’t own its target.

### C Variadic Functions

- [withVaList(_:_:)](/documentation/swift/withvalist(_:_:)): Invokes the given closure with a C `va_list` argument derived from the given array of arguments.
- [CVaListPointer](/documentation/swift/cvalistpointer)
- [CVarArg](/documentation/swift/cvararg): A type whose instances can be encoded, and appropriately passed, as elements of a C `va_list`.
- [getVaList(_:)](/documentation/swift/getvalist(_:)): Returns a `CVaListPointer` that is backed by autoreleased storage, built from the given array of arguments.

### Pointers to Values

- [withUnsafePointer(to:_:)](/documentation/swift/withunsafepointer(to:_:)-9fjn6): Invokes the given closure with a pointer to the given argument.
- [withUnsafePointer(to:_:)](/documentation/swift/withunsafepointer(to:_:)-35wrn): Invokes the given closure with a pointer to the given argument.
- [withUnsafeMutablePointer(to:_:)](/documentation/swift/withunsafemutablepointer(to:_:)): Calls the given closure with a mutable pointer to the given argument.
- [withUnsafeBytes(of:_:)](/documentation/swift/withunsafebytes(of:_:)-5zxtl): Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [withUnsafeBytes(of:_:)](/documentation/swift/withunsafebytes(of:_:)-5gesg): Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [withUnsafeMutableBytes(of:_:)](/documentation/swift/withunsafemutablebytes(of:_:)): Invokes the given closure with a mutable buffer pointer covering the raw bytes of the given argument.

### Aliases for Imported C Types

- [CBool](/documentation/swift/cbool): The C ‘_Bool’ and C++ ‘bool’ type.
- [CChar](/documentation/swift/cchar): The C ‘char’ type.
- [CChar8](/documentation/swift/cchar8): The C++20 ‘char8_t’ type, which has UTF-8 encoding.
- [CChar16](/documentation/swift/cchar16): The C++11 ‘char16_t’ type, which has UTF-16 encoding.
- [CChar32](/documentation/swift/cchar32): The C++11 ‘char32_t’ type, which has UTF-32 encoding.
- [CDouble](/documentation/swift/cdouble): The C ‘double’ type.
- [CLongDouble](/documentation/swift/clongdouble)
- [CFloat](/documentation/swift/cfloat): The C ‘float’ type.
- [CFloat16](/documentation/swift/cfloat16): The C ‘_Float16’ type.
- [CInt](/documentation/swift/cint)
- [CLong](/documentation/swift/clong)
- [CLongLong](/documentation/swift/clonglong): The C ‘long long’ type.
- [CShort](/documentation/swift/cshort): The C ‘short’ type.
- [CSignedChar](/documentation/swift/csignedchar): The C ‘signed char’ type.
- [CUnsignedChar](/documentation/swift/cunsignedchar): The C ‘unsigned char’ type.
- [CUnsignedInt](/documentation/swift/cunsignedint)
- [CUnsignedLong](/documentation/swift/cunsignedlong)
- [CUnsignedLongLong](/documentation/swift/cunsignedlonglong): The C ‘unsigned long long’ type.
- [CUnsignedShort](/documentation/swift/cunsignedshort): The C ‘unsigned short’ type.
- [CWideChar](/documentation/swift/cwidechar)

## See Also

### Programming Tasks

- [Input and Output](/documentation/swift/input-and-output): Print values to the console, read from and write to text streams, and use command line arguments.
- [Debugging and Reflection](/documentation/swift/debugging-and-reflection): Fortify your code with runtime checks, and examine your values’ runtime representation.
- [Macros](/documentation/swift/macros): Generate boilerplate code and perform other compile-time operations.
- [Concurrency](/documentation/swift/concurrency): Perform asynchronous and parallel operations.
- [Key-Path Expressions](/documentation/swift/key-path-expressions): Use key-path expressions to access properties dynamically.
- [Manual Memory Management](/documentation/swift/manual-memory-management): Allocate and manage memory manually.
- [Type Casting and Existential Types](/documentation/swift/type-casting-and-existential-types): Perform casts between types or represent values of any type.
- [Operator Declarations](/documentation/swift/operator-declarations): Work with prefix, postfix, and infix operators.
