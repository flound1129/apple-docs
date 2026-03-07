# AnyLayout

A type-erased instance of the layout protocol.

```swift
@frozen struct AnyLayout
```

## Overview

Use an `AnyLayout` instance to enable dynamically changing the type of a layout container without destroying the state of the subviews. For example, you can create a layout that changes between horizontal and vertical layouts based on the current Dynamic Type setting:

```swift
struct DynamicLayoutExample: View {
    @Environment(\.dynamicTypeSize) var dynamicTypeSize

    var body: some View {
        let layout = dynamicTypeSize <= .medium ?
            AnyLayout(HStackLayout()) : AnyLayout(VStackLayout())

        layout {
            Text("First label")
            Text("Second label")
        }
    }
}
```

The types that you use with `AnyLayout` must conform to the [Layout](/documentation/swiftui/layout) protocol. The above example chooses between the [HStackLayout](/documentation/swiftui/hstacklayout) and [VStackLayout](/documentation/swiftui/vstacklayout) types, which are versions of the built-in [HStack](/documentation/swiftui/hstack) and [VStack](/documentation/swiftui/vstack) containers that conform to the protocol. You can also use custom layout types that you define.

### Creating the layout

- [init(_:)](/documentation/swiftui/anylayout/init(_:)): Creates a type-erased value that wraps the specified layout.

## See Also

### Transitioning between layout types

- [HStackLayout](/documentation/swiftui/hstacklayout): A horizontal container that you can use in conditional layouts.
- [VStackLayout](/documentation/swiftui/vstacklayout): A vertical container that you can use in conditional layouts.
- [ZStackLayout](/documentation/swiftui/zstacklayout): An overlaying container that you can use in conditional layouts.
- [GridLayout](/documentation/swiftui/gridlayout): A grid that you can use in conditional layouts.
