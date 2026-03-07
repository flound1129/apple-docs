# SubscriptionView

A view that subscribes to a publisher with an action.

```swift
@frozen struct SubscriptionView<PublisherType, Content> where PublisherType : Publisher, Content : View, PublisherType.Failure == Never
```

### Creating a subscription view

- [init(content:publisher:action:)](/documentation/swiftui/subscriptionview/init(content:publisher:action:))

### Managing the subscription

- [publisher](/documentation/swiftui/subscriptionview/publisher): The `Publisher` that is being subscribed.
- [action](/documentation/swiftui/subscriptionview/action): The `Action` executed when `publisher` emits an event.
- [content](/documentation/swiftui/subscriptionview/content): The content view.

## See Also

### Supporting view types

- [AnyView](/documentation/swiftui/anyview): A type-erased view.
- [EmptyView](/documentation/swiftui/emptyview): A view that doesn’t contain any content.
- [EquatableView](/documentation/swiftui/equatableview): A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.
- [TupleView](/documentation/swiftui/tupleview): A View created from a swift tuple of View values.
