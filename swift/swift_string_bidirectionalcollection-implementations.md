# BidirectionalCollection Implementations

### Structures

- [String.Index](/documentation/swift/string/index): A position of a character or code unit in a string.

### Instance Properties

- [endIndex](/documentation/swift/string/endindex): A string’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [last](/documentation/swift/string/last): The last element of the collection.
- [startIndex](/documentation/swift/string/startindex): The position of the first character in a nonempty string.

### Instance Methods

- [difference(from:)](/documentation/swift/string/difference(from:)): Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [difference(from:by:)](/documentation/swift/string/difference(from:by:)): Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [distance(from:to:)](/documentation/swift/string/distance(from:to:)): Returns the distance between two indices.
- [dropLast(_:)](/documentation/swift/string/droplast(_:)): Returns a subsequence containing all but the specified number of final elements.
- [formIndex(before:)](/documentation/swift/string/formindex(before:)): Replaces the given index with its predecessor.
- [index(_:offsetBy:)](/documentation/swift/string/index(_:offsetby:)): Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:limitedBy:)](/documentation/swift/string/index(_:offsetby:limitedby:)): Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [index(after:)](/documentation/swift/string/index(after:)): Returns the position immediately after the given index.
- [index(before:)](/documentation/swift/string/index(before:)): Returns the position immediately before the given index.
- [last(where:)](/documentation/swift/string/last(where:)): Returns the last element of the sequence that satisfies the given predicate.
- [lastIndex(of:)](/documentation/swift/string/lastindex(of:)): Returns the last index where the specified value appears in the collection.
- [lastIndex(where:)](/documentation/swift/string/lastindex(where:)): Returns the index of the last element in the collection that matches the given predicate.
- [reversed()](/documentation/swift/string/reversed()): Returns a view presenting the elements of the collection in reverse order.
- [suffix(_:)](/documentation/swift/string/suffix(_:)): Returns a subsequence, up to the given maximum length, containing the final elements of the collection.

### Subscripts

- [subscript(_:)](/documentation/swift/string/subscript(_:)-2so14): Accesses a contiguous subrange of the collection’s elements.
- [subscript(_:)](/documentation/swift/string/subscript(_:)-lc0v): Accesses the character at the given position.
