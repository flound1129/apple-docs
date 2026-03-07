# OpenSettingsAction

An action that presents the settings scene for an app.

```swift
@MainActor @preconcurrency struct OpenSettingsAction
```

## Overview

Use the [openSettings](/documentation/swiftui/environmentvalues/opensettings) environment value to get the instance of this structure for a given [Environment](/documentation/swiftui/environment). Then call the instance to open a window. You call the instance directly because it defines a [callAsFunction()](/documentation/swiftui/opensettingsaction/callasfunction()) method that Swift calls when you call the instance.

For example, you can define a button that opens the settings window to a particular tab:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        #if os(macOS)
        Settings {
            SettingsView()
        }
        #endif
    }
}

struct SettingsView: View {
    @AppStorage("selectedSettingsTab")
    private var selectedSettingsTab = SettingsTab.general

    var body: some View {
        TabView(selection: $selectedSettingsTab) {
            GeneralSettings()
            AdvancedSettings()
        }
    }
}

struct AdvancedSettingsButton: View {
    @AppStorage("selectedSettingsTab")
    private var selectedSettingsTab = SettingsTab.general

    @Environment(\.openSettings) private var openSettings

    var body: some View {
        Button("Open Advanced Settings…") {
            selectedSettingsTab = .advanced
            openSettings()
        }
    }
}

enum SettingsTab: Int {
    case general
    case advanced
}
```

### Instance Methods

- [callAsFunction()](/documentation/swiftui/opensettingsaction/callasfunction()): Opens the window associated to the [Settings](/documentation/swiftui/settings) scene defined by this app, if one exists.

## See Also

### Managing a settings window

- [Settings](/documentation/swiftui/settings): A scene that presents an interface for viewing and modifying an app’s settings.
- [SettingsLink](/documentation/swiftui/settingslink): A view that opens the Settings scene defined by an app.
- [openSettings](/documentation/swiftui/environmentvalues/opensettings): A Settings presentation action stored in a view’s environment.
