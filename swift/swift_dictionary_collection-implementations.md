# Collection Implementations

### Structures

- [Dictionary.Index](/documentation/swift/dictionary/index): The position of a key-value pair in a dictionary.

### Instance Properties

- [count](/documentation/swift/dictionary/count): The number of key-value pairs in the dictionary.
- [endIndex](/documentation/swift/dictionary/endindex): The dictionary’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [first](/documentation/swift/dictionary/first): The first element of the collection.
- [indices](/documentation/swift/dictionary/indices-swift.property): The indices that are valid for subscripting the collection, in ascending order.
- [isEmpty](/documentation/swift/dictionary/isempty): A Boolean value that indicates whether the dictionary is empty.
- [startIndex](/documentation/swift/dictionary/startindex): The position of the first element in a nonempty dictionary.
- [underestimatedCount](/documentation/swift/dictionary/underestimatedcount): A value less than or equal to the number of elements in the collection.

### Instance Methods

- [distance(from:to:)](/documentation/swift/dictionary/distance(from:to:)): Returns the distance between two indices.
- [drop(while:)](/documentation/swift/dictionary/drop(while:)): Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [dropFirst(_:)](/documentation/swift/dictionary/dropfirst(_:)): Returns a subsequence containing all but the given number of initial elements.
- [dropLast(_:)](/documentation/swift/dictionary/droplast(_:)): Returns a subsequence containing all but the specified number of final elements.
- [firstIndex(where:)](/documentation/swift/dictionary/firstindex(where:)): Returns the first index in which an element of the collection satisfies the given predicate.
- [formIndex(_:offsetBy:)](/documentation/swift/dictionary/formindex(_:offsetby:)): Offsets the given index by the specified distance.
- [formIndex(_:offsetBy:limitedBy:)](/documentation/swift/dictionary/formindex(_:offsetby:limitedby:)): Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [formIndex(after:)](/documentation/swift/dictionary/formindex(after:)): Replaces the given index with its successor.
- [index(_:offsetBy:)](/documentation/swift/dictionary/index(_:offsetby:)): Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:limitedBy:)](/documentation/swift/dictionary/index(_:offsetby:limitedby:)): Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [index(after:)](/documentation/swift/dictionary/index(after:)): Returns the position immediately after the given index.
- [indices(where:)](/documentation/swift/dictionary/indices(where:)): Returns the indices of all the elements that match the given predicate.
- [map(_:)](/documentation/swift/dictionary/map(_:)-5p6p2): Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [prefix(_:)](/documentation/swift/dictionary/prefix(_:)): Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [prefix(through:)](/documentation/swift/dictionary/prefix(through:)): Returns a subsequence from the start of the collection through the specified position.
- [prefix(upTo:)](/documentation/swift/dictionary/prefix(upto:)): Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [prefix(while:)](/documentation/swift/dictionary/prefix(while:)): Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [randomElement()](/documentation/swift/dictionary/randomelement()): Returns a random element of the collection.
- [randomElement(using:)](/documentation/swift/dictionary/randomelement(using:)): Returns a random element of the collection, using the given generator as a source for randomness.
- [removingSubranges(_:)](/documentation/swift/dictionary/removingsubranges(_:)): Returns a collection of the elements in this collection that are not represented by the given range set.
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](/documentation/swift/dictionary/split(maxsplits:omittingemptysubsequences:whereseparator:)): Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [suffix(_:)](/documentation/swift/dictionary/suffix(_:)): Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [suffix(from:)](/documentation/swift/dictionary/suffix(from:)): Returns a subsequence from the specified position to the end of the collection.

### Subscripts

- [subscript(_:)](/documentation/swift/dictionary/subscript(_:)-2ny9y): Accesses a contiguous subrange of the collection’s elements.
- [subscript(_:)](/documentation/swift/dictionary/subscript(_:)-392o0): Accesses a view of this collection with the elements at the given indices.
- [subscript(_:)](/documentation/swift/dictionary/subscript(_:)-4al9z)
- [subscript(_:)](/documentation/swift/dictionary/subscript(_:)-4bhoo): Accesses the key-value pair at the specified position.
- [subscript(_:)](/documentation/swift/dictionary/subscript(_:)-4h7sk): Accesses the contiguous subrange of the collection’s elements specified by a range expression.

### Type Aliases

- [Dictionary.Indices](/documentation/swift/dictionary/indices): A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Dictionary.SubSequence](/documentation/swift/dictionary/subsequence): A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
