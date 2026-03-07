# ContentMarginPlacement

The placement of margins.

```swift
struct ContentMarginPlacement
```

## Overview

Different views can support customizating margins that appear in different parts of that view. Use values of this type to customize those margins of a particular placement.

For example, use a [scrollIndicators](/documentation/swiftui/contentmarginplacement/scrollindicators) placement to customize the margins of scrollable view’s scroll indicators separately from the margins of a scrollable view’s content.

Use this type with the [contentMargins(_:for:)](/documentation/swiftui/view/contentmargins(_:for:)) modifier.

### Getting the placement

- [automatic](/documentation/swiftui/contentmarginplacement/automatic): The automatic placement.
- [scrollContent](/documentation/swiftui/contentmarginplacement/scrollcontent): The scroll content placement.
- [scrollIndicators](/documentation/swiftui/contentmarginplacement/scrollindicators): The scroll indicators placement.

## See Also

### Setting margins

- [contentMargins(_:for:)](/documentation/swiftui/view/contentmargins(_:for:)): Configures the content margin for a provided placement.
- [contentMargins(_:_:for:)](/documentation/swiftui/view/contentmargins(_:_:for:)): Configures the content margin for a provided placement.
