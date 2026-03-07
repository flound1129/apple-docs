# MenuStyle

A type that applies standard interaction behavior and a custom appearance to all menus within a view hierarchy.

```swift
@MainActor @preconcurrency protocol MenuStyle
```

## Overview

To configure the current menu style for a view hierarchy, use the [menuStyle(_:)](/documentation/swiftui/view/menustyle(_:)) modifier.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

### Getting built-in menu styles

- [automatic](/documentation/swiftui/menustyle/automatic): The default menu style, based on the menu’s context.
- [button](/documentation/swiftui/menustyle/button): A menu style that displays a button that toggles the display of the menu’s contents when pressed.
- [borderedButton](/documentation/swiftui/menustyle/borderedbutton): A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed.
- [borderlessButton](/documentation/swiftui/menustyle/borderlessbutton): A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed.

### Creating custom menu styles

- [makeBody(configuration:)](/documentation/swiftui/menustyle/makebody(configuration:)): Creates a view that represents the body of a menu.
- [MenuStyle.Configuration](/documentation/swiftui/menustyle/configuration): The properties of a menu.
- [Body](/documentation/swiftui/menustyle/body): A view that represents the body of a menu.

### Supporting types

- [DefaultMenuStyle](/documentation/swiftui/defaultmenustyle): The default menu style, based on the menu’s context.
- [ButtonMenuStyle](/documentation/swiftui/buttonmenustyle): A menu style that displays a button that toggles the display of the menu’s contents when pressed.
- [BorderlessButtonMenuStyle](/documentation/swiftui/borderlessbuttonmenustyle): A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed.
- [BorderedButtonMenuStyle](/documentation/swiftui/borderedbuttonmenustyle): A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed.

## See Also

### Styling menus

- [menuStyle(_:)](/documentation/swiftui/view/menustyle(_:)): Sets the style for menus within this view.
- [MenuStyleConfiguration](/documentation/swiftui/menustyleconfiguration): A configuration of a menu.
