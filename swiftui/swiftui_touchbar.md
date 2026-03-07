# TouchBar

A container for a view that you can show in the Touch Bar.

```swift
struct TouchBar<Content> where Content : View
```

### Creating a Touch Bar view

- [init(content:)](/documentation/swiftui/touchbar/init(content:)): Creates a non-customizable Touch Bar view container.
- [init(id:content:)](/documentation/swiftui/touchbar/init(id:content:)): Creates a customizable Touch Bar view container with a globally unique identifier.

## See Also

### Managing Touch Bar input

- [touchBar(content:)](/documentation/swiftui/view/touchbar(content:)): Sets the content that the Touch Bar displays.
- [touchBar(_:)](/documentation/swiftui/view/touchbar(_:)): Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [touchBarItemPrincipal(_:)](/documentation/swiftui/view/touchbaritemprincipal(_:)): Sets principal views that have special significance to this Touch Bar.
- [touchBarCustomizationLabel(_:)](/documentation/swiftui/view/touchbarcustomizationlabel(_:)): Sets a user-visible string that identifies the view’s functionality.
- [touchBarItemPresence(_:)](/documentation/swiftui/view/touchbaritempresence(_:)): Sets the behavior of the user-customized view.
- [TouchBarItemPresence](/documentation/swiftui/touchbaritempresence): Options that affect user customization of the Touch Bar.
