# MenuButton

A button that displays a menu containing a list of choices when pressed.

```swift
struct MenuButton<Label, Content> where Label : View, Content : View
```

### Creating a menu button

- [init(_:content:)](/documentation/swiftui/menubutton/init(_:content:)): Creates a menu button with the specified localized title and content.
- [init(label:content:)](/documentation/swiftui/menubutton/init(label:content:)): Creates a menu button with the specified label and content.

### Styling a menu button

- [menuButtonStyle(_:)](/documentation/swiftui/view/menubuttonstyle(_:)): Sets the style for menu buttons within this view.
- [MenuButtonStyle](/documentation/swiftui/menubuttonstyle): A custom specification for the appearance and interaction of a menu button.

## See Also

### Deprecated types

- [PullDownButton](/documentation/swiftui/pulldownbutton)
- [ContextMenu](/documentation/swiftui/contextmenu): A container for views that you present as menu items in a context menu.
