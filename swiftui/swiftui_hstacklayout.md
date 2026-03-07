# HStackLayout

A horizontal container that you can use in conditional layouts.

```swift
@frozen struct HStackLayout
```

## Overview

This layout container behaves like an [HStack](/documentation/swiftui/hstack), but conforms to the [Layout](/documentation/swiftui/layout) protocol so you can use it in the conditional layouts that you construct with [AnyLayout](/documentation/swiftui/anylayout). If you don’t need a conditional layout, use [HStack](/documentation/swiftui/hstack) instead.

### Creating a horizontal stack

- [init(alignment:spacing:)](/documentation/swiftui/hstacklayout/init(alignment:spacing:)): Creates a horizontal stack with the specified spacing and vertical alignment.

### Getting the stack’s properties

- [alignment](/documentation/swiftui/hstacklayout/alignment): The vertical alignment of subviews.
- [spacing](/documentation/swiftui/hstacklayout/spacing): The distance between adjacent subviews.

## See Also

### Transitioning between layout types

- [AnyLayout](/documentation/swiftui/anylayout): A type-erased instance of the layout protocol.
- [VStackLayout](/documentation/swiftui/vstacklayout): A vertical container that you can use in conditional layouts.
- [ZStackLayout](/documentation/swiftui/zstacklayout): An overlaying container that you can use in conditional layouts.
- [GridLayout](/documentation/swiftui/gridlayout): A grid that you can use in conditional layouts.
