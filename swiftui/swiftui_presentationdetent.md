# PresentationDetent

A type that represents a height where a sheet naturally rests.

```swift
struct PresentationDetent
```

### Getting built-in detents

- [large](/documentation/swiftui/presentationdetent/large): The system detent for a sheet at full height.
- [medium](/documentation/swiftui/presentationdetent/medium): The system detent for a sheet that’s approximately half the height of the screen, and is inactive in compact height.

### Creating custom detents

- [custom(_:)](/documentation/swiftui/presentationdetent/custom(_:)): A custom detent with a calculated height.
- [fraction(_:)](/documentation/swiftui/presentationdetent/fraction(_:)): A custom detent with the specified fractional height.
- [height(_:)](/documentation/swiftui/presentationdetent/height(_:)): A custom detent with the specified height.
- [PresentationDetent.Context](/documentation/swiftui/presentationdetent/context): Information that you use to calculate the presentation’s height.

## See Also

### Configuring a sheet’s height

- [presentationDetents(_:)](/documentation/swiftui/view/presentationdetents(_:)): Sets the available detents for the enclosing sheet.
- [presentationDetents(_:selection:)](/documentation/swiftui/view/presentationdetents(_:selection:)): Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [presentationContentInteraction(_:)](/documentation/swiftui/view/presentationcontentinteraction(_:)): Configures the behavior of swipe gestures on a presentation.
- [presentationDragIndicator(_:)](/documentation/swiftui/view/presentationdragindicator(_:)): Sets the visibility of the drag indicator on top of a sheet.
- [CustomPresentationDetent](/documentation/swiftui/custompresentationdetent): The definition of a custom detent with a calculated height.
- [PresentationContentInteraction](/documentation/swiftui/presentationcontentinteraction): A behavior that you can use to influence how a presentation responds to swipe gestures.
