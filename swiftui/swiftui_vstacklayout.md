# VStackLayout

A vertical container that you can use in conditional layouts.

```swift
@frozen struct VStackLayout
```

## Overview

This layout container behaves like a [VStack](/documentation/swiftui/vstack), but conforms to the [Layout](/documentation/swiftui/layout) protocol so you can use it in the conditional layouts that you construct with [AnyLayout](/documentation/swiftui/anylayout). If you don’t need a conditional layout, use [VStack](/documentation/swiftui/vstack) instead.

### Creating a vertical stack

- [init(alignment:spacing:)](/documentation/swiftui/vstacklayout/init(alignment:spacing:)): Creates a vertical stack with the specified spacing and horizontal alignment.

### Getting the stack’s properties

- [alignment](/documentation/swiftui/vstacklayout/alignment): The horizontal alignment of subviews.
- [spacing](/documentation/swiftui/vstacklayout/spacing): The distance between adjacent subviews.

## See Also

### Transitioning between layout types

- [AnyLayout](/documentation/swiftui/anylayout): A type-erased instance of the layout protocol.
- [HStackLayout](/documentation/swiftui/hstacklayout): A horizontal container that you can use in conditional layouts.
- [ZStackLayout](/documentation/swiftui/zstacklayout): An overlaying container that you can use in conditional layouts.
- [GridLayout](/documentation/swiftui/gridlayout): A grid that you can use in conditional layouts.
