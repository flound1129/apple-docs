# Grouping data with lazy stack views

Split content into logical sections inside lazy stack views.

## Overview

[LazyHStack](/documentation/swiftui/lazyhstack) and [LazyVStack](/documentation/swiftui/lazyvstack) views are both able to display groups of views organized into logical sections, arranging their children in lines that grow horizontally and vertically, respectively. These stacks are “lazy” in that the stack views don’t create items until they need to be rendered onscreen. Like stack views, lazy stacks don’t include any inherent support for scrolling, and you should wrap lazy stack views in [ScrollView](/documentation/swiftui/scrollview) containers.

To group content or data inside a lazy stack view, use [Section](/documentation/swiftui/section) instances as containers for collections of grouped views. [Section](/documentation/swiftui/section) views don’t have any visual representation themselves but can contain header and footer views that can either scroll with the stack’s content or that you can pin to the top or bottom of the [ScrollView](/documentation/swiftui/scrollview).

> **Note:**
> Use [Section](/documentation/swiftui/section) views to get platform-appropriate grouping inside stack views or lazy stacks, lazy grids, [List](/documentation/swiftui/list), [CommandMenu](/documentation/swiftui/commandmenu), [Form](/documentation/swiftui/form), and several other container types.
>

The code samples in this article build a user interface for visualizing shades of primary colors. Each section in the stack represents a primary color, containing five subviews, each showing a different variation of the color.

![A screenshot showing a lazy stack view with multiple sections. Each section header contains the name of the color, followed by a set of views showing varying shades of that color.]

### Prepare your data

As with views contained within a stack, each [Section](/documentation/swiftui/section) must be uniquely identifiable when iterated by [ForEach](/documentation/swiftui/foreach). In this example, `ColorData` instances represent the sections, and `ShadeData` instances represent the shades of each color inside a section. Both `ColorData` and `ShadeData` conform to the [Identifiable](/documentation/Swift/Identifiable) protocol.

```swift
struct ColorData: Identifiable {
    let id = UUID()
    let name: String
    let color: Color
    let variations: [ShadeData]

    struct ShadeData: Identifiable {
        let id = UUID()
        var brightness: Double
    }

    init(color: Color, name: String) {
        self.name = name
        self.color = color
        self.variations = stride(from: 0.0, to: 0.5, by: 0.1)
            .map { ShadeData(brightness: $0) }
    }
}
```

### Display sections with headers and footers

The `ColorSelectionView` below sets up an array containing `ColorData` instances for each primary color. The [LazyVStack](/documentation/swiftui/lazyvstack) iterates over the array of color data to create sections, then iterates over the `variations` to create views from the shades.

```swift
struct ColorSelectionView: View {
    let sections = [
        ColorData(color: .red, name: "Reds"),
        ColorData(color: .green, name: "Greens"),
        ColorData(color: .blue, name: "Blues")
    ]

    var body: some View {
        ScrollView {
            LazyVStack(spacing: 1) {
                ForEach(sections) { section in
                    Section(header: SectionHeaderView(colorData: section)) {
                        ForEach(section.variations) { variation in
                            section.color
                                .brightness(variation.brightness)
                                .frame(height: 20)
                        }
                    }
                }
            }
        }
    }
}
```

Group data with [Section](/documentation/swiftui/section) views and pass in a header or footer view with the `header` and `footer` properties. This example implements a `SectionHeaderView` as a header view, containing a semi-transparent stack view and the name of the section’s color in a [Text](/documentation/swiftui/text) label.

```swift
struct SectionHeaderView: View {
    var colorData: ColorData

    var body: some View {
        HStack {
            Text(colorData.name)
                .font(.headline)
                .foregroundColor(colorData.color)
            Spacer()
        }
        .padding()
        .background(Color.primary
                        .colorInvert()
                        .opacity(0.75))
    }
}
```

For more information on using [ForEach](/documentation/swiftui/foreach) to repeat views inside a stack, see [Creating performant scrollable stacks](/documentation/swiftui/creating-performant-scrollable-stacks).

### Keep important information visible

By default, section header and footer views will scroll in sync with section content. If you want header and footer views to always remain visible, regardless of whether the top or bottom of the section is visible, then specify a set of [PinnedScrollableViews](/documentation/swiftui/pinnedscrollableviews) for the `pinnedViews` property of the lazy stack view.

```swift
LazyVStack(spacing: 1, pinnedViews: [.sectionHeaders]) {
    // ...
}
```

In [LazyVStack](/documentation/swiftui/lazyvstack) containers, headers attach to the top and footers to the bottom. In [LazyHStack](/documentation/swiftui/lazyhstack) containers, headers attach to the leading edge and footers to the trailing edge.

With this change, section headers are pinned to the top of the view as the user begins to scroll.

![A screenshot showing a lazy stack view with multiple sections, configured in the same way as in the first screenshot. In this screenshot, the user has scrolled down and the colored views show behind the section header, which is pinned to the top of the container view.]

## See Also

### Dynamically arranging views in one dimension

- [Creating performant scrollable stacks](/documentation/swiftui/creating-performant-scrollable-stacks): Display large numbers of repeated views efficiently with scroll views, stack views, and lazy stacks.
- [LazyHStack](/documentation/swiftui/lazyhstack): A view that arranges its children in a line that grows horizontally, creating items only as needed.
- [LazyVStack](/documentation/swiftui/lazyvstack): A view that arranges its children in a line that grows vertically, creating items only as needed.
- [PinnedScrollableViews](/documentation/swiftui/pinnedscrollableviews): A set of view types that may be pinned to the bounds of a scroll view.
