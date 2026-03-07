# MenuBarExtraStyle

A specification for the appearance and behavior of a menu bar extra scene.

```swift
protocol MenuBarExtraStyle
```

### Getting menu bar extra styles

- [automatic](/documentation/swiftui/menubarextrastyle/automatic): The default menu bar extra style.
- [menu](/documentation/swiftui/menubarextrastyle/menu): A menu bar extra style that renders its contents as a menu that pulls down from the icon in the menu bar.
- [window](/documentation/swiftui/menubarextrastyle/window): A menu bar extra style that renders its contents in a popover-like window.

### Supporting types

- [AutomaticMenuBarExtraStyle](/documentation/swiftui/automaticmenubarextrastyle): The default menu bar extra style. You can also use [automatic](/documentation/swiftui/menubarextrastyle/automatic) to construct this style.
- [PullDownMenuBarExtraStyle](/documentation/swiftui/pulldownmenubarextrastyle): A menu bar extra style that renders its contents as a menu that pulls down from the icon in the menu bar.
- [WindowMenuBarExtraStyle](/documentation/swiftui/windowmenubarextrastyle): A menu bar extra style that renders its contents in a popover-like window.

## See Also

### Creating a menu bar extra

- [MenuBarExtra](/documentation/swiftui/menubarextra): A scene that renders itself as a persistent control in the system menu bar.
- [menuBarExtraStyle(_:)](/documentation/swiftui/scene/menubarextrastyle(_:)): Sets the style for menu bar extra created by this scene.
