# EmptyView

A view that doesn’t contain any content.

```swift
@frozen struct EmptyView
```

## Overview

You will rarely, if ever, need to create an `EmptyView` directly. Instead, `EmptyView` represents the absence of a view.

SwiftUI uses `EmptyView` in situations where a SwiftUI view type defines one or more child views with generic parameters, and allows the child views to be absent. When absent, the child view’s type in the generic type parameter is `EmptyView`.

The following example creates an indeterminate [ProgressView](/documentation/swiftui/progressview) without a label. The [ProgressView](/documentation/swiftui/progressview) type declares two generic parameters, `Label` and `CurrentValueLabel`, for the types used by its subviews. When both subviews are absent, like they are here, the resulting type is `ProgressView<EmptyView, EmptyView>`, as indicated by the example’s output:

```swift
let progressView = ProgressView()
print("\(type(of:progressView))")
// Prints: ProgressView<EmptyView, EmptyView>
```

### Creating an empty view

- [init()](/documentation/swiftui/emptyview/init()): Creates an empty view.

## See Also

### Supporting view types

- [AnyView](/documentation/swiftui/anyview): A type-erased view.
- [EquatableView](/documentation/swiftui/equatableview): A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.
- [SubscriptionView](/documentation/swiftui/subscriptionview): A view that subscribes to a publisher with an action.
- [TupleView](/documentation/swiftui/tupleview): A View created from a swift tuple of View values.
