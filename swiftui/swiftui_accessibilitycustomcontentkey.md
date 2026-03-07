# AccessibilityCustomContentKey

Key used to specify the identifier and label associated with an entry of additional accessibility information.

```swift
struct AccessibilityCustomContentKey
```

## Overview

Use `AccessibilityCustomContentKey` and the associated modifiers taking this value as a parameter in order to simplify clearing or replacing entries of additional information that are manipulated from multiple places in your code.

### Creating a key

- [init(_:)](/documentation/swiftui/accessibilitycustomcontentkey/init(_:)): Create an `AccessibilityCustomContentKey` with the specified label.
- [init(_:id:)](/documentation/swiftui/accessibilitycustomcontentkey/init(_:id:)): Create an `AccessibilityCustomContentKey` with the specified label and identifier.

## See Also

### Adding custom descriptions

- [accessibilityCustomContent(_:_:importance:)](/documentation/swiftui/view/accessibilitycustomcontent(_:_:importance:)): Add additional accessibility information to the view.
