# Subview

An opaque value representing a subview of another view.

```swift
struct Subview
```

## Overview

Access to a `Subview` can be obtained by using `ForEach(subviews:)` or `Group(subviews:)`.

Subviews are proxies to the resolved view they represent, meaning that modifiers applied to the original view will be applied before modifiers applied to the subview, and the view is resolved using the environment of its container, *not* the environment of the its subview proxy. Additionally, because subviews must represent a single leaf view, or container, a subview may represent a view after the application of styles. As such, attempting to apply a style to it may have no affect.

### Structures

- [Subview.ID](/documentation/swiftui/subview/id-swift.struct): A unique identifier for a subview.

### Instance Properties

- [containerValues](/documentation/swiftui/subview/containervalues): The container values associated with the given subview.
- [id](/documentation/swiftui/subview/id-swift.property): The unique identifier of the view.

### Enumerations

- [Subview.ContainerSizingOptions](/documentation/swiftui/subview/containersizingoptions): Options on how all subviews should be sized when in a container.

## See Also

### Accessing a container’s subviews

- [SubviewsCollection](/documentation/swiftui/subviewscollection): An opaque collection representing the subviews of view.
- [SubviewsCollectionSlice](/documentation/swiftui/subviewscollectionslice): A slice of a SubviewsCollection.
- [containerValue(_:_:)](/documentation/swiftui/view/containervalue(_:_:)): Sets a particular container value of a view.
- [ContainerValues](/documentation/swiftui/containervalues): A collection of container values associated with a given view.
- [ContainerValueKey](/documentation/swiftui/containervaluekey): A key for accessing container values.
