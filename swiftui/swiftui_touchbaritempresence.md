# TouchBarItemPresence

Options that affect user customization of the Touch Bar.

```swift
enum TouchBarItemPresence
```

### Getting presence options

- [TouchBarItemPresence.default(_:)](/documentation/swiftui/touchbaritempresence/default(_:)): The Touch Bar view is visible by default, but can be removed during customization.
- [TouchBarItemPresence.optional(_:)](/documentation/swiftui/touchbaritempresence/optional(_:)): The Touch Bar view isn’t visible by default, but appears in the customization palette.
- [TouchBarItemPresence.required(_:)](/documentation/swiftui/touchbaritempresence/required(_:)): The Touch Bar view is visible by default and cannot be removed during customization.

## See Also

### Managing Touch Bar input

- [touchBar(content:)](/documentation/swiftui/view/touchbar(content:)): Sets the content that the Touch Bar displays.
- [touchBar(_:)](/documentation/swiftui/view/touchbar(_:)): Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [touchBarItemPrincipal(_:)](/documentation/swiftui/view/touchbaritemprincipal(_:)): Sets principal views that have special significance to this Touch Bar.
- [touchBarCustomizationLabel(_:)](/documentation/swiftui/view/touchbarcustomizationlabel(_:)): Sets a user-visible string that identifies the view’s functionality.
- [touchBarItemPresence(_:)](/documentation/swiftui/view/touchbaritempresence(_:)): Sets the behavior of the user-customized view.
- [TouchBar](/documentation/swiftui/touchbar): A container for a view that you can show in the Touch Bar.
