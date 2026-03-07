# VerticalAlignment

An alignment position along the vertical axis.

```swift
@frozen struct VerticalAlignment
```

## Overview

Use vertical alignment guides to position views relative to one another vertically, like when you place views side-by-side in an [HStack](/documentation/swiftui/hstack) or when you create a row of views in a [Grid](/documentation/swiftui/grid) using [GridRow](/documentation/swiftui/gridrow). The following example demonstrates common built-in vertical alignments:

![Five rows of content. Each row contains text inside]

You can generate the example above by creating a series of rows implemented as horizontal stacks, where you configure each stack with a different alignment guide:

```swift
private struct VerticalAlignmentGallery: View {
    var body: some View {
        VStack(spacing: 30) {
            row(alignment: .top, text: "Top")
            row(alignment: .center, text: "Center")
            row(alignment: .bottom, text: "Bottom")
            row(alignment: .firstTextBaseline, text: "First Text Baseline")
            row(alignment: .lastTextBaseline, text: "Last Text Baseline")
        }
    }

    private func row(alignment: VerticalAlignment, text: String) -> some View {
        HStack(alignment: alignment, spacing: 0) {
            Color.red.frame(height: 1)
            Text(text).font(.title).border(.gray)
            Color.red.frame(height: 1)
        }
    }
}
```

During layout, SwiftUI aligns the views inside each stack by bringing together the specified guides of the affected views. SwiftUI calculates the position of a guide for a particular view based on the characteristics of the view. For example, the [center](/documentation/swiftui/verticalalignment/center) guide appears at half the height of the view. You can override the guide calculation for a particular view using the [alignmentGuide(_:computeValue:)](/documentation/swiftui/view/alignmentguide(_:computevalue:)) view modifier.

### Text baseline alignment

Use the [firstTextBaseline](/documentation/swiftui/verticalalignment/firsttextbaseline) or [lastTextBaseline](/documentation/swiftui/verticalalignment/lasttextbaseline) guide to match the bottom of either the top- or bottom-most line of text that a view contains, respectively. Text baseline alignment excludes the parts of characters that descend below the baseline, like the tail on lower case g and j:

```swift
row(alignment: .firstTextBaseline, text: "fghijkl")
```

If you use a text baseline alignment on a view that contains no text, SwiftUI applies the equivalent of [bottom](/documentation/swiftui/verticalalignment/bottom) alignment instead. For the row in the example above, SwiftUI matches the bottom of the horizontal lines with the baseline of the text:

![A string containing the lowercase letters f, g, h, i, j, and]

Aligning a text view to its baseline rather than to the bottom of its frame produces the best layout effect in many cases, like when creating forms. For example, you can align the baseline of descriptive text in one [GridRow](/documentation/swiftui/gridrow) cell with the baseline of a text field, or the label of a checkbox, in another cell in the same row.

### Custom alignment guides

You can create a custom vertical alignment guide by first creating a type that conforms to the [AlignmentID](/documentation/swiftui/alignmentid) protocol, and then using that type to initialize a new static property on `VerticalAlignment`:

```swift
private struct FirstThirdAlignment: AlignmentID {
    static func defaultValue(in context: ViewDimensions) -> CGFloat {
        context.height / 3
    }
}

extension VerticalAlignment {
    static let firstThird = VerticalAlignment(FirstThirdAlignment.self)
}
```

You implement the [defaultValue(in:)](/documentation/swiftui/alignmentid/defaultvalue(in:)) method to calculate a default value for the custom alignment guide. The method receives a [ViewDimensions](/documentation/swiftui/viewdimensions) instance that you can use to calculate a value based on characteristics of the view. The example above places the guide at one-third of the height of the view as measured from the view’s origin.

You can then use the custom alignment guide like any built-in guide. For example, you can use it as the `alignment` parameter to an [HStack](/documentation/swiftui/hstack), or to alter the guide calculation for a specific view using the [alignmentGuide(_:computeValue:)](/documentation/swiftui/view/alignmentguide(_:computevalue:)) view modifier.

### Composite alignment

Combine a `VerticalAlignment` with a [HorizontalAlignment](/documentation/swiftui/horizontalalignment) to create a composite [Alignment](/documentation/swiftui/alignment) that indicates both vertical and horizontal positioning in one value. For example, you could combine your custom `firstThird` vertical alignment from the previous section with a built-in [center](/documentation/swiftui/horizontalalignment/center) horizontal alignment to use in a [ZStack](/documentation/swiftui/zstack):

```swift
struct LayeredHorizontalStripes: View {
    var body: some View {
        ZStack(alignment: Alignment(horizontal: .center, vertical: .firstThird)) {
            horizontalStripes(color: .blue)
                .frame(width: 180, height: 90)
            horizontalStripes(color: .green)
                .frame(width: 70, height: 60)
        }
    }

    private func horizontalStripes(color: Color) -> some View {
        VStack(spacing: 1) {
            ForEach(0..<3) { _ in color }
        }
    }
}
```

The example above uses widths and heights that generate two mismatched sets of three vertical stripes. The [ZStack](/documentation/swiftui/zstack) centers the two sets horizontally and aligns them vertically one-third from the top of each set. This aligns the bottom edges of the top stripe from each set:

![Two sets of three vertically stacked rectangles. The first]

### Getting guides

- [top](/documentation/swiftui/verticalalignment/top): A guide that marks the top edge of the view.
- [center](/documentation/swiftui/verticalalignment/center): A guide that marks the vertical center of the view.
- [bottom](/documentation/swiftui/verticalalignment/bottom): A guide that marks the bottom edge of the view.
- [firstTextBaseline](/documentation/swiftui/verticalalignment/firsttextbaseline): A guide that marks the top-most text baseline in a view.
- [lastTextBaseline](/documentation/swiftui/verticalalignment/lasttextbaseline): A guide that marks the bottom-most text baseline in a view.

### Creating a custom alignment

- [init(_:)](/documentation/swiftui/verticalalignment/init(_:)): Creates a custom vertical alignment of the specified type.
- [combineExplicit(_:)](/documentation/swiftui/verticalalignment/combineexplicit(_:)): Merges a sequence of explicit alignment values produced by this instance.

## See Also

### Aligning views

- [Aligning views within a stack](/documentation/swiftui/aligning-views-within-a-stack): Position views inside a stack using alignment guides.
- [Aligning views across stacks](/documentation/swiftui/aligning-views-across-stacks): Create a custom alignment and use it to align views across multiple stacks.
- [alignmentGuide(_:computeValue:)](/documentation/swiftui/view/alignmentguide(_:computevalue:)): Sets the view’s horizontal alignment.
- [Alignment](/documentation/swiftui/alignment): An alignment in both axes.
- [HorizontalAlignment](/documentation/swiftui/horizontalalignment): An alignment position along the horizontal axis.
- [DepthAlignment](/documentation/swiftui/depthalignment): An alignment position along the depth axis.
- [AlignmentID](/documentation/swiftui/alignmentid): A type that you use to create custom alignment guides.
- [ViewDimensions](/documentation/swiftui/viewdimensions): A view’s size and alignment guides in its own coordinate space.
- [ViewDimensions3D](/documentation/swiftui/viewdimensions3d): A view’s 3D size and alignment guides in its own coordinate space.
- [SpatialContainer](/documentation/swiftui/spatialcontainer): A layout container that aligns overlapping content in 3D space.
