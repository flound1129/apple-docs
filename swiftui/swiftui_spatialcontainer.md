# SpatialContainer

A layout container that aligns overlapping content in 3D space.

```swift
@frozen struct SpatialContainer
```

## Overview

The container will take the max size of each dimension of each of its children, aligning its children based on the `alignment`.

### Initializers

- [init(alignment:)](/documentation/swiftui/spatialcontainer/init(alignment:)): Creates a spatial container layout with the specified 3D alignment.

## See Also

### Aligning views

- [Aligning views within a stack](/documentation/swiftui/aligning-views-within-a-stack): Position views inside a stack using alignment guides.
- [Aligning views across stacks](/documentation/swiftui/aligning-views-across-stacks): Create a custom alignment and use it to align views across multiple stacks.
- [alignmentGuide(_:computeValue:)](/documentation/swiftui/view/alignmentguide(_:computevalue:)): Sets the view’s horizontal alignment.
- [Alignment](/documentation/swiftui/alignment): An alignment in both axes.
- [HorizontalAlignment](/documentation/swiftui/horizontalalignment): An alignment position along the horizontal axis.
- [VerticalAlignment](/documentation/swiftui/verticalalignment): An alignment position along the vertical axis.
- [DepthAlignment](/documentation/swiftui/depthalignment): An alignment position along the depth axis.
- [AlignmentID](/documentation/swiftui/alignmentid): A type that you use to create custom alignment guides.
- [ViewDimensions](/documentation/swiftui/viewdimensions): A view’s size and alignment guides in its own coordinate space.
- [ViewDimensions3D](/documentation/swiftui/viewdimensions3d): A view’s 3D size and alignment guides in its own coordinate space.
