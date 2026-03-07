# ScrollIndicatorVisibility

The visibility of scroll indicators of a UI element.

```swift
struct ScrollIndicatorVisibility
```

## Overview

Pass a value of this type to the [scrollIndicators(_:axes:)](/documentation/swiftui/view/scrollindicators(_:axes:)) method to specify the preferred scroll indicator visibility of a view hierarchy.

### Getting visibilties

- [automatic](/documentation/swiftui/scrollindicatorvisibility/automatic): Scroll indicator visibility depends on the policies of the component accepting the visibility configuration.
- [hidden](/documentation/swiftui/scrollindicatorvisibility/hidden): Hide the scroll indicators.
- [never](/documentation/swiftui/scrollindicatorvisibility/never): Scroll indicators should never be visible.
- [visible](/documentation/swiftui/scrollindicatorvisibility/visible): Show the scroll indicators.

## See Also

### Showing scroll indicators

- [scrollIndicatorsFlash(onAppear:)](/documentation/swiftui/view/scrollindicatorsflash(onappear:)): Flashes the scroll indicators of a scrollable view when it appears.
- [scrollIndicatorsFlash(trigger:)](/documentation/swiftui/view/scrollindicatorsflash(trigger:)): Flashes the scroll indicators of scrollable views when a value changes.
- [scrollIndicators(_:axes:)](/documentation/swiftui/view/scrollindicators(_:axes:)): Sets the visibility of scroll indicators within this view.
- [horizontalScrollIndicatorVisibility](/documentation/swiftui/environmentvalues/horizontalscrollindicatorvisibility): The visibility to apply to scroll indicators of any horizontally scrollable content.
- [verticalScrollIndicatorVisibility](/documentation/swiftui/environmentvalues/verticalscrollindicatorvisibility): The visiblity to apply to scroll indicators of any vertically scrollable content.
