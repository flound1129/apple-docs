# LayoutSubview

A proxy that represents one subview of a layout.

```swift
struct LayoutSubview
```

## Overview

This type acts as a proxy for a view that your custom layout container places in the user interface. [Layout](/documentation/swiftui/layout) protocol methods receive a [LayoutSubviews](/documentation/swiftui/layoutsubviews) collection that contains exactly one proxy for each of the subviews arranged by your container.

Use a proxy to get information about the associated subview, like its dimensions, layout priority, or custom layout values. You also use the proxy to tell its corresponding subview where to appear by calling the proxy’s [place(at:anchor:proposal:)](/documentation/swiftui/layoutsubview/place(at:anchor:proposal:)) method. Do this once for each subview from your implementation of the layout’s [placeSubviews(in:proposal:subviews:cache:)](/documentation/swiftui/layout/placesubviews(in:proposal:subviews:cache:)) method.

You can read custom layout values associated with a subview by using the property’s key as an index on the subview. For more information about defining, setting, and reading custom values, see [LayoutValueKey](/documentation/swiftui/layoutvaluekey).

### Placing the subview

- [place(at:anchor:proposal:)](/documentation/swiftui/layoutsubview/place(at:anchor:proposal:)): Assigns a position and proposed size to the subview.

### Getting subview characteristics

- [dimensions(in:)](/documentation/swiftui/layoutsubview/dimensions(in:)): Asks the subview for its dimensions and alignment guides.
- [sizeThatFits(_:)](/documentation/swiftui/layoutsubview/sizethatfits(_:)): Asks the subview for its size.
- [spacing](/documentation/swiftui/layoutsubview/spacing): The subviews’s preferred spacing values.
- [priority](/documentation/swiftui/layoutsubview/priority): The layout priority of the subview.

### Getting custom values

- [subscript(_:)](/documentation/swiftui/layoutsubview/subscript(_:)): Gets the value for the subview that’s associated with the specified key.

### Instance Properties

- [containerValues](/documentation/swiftui/layoutsubview/containervalues): The container values associated with the given subview.

## See Also

### Creating a custom layout container

- [Composing custom layouts with SwiftUI](/documentation/swiftui/composing-custom-layouts-with-swiftui): Arrange views in your app’s interface using layout tools that SwiftUI provides.
- [Layout](/documentation/swiftui/layout): A type that defines the geometry of a collection of views.
- [LayoutSubviews](/documentation/swiftui/layoutsubviews): A collection of proxy values that represent the subviews of a layout view.
