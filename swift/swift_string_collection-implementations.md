# Collection Implementations

### Structures

- [String.Iterator](/documentation/swift/string/iterator): A type that provides the collection’s iteration interface and encapsulates its iteration state.

### Instance Properties

- [count](/documentation/swift/string/count): The number of characters in a string.
- [first](/documentation/swift/string/first): The first element of the collection.
- [indices](/documentation/swift/string/indices-swift.property): The indices that are valid for subscripting the collection, in ascending order.
- [isEmpty](/documentation/swift/string/isempty): A Boolean value indicating whether a string has no characters.
- [underestimatedCount](/documentation/swift/string/underestimatedcount): A value less than or equal to the number of elements in the collection.

### Instance Methods

- [drop(while:)](/documentation/swift/string/drop(while:)): Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [dropFirst(_:)](/documentation/swift/string/dropfirst(_:)): Returns a subsequence containing all but the given number of initial elements.
- [firstIndex(of:)](/documentation/swift/string/firstindex(of:)): Returns the first index where the specified value appears in the collection.
- [firstIndex(where:)](/documentation/swift/string/firstindex(where:)): Returns the first index in which an element of the collection satisfies the given predicate.
- [formIndex(_:offsetBy:)](/documentation/swift/string/formindex(_:offsetby:)): Offsets the given index by the specified distance.
- [formIndex(_:offsetBy:limitedBy:)](/documentation/swift/string/formindex(_:offsetby:limitedby:)): Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [formIndex(after:)](/documentation/swift/string/formindex(after:)): Replaces the given index with its successor.
- [index(of:)](/documentation/swift/string/index(of:)): Returns the first index where the specified value appears in the collection.
- [indices(of:)](/documentation/swift/string/indices(of:)): Returns the indices of all the elements that are equal to the given element.
- [indices(where:)](/documentation/swift/string/indices(where:)): Returns the indices of all the elements that match the given predicate.
- [makeIterator()](/documentation/swift/string/makeiterator()): Returns an iterator over the elements of the collection.
- [map(_:)](/documentation/swift/string/map(_:)-5p6pd): Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [prefix(_:)](/documentation/swift/string/prefix(_:)): Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [prefix(through:)](/documentation/swift/string/prefix(through:)): Returns a subsequence from the start of the collection through the specified position.
- [prefix(upTo:)](/documentation/swift/string/prefix(upto:)): Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [prefix(while:)](/documentation/swift/string/prefix(while:)): Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [randomElement()](/documentation/swift/string/randomelement()): Returns a random element of the collection.
- [randomElement(using:)](/documentation/swift/string/randomelement(using:)): Returns a random element of the collection, using the given generator as a source for randomness.
- [removingSubranges(_:)](/documentation/swift/string/removingsubranges(_:)): Returns a collection of the elements in this collection that are not represented by the given range set.
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](/documentation/swift/string/split(maxsplits:omittingemptysubsequences:whereseparator:)): Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [split(separator:maxSplits:omittingEmptySubsequences:)](/documentation/swift/string/split(separator:maxsplits:omittingemptysubsequences:)): Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [suffix(from:)](/documentation/swift/string/suffix(from:)): Returns a subsequence from the specified position to the end of the collection.

### Subscripts

- [subscript(_:)](/documentation/swift/string/subscript(_:)-392on): Accesses a view of this collection with the elements at the given indices.
- [subscript(_:)](/documentation/swift/string/subscript(_:)-4al9c)
- [subscript(_:)](/documentation/swift/string/subscript(_:)-4h7s3): Accesses the contiguous subrange of the collection’s elements specified by a range expression.

### Type Aliases

- [String.Indices](/documentation/swift/string/indices): A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [String.SubSequence](/documentation/swift/string/subsequence): A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
