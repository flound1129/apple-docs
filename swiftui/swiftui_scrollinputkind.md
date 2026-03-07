# ScrollInputKind

Inputs used to scroll views.

```swift
struct ScrollInputKind
```

### Type Properties

- [handGestureShortcut](/documentation/swiftui/scrollinputkind/handgestureshortcut): A finger or wrist movement that the user can perform in order to scroll a view.
- [look](/documentation/swiftui/scrollinputkind/look): On visionOS, by looking at the edge of a scroll view the content can automatically scroll. The axes will be determined automatically.

### Type Methods

- [look(axes:)](/documentation/swiftui/scrollinputkind/look(axes:)): On visionOS, by looking at the edge of a scroll view the content can automatically scroll. This contructor method takes a set of the scrollable axes.

## See Also

### Managing scrolling for different inputs

- [scrollInputBehavior(_:for:)](/documentation/swiftui/view/scrollinputbehavior(_:for:)): Enables or disables scrolling in scrollable views when using particular inputs.
- [ScrollInputBehavior](/documentation/swiftui/scrollinputbehavior): A type that defines whether input should scroll a view.
