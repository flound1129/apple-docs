# String

A Unicode string value that is a collection of characters.

```swift
@frozen struct String
```

## Overview

A string is a series of characters, such as `"Swift"`, that forms a collection. Strings in Swift are Unicode correct and locale insensitive, and are designed to be efficient. The `String` type bridges with the Objective-C class `NSString` and offers interoperability with C functions that works with strings.

You can create new strings using string literals or string interpolations. A *string literal* is a series of characters enclosed in quotes.

```swift
let greeting = "Welcome!"
```

*String interpolations* are string literals that evaluate any included expressions and convert the results to string form. String interpolations give you an easy way to build a string from multiple pieces. Wrap each expression in a string interpolation in parentheses, prefixed by a backslash.

```swift
let name = "Rosa"
let personalizedGreeting = "Welcome, \(name)!"
// personalizedGreeting == "Welcome, Rosa!"

let price = 2
let number = 3
let cookiePrice = "\(number) cookies: $\(price * number)."
// cookiePrice == "3 cookies: $6."
```

Combine strings using the concatenation operator (`+`).

```swift
let longerGreeting = greeting + " We're glad you're here!"
// longerGreeting == "Welcome! We're glad you're here!"
```

Multiline string literals are enclosed in three double quotation marks (`"""`), with each delimiter on its own line. Indentation is stripped from each line of a multiline string literal to match the indentation of the closing delimiter.

