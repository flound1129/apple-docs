# LayoutSubviews

A collection of proxy values that represent the subviews of a layout view.

```swift
struct LayoutSubviews
```

## Overview

You receive a `LayoutSubviews` input to your implementations of [Layout](/documentation/swiftui/layout) protocol methods, like [placeSubviews(in:proposal:subviews:cache:)](/documentation/swiftui/layout/placesubviews(in:proposal:subviews:cache:)) and [sizeThatFits(proposal:subviews:cache:)](/documentation/swiftui/layout/sizethatfits(proposal:subviews:cache:)). The `subviews` parameter (which the protocol aliases to the [Layout.Subviews](/documentation/swiftui/layout/subviews) type) is a collection that contains proxies for the layout’s subviews (of type [LayoutSubview](/documentation/swiftui/layoutsubview)). The proxies appear in the collection in the same order that they appear in the [ViewBuilder](/documentation/swiftui/viewbuilder) input to the layout container. Use the proxies to perform layout operations.

Access the proxies in the collection as you would the contents of any Swift random-access collection. For example, you can enumerate all of the subviews and their indices to inspect or operate on them:

```swift
for (index, subview) in subviews.enumerated() {
    // ...
}
```

### Getting the layout direction

- [layoutDirection](/documentation/swiftui/layoutsubviews/layoutdirection): The layout direction inherited by the container view.

### Accessing subviews

- [subscript(_:)](/documentation/swiftui/layoutsubviews/subscript(_:)): Gets the subview proxies in the specified range.
- [startIndex](/documentation/swiftui/layoutsubviews/startindex): The index of the first subview.
- [endIndex](/documentation/swiftui/layoutsubviews/endindex): An index that’s one higher than the last subview.
- [LayoutSubviews.Element](/documentation/swiftui/layoutsubviews/element): A type that contains a proxy value.
- [LayoutSubviews.Index](/documentation/swiftui/layoutsubviews/index): A type that you can use to index proxy values.
- [LayoutSubviews.SubSequence](/documentation/swiftui/layoutsubviews/subsequence): A type that contains a subsequence of proxy values.

## See Also

### Creating a custom layout container

- [Composing custom layouts with SwiftUI](/documentation/swiftui/composing-custom-layouts-with-swiftui): Arrange views in your app’s interface using layout tools that SwiftUI provides.
- [Layout](/documentation/swiftui/layout): A type that defines the geometry of a collection of views.
- [LayoutSubview](/documentation/swiftui/layoutsubview): A proxy that represents one subview of a layout.
