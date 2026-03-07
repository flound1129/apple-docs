# EquatableView

A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.

```swift
@frozen struct EquatableView<Content> where Content : Equatable, Content : View
```

### Creating an equatable view

- [init(content:)](/documentation/swiftui/equatableview/init(content:))
- [content](/documentation/swiftui/equatableview/content)

## See Also

### Supporting view types

- [AnyView](/documentation/swiftui/anyview): A type-erased view.
- [EmptyView](/documentation/swiftui/emptyview): A view that doesn’t contain any content.
- [SubscriptionView](/documentation/swiftui/subscriptionview): A view that subscribes to a publisher with an action.
- [TupleView](/documentation/swiftui/tupleview): A View created from a swift tuple of View values.
