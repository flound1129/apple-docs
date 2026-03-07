# CommandMenu

Command menus are stand-alone, top-level containers for controls that perform related, app-specific commands.

```swift
struct CommandMenu<Content> where Content : View
```

## Overview

Command menus are realized as menu bar menus on macOS, inserted between the built-in View and Window menus in order of declaration. On iOS, iPadOS, and tvOS, SwiftUI creates key commands for each of a menu’s commands that has a keyboard shortcut.

### Creating a command menu

- [init(_:content:)](/documentation/swiftui/commandmenu/init(_:content:)): Creates a new menu with a localized name for a collection of app- specific commands, inserted in the standard location for app menus (after the View menu, in order with other menus declared without an explicit location).

## See Also

### Defining commands

- [commands(content:)](/documentation/swiftui/scene/commands(content:)): Adds commands to the scene.
- [commandsRemoved()](/documentation/swiftui/scene/commandsremoved()): Removes all commands defined by the modified scene.
- [commandsReplaced(content:)](/documentation/swiftui/scene/commandsreplaced(content:)): Replaces all commands defined by the modified scene with the commands from the builder.
- [Commands](/documentation/swiftui/commands): Conforming types represent a group of related commands that can be exposed to the user via the main menu on macOS and key commands on iOS.
- [CommandGroup](/documentation/swiftui/commandgroup): Groups of controls that you can add to existing command menus.
- [CommandsBuilder](/documentation/swiftui/commandsbuilder): Constructs command sets from multi-expression closures. Like `ViewBuilder`, it supports up to ten expressions in the closure body.
- [CommandGroupPlacement](/documentation/swiftui/commandgroupplacement): The standard locations that you can place new command groups relative to.
