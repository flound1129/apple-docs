# ImportFromDevicesCommands

A built-in set of commands that enables importing content from nearby devices.

```swift
struct ImportFromDevicesCommands
```

## Overview

This set of commands adds items based on nearby devices and capabilities, like taking photos or scanning documents. Views can receive imported content from these menu items by using the [importsItemProviders(_:onImport:)](/documentation/swiftui/view/importsitemproviders(_:onimport:)) modifier.

These commands are optional and you can explicitly request them by passing a value of this type to the [commands(content:)](/documentation/swiftui/scene/commands(content:)) modifier.

### Creating the command group

- [init()](/documentation/swiftui/importfromdevicescommands/init()): Creates a new set of device import commands.

## See Also

### Getting built-in command groups

- [SidebarCommands](/documentation/swiftui/sidebarcommands): A built-in set of commands for manipulating window sidebars.
- [TextEditingCommands](/documentation/swiftui/texteditingcommands): A built-in group of commands for searching, editing, and transforming selections of text.
- [TextFormattingCommands](/documentation/swiftui/textformattingcommands): A built-in set of commands for transforming the styles applied to selections of text.
- [ToolbarCommands](/documentation/swiftui/toolbarcommands): A built-in set of commands for manipulating window toolbars.
- [InspectorCommands](/documentation/swiftui/inspectorcommands): A built-in set of commands for manipulating inspectors.
- [EmptyCommands](/documentation/swiftui/emptycommands): An empty group of commands.
