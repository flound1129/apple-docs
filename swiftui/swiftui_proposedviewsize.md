# ProposedViewSize

A proposal for the size of a view.

```swift
@frozen struct ProposedViewSize
```

## Overview

During layout in SwiftUI, views choose their own size, but they do that in response to a size proposal from their parent view. When you create a custom layout using the [Layout](/documentation/swiftui/layout) protocol, your layout container participates in this process using `ProposedViewSize` instances. The layout protocol’s methods take a proposed size input that you can take into account when arranging views and calculating the size of the composite container. Similarly, your layout proposes a size to each of its own subviews when it measures and places them.

Layout containers typically measure their subviews by proposing several sizes and looking at the responses. The container can use this information to decide how to allocate space among its subviews. A layout might try the following special proposals:

- The [zero](/documentation/swiftui/proposedviewsize/zero) proposal; the view responds with its minimum size.
- The [infinity](/documentation/swiftui/proposedviewsize/infinity) proposal; the view responds with its maximum size.
- The [unspecified](/documentation/swiftui/proposedviewsize/unspecified) proposal; the view responds with its ideal size.

A layout might also try special cases for one dimension at a time. For example, an [HStack](/documentation/swiftui/hstack) might measure the flexibility of its subviews’ widths, while using a fixed value for the height.

### Getting standard proposals

- [zero](/documentation/swiftui/proposedviewsize/zero): A size proposal that contains zero in both dimensions.
- [infinity](/documentation/swiftui/proposedviewsize/infinity): A size proposal that contains infinity in both dimensions.
- [unspecified](/documentation/swiftui/proposedviewsize/unspecified): The proposed size with both dimensions left unspecified.

### Creating a custom size proposal

- [init(_:)](/documentation/swiftui/proposedviewsize/init(_:)): Creates a new proposed size from a specified size.
- [init(width:height:)](/documentation/swiftui/proposedviewsize/init(width:height:)): Creates a new proposed size using the specified width and height.

### Getting the proposal’s dimensions

- [height](/documentation/swiftui/proposedviewsize/height): The proposed vertical size measured in points.
- [width](/documentation/swiftui/proposedviewsize/width): The proposed horizontal size measured in points.

### Modifying a proposal

- [replacingUnspecifiedDimensions(by:)](/documentation/swiftui/proposedviewsize/replacingunspecifieddimensions(by:)): Creates a new proposal that replaces unspecified dimensions in this proposal with the corresponding dimension of the specified size.

## See Also

### Configuring a custom layout

- [LayoutProperties](/documentation/swiftui/layoutproperties): Layout-specific properties of a layout container.
- [ViewSpacing](/documentation/swiftui/viewspacing): A collection of the geometric spacing preferences of a view.
