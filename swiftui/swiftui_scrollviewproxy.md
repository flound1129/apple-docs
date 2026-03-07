# ScrollViewProxy

A proxy value that supports programmatic scrolling of the scrollable views within a view hierarchy.

```swift
struct ScrollViewProxy
```

## Overview

You don’t create instances of `ScrollViewProxy` directly. Instead, your [ScrollViewReader](/documentation/swiftui/scrollviewreader) receives an instance of `ScrollViewProxy` in its `content` view builder. You use actions within this view builder, such as button and gesture handlers or the [onChange(of:perform:)](/documentation/swiftui/view/onchange(of:perform:)) method, to call the proxy’s [scrollTo(_:anchor:)](/documentation/swiftui/scrollviewproxy/scrollto(_:anchor:)) method.

### Performing scrolling

- [scrollTo(_:anchor:)](/documentation/swiftui/scrollviewproxy/scrollto(_:anchor:)): Scans all scroll views contained by the proxy for the first with a child view with identifier `id`, and then scrolls to that view.

## See Also

### Creating a scroll view

- [ScrollView](/documentation/swiftui/scrollview): A scrollable view.
- [ScrollViewReader](/documentation/swiftui/scrollviewreader): A view that provides programmatic scrolling, by working with a proxy to scroll to known child views.
