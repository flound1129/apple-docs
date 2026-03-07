# RedactionReasons

The reasons to apply a redaction to data displayed on screen.

```swift
struct RedactionReasons
```

### Getting redaction reasons

- [invalidated](/documentation/swiftui/redactionreasons/invalidated): Displayed data should appear as invalidated and pending a new update.
- [placeholder](/documentation/swiftui/redactionreasons/placeholder): Displayed data should appear as generic placeholders.
- [privacy](/documentation/swiftui/redactionreasons/privacy): Displayed data should be obscured to protect private information.

### Creating redaction reasons

- [init(rawValue:)](/documentation/swiftui/redactionreasons/init(rawvalue:)): Creates a new set from a raw value.
- [rawValue](/documentation/swiftui/redactionreasons/rawvalue): The raw value.

## See Also

### Redacting private content

- [Designing your app for the Always On state](/documentation/watchOS-Apps/designing-your-app-for-the-always-on-state): Customize your watchOS app’s user interface for continuous display.
- [privacySensitive(_:)](/documentation/swiftui/view/privacysensitive(_:)): Marks the view as containing sensitive, private user data.
- [redacted(reason:)](/documentation/swiftui/view/redacted(reason:)): Adds a reason to apply a redaction to this view hierarchy.
- [unredacted()](/documentation/swiftui/view/unredacted()): Removes any reason to apply a redaction to this view hierarchy.
- [redactionReasons](/documentation/swiftui/environmentvalues/redactionreasons): The current redaction reasons applied to the view hierarchy.
- [isSceneCaptured](/documentation/swiftui/environmentvalues/isscenecaptured): The current capture state.
