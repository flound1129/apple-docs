# Collections

Store and organize data using arrays, dictionaries, sets, and other data structures.

### Arrays and Dictionaries

- [Array](/documentation/swift/array): An ordered, random-access collection.
- [Dictionary](/documentation/swift/dictionary): A collection whose elements are key-value pairs.
- [InlineArray](/documentation/swift/inlinearray): A fixed-size array.

### Sets

- [Set](/documentation/swift/set): An unordered collection of unique elements.
- [OptionSet](/documentation/swift/optionset): A type that presents a mathematical set interface to a bit set.

### Ranges

- [..<(_:_:)](/documentation/swift/comparable/'.._(_:_:)): Returns a half-open range that contains its lower bound but not its upper bound.
- [Range](/documentation/swift/range): A half-open interval from a lower bound up to, but not including, an upper bound.
- [RangeSet](/documentation/swift/rangeset): A set of values of any comparable type, represented by ranges.
- [...(_:_:)](/documentation/swift/comparable/'...(_:_:)): Returns a closed range that contains both of its bounds.
- [ClosedRange](/documentation/swift/closedrange): An interval from a lower bound up to, and including, an upper bound.

### Strides

- [stride(from:to:by:)](/documentation/swift/stride(from:to:by:)): Returns a sequence from a starting value to, but not including, an end value, stepping by the specified amount.
- [stride(from:through:by:)](/documentation/swift/stride(from:through:by:)): Returns a sequence from a starting value toward, and possibly including, an end value, stepping by the specified amount.

### Special-Use Collections

- [repeatElement(_:count:)](/documentation/swift/repeatelement(_:count:)): Creates a collection containing the specified number of the given element.
- [CollectionOfOne](/documentation/swift/collectionofone): A collection containing a single element.
- [EmptyCollection](/documentation/swift/emptycollection): A collection whose element type is `Element` but that is always empty.
- [KeyValuePairs](/documentation/swift/keyvaluepairs): A lightweight collection of key-value pairs.
- [DictionaryLiteral](/documentation/swift/dictionaryliteral)

### Dynamic Sequences

- [sequence(first:next:)](/documentation/swift/sequence(first:next:)): Returns a sequence formed from `first` and repeated lazy applications of `next`.
- [sequence(state:next:)](/documentation/swift/sequence(state:next:)): Returns a sequence formed from repeated lazy applications of `next` to a mutable `state`.

### Joint Iteration

- [zip(_:_:)](/documentation/swift/zip(_:_:)): Creates a sequence of pairs built out of two underlying sequences.

### Advanced Collection Topics

- [Sequence and Collection Protocols](/documentation/swift/sequence-and-collection-protocols): Write generic code that works with any collection, or build your own collection types.
- [Supporting Types](/documentation/swift/supporting-types): Use wrappers, indices, and iterators in operations like slicing, flattening, and reversing a collection.
- [Managed Buffers](/documentation/swift/managed-buffers): Build your own buffer-backed collection types.

## See Also

### Values and Collections

- [Numbers and Basic Values](/documentation/swift/numbers-and-basic-values): Model data with numbers, Boolean values, and other fundamental types.
- [Strings and Text](/documentation/swift/strings-and-text): Work with text using Unicode-safe strings.
- [Time](/documentation/swift/time-and-duration): Measure how long an operation takes and determine schedules in the future.
