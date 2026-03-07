# RandomAccessCollection Implementations

### Instance Properties

- [endIndex](/documentation/swift/array/endindex): The array’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [indices](/documentation/swift/array/indices-swift.property): The indices that are valid for subscripting the collection, in ascending order.
- [startIndex](/documentation/swift/array/startindex): The position of the first element in a nonempty array.

### Instance Methods

- [distance(from:to:)](/documentation/swift/array/distance(from:to:)): Returns the distance between two indices.
- [formIndex(after:)](/documentation/swift/array/formindex(after:)): Replaces the given index with its successor.
- [formIndex(before:)](/documentation/swift/array/formindex(before:)): Replaces the given index with its predecessor.
- [index(_:offsetBy:)](/documentation/swift/array/index(_:offsetby:)): Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:limitedBy:)](/documentation/swift/array/index(_:offsetby:limitedby:)): Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [index(after:)](/documentation/swift/array/index(after:)): Returns the position immediately after the given index.
- [index(before:)](/documentation/swift/array/index(before:)): Returns the position immediately before the given index.

### Subscripts

- [subscript(_:)](/documentation/swift/array/subscript(_:)-25iat): Accesses the element at the specified position.
- [subscript(_:)](/documentation/swift/array/subscript(_:)-53fvb): Accesses a contiguous subrange of the array’s elements.

### Type Aliases

- [Array.Index](/documentation/swift/array/index): The index type for arrays, `Int`.
- [Array.Indices](/documentation/swift/array/indices): The type that represents the indices that are valid for subscripting an array, in ascending order.
