# SubviewsCollection

An opaque collection representing the subviews of view.

```swift
struct SubviewsCollection
```

## Overview

Subviews collection constructs subviews on demand, so only access the part of the collection you need to create the resulting content.

You can get access to a view’s subview collection by using the `Group/init(sectionsOf:transform:)` initializer.

The collection’s elements are the pieces that make up the given view, and the collection as a whole acts as a proxy for the original view.

## See Also

### Accessing a container’s subviews

- [Subview](/documentation/swiftui/subview): An opaque value representing a subview of another view.
- [SubviewsCollectionSlice](/documentation/swiftui/subviewscollectionslice): A slice of a SubviewsCollection.
- [containerValue(_:_:)](/documentation/swiftui/view/containervalue(_:_:)): Sets a particular container value of a view.
- [ContainerValues](/documentation/swiftui/containervalues): A collection of container values associated with a given view.
- [ContainerValueKey](/documentation/swiftui/containervaluekey): A key for accessing container values.
