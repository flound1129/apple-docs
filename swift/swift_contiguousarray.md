# ContiguousArray

A contiguously stored array.

```swift
@frozen struct ContiguousArray<Element>
```

## Overview

The `ContiguousArray` type is a specialized array that always stores its elements in a contiguous region of memory. This contrasts with `Array`, which can store its elements in either a contiguous region of memory or an `NSArray` instance if its `Element` type is a class or `@objc` protocol.

If your array’s `Element` type is a class or `@objc` protocol and you do not need to bridge the array to `NSArray` or pass the array to Objective-C APIs, using `ContiguousArray` may be more efficient and have more predictable performance than `Array`. If the array’s `Element` type is a struct or enumeration, `Array` and `ContiguousArray` should have similar efficiency.

For more information about using arrays, see `Array` and `ArraySlice`, with which `ContiguousArray` shares most properties and methods.

### Initializers

- [init(_:)](/documentation/swift/contiguousarray/init(_:)): Creates an array containing the elements of a sequence.
- [init(capacity:initializingWith:)](/documentation/swift/contiguousarray/init(capacity:initializingwith:)): Creates an array with the specified capacity, and then calls the given closure with an output span covering the array’s uninitialized memory.
- [init(unsafeUninitializedCapacity:initializingWith:)](/documentation/swift/contiguousarray/init(unsafeuninitializedcapacity:initializingwith:)): Creates an array with the specified capacity, and then calls the given closure with a buffer covering the array’s uninitialized memory.

### Instance Properties

- [capacity](/documentation/swift/contiguousarray/capacity): The total number of elements that the array can contain without allocating new storage.
- [mutableSpan](/documentation/swift/contiguousarray/mutablespan)
- [span](/documentation/swift/contiguousarray/span)

### Instance Methods

- [append(addingCapacity:initializingWith:)](/documentation/swift/contiguousarray/append(addingcapacity:initializingwith:)): Grows the array to have enough capacity for the specified number of elements, then calls the closure with an output span covering the array’s uninitialized memory.
- [insert(_:at:)](/documentation/swift/contiguousarray/insert(_:at:)): Inserts a new element at the specified position.
- [remove(at:)](/documentation/swift/contiguousarray/remove(at:)): Removes and returns the element at the specified position.
- [reserveCapacity(_:)](/documentation/swift/contiguousarray/reservecapacity(_:)): Reserves enough space to store the specified number of elements.
- [withUnsafeBufferPointer(_:)](/documentation/swift/contiguousarray/withunsafebufferpointer(_:)): Calls a closure with a pointer to the array’s contiguous storage.
- [withUnsafeBytes(_:)](/documentation/swift/contiguousarray/withunsafebytes(_:)): Calls the given closure with a pointer to the underlying bytes of the array’s contiguous storage.
- [withUnsafeMutableBufferPointer(_:)](/documentation/swift/contiguousarray/withunsafemutablebufferpointer(_:)): Calls the given closure with a pointer to the array’s mutable contiguous storage.
- [withUnsafeMutableBytes(_:)](/documentation/swift/contiguousarray/withunsafemutablebytes(_:)): Calls the given closure with a pointer to the underlying bytes of the array’s mutable contiguous storage.

### Default Implementations

- [Attachable Implementations](/documentation/swift/contiguousarray/attachable-implementations)
- [BidirectionalCollection Implementations](/documentation/swift/contiguousarray/bidirectionalcollection-implementations)
- [Collection Implementations](/documentation/swift/contiguousarray/collection-implementations)
- [CustomDebugStringConvertible Implementations](/documentation/swift/contiguousarray/customdebugstringconvertible-implementations)
- [CustomReflectable Implementations](/documentation/swift/contiguousarray/customreflectable-implementations)
- [CustomStringConvertible Implementations](/documentation/swift/contiguousarray/customstringconvertible-implementations)
- [Decodable Implementations](/documentation/swift/contiguousarray/decodable-implementations)
- [Encodable Implementations](/documentation/swift/contiguousarray/encodable-implementations)
- [Equatable Implementations](/documentation/swift/contiguousarray/equatable-implementations)
- [ExpressibleByArrayLiteral Implementations](/documentation/swift/contiguousarray/expressiblebyarrayliteral-implementations)
- [Hashable Implementations](/documentation/swift/contiguousarray/hashable-implementations)
- [MutableCollection Implementations](/documentation/swift/contiguousarray/mutablecollection-implementations)
- [OperationParameter Implementations](/documentation/swift/contiguousarray/operationparameter-implementations)
- [RandomAccessCollection Implementations](/documentation/swift/contiguousarray/randomaccesscollection-implementations)
- [RangeReplaceableCollection Implementations](/documentation/swift/contiguousarray/rangereplaceablecollection-implementations)
- [Sequence Implementations](/documentation/swift/contiguousarray/sequence-implementations)

## See Also

### Related Array Types

- [ArraySlice](/documentation/swift/arrayslice): A slice of an `Array`, `ContiguousArray`, or `ArraySlice` instance.
