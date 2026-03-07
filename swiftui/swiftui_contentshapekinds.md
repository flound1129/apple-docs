# ContentShapeKinds

A kind for the content shape of a view.

```swift
struct ContentShapeKinds
```

## Overview

The kind is used by the system to influence various effects, hit-testing, and more.

### Getting shape kinds

- [interaction](/documentation/swiftui/contentshapekinds/interaction): The kind for hit-testing and accessibility.
- [dragPreview](/documentation/swiftui/contentshapekinds/dragpreview): The kind for drag and drop previews.
- [contextMenuPreview](/documentation/swiftui/contentshapekinds/contextmenupreview): The kind for context menu previews.
- [focusEffect](/documentation/swiftui/contentshapekinds/focuseffect): The kind for the focus effect.
- [hoverEffect](/documentation/swiftui/contentshapekinds/hovereffect): The kind for hover effects.
- [accessibility](/documentation/swiftui/contentshapekinds/accessibility): The kind for accessibility visuals and sorting.

### Creating a set of options

- [init(rawValue:)](/documentation/swiftui/contentshapekinds/init(rawvalue:)): Creates a content shape kind.

## See Also

### Controlling hit testing

- [allowsTightening(_:)](/documentation/swiftui/view/allowstightening(_:)): Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [contentShape(_:eoFill:)](/documentation/swiftui/view/contentshape(_:eofill:)): Defines the content shape for hit testing.
- [contentShape(_:_:eoFill:)](/documentation/swiftui/view/contentshape(_:_:eofill:)): Sets the content shape for this view.
