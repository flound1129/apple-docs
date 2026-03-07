# InspectorCommands

A built-in set of commands for manipulating inspectors.

```swift
struct InspectorCommands
```

## Overview

`InspectorCommands` include a command for toggling the presented state of the inspector with a keyboard shortcut of Control-Command-I.

These commands are optional and can be explicitly requested by passing a value of this type to the [commands(content:)](/documentation/swiftui/scene/commands(content:)) modifier:

```swift
@State var presented = true
WindowGroup {
    MainView()
        .inspector(isPresented: $presented) {
            InspectorView()
        }
}
.commands {
    InspectorCommands()
}
```

### Creating a command

- [init()](/documentation/swiftui/inspectorcommands/init()): A new value describing the built-in inspector-related commands.

## See Also

### Getting built-in command groups

- [SidebarCommands](/documentation/swiftui/sidebarcommands): A built-in set of commands for manipulating window sidebars.
- [TextEditingCommands](/documentation/swiftui/texteditingcommands): A built-in group of commands for searching, editing, and transforming selections of text.
- [TextFormattingCommands](/documentation/swiftui/textformattingcommands): A built-in set of commands for transforming the styles applied to selections of text.
- [ToolbarCommands](/documentation/swiftui/toolbarcommands): A built-in set of commands for manipulating window toolbars.
- [ImportFromDevicesCommands](/documentation/swiftui/importfromdevicescommands): A built-in set of commands that enables importing content from nearby devices.
- [EmptyCommands](/documentation/swiftui/emptycommands): An empty group of commands.
