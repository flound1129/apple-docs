# Sequence Implementations

### Instance Properties

- [lazy](/documentation/swift/array/lazy): A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.

### Instance Methods

- [allSatisfy(_:)](/documentation/swift/array/allsatisfy(_:)): Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [compactMap(_:)](/documentation/swift/array/compactmap(_:)): Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [contains(_:)](/documentation/swift/array/contains(_:)): Returns a Boolean value indicating whether the sequence contains the given element.
- [contains(where:)](/documentation/swift/array/contains(where:)): Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [count(where:)](/documentation/swift/array/count(where:)): Returns the number of elements in the sequence that satisfy the given predicate.
- [elementsEqual(_:)](/documentation/swift/array/elementsequal(_:)): Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [elementsEqual(_:by:)](/documentation/swift/array/elementsequal(_:by:)): Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [enumerated()](/documentation/swift/array/enumerated()): Returns a sequence of pairs (*n*, *x*), where *n* represents a consecutive integer starting at zero and *x* represents an element of the sequence.
- [filter(_:)](/documentation/swift/array/filter(_:)): Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [first(where:)](/documentation/swift/array/first(where:)): Returns the first element of the sequence that satisfies the given predicate.
- [flatMap(_:)](/documentation/swift/array/flatmap(_:)-6chu8)
- [flatMap(_:)](/documentation/swift/array/flatmap(_:)-i3mr): Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [forEach(_:)](/documentation/swift/array/foreach(_:)): Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [joined()](/documentation/swift/array/joined()): Returns the elements of this sequence of sequences, concatenated.
- [joined(separator:)](/documentation/swift/array/joined(separator:)-1ckod): Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [joined(separator:)](/documentation/swift/array/joined(separator:)-7uber): Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [lexicographicallyPrecedes(_:)](/documentation/swift/array/lexicographicallyprecedes(_:)): Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [lexicographicallyPrecedes(_:by:)](/documentation/swift/array/lexicographicallyprecedes(_:by:)): Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [map(_:)](/documentation/swift/array/map(_:)-9jnp5): Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [max()](/documentation/swift/array/max()): Returns the maximum element in the sequence.
- [max(by:)](/documentation/swift/array/max(by:)): Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [min()](/documentation/swift/array/min()): Returns the minimum element in the sequence.
- [min(by:)](/documentation/swift/array/min(by:)): Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [reduce(_:_:)](/documentation/swift/array/reduce(_:_:)): Returns the result of combining the elements of the sequence using the given closure.
- [reduce(into:_:)](/documentation/swift/array/reduce(into:_:)): Returns the result of combining the elements of the sequence using the given closure.
- [shuffled()](/documentation/swift/array/shuffled()): Returns the elements of the sequence, shuffled.
- [shuffled(using:)](/documentation/swift/array/shuffled(using:)): Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [sorted()](/documentation/swift/array/sorted()): Returns the elements of the sequence, sorted.
- [sorted(by:)](/documentation/swift/array/sorted(by:)): Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [split(separator:maxSplits:omittingEmptySubsequences:)](/documentation/swift/array/split(separator:maxsplits:omittingemptysubsequences:)-9bdwk): Returns the longest possible subsequences of the sequence, in order, around elements equal to the given element.
- [starts(with:)](/documentation/swift/array/starts(with:)): Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [starts(with:by:)](/documentation/swift/array/starts(with:by:)): Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [withContiguousStorageIfAvailable(_:)](/documentation/swift/array/withcontiguousstorageifavailable(_:)): Executes a closure on the sequence’s contiguous storage.
- [withContiguousStorageIfAvailable(_:)](/documentation/swift/array/withcontiguousstorageifavailable(_:)-1ynsc): Executes a closure on the sequence’s contiguous storage.
