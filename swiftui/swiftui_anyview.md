# AnyView

A type-erased view.

```swift
@frozen struct AnyView
```

## Overview

An `AnyView` allows changing the type of view used in a given view hierarchy. Whenever the type of view used with an `AnyView` changes, the old hierarchy is destroyed and a new hierarchy is created for the new type.

### Creating a view

- [init(_:)](/documentation/swiftui/anyview/init(_:)): Create an instance that type-erases `view`.
- [init(erasing:)](/documentation/swiftui/anyview/init(erasing:))

## See Also

### Supporting view types

- [EmptyView](/documentation/swiftui/emptyview): A view that doesn’t contain any content.
- [EquatableView](/documentation/swiftui/equatableview): A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.
- [SubscriptionView](/documentation/swiftui/subscriptionview): A view that subscribes to a publisher with an action.
- [TupleView](/documentation/swiftui/tupleview): A View created from a swift tuple of View values.
