# Sequence Implementations

### Structures

- [Dictionary.Iterator](/documentation/swift/dictionary/iterator): An iterator over the members of a `Dictionary<Key, Value>`.

### Instance Properties

- [lazy](/documentation/swift/dictionary/lazy): A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.

### Instance Methods

- [allSatisfy(_:)](/documentation/swift/dictionary/allsatisfy(_:)): Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [compactMap(_:)](/documentation/swift/dictionary/compactmap(_:)): Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [contains(where:)](/documentation/swift/dictionary/contains(where:)): Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [count(where:)](/documentation/swift/dictionary/count(where:)): Returns the number of elements in the sequence that satisfy the given predicate.
- [elementsEqual(_:by:)](/documentation/swift/dictionary/elementsequal(_:by:)): Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [enumerated()](/documentation/swift/dictionary/enumerated()): Returns a sequence of pairs (*n*, *x*), where *n* represents a consecutive integer starting at zero and *x* represents an element of the sequence.
- [first(where:)](/documentation/swift/dictionary/first(where:)): Returns the first element of the sequence that satisfies the given predicate.
- [flatMap(_:)](/documentation/swift/dictionary/flatmap(_:)-6chv9)
- [flatMap(_:)](/documentation/swift/dictionary/flatmap(_:)-i3ly): Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [forEach(_:)](/documentation/swift/dictionary/foreach(_:)): Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [lexicographicallyPrecedes(_:by:)](/documentation/swift/dictionary/lexicographicallyprecedes(_:by:)): Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [makeIterator()](/documentation/swift/dictionary/makeiterator()): Returns an iterator over the dictionary’s key-value pairs.
- [map(_:)](/documentation/swift/dictionary/map(_:)-9jnoc): Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [max(by:)](/documentation/swift/dictionary/max(by:)): Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [min(by:)](/documentation/swift/dictionary/min(by:)): Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [reduce(_:_:)](/documentation/swift/dictionary/reduce(_:_:)): Returns the result of combining the elements of the sequence using the given closure.
- [reduce(into:_:)](/documentation/swift/dictionary/reduce(into:_:)): Returns the result of combining the elements of the sequence using the given closure.
- [reversed()](/documentation/swift/dictionary/reversed()): Returns an array containing the elements of this sequence in reverse order.
- [shuffled()](/documentation/swift/dictionary/shuffled()): Returns the elements of the sequence, shuffled.
- [shuffled(using:)](/documentation/swift/dictionary/shuffled(using:)): Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [sorted(by:)](/documentation/swift/dictionary/sorted(by:)): Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [starts(with:by:)](/documentation/swift/dictionary/starts(with:by:)): Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [withContiguousStorageIfAvailable(_:)](/documentation/swift/dictionary/withcontiguousstorageifavailable(_:)): Executes a closure on the sequence’s contiguous storage.
