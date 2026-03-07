# ScrollViewReader

A view that provides programmatic scrolling, by working with a proxy to scroll to known child views.

```swift
@frozen struct ScrollViewReader<Content> where Content : View
```

## Overview

The scroll view reader’s content view builder receives a [ScrollViewProxy](/documentation/swiftui/scrollviewproxy) instance; you use the proxy’s [scrollTo(_:anchor:)](/documentation/swiftui/scrollviewproxy/scrollto(_:anchor:)) to perform scrolling.

The following example creates a [ScrollView](/documentation/swiftui/scrollview) containing 100 views that together display a color gradient. It also contains two buttons, one each at the top and bottom. The top button tells the [ScrollViewProxy](/documentation/swiftui/scrollviewproxy) to scroll to the bottom button, and vice versa.

```swift
@Namespace var topID
@Namespace var bottomID

var body: some View {
    ScrollViewReader { proxy in
        ScrollView {
            Button("Scroll to Bottom") {
                withAnimation {
                    proxy.scrollTo(bottomID)
                }
            }
            .id(topID)

            VStack(spacing: 0) {
                ForEach(0..<100) { i in
                    color(fraction: Double(i) / 100)
                        .frame(height: 32)
                }
            }

            Button("Top") {
                withAnimation {
                    proxy.scrollTo(topID)
                }
            }
            .id(bottomID)
        }
    }
}

func color(fraction: Double) -> Color {
    Color(red: fraction, green: 1 - fraction, blue: 0.5)
}
```

![A scroll view, with a button labeled “Scroll to Bottom” at top.]

> **Important:**
> You may not use the [ScrollViewProxy](/documentation/swiftui/scrollviewproxy) during execution of the `content` view builder; doing so results in a runtime error. Instead, only actions created within `content` can call the proxy, such as gesture handlers or a view’s `onChange(of:perform:)` method.
>

### Creating a scroll view reader

- [init(content:)](/documentation/swiftui/scrollviewreader/init(content:)): Creates an instance that can perform programmatic scrolling of its child scroll views.

### Configuring a scroll view reader

- [content](/documentation/swiftui/scrollviewreader/content): The view builder that creates the reader’s content.

## See Also

### Creating a scroll view

- [ScrollView](/documentation/swiftui/scrollview): A scrollable view.
- [ScrollViewProxy](/documentation/swiftui/scrollviewproxy): A proxy value that supports programmatic scrolling of the scrollable views within a view hierarchy.
