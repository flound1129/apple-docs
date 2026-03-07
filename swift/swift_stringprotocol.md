# StringProtocol

A type that can represent a string as a collection of characters.

```swift
protocol StringProtocol : BidirectionalCollection, Comparable, ExpressibleByStringInterpolation, Hashable, LosslessStringConvertible, TextOutputStream, TextOutputStreamable where Self.Element == Character, Self.Index == String.Index, Self.StringInterpolation == DefaultStringInterpolation, Self.SubSequence : StringProtocol
```

## Overview

Do not declare new conformances to `StringProtocol`. Only the `String` and `Substring` types in the standard library are valid conforming types.

### Operators

- [!=(_:_:)](/documentation/swift/stringprotocol/!=(_:_:))

### Associated Types

- [SubSequence](/documentation/swift/stringprotocol/subsequence): A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
- [UTF16View](/documentation/swift/stringprotocol/utf16view)
- [UTF8View](/documentation/swift/stringprotocol/utf8view)
- [UnicodeScalarView](/documentation/swift/stringprotocol/unicodescalarview)

### Initializers

- [init(cString:)](/documentation/swift/stringprotocol/init(cstring:)): Creates a string from the null-terminated, UTF-8 encoded sequence of bytes at the given pointer.
- [init(decoding:as:)](/documentation/swift/stringprotocol/init(decoding:as:)): Creates a string from the given Unicode code units in the specified encoding.
- [init(decodingCString:as:)](/documentation/swift/stringprotocol/init(decodingcstring:as:)): Creates a string from the null-terminated sequence of bytes at the given pointer.

### Instance Properties

- [capitalized](/documentation/swift/stringprotocol/capitalized): A copy of the string with each word changed to its corresponding capitalized spelling.
- [decomposedStringWithCanonicalMapping](/documentation/swift/stringprotocol/decomposedstringwithcanonicalmapping): A string created by normalizing the string’s contents using Form D.
- [decomposedStringWithCompatibilityMapping](/documentation/swift/stringprotocol/decomposedstringwithcompatibilitymapping): A string created by normalizing the string’s contents using Form KD.
- [fastestEncoding](/documentation/swift/stringprotocol/fastestencoding): The fastest encoding to which the string can be converted without loss of information.
- [hash](/documentation/swift/stringprotocol/hash): An unsigned integer that can be used as a hash table address.
- [localizedCapitalized](/documentation/swift/stringprotocol/localizedcapitalized): A capitalized representation of the string that is produced using the current locale.
- [localizedLowercase](/documentation/swift/stringprotocol/localizedlowercase): A lowercase version of the string that is produced using the current locale.
- [localizedUppercase](/documentation/swift/stringprotocol/localizeduppercase): An uppercase version of the string that is produced using the current locale.
- [precomposedStringWithCanonicalMapping](/documentation/swift/stringprotocol/precomposedstringwithcanonicalmapping): A string created by normalizing the string’s contents using Form C.
- [precomposedStringWithCompatibilityMapping](/documentation/swift/stringprotocol/precomposedstringwithcompatibilitymapping): A string created by normalizing the string’s contents using Form KC.
- [removingPercentEncoding](/documentation/swift/stringprotocol/removingpercentencoding): A new string made from the string by replacing all percent encoded sequences with the matching UTF-8 characters.
- [smallestEncoding](/documentation/swift/stringprotocol/smallestencoding): The smallest encoding to which the string can be converted without loss of information.
- [unicodeScalars](/documentation/swift/stringprotocol/unicodescalars)
- [utf16](/documentation/swift/stringprotocol/utf16)
- [utf8](/documentation/swift/stringprotocol/utf8)

### Instance Methods