```swift
let banner = """
          __,
         (           o  /) _/_
          `.  , , , ,  //  /
        (___)(_(_/_(_ //_ (__
                     /)
                    (/
        """
```

# Modifying and Comparing Strings

Strings always have value semantics. Modifying a copy of a string leaves the original unaffected.

```swift
var otherGreeting = greeting
otherGreeting += " Have a nice time!"
// otherGreeting == "Welcome! Have a nice time!"

print(greeting)
// Prints "Welcome!"
```

Comparing strings for equality using the equal-to operator (`==`) or a relational operator (like `<` or `>=`) is always performed using Unicode canonical representation. As a result, different representations of a string compare as being equal.

```swift
let cafe1 = "Cafe\u{301}"
let cafe2 = "Café"
print(cafe1 == cafe2)
// Prints "true"
```

The Unicode scalar value `"\u{301}"` modifies the preceding character to include an accent, so `"e\u{301}"` has the same canonical representation as the single Unicode scalar value `"é"`.

Basic string operations are not sensitive to locale settings, ensuring that string comparisons and other operations always have a single, stable result, allowing strings to be used as keys in `Dictionary` instances and for other purposes.

# Accessing String Elements

A string is a collection of *extended grapheme clusters*, which approximate human-readable characters. Many individual characters, such as “é”, “김”, and “🇮🇳”, can be made up of multiple Unicode scalar values. These scalar values are combined by Unicode’s boundary algorithms into extended grapheme clusters, represented by the Swift `Character` type. Each element of a string is represented by a `Character` instance.

For example, to retrieve the first word of a longer string, you can search for a space and then create a substring from a prefix of the string up to that point:

```swift
let name = "Marie Curie"
let firstSpace = name.firstIndex(of: " ") ?? name.endIndex
let firstName = name[..<firstSpace]
// firstName == "Marie"
```

The `firstName` constant is an instance of the `Substring` type—a type that represents substrings of a string while sharing the original string’s storage. Substrings present the same interface as strings.

```swift
print("\(name)'s first name has \(firstName.count) letters.")
// Prints "Marie Curie's first name has 5 letters."
```

# Accessing a String’s Unicode Representation

If you need to access the contents of a string as encoded in different Unicode encodings, use one of the string’s `unicodeScalars`, `utf16`, or `utf8` properties. Each property provides access to a view of the string as a series of code units, each encoded in a different Unicode encoding.

To demonstrate the different views available for every string, the following examples use this `String` instance:

```swift
let cafe = "Cafe\u{301} du 🌍"
print(cafe)
// Prints "Café du 🌍"
```

The `cafe` string is a collection of the nine characters that are visible when the string is displayed.

```swift
print(cafe.count)
// Prints "9"
print(Array(cafe))
// Prints "["C", "a", "f", "é", " ", "d", "u", " ", "🌍"]"
```

## Unicode Scalar View

A string’s `unicodeScalars` property is a collection of Unicode scalar values, the 21-bit codes that are the basic unit of Unicode. Each scalar value is represented by a `Unicode.Scalar` instance and is equivalent to a UTF-32 code unit.

```swift
print(cafe.unicodeScalars.count)
// Prints "10"
print(Array(cafe.unicodeScalars))
// Prints "["C", "a", "f", "e", "\u{0301}", " ", "d", "u", " ", "\u{0001F30D}"]"
print(cafe.unicodeScalars.map { $0.value })
// Prints "[67, 97, 102, 101, 769, 32, 100, 117, 32, 127757]"
```

The `unicodeScalars` view’s elements comprise each Unicode scalar value in the `cafe` string. In particular, because `cafe` was declared using the decomposed form of the `"é"` character, `unicodeScalars` contains the scalar values for both the letter `"e"` (101) and the accent character `"´"` (769).

## UTF-16 View

A string’s `utf16` property is a collection of UTF-16 code units, the 16-bit encoding form of the string’s Unicode scalar values. Each code unit is stored as a `UInt16` instance.

```swift
print(cafe.utf16.count)
// Prints "11"
print(Array(cafe.utf16))
// Prints "[67, 97, 102, 101, 769, 32, 100, 117, 32, 55356, 57101]"
```

The elements of the `utf16` view are the code units for the string when encoded in UTF-16. These elements match those accessed through indexed `NSString` APIs.

```swift
let nscafe = cafe as NSString
print(nscafe.length)
// Prints "11"
print(nscafe.character(at: 3))
// Prints "101"
```

## UTF-8 View

A string’s `utf8` property is a collection of UTF-8 code units, the 8-bit encoding form of the string’s Unicode scalar values. Each code unit is stored as a `UInt8` instance.

```swift
print(cafe.utf8.count)
// Prints "14"
print(Array(cafe.utf8))
// Prints "[67, 97, 102, 101, 204, 129, 32, 100, 117, 32, 240, 159, 140, 141]"
```

The elements of the `utf8` view are the code units for the string when encoded in UTF-8. This representation matches the one used when `String` instances are passed to C APIs.

```swift
let cLength = strlen(cafe)
print(cLength)
// Prints "14"
```

# Measuring the Length of a String

When you need to know the length of a string, you must first consider what you’ll use the length for. Are you measuring the number of characters that will be displayed on the screen, or are you measuring the amount of storage needed for the string in a particular encoding? A single string can have greatly differing lengths when measured by its different views.

For example, an ASCII character like the capital letter *A* is represented by a single element in each of its four views. The Unicode scalar value of *A* is `65`, which is small enough to fit in a single code unit in both UTF-16 and UTF-8.

```swift
let capitalA = "A"
print(capitalA.count)
// Prints "1"
print(capitalA.unicodeScalars.count)
// Prints "1"
print(capitalA.utf16.count)
// Prints "1"
print(capitalA.utf8.count)
// Prints "1"
```

On the other hand, an emoji flag character is constructed from a pair of Unicode scalar values, like `"\u{1F1F5}"` and `"\u{1F1F7}"`. Each of these scalar values, in turn, is too large to fit into a single UTF-16 or UTF-8 code unit. As a result, each view of the string `"🇵🇷"` reports a different length.

```swift
let flag = "🇵🇷"
print(flag.count)
// Prints "1"
print(flag.unicodeScalars.count)
// Prints "2"
print(flag.utf16.count)
// Prints "4"
print(flag.utf8.count)
// Prints "8"
```

To check whether a string is empty, use its `isEmpty` property instead of comparing the length of one of the views to `0`. Unlike with `isEmpty`, calculating a view’s `count` property requires iterating through the elements of the string.

# Accessing String View Elements

To find individual elements of a string, use the appropriate view for your task. For example, to retrieve the first word of a longer string, you can search the string for a space and then create a new string from a prefix of the string up to that point.

```swift
let name = "Marie Curie"
let firstSpace = name.firstIndex(of: " ") ?? name.endIndex
let firstName = name[..<firstSpace]
print(firstName)
// Prints "Marie"
```

Strings and their views share indices, so you can access the UTF-8 view of the `name` string using the same `firstSpace` index.

```swift
print(Array(name.utf8[..<firstSpace]))
// Prints "[77, 97, 114, 105, 101]"
```

Note that an index into one view may not have an exact corresponding position in another view. For example, the `flag` string declared above comprises a single character, but is composed of eight code units when encoded as UTF-8. The following code creates constants for the first and second positions in the `flag.utf8` view. Accessing the `utf8` view with these indices yields the first and second code UTF-8 units.

```swift
let firstCodeUnit = flag.startIndex
let secondCodeUnit = flag.utf8.index(after: firstCodeUnit)
// flag.utf8[firstCodeUnit] == 240
// flag.utf8[secondCodeUnit] == 159
```

When used to access the elements of the `flag` string itself, however, the `secondCodeUnit` index does not correspond to the position of a specific character. Instead of only accessing the specific UTF-8 code unit, that index is treated as the position of the character at the index’s encoded offset. In the case of `secondCodeUnit`, that character is still the flag itself.

```swift
// flag[firstCodeUnit] == "🇵🇷"
// flag[secondCodeUnit] == "🇵🇷"
```

If you need to validate that an index from one string’s view corresponds with an exact position in another view, use the index’s `samePosition(in:)` method or the `init(_:within:)` initializer.

```swift
if let exactIndex = secondCodeUnit.samePosition(in: flag) {
    print(flag[exactIndex])
} else {
    print("No exact match for this position.")
}
// Prints "No exact match for this position."
```

# Performance Optimizations

Although strings in Swift have value semantics, strings use a copy-on-write strategy to store their data in a buffer. This buffer can then be shared by different copies of a string. A string’s data is only copied lazily, upon mutation, when more than one string instance is using the same buffer. Therefore, the first in any sequence of mutating operations may cost O(*n*) time and space.

When a string’s contiguous storage fills up, a new buffer must be allocated and data must be moved to the new storage. String buffers use an exponential growth strategy that makes appending to a string a constant time operation when averaged over many append operations.

# Bridging Between String and NSString

Any `String` instance can be bridged to `NSString` using the type-cast operator (`as`), and any `String` instance that originates in Objective-C may use an `NSString` instance as its storage. Because any arbitrary subclass of `NSString` can become a `String` instance, there are no guarantees about representation or efficiency when a `String` instance is backed by `NSString` storage. Because `NSString` is immutable, it is just as though the storage was shared by a copy. The first in any sequence of mutating operations causes elements to be copied into unique, contiguous storage which may cost O(*n*) time and space, where *n* is the length of the string’s encoded representation (or more, if the underlying `NSString` has unusual performance characteristics).

For more information about the Unicode terms used in this discussion, see the [Unicode.org glossary](http://www.unicode.org/glossary/). In particular, this discussion mentions [extended grapheme clusters](http://www.unicode.org/glossary/#extended_grapheme_cluster), [Unicode scalar values](http://www.unicode.org/glossary/#unicode_scalar_value), and [canonical equivalence](http://www.unicode.org/glossary/#canonical_equivalent).

### Creating a String

- [init(decoding:)](/documentation/swift/string/init(decoding:)-nm7v): Creates a string by interpreting the file path’s content as UTF-8 on Unix and UTF-16 on Windows.
- [init()](/documentation/swift/string/init()): Creates an empty string.
- [init(_:)](/documentation/swift/string/init(_:)-8v3fo): Creates a string containing the given character.
- [init(_:)](/documentation/swift/string/init(_:)-8og6g): Creates a new string containing the characters in the given sequence.
- [init(_:)](/documentation/swift/string/init(_:)-1ip93): Creates a new instance of a collection containing the elements of a sequence.
- [init(_:)](/documentation/swift/string/init(_:)-50pwi): Creates a new string containing the characters in the given sequence.
- [init(_:)](/documentation/swift/string/init(_:)-14lv5): Creates a new string from the given substring.
- [init(repeating:count:)](/documentation/swift/string/init(repeating:count:)-23xjt): Creates a new string representing the given string repeated the specified number of times.
- [init(repeating:count:)](/documentation/swift/string/init(repeating:count:)-11bpi): Creates a string representing the given character repeated the specified number of times.
- [init(unsafeUninitializedCapacity:initializingUTF8With:)](/documentation/swift/string/init(unsafeuninitializedcapacity:initializingutf8with:)): Creates a new string with the specified capacity in UTF-8 code units, and then calls the given closure with a buffer covering the string’s uninitialized memory.

### Inspecting a String

- [isEmpty](/documentation/swift/string/isempty): A Boolean value indicating whether a string has no characters.
- [count](/documentation/swift/string/count): The number of characters in a string.

### Creating a String from Unicode Data

- [init(_:)](/documentation/swift/string/init(_:)-8ay23)
- [init(data:encoding:)](/documentation/swift/string/init(data:encoding:)): Returns a `String` initialized by converting given `data` into Unicode characters using a given `encoding`.
- [init(validatingUTF8:)](/documentation/swift/string/init(validatingutf8:)-208fn): Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.
- [init(validating:as:)](/documentation/swift/string/init(validating:as:)-84qr9): Creates a new string by copying and validating the sequence of code units passed in, according to the specified encoding.
- [init(validating:as:)](/documentation/swift/string/init(validating:as:)-5cw2c): Creates a new string by copying and validating the sequence of code units passed in, according to the specified encoding.
- [init(utf8String:)](/documentation/swift/string/init(utf8string:)-8qmaq): Creates a string by copying the data from a given null-terminated array of UTF8-encoded bytes.
- [init(utf8String:)](/documentation/swift/string/init(utf8string:)-3mcco): Creates a string by copying the data from a given null-terminated C array of UTF8-encoded bytes.
- [init(utf16CodeUnits:count:)](/documentation/swift/string/init(utf16codeunits:count:)): Creates a new string that contains the specified number of characters from the given C array of Unicode characters.
- [init(utf16CodeUnitsNoCopy:count:freeWhenDone:)](/documentation/swift/string/init(utf16codeunitsnocopy:count:freewhendone:)): Creates a new string that contains the specified number of characters from the given C array of UTF-16 code units.
- [init(decoding:as:)](/documentation/swift/string/init(decoding:as:)): Creates a string from the given Unicode code units in the specified encoding.

### Creating a String Using Formats

- [init(format:_:)](/documentation/swift/string/init(format:_:)): Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted.
- [init(format:arguments:)](/documentation/swift/string/init(format:arguments:)): Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to the user’s default locale.
- [init(format:locale:_:)](/documentation/swift/string/init(format:locale:_:)): Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information.
- [init(format:locale:arguments:)](/documentation/swift/string/init(format:locale:arguments:)): Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information.
- [localizedStringWithFormat(_:_:)](/documentation/swift/string/localizedstringwithformat(_:_:)): Returns a string created by using a given format string as a template into which the remaining argument values are substituted according to the user’s default locale.

### Creating a Localized String

- [init(localized:table:bundle:locale:comment:)](/documentation/swift/string/init(localized:table:bundle:locale:comment:)): Creates a localized string from an interpolated string.
- [init(localized:options:table:bundle:locale:comment:)](/documentation/swift/string/init(localized:options:table:bundle:locale:comment:)): Creates a localized string from an interpolated string, applying the specified options.
- [String.LocalizationValue](/documentation/swift/string/localizationvalue): A reference to a localizable string, with optional string interpolation.
- [String.LocalizationOptions](/documentation/swift/string/localizationoptions): Options to apply when initializing a localized string.
- [init(localized:defaultValue:table:bundle:locale:comment:)](/documentation/swift/string/init(localized:defaultvalue:table:bundle:locale:comment:)): Creates a localized string from an arbitrary static string key.
- [init(localized:defaultValue:options:table:bundle:locale:comment:)](/documentation/swift/string/init(localized:defaultvalue:options:table:bundle:locale:comment:)): Creates a localized string from an arbitrary static string key, applying the specified options.
- [init(localized:)](/documentation/swift/string/init(localized:)): Creates a localized string from a localized string resource.
- [init(localized:options:)](/documentation/swift/string/init(localized:options:)): Creates a localized string from a localized string resource, applying the specified options.

### Converting Numeric Values

- [init(_:radix:uppercase:)](/documentation/swift/string/init(_:radix:uppercase:)): Creates a string representing the given value in base 10, or some other specified base.

### Converting a C String

- [init(bytes:encoding:)](/documentation/swift/string/init(bytes:encoding:)): Creates a new string equivalent to the given bytes interpreted in the specified encoding. Note: This API does not interpret embedded nulls as termination of the string. Use `String?(validatingCString:)` instead for null-terminated C strings.
- [init(bytesNoCopy:length:encoding:freeWhenDone:)](/documentation/swift/string/init(bytesnocopy:length:encoding:freewhendone:)): Creates a new string that contains the specified number of bytes from the given buffer, interpreted in the specified encoding, and optionally frees the buffer.
- [init(validatingCString:)](/documentation/swift/string/init(validatingcstring:)-992vo): Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.
- [init(validatingCString:)](/documentation/swift/string/init(validatingcstring:)-98wra): Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given array.
- [init(cString:)](/documentation/swift/string/init(cstring:)-2p84k): Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init(cString:)](/documentation/swift/string/init(cstring:)-6kr8s): Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init(cString:encoding:)](/documentation/swift/string/init(cstring:encoding:)-3h7bc): Produces a string by copying the null-terminated bytes in a given array, interpreted according to a given encoding.
- [init(cString:encoding:)](/documentation/swift/string/init(cstring:encoding:)-3qgzd): Produces a string by copying the null-terminated bytes in a given C array, interpreted according to a given encoding.
- [init(decodingCString:as:)](/documentation/swift/string/init(decodingcstring:as:)-8way7): Creates a new string by copying the null-terminated sequence of code units referenced by the given array.
- [decodeCString(_:as:repairingInvalidCodeUnits:)](/documentation/swift/string/decodecstring(_:as:repairinginvalidcodeunits:)-46n2p): Creates a new string by copying the null-terminated data referenced by the given pointer using the specified encoding.

### Converting Other Types to Strings

- [init(_:)](/documentation/swift/string/init(_:)-1ywfq): Creates an instance from the description of a given `LosslessStringConvertible` instance.
- [init(describing:)](/documentation/swift/string/init(describing:)-588wb): Creates a string representing the given value.
- [init(describing:)](/documentation/swift/string/init(describing:)-hsqw): Creates a string representing the given value.
- [init(describing:)](/documentation/swift/string/init(describing:)-6ttci): Creates a string representing the given value.
- [init(describing:)](/documentation/swift/string/init(describing:)-67ncf): Creates a string representing the given value.
- [init(reflecting:)](/documentation/swift/string/init(reflecting:)): Creates a string with a detailed representation of the given value, suitable for debugging.

### Creating a String from a File or URL

- [init(contentsOf:)](/documentation/swift/string/init(contentsof:))
- [init(contentsOf:encoding:)](/documentation/swift/string/init(contentsof:encoding:)): Produces a string created by reading data from a given URL interpreted using a given encoding.
- [init(contentsOf:usedEncoding:)](/documentation/swift/string/init(contentsof:usedencoding:)): Produces a string created by reading data from a given URL and returns by reference the encoding used to interpret the data.
- [init(contentsOfFile:)](/documentation/swift/string/init(contentsoffile:))
- [init(contentsOfFile:encoding:)](/documentation/swift/string/init(contentsoffile:encoding:)): Produces a string created by reading data from the file at a given path interpreted using a given encoding.
- [init(contentsOfFile:usedEncoding:)](/documentation/swift/string/init(contentsoffile:usedencoding:)): Produces a string created by reading data from the file at a given path and returns by reference the encoding used to interpret the file.

### Writing to a File or URL

- [write(_:)](/documentation/swift/string/write(_:)): Appends the given string to this string.
- [write(to:)](/documentation/swift/string/write(to:)): Writes the string into the given output stream.

### Appending Strings and Characters

- [append(_:)](/documentation/swift/string/append(_:)-4xa8f): Appends the given string to this string.
- [append(_:)](/documentation/swift/string/append(_:)-4xi3j): Appends the given character to the string.
- [append(contentsOf:)](/documentation/swift/string/append(contentsof:)-oxek)
- [append(contentsOf:)](/documentation/swift/string/append(contentsof:)-9vb4t)
- [append(contentsOf:)](/documentation/swift/string/append(contentsof:)-7est5): Appends the characters in the given sequence to the string.
- [append(contentsOf:)](/documentation/swift/string/append(contentsof:)-9foms): Adds the elements of a sequence or collection to the end of this collection.
- [reserveCapacity(_:)](/documentation/swift/string/reservecapacity(_:)): Reserves enough space in the string’s underlying storage to store the specified number of ASCII characters.
- [+(_:_:)](/documentation/swift/string/+(_:_:))
- [+=(_:_:)](/documentation/swift/string/+=(_:_:))
- [+(_:_:)](/documentation/swift/string/+(_:_:)-6h59y): Creates a new collection by concatenating the elements of a sequence and a collection.
- [+(_:_:)](/documentation/swift/string/+(_:_:)-n329): Creates a new collection by concatenating the elements of a collection and a sequence.
- [+(_:_:)](/documentation/swift/string/+(_:_:)-9fm57): Creates a new collection by concatenating the elements of two collections.
- [+=(_:_:)](/documentation/swift/string/+=(_:_:)-676gx): Appends the elements of a sequence to a range-replaceable collection.

### Inserting Characters

- [insert(_:at:)](/documentation/swift/string/insert(_:at:)): Inserts a new character at the specified position.
- [insert(_:at:)](/documentation/swift/string/insert(_:at:)-88yqh): Inserts a new element into the collection at the specified position.
- [insert(contentsOf:at:)](/documentation/swift/string/insert(contentsof:at:)-rdu9): Inserts the elements of a sequence into the collection at the specified position.
- [insert(contentsOf:at:)](/documentation/swift/string/insert(contentsof:at:)): Inserts a collection of characters at the specified position.

### Replacing Substrings

- [replaceSubrange(_:with:)](/documentation/swift/string/replacesubrange(_:with:)): Replaces the text within the specified bounds with the given characters.
- [replaceSubrange(_:with:)](/documentation/swift/string/replacesubrange(_:with:)-72947): Replaces the specified subrange of elements with the given collection.

### Removing Substrings

- [remove(at:)](/documentation/swift/string/remove(at:)): Removes and returns the character at the specified position.
- [remove(at:)](/documentation/swift/string/remove(at:)-5g0wm): Removes and returns the element at the specified position.
- [removeAll(keepingCapacity:)](/documentation/swift/string/removeall(keepingcapacity:)): Replaces this string with the empty string.
- [removeAll(where:)](/documentation/swift/string/removeall(where:)): Removes all the elements that satisfy the given predicate.
- [removeFirst()](/documentation/swift/string/removefirst()): Removes and returns the first element of the collection.
- [removeFirst(_:)](/documentation/swift/string/removefirst(_:)): Removes the specified number of elements from the beginning of the collection.
- [removeLast()](/documentation/swift/string/removelast()): Removes and returns the last element of the collection.
- [removeLast(_:)](/documentation/swift/string/removelast(_:)): Removes the specified number of elements from the end of the collection.
- [removeSubrange(_:)](/documentation/swift/string/removesubrange(_:)): Removes the characters in the given range.
- [removeSubrange(_:)](/documentation/swift/string/removesubrange(_:)-8maxn): Removes the elements in the specified subrange from the collection.
- [removeSubrange(_:)](/documentation/swift/string/removesubrange(_:)-9twng): Removes the elements in the specified subrange from the collection.
- [filter(_:)](/documentation/swift/string/filter(_:)): Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.
- [drop(while:)](/documentation/swift/string/drop(while:)): Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [dropFirst(_:)](/documentation/swift/string/dropfirst(_:)): Returns a subsequence containing all but the given number of initial elements.
- [dropLast(_:)](/documentation/swift/string/droplast(_:)): Returns a subsequence containing all but the specified number of final elements.
- [popLast()](/documentation/swift/string/poplast()): Removes and returns the last element of the collection.

### Changing Case

- [lowercased()](/documentation/swift/string/lowercased()): Returns a lowercase version of the string.
- [uppercased()](/documentation/swift/string/uppercased()): Returns an uppercase version of the string.

### Comparing Strings Using Operators

- [==(_:_:)](/documentation/swift/string/==(_:_:)): Returns a Boolean value indicating whether two values are equal.
- [==(_:_:)](/documentation/swift/string/==(_:_:)-8kzxf)
- [!=(_:_:)](/documentation/swift/string/!=(_:_:)-1bb05): Returns a Boolean value indicating whether two values are not equal.
- [!=(_:_:)](/documentation/swift/string/!=(_:_:)-frzf)
- [~=(_:_:)](/documentation/swift/string/~=(_:_:))

### Comparing Characters

- [elementsEqual(_:)](/documentation/swift/string/elementsequal(_:)): Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [elementsEqual(_:by:)](/documentation/swift/string/elementsequal(_:by:)): Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [starts(with:)](/documentation/swift/string/starts(with:)): Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [starts(with:by:)](/documentation/swift/string/starts(with:by:)): Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [lexicographicallyPrecedes(_:)](/documentation/swift/string/lexicographicallyprecedes(_:)): Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [lexicographicallyPrecedes(_:by:)](/documentation/swift/string/lexicographicallyprecedes(_:by:)): Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.

### Creating and Applying Differences

- [applying(_:)](/documentation/swift/string/applying(_:)): Applies the given difference to this collection.
- [difference(from:)](/documentation/swift/string/difference(from:)): Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [difference(from:by:)](/documentation/swift/string/difference(from:by:)): Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.

### Finding Substrings

- [hasPrefix(_:)](/documentation/swift/string/hasprefix(_:))
- [hasSuffix(_:)](/documentation/swift/string/hassuffix(_:))

### Finding Characters

- [contains(_:)](/documentation/swift/string/contains(_:)): Returns a Boolean value indicating whether the sequence contains the given element.
- [allSatisfy(_:)](/documentation/swift/string/allsatisfy(_:)): Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [contains(where:)](/documentation/swift/string/contains(where:)): Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [first(where:)](/documentation/swift/string/first(where:)): Returns the first element of the sequence that satisfies the given predicate.
- [firstIndex(of:)](/documentation/swift/string/firstindex(of:)): Returns the first index where the specified value appears in the collection.
- [firstIndex(where:)](/documentation/swift/string/firstindex(where:)): Returns the first index in which an element of the collection satisfies the given predicate.
- [last(where:)](/documentation/swift/string/last(where:)): Returns the last element of the sequence that satisfies the given predicate.
- [lastIndex(of:)](/documentation/swift/string/lastindex(of:)): Returns the last index where the specified value appears in the collection.
- [lastIndex(where:)](/documentation/swift/string/lastindex(where:)): Returns the index of the last element in the collection that matches the given predicate.
- [max()](/documentation/swift/string/max()): Returns the maximum element in the sequence.
- [max(_:_:)](/documentation/swift/string/max(_:_:))
- [max(by:)](/documentation/swift/string/max(by:)): Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [min()](/documentation/swift/string/min()): Returns the minimum element in the sequence.
- [min(_:_:)](/documentation/swift/string/min(_:_:))
- [min(by:)](/documentation/swift/string/min(by:)): Returns the minimum element in the sequence, using the given predicate as the comparison between elements.

### Getting Substrings

- [subscript(_:)](/documentation/swift/string/subscript(_:)-2so14): Accesses a contiguous subrange of the collection’s elements.
- [subscript(_:)](/documentation/swift/string/subscript(_:)-4h7s3): Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(_:)](/documentation/swift/string/subscript(_:)-4al9c)
- [prefix(_:)](/documentation/swift/string/prefix(_:)): Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [prefix(through:)](/documentation/swift/string/prefix(through:)): Returns a subsequence from the start of the collection through the specified position.
- [prefix(upTo:)](/documentation/swift/string/prefix(upto:)): Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [prefix(while:)](/documentation/swift/string/prefix(while:)): Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [suffix(_:)](/documentation/swift/string/suffix(_:)): Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [suffix(from:)](/documentation/swift/string/suffix(from:)): Returns a subsequence from the specified position to the end of the collection.

### Splitting a String

- [split(separator:maxSplits:omittingEmptySubsequences:)](/documentation/swift/string/split(separator:maxsplits:omittingemptysubsequences:)): Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](/documentation/swift/string/split(maxsplits:omittingemptysubsequences:whereseparator:)): Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.

### Getting Characters and Bytes

- [subscript(_:)](/documentation/swift/string/subscript(_:)-lc0v): Accesses the character at the given position.
- [first](/documentation/swift/string/first): The first element of the collection.
- [last](/documentation/swift/string/last): The last element of the collection.
- [randomElement()](/documentation/swift/string/randomelement()): Returns a random element of the collection.
- [randomElement(using:)](/documentation/swift/string/randomelement(using:)): Returns a random element of the collection, using the given generator as a source for randomness.

### Working with Encodings

- [availableStringEncodings](/documentation/swift/string/availablestringencodings): An array of the encodings that strings support in the application’s environment.
- [defaultCStringEncoding](/documentation/swift/string/defaultcstringencoding): The C-string encoding assumed for any method accepting a C string as an argument.
- [localizedName(of:)](/documentation/swift/string/localizedname(of:)): Returns a human-readable string giving the name of the specified encoding.
- [isContiguousUTF8](/documentation/swift/string/iscontiguousutf8): Returns whether this string’s storage contains validly-encoded UTF-8 contents in contiguous memory.
- [makeContiguousUTF8()](/documentation/swift/string/makecontiguousutf8()): If this string is not contiguous, make it so. If this mutates the string, it will invalidate any pre-existing indices.
- [withUTF8(_:)](/documentation/swift/string/withutf8(_:)): Runs `body` over the content of this string in contiguous memory. If this string is not contiguous, this will first make it contiguous, which will also speed up subsequent access. If this mutates the string, it will invalidate any pre-existing indices.

### Working with String Views

- [unicodeScalars](/documentation/swift/string/unicodescalars): The string’s value represented as a collection of Unicode scalar values.
- [init(_:)](/documentation/swift/string/init(_:)-2t931): Creates a string corresponding to the given collection of Unicode scalars.
- [init(_:)](/documentation/swift/string/init(_:)-11jx3): Creates a String having the given content.
- [utf16](/documentation/swift/string/utf16): A UTF-16 encoding of `self`.
- [init(_:)](/documentation/swift/string/init(_:)-wbcx): Creates a string corresponding to the given sequence of UTF-16 code units.
- [init(_:)](/documentation/swift/string/init(_:)-expd): Creates a String having the given content.
- [utf8](/documentation/swift/string/utf8): A UTF-8 encoding of `self`.
- [init(_:)](/documentation/swift/string/init(_:)-6sprj): Creates a string corresponding to the given sequence of UTF-8 code units.
- [init(_:)](/documentation/swift/string/init(_:)-83bub): Creates a String having the given content.

### Transforming a String’s Characters

- [compactMap(_:)](/documentation/swift/string/compactmap(_:)): Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [flatMap(_:)](/documentation/swift/string/flatmap(_:)-i3m9): Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [flatMap(_:)](/documentation/swift/string/flatmap(_:)-6chuq)
- [reduce(_:_:)](/documentation/swift/string/reduce(_:_:)): Returns the result of combining the elements of the sequence using the given closure.
- [reduce(into:_:)](/documentation/swift/string/reduce(into:_:)): Returns the result of combining the elements of the sequence using the given closure.
- [lazy](/documentation/swift/string/lazy): A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.

### Iterating over a String’s Characters

- [forEach(_:)](/documentation/swift/string/foreach(_:)): Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [enumerated()](/documentation/swift/string/enumerated()): Returns a sequence of pairs (*n*, *x*), where *n* represents a consecutive integer starting at zero and *x* represents an element of the sequence.
- [makeIterator()](/documentation/swift/string/makeiterator()): Returns an iterator over the elements of the collection.
- [underestimatedCount](/documentation/swift/string/underestimatedcount): A value less than or equal to the number of elements in the collection.

### Reordering a String’s Characters

- [sorted()](/documentation/swift/string/sorted()): Returns the elements of the sequence, sorted.
- [sorted(by:)](/documentation/swift/string/sorted(by:)): Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [reversed()](/documentation/swift/string/reversed()): Returns a view presenting the elements of the collection in reverse order.
- [shuffled()](/documentation/swift/string/shuffled()): Returns the elements of the sequence, shuffled.
- [shuffled(using:)](/documentation/swift/string/shuffled(using:)): Returns the elements of the sequence, shuffled using the given generator as a source for randomness.

### Getting C Strings

- [utf8CString](/documentation/swift/string/utf8cstring): A contiguously stored null-terminated UTF-8 representation of the string.
- [withCString(_:)](/documentation/swift/string/withcstring(_:)): Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of UTF-8 code units.
- [withCString(encodedAs:_:)](/documentation/swift/string/withcstring(encodedas:_:)): Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of code units.

### Working with Paths

- [init(_:)](/documentation/swift/string/init(_:)-3a5mh)
- [init(validatingUTF8:)](/documentation/swift/string/init(validatingutf8:)-6i0in)

### Manipulating Indices

- [startIndex](/documentation/swift/string/startindex): The position of the first character in a nonempty string.
- [endIndex](/documentation/swift/string/endindex): A string’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [index(after:)](/documentation/swift/string/index(after:)): Returns the position immediately after the given index.
- [formIndex(after:)](/documentation/swift/string/formindex(after:)): Replaces the given index with its successor.
- [index(before:)](/documentation/swift/string/index(before:)): Returns the position immediately before the given index.
- [formIndex(before:)](/documentation/swift/string/formindex(before:)): Replaces the given index with its predecessor.
- [index(_:offsetBy:)](/documentation/swift/string/index(_:offsetby:)): Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:limitedBy:)](/documentation/swift/string/index(_:offsetby:limitedby:)): Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [formIndex(_:offsetBy:)](/documentation/swift/string/formindex(_:offsetby:)): Offsets the given index by the specified distance.
- [formIndex(_:offsetBy:limitedBy:)](/documentation/swift/string/formindex(_:offsetby:limitedby:)): Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [distance(from:to:)](/documentation/swift/string/distance(from:to:)): Returns the distance between two indices.
- [indices](/documentation/swift/string/indices-swift.property): The indices that are valid for subscripting the collection, in ascending order.

### Creating a Range Expression

- [...(_:_:)](/documentation/swift/string/'...(_:_:)): Returns a closed range that contains both of its bounds.
- [...(_:)](/documentation/swift/string/'...(_:)-4mm4o): Returns a partial range up to, and including, its upper bound.
- [...(_:)](/documentation/swift/string/'...(_:)-6ct5g): Returns a partial range extending upward from a lower bound.

### Encoding and Decoding

- [encode(to:)](/documentation/swift/string/encode(to:)): Encodes this value into the given encoder.
- [init(from:)](/documentation/swift/string/init(from:)): Creates a new instance by decoding from the given decoder.

### Describing a String

- [description](/documentation/swift/string/description): The value of this string.
- [debugDescription](/documentation/swift/string/debugdescription): A representation of the string that is suitable for debugging.
- [customMirror](/documentation/swift/string/custommirror): A mirror that reflects the `String` instance.
- [hashValue](/documentation/swift/string/hashvalue): The hash value.
- [hash(into:)](/documentation/swift/string/hash(into:)): Hashes the essential components of this value by feeding them into the given hasher.

### Infrequently Used Functionality

- [index(of:)](/documentation/swift/string/index(of:)): Returns the first index where the specified value appears in the collection.
- [init(_:)](/documentation/swift/string/init(_:)-5a5lw)
- [init(stringInterpolation:)](/documentation/swift/string/init(stringinterpolation:)): Creates a new instance from an interpolated string literal.
- [init(stringLiteral:)](/documentation/swift/string/init(stringliteral:)): Creates an instance initialized to the given string value.
- [init(unicodeScalarLiteral:)](/documentation/swift/string/init(unicodescalarliteral:))
- [init(extendedGraphemeClusterLiteral:)](/documentation/swift/string/init(extendedgraphemeclusterliteral:))
- [customPlaygroundQuickLook](/documentation/swift/string/customplaygroundquicklook): A custom playground Quick Look for the `String` instance.
- [withContiguousStorageIfAvailable(_:)](/documentation/swift/string/withcontiguousstorageifavailable(_:)): Executes a closure on the sequence’s contiguous storage.

### Reference Types

- [NSString](/documentation/Foundation/NSString): A static, plain-text Unicode string object.
- [NSMutableString](/documentation/Foundation/NSMutableString): A dynamic plain-text Unicode string object.

### Related String Types

- [Substring](/documentation/swift/substring): A slice of a string.
- [StringProtocol](/documentation/swift/stringprotocol): A type that can represent a string as a collection of characters.
- [String.Index](/documentation/swift/string/index): A position of a character or code unit in a string.
- [String.UnicodeScalarView](/documentation/swift/string/unicodescalarview): A view of a string’s contents as a collection of Unicode scalar values.
- [String.UTF16View](/documentation/swift/string/utf16view): A view of a string’s contents as a collection of UTF-16 code units.
- [String.UTF8View](/documentation/swift/string/utf8view): A view of a string’s contents as a collection of UTF-8 code units.
- [String.Iterator](/documentation/swift/string/iterator): A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [String.Encoding](/documentation/swift/string/encoding)

### Structures

- [String.Comparator](/documentation/swift/string/comparator): A `String` comparison performed using the given comparison options and locale.
- [String.IntentInputOptions](/documentation/swift/string/intentinputoptions)
- [String.StandardComparator](/documentation/swift/string/standardcomparator): Compares `String`s using one of a fixed set of standard comparison algorithms.

### Initializers

- [init(_:)](/documentation/swift/string/init(_:)-1oup7)
- [init(_:)](/documentation/swift/string/init(_:)-5ruqx)
- [init(cString:)](/documentation/swift/string/init(cstring:)-1gatt)
- [init(cString:)](/documentation/swift/string/init(cstring:)-295hy)
- [init(cString:)](/documentation/swift/string/init(cstring:)-472zs): Creates a new string by copying the null-terminated UTF-8 data referenced by the given array.
- [init(cString:)](/documentation/swift/string/init(cstring:)-54awj): Creates a new string by copying the null-terminated UTF-8 data referenced by the given array.
- [init(cString:)](/documentation/swift/string/init(cstring:)-cgw2)
- [init(cString:encoding:)](/documentation/swift/string/init(cstring:encoding:)-358mb)
- [init(cString:encoding:)](/documentation/swift/string/init(cstring:encoding:)-4ydt6)
- [init(copying:)](/documentation/swift/string/init(copying:)): Creates a new string, copying the specified code units.
- [init(decoding:)](/documentation/swift/string/init(decoding:)-364r2): On Unix, creates the string `"/"`
- [init(decoding:)](/documentation/swift/string/init(decoding:)-9xh58): Creates a string by interpreting the path component’s content as UTF-8 on Unix and UTF-16 on Windows.
- [init(decodingCString:as:)](/documentation/swift/string/init(decodingcstring:as:)-2zmjc)
- [init(decodingCString:as:)](/documentation/swift/string/init(decodingcstring:as:)-534rp)
- [init(describingForTest:)](/documentation/swift/string/init(describingfortest:)): Initialize this instance so that it can be presented in a test’s output.
- [init(platformString:)](/documentation/swift/string/init(platformstring:)-341sr)
- [init(platformString:)](/documentation/swift/string/init(platformstring:)-36ydz)
- [init(platformString:)](/documentation/swift/string/init(platformstring:)-5j2y3): Creates a string by interpreting the null-terminated platform string as UTF-8 on Unix and UTF-16 on Windows.
- [init(platformString:)](/documentation/swift/string/init(platformstring:)-7hjry): Creates a string by interpreting the null-terminated platform string as UTF-8 on Unix and UTF-16 on Windows.
- [init(utf8String:)](/documentation/swift/string/init(utf8string:)-5v4k8)
- [init(utf8String:)](/documentation/swift/string/init(utf8string:)-7t980)
- [init(validating:)](/documentation/swift/string/init(validating:)-6r2j9): On Unix, creates the string `"/"`
- [init(validating:)](/documentation/swift/string/init(validating:)-95n8b): Creates a string from a path component, validating its contents as UTF-8 on Unix and UTF-16 on Windows.
- [init(validating:)](/documentation/swift/string/init(validating:)-9dx2b): Creates a string from a file path, validating its contents as UTF-8 on Unix and UTF-16 on Windows.
- [init(validatingCString:)](/documentation/swift/string/init(validatingcstring:)-1x5p0)
- [init(validatingCString:)](/documentation/swift/string/init(validatingcstring:)-7gjlg)
- [init(validatingPlatformString:)](/documentation/swift/string/init(validatingplatformstring:)-2920w): Creates a string by interpreting the null-terminated platform string as UTF-8 on Unix and UTF-16 on Windows.
- [init(validatingPlatformString:)](/documentation/swift/string/init(validatingplatformstring:)-8x1kn)
- [init(validatingPlatformString:)](/documentation/swift/string/init(validatingplatformstring:)-91z6f): Creates a string by interpreting the null-terminated platform string as UTF-8 on Unix and UTF-16 on Windows.
- [init(validatingPlatformString:)](/documentation/swift/string/init(validatingplatformstring:)-go44)
- [init(validatingUTF8:)](/documentation/swift/string/init(validatingutf8:)-2m5lb): Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given array.
- [init(validatingUTF8:)](/documentation/swift/string/init(validatingutf8:)-2o7g5)
- [init(validatingUTF8:)](/documentation/swift/string/init(validatingutf8:)-8awk3)

### Instance Properties

- [characters](/documentation/swift/string/characters): A view of the string’s contents as a collection of characters.
- [utf8Span](/documentation/swift/string/utf8span): A UTF-8 span over the code units that make up this string.

### Instance Methods

- [data(using:allowLossyConversion:)](/documentation/swift/string/data(using:allowlossyconversion:))
- [withMutableCharacters(_:)](/documentation/swift/string/withmutablecharacters(_:)): Applies the given closure to a mutable view of the string’s characters.
- [withPlatformString(_:)](/documentation/swift/string/withplatformstring(_:)): Calls the given closure with a pointer to the contents of the string, represented as a null-terminated platform string.

### Type Aliases

- [String.CharacterView](/documentation/swift/string/characterview): A view of a string’s contents as a collection of characters.
- [String.CompareOptions](/documentation/swift/string/compareoptions)
- [String.EncodingConversionOptions](/documentation/swift/string/encodingconversionoptions)
- [String.EnumerationOptions](/documentation/swift/string/enumerationoptions)
- [String.IndexDistance](/documentation/swift/string/indexdistance): A type that represents the number of steps between two `String.Index` values, where one value is reachable from the other.
- [String.Output](/documentation/swift/string/output)
- [String.Specification](/documentation/swift/string/specification)
- [String.UnicodeScalarIndex](/documentation/swift/string/unicodescalarindex): The index type for a string’s `unicodeScalars` view.
- [String.UnwrappedType](/documentation/swift/string/unwrappedtype)
- [String.ValueType](/documentation/swift/string/valuetype)

### Type Properties

- [defaultResolverSpecification](/documentation/swift/string/defaultresolverspecification)

### Type Methods

- [decodeCString(_:as:repairingInvalidCodeUnits:)](/documentation/swift/string/decodecstring(_:as:repairinginvalidcodeunits:)-2l7u6)
- [decodeCString(_:as:repairingInvalidCodeUnits:)](/documentation/swift/string/decodecstring(_:as:repairinginvalidcodeunits:)-3mvvy)
- [decodeCString(_:as:repairingInvalidCodeUnits:)](/documentation/swift/string/decodecstring(_:as:repairinginvalidcodeunits:)-9pdmv)

### Default Implementations

- [Attachable Implementations](/documentation/swift/string/attachable-implementations)
- [BidirectionalCollection Implementations](/documentation/swift/string/bidirectionalcollection-implementations)
- [CodingKeyRepresentable Implementations](/documentation/swift/string/codingkeyrepresentable-implementations)
- [Collection Implementations](/documentation/swift/string/collection-implementations)
- [Comparable Implementations](/documentation/swift/string/comparable-implementations)
- [CustomDebugStringConvertible Implementations](/documentation/swift/string/customdebugstringconvertible-implementations)
- [CustomReflectable Implementations](/documentation/swift/string/customreflectable-implementations)
- [CustomStringConvertible Implementations](/documentation/swift/string/customstringconvertible-implementations)
- [Decodable Implementations](/documentation/swift/string/decodable-implementations)
- [Encodable Implementations](/documentation/swift/string/encodable-implementations)
- [Equatable Implementations](/documentation/swift/string/equatable-implementations)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](/documentation/swift/string/expressiblebyextendedgraphemeclusterliteral-implementations)
- [ExpressibleByStringInterpolation Implementations](/documentation/swift/string/expressiblebystringinterpolation-implementations)
- [ExpressibleByStringLiteral Implementations](/documentation/swift/string/expressiblebystringliteral-implementations)
- [ExpressibleByUnicodeScalarLiteral Implementations](/documentation/swift/string/expressiblebyunicodescalarliteral-implementations)
- [Hashable Implementations](/documentation/swift/string/hashable-implementations)
- [LosslessStringConvertible Implementations](/documentation/swift/string/losslessstringconvertible-implementations)
- [RangeReplaceableCollection Implementations](/documentation/swift/string/rangereplaceablecollection-implementations)
- [Sequence Implementations](/documentation/swift/string/sequence-implementations)
- [StringProtocol Implementations](/documentation/swift/string/stringprotocol-implementations)
- [TextOutputStream Implementations](/documentation/swift/string/textoutputstream-implementations)
- [TextOutputStreamable Implementations](/documentation/swift/string/textoutputstreamable-implementations)

## See Also

### Standard Library

- [Int](/documentation/swift/int): A signed integer value type.
- [Double](/documentation/swift/double): A double-precision (64-bit), floating-point value type.
- [Array](/documentation/swift/array): An ordered, random-access collection.
- [Dictionary](/documentation/swift/dictionary): A collection whose elements are key-value pairs.
- [Swift Standard Library](/documentation/swift/swift-standard-library): Solve complex problems and write high-performance, readable code.
