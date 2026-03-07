# HStack

A view that arranges its subviews in a horizontal line.

```swift
@frozen struct HStack<Content> where Content : View
```

## Overview

Unlike [LazyHStack](/documentation/swiftui/lazyhstack), which only renders the views when your app needs to display them onscreen, an `HStack` renders the views all at once, regardless of whether they are on- or offscreen. Use the regular `HStack` when you have a small number of subviews or don’t want the delayed rendering behavior of the “lazy” version.

The following example shows a simple horizontal stack of five text views:

```swift
var body: some View {
    HStack(
        alignment: .top,
        spacing: 10
    ) {
        ForEach(
            1...5,
            id: \.self
        ) {
            Text("Item \($0)")
        }
    }
}
```

![Five text views, named Item 1 through Item 5, arranged in a]

> **Note:**
> If you need a horizontal stack that conforms to the [Layout](/documentation/swiftui/layout) protocol, like when you want to create a conditional layout using [AnyLayout](/documentation/swiftui/anylayout), use [HStackLayout](/documentation/swiftui/hstacklayout) instead.
>

### Creating a stack

- [init(alignment:spacing:content:)](/documentation/swiftui/hstack/init(alignment:spacing:content:)): Creates a horizontal stack with the given spacing and vertical alignment.

## See Also

### Statically arranging views in one dimension

- [Building layouts with stack views](/documentation/swiftui/building-layouts-with-stack-views): Compose complex layouts from primitive container views.
- [VStack](/documentation/swiftui/vstack): A view that arranges its subviews in a vertical line.