- [addingPercentEncoding(withAllowedCharacters:)](/documentation/swift/stringprotocol/addingpercentencoding(withallowedcharacters:)): Returns a new string created by replacing all characters in the string not in the specified set with percent encoded characters.
- [addingPercentEscapes(using:)](/documentation/swift/stringprotocol/addingpercentescapes(using:)): Returns a representation of the `String` using a given encoding to determine the percent escapes necessary to convert the `String` into a legal URL string.
- [appending(_:)](/documentation/swift/stringprotocol/appending(_:)): Returns a new string created by appending the given string.
- [appendingFormat(_:_:)](/documentation/swift/stringprotocol/appendingformat(_:_:)): Returns a string created by appending a string constructed from a given format string and the following arguments.
- [applyingTransform(_:reverse:)](/documentation/swift/stringprotocol/applyingtransform(_:reverse:)): Perform string transliteration.
- [cString(using:)](/documentation/swift/stringprotocol/cstring(using:)): Returns a representation of the string as a C string using a given encoding.
- [canBeConverted(to:)](/documentation/swift/stringprotocol/canbeconverted(to:)): Returns a Boolean value that indicates whether the string can be converted to the specified encoding without loss of information.
- [capitalized(with:)](/documentation/swift/stringprotocol/capitalized(with:)): Returns a capitalized representation of the string using the specified locale.
- [caseInsensitiveCompare(_:)](/documentation/swift/stringprotocol/caseinsensitivecompare(_:)): Returns the result of invoking `compare:options:` with `NSCaseInsensitiveSearch` as the only option.
- [commonPrefix(with:options:)](/documentation/swift/stringprotocol/commonprefix(with:options:)): Returns a string containing characters this string and the given string have in common, starting from the beginning of each up to the first characters that aren’t equivalent.
- [compare(_:options:range:locale:)](/documentation/swift/stringprotocol/compare(_:options:range:locale:)): Compares the string using the specified options and returns the lexical ordering for the range.
- [completePath(into:caseSensitive:matchesInto:filterTypes:)](/documentation/swift/stringprotocol/completepath(into:casesensitive:matchesinto:filtertypes:)): Interprets the string as a path in the file system and attempts to perform filename completion, returning a numeric value that indicates whether a match was possible, and by reference the longest path that matches the string.
- [components(separatedBy:)](/documentation/swift/stringprotocol/components(separatedby:)-4j26n): Returns an array containing substrings from the string that have been divided by characters in the given set.
- [components(separatedBy:)](/documentation/swift/stringprotocol/components(separatedby:)-8gl9t): Returns an array containing substrings from the string that have been divided by the given separator.
- [contains(_:)](/documentation/swift/stringprotocol/contains(_:)-40kbf): Returns `true` if `other` is non-empty and contained within `self` by case-sensitive, non-literal search. Otherwise, returns `false`.
- [contains(_:)](/documentation/swift/stringprotocol/contains(_:)-78f5t)
- [contains(_:)](/documentation/swift/stringprotocol/contains(_:)-78p35)
- [data(using:allowLossyConversion:)](/documentation/swift/stringprotocol/data(using:allowlossyconversion:)): Returns a `Data` containing a representation of the `String` encoded using a given encoding.
- [dataDetectorMatches(_:options:)](/documentation/swift/stringprotocol/datadetectormatches(_:options:)): Searches for known data types in a string or a substring.
- [enumerateLines(invoking:)](/documentation/swift/stringprotocol/enumeratelines(invoking:)): Enumerates all the lines in a string.
- [enumerateLinguisticTags(in:scheme:options:orthography:invoking:)](/documentation/swift/stringprotocol/enumeratelinguistictags(in:scheme:options:orthography:invoking:)): Performs linguistic analysis on the specified string by enumerating the specific range of the string, providing the Block with the located tags.
- [enumerateSubstrings(in:options:_:)](/documentation/swift/stringprotocol/enumeratesubstrings(in:options:_:)): Enumerates the substrings of the specified type in the specified range of the string.
- [folding(options:locale:)](/documentation/swift/stringprotocol/folding(options:locale:)): Returns a string with the given character folding options applied.
- [getBytes(_:maxLength:usedLength:encoding:options:range:remaining:)](/documentation/swift/stringprotocol/getbytes(_:maxlength:usedlength:encoding:options:range:remaining:)): Writes the given `range` of characters into `buffer` in a given `encoding`, without any allocations.  Does not NULL-terminate.
- [getCString(_:maxLength:encoding:)](/documentation/swift/stringprotocol/getcstring(_:maxlength:encoding:)): Converts the `String`’s content to a given encoding and stores them in a buffer.
- [getLineStart(_:end:contentsEnd:for:)](/documentation/swift/stringprotocol/getlinestart(_:end:contentsend:for:)): Returns by reference the beginning of the first line and the end of the last line touched by the given range.
- [getParagraphStart(_:end:contentsEnd:for:)](/documentation/swift/stringprotocol/getparagraphstart(_:end:contentsend:for:)): Returns by reference the beginning of the first paragraph and the end of the last paragraph touched by the given range.
- [hasPrefix(_:)](/documentation/swift/stringprotocol/hasprefix(_:))
- [hasSuffix(_:)](/documentation/swift/stringprotocol/hassuffix(_:))
- [lengthOfBytes(using:)](/documentation/swift/stringprotocol/lengthofbytes(using:)): Returns the number of bytes required to store the `String` in a given encoding.
- [lineRange(for:)](/documentation/swift/stringprotocol/linerange(for:)): Returns the range of characters representing the line or lines containing a given range.
- [linguisticTags(in:scheme:options:orthography:tokenRanges:)](/documentation/swift/stringprotocol/linguistictags(in:scheme:options:orthography:tokenranges:)): Returns an array of linguistic tags for the specified range and requested tags within the receiving string.
- [localizedCaseInsensitiveCompare(_:)](/documentation/swift/stringprotocol/localizedcaseinsensitivecompare(_:)): Compares the string and the given string using a case-insensitive, localized, comparison.
- [localizedCaseInsensitiveContains(_:)](/documentation/swift/stringprotocol/localizedcaseinsensitivecontains(_:)): Returns a Boolean value indicating whether the given string is non-empty and contained within this string by case-insensitive, non-literal search, taking into account the current locale.
- [localizedCompare(_:)](/documentation/swift/stringprotocol/localizedcompare(_:)): Compares the string and the given string using a localized comparison.
- [localizedStandardCompare(_:)](/documentation/swift/stringprotocol/localizedstandardcompare(_:)): Compares the string and the given string as sorted by the Finder.
- [localizedStandardContains(_:)](/documentation/swift/stringprotocol/localizedstandardcontains(_:)): Returns a Boolean value indicating whether the string contains the given string, taking the current locale into account.
- [localizedStandardRange(of:)](/documentation/swift/stringprotocol/localizedstandardrange(of:)): Finds and returns the range of the first occurrence of a given string, taking the current locale into account.  Returns `nil` if the string was not found.
- [lowercased()](/documentation/swift/stringprotocol/lowercased())
- [lowercased(with:)](/documentation/swift/stringprotocol/lowercased(with:)): Returns a version of the string with all letters converted to lowercase, taking into account the specified locale.
- [maximumLengthOfBytes(using:)](/documentation/swift/stringprotocol/maximumlengthofbytes(using:)): Returns the maximum number of bytes needed to store the `String` in a given encoding.
- [padding(toLength:withPad:startingAt:)](/documentation/swift/stringprotocol/padding(tolength:withpad:startingat:)): Returns a new string formed from the `String` by either removing characters from the end, or by appending as many occurrences as necessary of a given pad string.
- [paragraphRange(for:)](/documentation/swift/stringprotocol/paragraphrange(for:)): Returns the range of characters representing the paragraph or paragraphs containing a given range.
- [propertyList()](/documentation/swift/stringprotocol/propertylist()): Parses the `String` as a text representation of a property list, returning an NSString, NSData, NSArray, or NSDictionary object, according to the topmost element.
- [propertyListFromStringsFileFormat()](/documentation/swift/stringprotocol/propertylistfromstringsfileformat()): Returns a dictionary object initialized with the keys and values found in the `String`.
- [range(of:options:range:locale:)](/documentation/swift/stringprotocol/range(of:options:range:locale:)): Finds and returns the range of the first occurrence of a given string within a given range of the `String`, subject to given options, using the specified locale, if any.
- [rangeOfCharacter(from:options:range:)](/documentation/swift/stringprotocol/rangeofcharacter(from:options:range:)): Finds and returns the range in the `String` of the first character from a given character set found in a given range with given options.
- [rangeOfComposedCharacterSequence(at:)](/documentation/swift/stringprotocol/rangeofcomposedcharactersequence(at:)): Returns the range in the `String` of the composed character sequence located at a given index.
- [rangeOfComposedCharacterSequences(for:)](/documentation/swift/stringprotocol/rangeofcomposedcharactersequences(for:)): Returns the range in the string of the composed character sequences for a given range.
- [replacingCharacters(in:with:)](/documentation/swift/stringprotocol/replacingcharacters(in:with:)): Returns a new string in which the characters in a specified range of the `String` are replaced by a given string.
- [replacingOccurrences(of:with:options:range:)](/documentation/swift/stringprotocol/replacingoccurrences(of:with:options:range:)): Returns a new string in which all occurrences of a target string in a specified range of the string are replaced by another given string.
- [replacingPercentEscapes(using:)](/documentation/swift/stringprotocol/replacingpercentescapes(using:)): Returns a new string made by replacing in the `String` all percent escapes with the matching characters as determined by a given encoding.
- [split(separator:maxSplits:omittingEmptySubsequences:)](/documentation/swift/stringprotocol/split(separator:maxsplits:omittingemptysubsequences:)-7mfus)
- [split(separator:maxSplits:omittingEmptySubsequences:)](/documentation/swift/stringprotocol/split(separator:maxsplits:omittingemptysubsequences:)-8wzc1)
- [substring(from:)](/documentation/swift/stringprotocol/substring(from:)): Returns a new string containing the characters of the `String` from the one at a given index to the end.
- [substring(to:)](/documentation/swift/stringprotocol/substring(to:)): Returns a new string containing the characters of the `String` up to, but not including, the one at a given index.
- [substring(with:)](/documentation/swift/stringprotocol/substring(with:)): Returns a string object containing the characters of the `String` that lie within a given range.
- [trimmingCharacters(in:)](/documentation/swift/stringprotocol/trimmingcharacters(in:)): Returns a new string made by removing from both ends of the `String` characters contained in a given character set.
- [uppercased()](/documentation/swift/stringprotocol/uppercased())
- [uppercased(with:)](/documentation/swift/stringprotocol/uppercased(with:)): Returns a version of the string with all letters converted to uppercase, taking into account the specified locale.
- [withCString(_:)](/documentation/swift/stringprotocol/withcstring(_:)): Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of UTF-8 code units.
- [withCString(encodedAs:_:)](/documentation/swift/stringprotocol/withcstring(encodedas:_:)): Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of code units.
- [write(to:atomically:encoding:)](/documentation/swift/stringprotocol/write(to:atomically:encoding:)): Writes the contents of the `String` to the URL specified by url using the specified encoding.
- [write(toFile:atomically:encoding:)](/documentation/swift/stringprotocol/write(tofile:atomically:encoding:)): Writes the contents of the `String` to a file at a given path using a given encoding.

## See Also

### Related String Types

- [Substring](/documentation/swift/substring): A slice of a string.
- [String.Index](/documentation/swift/string/index): A position of a character or code unit in a string.
- [String.UnicodeScalarView](/documentation/swift/string/unicodescalarview): A view of a string’s contents as a collection of Unicode scalar values.
- [String.UTF16View](/documentation/swift/string/utf16view): A view of a string’s contents as a collection of UTF-16 code units.
- [String.UTF8View](/documentation/swift/string/utf8view): A view of a string’s contents as a collection of UTF-8 code units.
- [String.Iterator](/documentation/swift/string/iterator): A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [String.Encoding](/documentation/swift/string/encoding)
