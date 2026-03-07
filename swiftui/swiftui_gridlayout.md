# GridLayout

A grid that you can use in conditional layouts.

```swift
@frozen struct GridLayout
```

## Overview

This layout container behaves like a [Grid](/documentation/swiftui/grid), but conforms to the [Layout](/documentation/swiftui/layout) protocol so you can use it in the conditional layouts that you construct with [AnyLayout](/documentation/swiftui/anylayout). If you don’t need a conditional layout, use [Grid](/documentation/swiftui/grid) instead.

### Creating a grid

- [init(alignment:horizontalSpacing:verticalSpacing:)](/documentation/swiftui/gridlayout/init(alignment:horizontalspacing:verticalspacing:)): Creates a grid with the specified spacing and alignment.

### Getting the grid’s properties

- [alignment](/documentation/swiftui/gridlayout/alignment): The alignment of subviews.
- [horizontalSpacing](/documentation/swiftui/gridlayout/horizontalspacing): The horizontal distance between adjacent subviews.
- [verticalSpacing](/documentation/swiftui/gridlayout/verticalspacing): The vertical distance between adjacent subviews.

### Type Aliases

- [GridLayout.Body](/documentation/swiftui/gridlayout/body)

### Default Implementations

- [Layout Implementations](/documentation/swiftui/gridlayout/layout-implementations)

## See Also

### Transitioning between layout types

- [AnyLayout](/documentation/swiftui/anylayout): A type-erased instance of the layout protocol.
- [HStackLayout](/documentation/swiftui/hstacklayout): A horizontal container that you can use in conditional layouts.
- [VStackLayout](/documentation/swiftui/vstacklayout): A vertical container that you can use in conditional layouts.
- [ZStackLayout](/documentation/swiftui/zstacklayout): An overlaying container that you can use in conditional layouts.
