# Sequence Implementations

### Instance Properties

- [lazy](/documentation/swift/string/lazy): A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.

### Instance Methods

- [allSatisfy(_:)](/documentation/swift/string/allsatisfy(_:)): Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [compactMap(_:)](/documentation/swift/string/compactmap(_:)): Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [contains(_:)](/documentation/swift/string/contains(_:)): Returns a Boolean value indicating whether the sequence contains the given element.
- [contains(where:)](/documentation/swift/string/contains(where:)): Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [count(where:)](/documentation/swift/string/count(where:)): Returns the number of elements in the sequence that satisfy the given predicate.
- [elementsEqual(_:)](/documentation/swift/string/elementsequal(_:)): Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [elementsEqual(_:by:)](/documentation/swift/string/elementsequal(_:by:)): Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [enumerated()](/documentation/swift/string/enumerated()): Returns a sequence of pairs (*n*, *x*), where *n* represents a consecutive integer starting at zero and *x* represents an element of the sequence.
- [first(where:)](/documentation/swift/string/first(where:)): Returns the first element of the sequence that satisfies the given predicate.
- [flatMap(_:)](/documentation/swift/string/flatmap(_:)-6chuq)
- [flatMap(_:)](/documentation/swift/string/flatmap(_:)-i3m9): Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [forEach(_:)](/documentation/swift/string/foreach(_:)): Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [lexicographicallyPrecedes(_:)](/documentation/swift/string/lexicographicallyprecedes(_:)): Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [lexicographicallyPrecedes(_:by:)](/documentation/swift/string/lexicographicallyprecedes(_:by:)): Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [map(_:)](/documentation/swift/string/map(_:)-9jnnv): Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [max()](/documentation/swift/string/max()): Returns the maximum element in the sequence.
- [max(by:)](/documentation/swift/string/max(by:)): Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [min()](/documentation/swift/string/min()): Returns the minimum element in the sequence.
- [min(by:)](/documentation/swift/string/min(by:)): Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [reduce(_:_:)](/documentation/swift/string/reduce(_:_:)): Returns the result of combining the elements of the sequence using the given closure.
- [reduce(into:_:)](/documentation/swift/string/reduce(into:_:)): Returns the result of combining the elements of the sequence using the given closure.
- [shuffled()](/documentation/swift/string/shuffled()): Returns the elements of the sequence, shuffled.
- [shuffled(using:)](/documentation/swift/string/shuffled(using:)): Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [sorted()](/documentation/swift/string/sorted()): Returns the elements of the sequence, sorted.
- [sorted(by:)](/documentation/swift/string/sorted(by:)): Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [starts(with:)](/documentation/swift/string/starts(with:)): Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [starts(with:by:)](/documentation/swift/string/starts(with:by:)): Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [withContiguousStorageIfAvailable(_:)](/documentation/swift/string/withcontiguousstorageifavailable(_:)): Executes a closure on the sequence’s contiguous storage.

### Type Aliases

- [String.Element](/documentation/swift/string/element): A type representing the sequence’s elements.
