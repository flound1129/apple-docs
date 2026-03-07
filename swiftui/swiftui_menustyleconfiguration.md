# MenuStyleConfiguration

A configuration of a menu.

```swift
struct MenuStyleConfiguration
```

## Overview

Use the [init(_:)](/documentation/swiftui/menu/init(_:)) initializer of [Menu](/documentation/swiftui/menu) to create an instance using the current menu style, which you can modify to create a custom style.

For example, the following code creates a new, custom style that adds a red border to the current menu style:

```swift
struct RedBorderMenuStyle: MenuStyle {
    func makeBody(configuration: Configuration) -> some View {
        Menu(configuration)
            .border(Color.red)
    }
}
```

### Setting the label and content

- [MenuStyleConfiguration.Label](/documentation/swiftui/menustyleconfiguration/label): A type-erased label of a menu.
- [MenuStyleConfiguration.Content](/documentation/swiftui/menustyleconfiguration/content): A type-erased content of a menu.

## See Also

### Styling menus

- [menuStyle(_:)](/documentation/swiftui/view/menustyle(_:)): Sets the style for menus within this view.
- [MenuStyle](/documentation/swiftui/menustyle): A type that applies standard interaction behavior and a custom appearance to all menus within a view hierarchy.
