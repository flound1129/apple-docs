# VStack

A view that arranges its subviews in a vertical line.

```swift
@frozen struct VStack<Content> where Content : View
```

## Overview

Unlike [LazyVStack](/documentation/swiftui/lazyvstack), which only renders the views when your app needs to display them, a `VStack` renders the views all at once, regardless of whether they are on- or offscreen. Use the regular `VStack` when you have a small number of subviews or don’t want the delayed rendering behavior of the “lazy” version.

The following example shows a simple vertical stack of 10 text views:

```swift
var body: some View {
    VStack(
        alignment: .leading,
        spacing: 10
    ) {
        ForEach(
            1...10,
            id: \.self
        ) {
            Text("Item \($0)")
        }
    }
}
```

![Ten text views, named Item 1 through Item 10, arranged in a]

> **Note:**
> If you need a vertical stack that conforms to the [Layout](/documentation/swiftui/layout) protocol, like when you want to create a conditional layout using [AnyLayout](/documentation/swiftui/anylayout), use [VStackLayout](/documentation/swiftui/vstacklayout) instead.
>

### Creating a stack

- [init(alignment:spacing:content:)](/documentation/swiftui/vstack/init(alignment:spacing:content:)): Creates an instance with the given spacing and horizontal alignment.

## See Also

### Statically arranging views in one dimension

- [Building layouts with stack views](/documentation/swiftui/building-layouts-with-stack-views): Compose complex layouts from primitive container views.
- [HStack](/documentation/swiftui/hstack): A view that arranges its subviews in a horizontal line.
