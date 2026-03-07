# Substring

A slice of a string.

```swift
@frozen struct Substring
```

## Overview

When you create a slice of a string, a `Substring` instance is the result. Operating on substrings is fast and efficient because a substring shares its storage with the original string. The `Substring` type presents the same interface as `String`, so you can avoid or defer any copying of the string’s contents.

The following example creates a `greeting` string, and then finds the substring of the first sentence:

```swift
let greeting = "Hi there! It's nice to meet you! 👋"
let endOfSentence = greeting.firstIndex(of: "!")!
let firstSentence = greeting[...endOfSentence]
// firstSentence == "Hi there!"
```

You can perform many string operations on a substring. Here, we find the length of the first sentence and create an uppercase version.

```swift
print("'\(firstSentence)' is \(firstSentence.count) characters long.")
// Prints "'Hi there!' is 9 characters long."

let shoutingSentence = firstSentence.uppercased()
// shoutingSentence == "HI THERE!"
```

# Converting a Substring to a String

This example defines a `rawData` string with some unstructured data, and then uses the string’s `prefix(while:)` method to create a substring of the numeric prefix:

```swift
let rawInput = "126 a.b 22219 zzzzzz"
let numericPrefix = rawInput.prefix(while: { "0"..."9" ~= $0 })
// numericPrefix is the substring "126"
```

When you need to store a substring or pass it to a function that requires a `String` instance, you can convert it to a `String` by using the `String(_:)` initializer. Calling this initializer copies the contents of the substring to a new string.

```swift
func parseAndAddOne(_ s: String) -> Int {
    return Int(s, radix: 10)! + 1
}
_ = parseAndAddOne(numericPrefix)
// error: cannot convert value...
let incrementedPrefix = parseAndAddOne(String(numericPrefix))
// incrementedPrefix == 127
```

Alternatively, you can convert the function that takes a `String` to one that is generic over the `StringProtocol` protocol. The following code declares a generic version of the `parseAndAddOne(_:)` function:

```swift
func genericParseAndAddOne<S: StringProtocol>(_ s: S) -> Int {
    return Int(s, radix: 10)! + 1
}
let genericallyIncremented = genericParseAndAddOne(numericPrefix)
// genericallyIncremented == 127
```

You can call this generic function with an instance of either `String` or `Substring`.

> **Important:**
> Don’t store substrings longer than you need them to perform a specific operation. A substring holds a reference to the entire storage of the string it comes from, not just to the portion it presents, even when there is no other reference to the original string. Storing substrings may, therefore, prolong the lifetime of string data that is no longer otherwise accessible, which can appear to be memory leakage.
>

### Operators

- [~=(_:_:)](/documentation/swift/substring/~=(_:_:))

### Initializers

- [init()](/documentation/swift/substring/init()): Creates an empty substring.
- [init(_:)](/documentation/swift/substring/init(_:)-4njms): Creates a Substring having the given content.
- [init(_:)](/documentation/swift/substring/init(_:)-61zpv): Creates a Substring having the given content.
- [init(_:)](/documentation/swift/substring/init(_:)-7k0au): Creates a Substring having the given content.

### Instance Properties

- [base](/documentation/swift/substring/base): Returns the underlying string from which this substring was derived.
- [characters](/documentation/swift/substring/characters): A view of the string’s contents as a collection of characters.
- [customPlaygroundQuickLook](/documentation/swift/substring/customplaygroundquicklook): A custom playground Quick Look for this instance.
- [isContiguousUTF8](/documentation/swift/substring/iscontiguousutf8): Returns whether this string’s storage contains validly-encoded UTF-8 contents in contiguous memory.
- [utf8Span](/documentation/swift/substring/utf8span): A UTF-8 span over the code units that make up this substring.

### Instance Methods

- [filter(_:)](/documentation/swift/substring/filter(_:))
- [makeContiguousUTF8()](/documentation/swift/substring/makecontiguousutf8()): If this string is not contiguous, make it so. If this mutates the substring, it will invalidate any pre-existing indices.
- [replaceSubrange(_:with:)](/documentation/swift/substring/replacesubrange(_:with:)-mfwu)
- [withMutableCharacters(_:)](/documentation/swift/substring/withmutablecharacters(_:)): Applies the given closure to a mutable view of the string’s characters.
- [withUTF8(_:)](/documentation/swift/substring/withutf8(_:)): Runs `body` over the content of this substring in contiguous memory. If this substring is not contiguous, this will first make it contiguous, which will also speed up subsequent access. If this mutates the substring, it will invalidate any pre-existing indices.

### Type Aliases

- [Substring.CharacterView](/documentation/swift/substring/characterview): A view of a string’s contents as a collection of characters.
- [Substring.Output](/documentation/swift/substring/output)

### Default Implementations

- [Attachable Implementations](/documentation/swift/substring/attachable-implementations)
- [BidirectionalCollection Implementations](/documentation/swift/substring/bidirectionalcollection-implementations)
- [Collection Implementations](/documentation/swift/substring/collection-implementations)
- [Comparable Implementations](/documentation/swift/substring/comparable-implementations)
- [CustomDebugStringConvertible Implementations](/documentation/swift/substring/customdebugstringconvertible-implementations)
- [CustomReflectable Implementations](/documentation/swift/substring/customreflectable-implementations)
- [CustomStringConvertible Implementations](/documentation/swift/substring/customstringconvertible-implementations)
- [Equatable Implementations](/documentation/swift/substring/equatable-implementations)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](/documentation/swift/substring/expressiblebyextendedgraphemeclusterliteral-implementations)
- [ExpressibleByStringInterpolation Implementations](/documentation/swift/substring/expressiblebystringinterpolation-implementations)
- [ExpressibleByStringLiteral Implementations](/documentation/swift/substring/expressiblebystringliteral-implementations)
- [ExpressibleByUnicodeScalarLiteral Implementations](/documentation/swift/substring/expressiblebyunicodescalarliteral-implementations)
- [Hashable Implementations](/documentation/swift/substring/hashable-implementations)
- [LosslessStringConvertible Implementations](/documentation/swift/substring/losslessstringconvertible-implementations)
- [RangeReplaceableCollection Implementations](/documentation/swift/substring/rangereplaceablecollection-implementations)
- [Sequence Implementations](/documentation/swift/substring/sequence-implementations)
- [StringProtocol Implementations](/documentation/swift/substring/stringprotocol-implementations)
- [TextOutputStream Implementations](/documentation/swift/substring/textoutputstream-implementations)
- [TextOutputStreamable Implementations](/documentation/swift/substring/textoutputstreamable-implementations)

## See Also

### Related String Types

- [StringProtocol](/documentation/swift/stringprotocol): A type that can represent a string as a collection of characters.
- [String.Index](/documentation/swift/string/index): A position of a character or code unit in a string.
- [String.UnicodeScalarView](/documentation/swift/string/unicodescalarview): A view of a string’s contents as a collection of Unicode scalar values.
- [String.UTF16View](/documentation/swift/string/utf16view): A view of a string’s contents as a collection of UTF-16 code units.
- [String.UTF8View](/documentation/swift/string/utf8view): A view of a string’s contents as a collection of UTF-8 code units.
- [String.Iterator](/documentation/swift/string/iterator): A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [String.Encoding](/documentation/swift/string/encoding)
