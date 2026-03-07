# SettingsLink

A view that opens the Settings scene defined by an app.

```swift
struct SettingsLink<Label> where Label : View
```

## Overview

On macOS, clicking on the link opens the window for the scene or orders it to the front if it is already open.

### Creating a settings link

- [init()](/documentation/swiftui/settingslink/init()): Creates a settings link with the default system label.
- [init(label:)](/documentation/swiftui/settingslink/init(label:)): Creates a settings link with a custom label.

### Supporting types

- [DefaultSettingsLinkLabel](/documentation/swiftui/defaultsettingslinklabel): The default label to use for a settings link.

## See Also

### Managing a settings window

- [Settings](/documentation/swiftui/settings): A scene that presents an interface for viewing and modifying an app’s settings.
- [OpenSettingsAction](/documentation/swiftui/opensettingsaction): An action that presents the settings scene for an app.
- [openSettings](/documentation/swiftui/environmentvalues/opensettings): A Settings presentation action stored in a view’s environment.
