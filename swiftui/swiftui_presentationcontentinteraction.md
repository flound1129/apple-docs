# PresentationContentInteraction

A behavior that you can use to influence how a presentation responds to swipe gestures.

```swift
struct PresentationContentInteraction
```

## Overview

Use values of this type with the [presentationContentInteraction(_:)](/documentation/swiftui/view/presentationcontentinteraction(_:)) modifier.

### Getting interaction behaviors

- [automatic](/documentation/swiftui/presentationcontentinteraction/automatic): The default swipe behavior for the presentation.
- [resizes](/documentation/swiftui/presentationcontentinteraction/resizes): A behavior that prioritizes resizing a presentation when swiping, rather than scrolling the content of the presentation.
- [scrolls](/documentation/swiftui/presentationcontentinteraction/scrolls): A behavior that prioritizes scrolling the content of a presentation when swiping, rather than resizing the presentation.

## See Also

### Configuring a sheet’s height

- [presentationDetents(_:)](/documentation/swiftui/view/presentationdetents(_:)): Sets the available detents for the enclosing sheet.
- [presentationDetents(_:selection:)](/documentation/swiftui/view/presentationdetents(_:selection:)): Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [presentationContentInteraction(_:)](/documentation/swiftui/view/presentationcontentinteraction(_:)): Configures the behavior of swipe gestures on a presentation.
- [presentationDragIndicator(_:)](/documentation/swiftui/view/presentationdragindicator(_:)): Sets the visibility of the drag indicator on top of a sheet.
- [PresentationDetent](/documentation/swiftui/presentationdetent): A type that represents a height where a sheet naturally rests.
- [CustomPresentationDetent](/documentation/swiftui/custompresentationdetent): The definition of a custom detent with a calculated height.
