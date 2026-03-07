# TextSelectability

A type that describes the ability to select text.

```swift
protocol TextSelectability
```

## Overview

To configure whether people can select text in your app, use the [textSelection(_:)](/documentation/swiftui/view/textselection(_:)) modifier, passing in a text selectability value like [enabled](/documentation/swiftui/textselectability/enabled) or [disabled](/documentation/swiftui/textselectability/disabled).

### Getting selectability options

- [enabled](/documentation/swiftui/textselectability/enabled): A selectability value that enables text selection by a person using your app.
- [disabled](/documentation/swiftui/textselectability/disabled): A selectability value that disables text selection by the person using your app.

### Specifying selectability

- [allowsSelection](/documentation/swiftui/textselectability/allowsselection): A Boolean value that indicates whether the selectability type allows selection.

### Supporting types

- [EnabledTextSelectability](/documentation/swiftui/enabledtextselectability): A selectability type that enables text selection by the person using your app.
- [DisabledTextSelectability](/documentation/swiftui/disabledtextselectability): A selectability type that disables text selection by the person using your app.

## See Also

### Selecting text

- [textSelection(_:)](/documentation/swiftui/view/textselection(_:)): Controls whether people can select text within this view.
- [TextSelection](/documentation/swiftui/textselection): Represents a selection of text.
- [textSelectionAffinity(_:)](/documentation/swiftui/view/textselectionaffinity(_:)): Sets the direction of a selection or cursor relative to a text character.
- [textSelectionAffinity](/documentation/swiftui/environmentvalues/textselectionaffinity): A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [TextSelectionAffinity](/documentation/swiftui/textselectionaffinity): A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [AttributedTextSelection](/documentation/swiftui/attributedtextselection): Represents a selection of attributed text.
