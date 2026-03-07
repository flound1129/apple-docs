# ScrollDismissesKeyboardMode

The ways that scrollable content can interact with the software keyboard.

```swift
struct ScrollDismissesKeyboardMode
```

## Overview

Use this type in a call to the [scrollDismissesKeyboard(_:)](/documentation/swiftui/view/scrolldismisseskeyboard(_:)) modifier to specify the dismissal behavior of scrollable views.

### Getting modes

- [automatic](/documentation/swiftui/scrolldismisseskeyboardmode/automatic): Determine the mode automatically based on the surrounding context.
- [immediately](/documentation/swiftui/scrolldismisseskeyboardmode/immediately): Dismiss the keyboard as soon as scrolling starts.
- [interactively](/documentation/swiftui/scrolldismisseskeyboardmode/interactively): Enable people to interactively dismiss the keyboard as part of the scroll operation.
- [never](/documentation/swiftui/scrolldismisseskeyboardmode/never): Never dismiss the keyboard automatically as a result of scrolling.

## See Also

### Interacting with a software keyboard

- [scrollDismissesKeyboard(_:)](/documentation/swiftui/view/scrolldismisseskeyboard(_:)): Configures the behavior in which scrollable content interacts with the software keyboard.
- [scrollDismissesKeyboardMode](/documentation/swiftui/environmentvalues/scrolldismisseskeyboardmode): The way that scrollable content interacts with the software keyboard.
