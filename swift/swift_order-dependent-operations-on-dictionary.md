# Order Dependent Operations on Dictionary

Perform order-dependent operations common to all collections, as implemented for `Dictionary`.

### Comparing Dictionaries

- [elementsEqual(_:by:)](/documentation/swift/dictionary/elementsequal(_:by:)): Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [starts(with:by:)](/documentation/swift/dictionary/starts(with:by:)): Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [lexicographicallyPrecedes(_:by:)](/documentation/swift/dictionary/lexicographicallyprecedes(_:by:)): Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.

### Manipulating Indices

- [startIndex](/documentation/swift/dictionary/startindex): The position of the first element in a nonempty dictionary.
- [endIndex](/documentation/swift/dictionary/endindex): The dictionary’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [index(after:)](/documentation/swift/dictionary/index(after:)): Returns the position immediately after the given index.
- [formIndex(after:)](/documentation/swift/dictionary/formindex(after:)): Replaces the given index with its successor.
- [index(_:offsetBy:)](/documentation/swift/dictionary/index(_:offsetby:)): Returns an index that is the specified distance from the given index.
- [formIndex(_:offsetBy:)](/documentation/swift/dictionary/formindex(_:offsetby:)): Offsets the given index by the specified distance.
- [index(_:offsetBy:limitedBy:)](/documentation/swift/dictionary/index(_:offsetby:limitedby:)): Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [formIndex(_:offsetBy:limitedBy:)](/documentation/swift/dictionary/formindex(_:offsetby:limitedby:)): Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [distance(from:to:)](/documentation/swift/dictionary/distance(from:to:)): Returns the distance between two indices.
- [indices](/documentation/swift/dictionary/indices-swift.property): The indices that are valid for subscripting the collection, in ascending order.

### Selecting Elements

- [subscript(_:)](/documentation/swift/dictionary/subscript(_:)-2ny9y): Accesses a contiguous subrange of the collection’s elements.
- [subscript(_:)](/documentation/swift/dictionary/subscript(_:)-4h7sk): Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(_:)](/documentation/swift/dictionary/subscript(_:)-4al9z)
- [prefix(_:)](/documentation/swift/dictionary/prefix(_:)): Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [prefix(through:)](/documentation/swift/dictionary/prefix(through:)): Returns a subsequence from the start of the collection through the specified position.
- [prefix(upTo:)](/documentation/swift/dictionary/prefix(upto:)): Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [prefix(while:)](/documentation/swift/dictionary/prefix(while:)): Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [suffix(_:)](/documentation/swift/dictionary/suffix(_:)): Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [suffix(from:)](/documentation/swift/dictionary/suffix(from:)): Returns a subsequence from the specified position to the end of the collection.

### Excluding Elements

- [dropFirst(_:)](/documentation/swift/dictionary/dropfirst(_:)): Returns a subsequence containing all but the given number of initial elements.
- [drop(while:)](/documentation/swift/dictionary/drop(while:)): Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [dropLast(_:)](/documentation/swift/dictionary/droplast(_:)): Returns a subsequence containing all but the specified number of final elements.
- [popFirst()](/documentation/swift/dictionary/popfirst()): Removes and returns the first key-value pair of the dictionary if the dictionary isn’t empty.

### Transforming a Dictionary’s Elements

- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](/documentation/swift/dictionary/split(maxsplits:omittingemptysubsequences:whereseparator:)): Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [reversed()](/documentation/swift/dictionary/reversed()): Returns an array containing the elements of this sequence in reverse order.
- [withContiguousStorageIfAvailable(_:)](/documentation/swift/dictionary/withcontiguousstorageifavailable(_:)): Executes a closure on the sequence’s contiguous storage.
