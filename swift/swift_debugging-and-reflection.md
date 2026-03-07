# Debugging and Reflection

Fortify your code with runtime checks, and examine your values’ runtime representation.

### Printing and Dumping

- [print(_:separator:terminator:)](/documentation/swift/print(_:separator:terminator:)): Writes the textual representations of the given items into the standard output.
- [print(_:separator:terminator:to:)](/documentation/swift/print(_:separator:terminator:to:)): Writes the textual representations of the given items into the given output stream.
- [debugPrint(_:separator:terminator:)](/documentation/swift/debugprint(_:separator:terminator:)): Writes the textual representations of the given items most suitable for debugging into the standard output.
- [debugPrint(_:separator:terminator:to:)](/documentation/swift/debugprint(_:separator:terminator:to:)): Writes the textual representations of the given items most suitable for debugging into the given output stream.
- [dump(_:name:indent:maxDepth:maxItems:)](/documentation/swift/dump(_:name:indent:maxdepth:maxitems:)): Dumps the given object’s contents using its mirror to standard output.
- [dump(_:to:name:indent:maxDepth:maxItems:)](/documentation/swift/dump(_:to:name:indent:maxdepth:maxitems:)): Dumps the given object’s contents using its mirror to the specified output stream.

### Testing

- [assert(_:_:file:line:)](/documentation/swift/assert(_:_:file:line:)): Performs a traditional C-style assert with an optional message.
- [assertionFailure(_:file:line:)](/documentation/swift/assertionfailure(_:file:line:)): Indicates that an internal consistency check failed.
- [precondition(_:_:file:line:)](/documentation/swift/precondition(_:_:file:line:)): Checks a necessary condition for making forward progress.
- [preconditionFailure(_:file:line:)](/documentation/swift/preconditionfailure(_:file:line:)): Indicates that a precondition was violated.

### Exiting a Program

- [fatalError(_:file:line:)](/documentation/swift/fatalerror(_:file:line:)): Unconditionally prints a given message and stops execution.
- [Never](/documentation/swift/never): A type that has no values and can’t be constructed.

### Querying Runtime Values

- [Mirror](/documentation/swift/mirror): A representation of the substructure and display style of an instance of any type.
- [ObjectIdentifier](/documentation/swift/objectidentifier): A unique identifier for a class instance, actor instance, or metatype.
- [type(of:)](/documentation/swift/type(of:)): Returns the dynamic type of a value.

### Customizing Your Type’s Reflection

- [CustomReflectable](/documentation/swift/customreflectable): A type that explicitly supplies its own mirror.
- [CustomLeafReflectable](/documentation/swift/customleafreflectable): A type that explicitly supplies its own mirror, but whose descendant classes are not represented in the mirror unless they also override `customMirror`.
- [CustomPlaygroundDisplayConvertible](/documentation/swift/customplaygrounddisplayconvertible): A type that supplies a custom description for playground logging.
- [PlaygroundQuickLook](/documentation/swift/playgroundquicklook): The sum of types that can be used as a Quick Look representation.
- [DebugDescription()](/documentation/swift/debugdescription()): Converts description definitions to a debugger Type Summary.

## See Also

### Programming Tasks

- [Input and Output](/documentation/swift/input-and-output): Print values to the console, read from and write to text streams, and use command line arguments.
- [Macros](/documentation/swift/macros): Generate boilerplate code and perform other compile-time operations.
- [Concurrency](/documentation/swift/concurrency): Perform asynchronous and parallel operations.
- [Key-Path Expressions](/documentation/swift/key-path-expressions): Use key-path expressions to access properties dynamically.
- [Manual Memory Management](/documentation/swift/manual-memory-management): Allocate and manage memory manually.
- [Type Casting and Existential Types](/documentation/swift/type-casting-and-existential-types): Perform casts between types or represent values of any type.
- [C Interoperability](/documentation/swift/c-interoperability): Use imported C types or call C variadic functions.
- [Operator Declarations](/documentation/swift/operator-declarations): Work with prefix, postfix, and infix operators.
