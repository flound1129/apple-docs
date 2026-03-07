# WindowStyle

A specification for the appearance and interaction of a window.

```swift
protocol WindowStyle
```

### Getting built-in window styles

- [automatic](/documentation/swiftui/windowstyle/automatic): The default window style.
- [hiddenTitleBar](/documentation/swiftui/windowstyle/hiddentitlebar): A window style which hides both the window’s title and the backing of the titlebar area, allowing more of the window’s content to show.
- [plain](/documentation/swiftui/windowstyle/plain): The plain window style.
- [titleBar](/documentation/swiftui/windowstyle/titlebar): A window style which displays the title bar section of the window.
- [volumetric](/documentation/swiftui/windowstyle/volumetric): A window style that creates a 3D volumetric window.

### Supporting types

- [DefaultWindowStyle](/documentation/swiftui/defaultwindowstyle): The default window style.
- [HiddenTitleBarWindowStyle](/documentation/swiftui/hiddentitlebarwindowstyle): A window style which hides both the window’s title and the backing of the titlebar area, allowing more of the window’s content to show.
- [PlainWindowStyle](/documentation/swiftui/plainwindowstyle): The plain window style.
- [TitleBarWindowStyle](/documentation/swiftui/titlebarwindowstyle): A window style which displays the title bar section of the window.
- [VolumetricWindowStyle](/documentation/swiftui/volumetricwindowstyle): A window style that creates a 3D volumetric window.

## See Also

### Creating windows

- [WindowGroup](/documentation/swiftui/windowgroup): A scene that presents a group of identically structured windows.
- [Window](/documentation/swiftui/window): A scene that presents its content in a single, unique window.
- [UtilityWindow](/documentation/swiftui/utilitywindow): A specialized window scene that provides secondary utility to the content of the main scenes of an application.
- [windowStyle(_:)](/documentation/swiftui/scene/windowstyle(_:)): Sets the style for windows created by this scene.
