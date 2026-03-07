# ZStackLayout

An overlaying container that you can use in conditional layouts.

```swift
@frozen struct ZStackLayout
```

## Overview

This layout container behaves like a [ZStack](/documentation/swiftui/zstack), but conforms to the [Layout](/documentation/swiftui/layout) protocol so you can use it in the conditional layouts that you construct with [AnyLayout](/documentation/swiftui/anylayout). If you don’t need a conditional layout, use [ZStack](/documentation/swiftui/zstack) instead.

### Creating a stack

- [init(alignment:)](/documentation/swiftui/zstacklayout/init(alignment:)): Creates a stack with the specified alignment.

### Getting the stack’s properties

- [alignment](/documentation/swiftui/zstacklayout/alignment): The alignment of subviews.

## See Also

### Transitioning between layout types

- [AnyLayout](/documentation/swiftui/anylayout): A type-erased instance of the layout protocol.
- [HStackLayout](/documentation/swiftui/hstacklayout): A horizontal container that you can use in conditional layouts.
- [VStackLayout](/documentation/swiftui/vstacklayout): A vertical container that you can use in conditional layouts.
- [GridLayout](/documentation/swiftui/gridlayout): A grid that you can use in conditional layouts.
