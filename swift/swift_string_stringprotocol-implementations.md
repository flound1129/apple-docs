# StringProtocol Implementations

### Structures

- [String.UTF16View](/documentation/swift/string/utf16view): A view of a string’s contents as a collection of UTF-16 code units.
- [String.UTF8View](/documentation/swift/string/utf8view): A view of a string’s contents as a collection of UTF-8 code units.
- [String.UnicodeScalarView](/documentation/swift/string/unicodescalarview): A view of a string’s contents as a collection of Unicode scalar values.

### Operators

- [!=(_:_:)](/documentation/swift/string/!=(_:_:)-frzf)
- [==(_:_:)](/documentation/swift/string/==(_:_:)-8kzxf)
- [>(_:_:)](/documentation/swift/string/_(_:_:)-6o7qv)
- [<(_:_:)](/documentation/swift/string/_(_:_:)-8d1wy)
- [<=(_:_:)](/documentation/swift/string/_=(_:_:)-5y22v)
- [>=(_:_:)](/documentation/swift/string/_=(_:_:)-nd86)

### Initializers

- [init(cString:)](/documentation/swift/string/init(cstring:)-2p84k): Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init(decoding:as:)](/documentation/swift/string/init(decoding:as:)): Creates a string from the given Unicode code units in the specified encoding.
- [init(decodingCString:as:)](/documentation/swift/string/init(decodingcstring:as:)-8yowf): Creates a new string by copying the null-terminated sequence of code units referenced by the given pointer.

### Instance Properties

- [unicodeScalars](/documentation/swift/string/unicodescalars): The string’s value represented as a collection of Unicode scalar values.
- [utf16](/documentation/swift/string/utf16): A UTF-16 encoding of `self`.
- [utf8](/documentation/swift/string/utf8): A UTF-8 encoding of `self`.

### Instance Methods

- [hasPrefix(_:)](/documentation/swift/string/hasprefix(_:))
- [hasSuffix(_:)](/documentation/swift/string/hassuffix(_:))
- [lowercased()](/documentation/swift/string/lowercased()): Returns a lowercase version of the string.
- [uppercased()](/documentation/swift/string/uppercased()): Returns an uppercase version of the string.
- [withCString(_:)](/documentation/swift/string/withcstring(_:)): Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of UTF-8 code units.
- [withCString(encodedAs:_:)](/documentation/swift/string/withcstring(encodedas:_:)): Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of code units.
