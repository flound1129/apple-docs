# Collection Implementations

### Instance Properties

- [count](/documentation/swift/array/count): The number of elements in the array.
- [first](/documentation/swift/array/first): The first element of the collection.
- [isEmpty](/documentation/swift/array/isempty): A Boolean value indicating whether the collection is empty.
- [underestimatedCount](/documentation/swift/array/underestimatedcount): A value less than or equal to the number of elements in the collection.

### Instance Methods

- [drop(while:)](/documentation/swift/array/drop(while:)): Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [dropFirst(_:)](/documentation/swift/array/dropfirst(_:)): Returns a subsequence containing all but the given number of initial elements.
- [firstIndex(of:)](/documentation/swift/array/firstindex(of:)): Returns the first index where the specified value appears in the collection.
- [firstIndex(where:)](/documentation/swift/array/firstindex(where:)): Returns the first index in which an element of the collection satisfies the given predicate.
- [formIndex(_:offsetBy:)](/documentation/swift/array/formindex(_:offsetby:)): Offsets the given index by the specified distance.
- [formIndex(_:offsetBy:limitedBy:)](/documentation/swift/array/formindex(_:offsetby:limitedby:)): Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [index(of:)](/documentation/swift/array/index(of:)): Returns the first index where the specified value appears in the collection.
- [indices(of:)](/documentation/swift/array/indices(of:)): Returns the indices of all the elements that are equal to the given element.
- [indices(where:)](/documentation/swift/array/indices(where:)): Returns the indices of all the elements that match the given predicate.
- [makeIterator()](/documentation/swift/array/makeiterator()): Returns an iterator over the elements of the collection.
- [map(_:)](/documentation/swift/array/map(_:)-5p6o3): Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [prefix(_:)](/documentation/swift/array/prefix(_:)): Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [prefix(through:)](/documentation/swift/array/prefix(through:)): Returns a subsequence from the start of the collection through the specified position.
- [prefix(upTo:)](/documentation/swift/array/prefix(upto:)): Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [prefix(while:)](/documentation/swift/array/prefix(while:)): Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [randomElement()](/documentation/swift/array/randomelement()): Returns a random element of the collection.
- [randomElement(using:)](/documentation/swift/array/randomelement(using:)): Returns a random element of the collection, using the given generator as a source for randomness.
- [removingSubranges(_:)](/documentation/swift/array/removingsubranges(_:)): Returns a collection of the elements in this collection that are not represented by the given range set.
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](/documentation/swift/array/split(maxsplits:omittingemptysubsequences:whereseparator:)): Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [split(separator:maxSplits:omittingEmptySubsequences:)](/documentation/swift/array/split(separator:maxsplits:omittingemptysubsequences:)-3dgmv): Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [suffix(from:)](/documentation/swift/array/suffix(from:)): Returns a subsequence from the specified position to the end of the collection.

### Subscripts

- [subscript(_:)](/documentation/swift/array/subscript(_:)-392p1): Accesses a view of this collection with the elements at the given indices.
- [subscript(_:)](/documentation/swift/array/subscript(_:)-4al8y)
- [subscript(_:)](/documentation/swift/array/subscript(_:)-4h7rl): Accesses the contiguous subrange of the collection’s elements specified by a range expression.

### Type Aliases

- [Array.Iterator](/documentation/swift/array/iterator): The type that allows iteration over an array’s elements.
- [Array.SubSequence](/documentation/swift/array/subsequence): A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
