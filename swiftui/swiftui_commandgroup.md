# CommandGroup

Groups of controls that you can add to existing command menus.

```swift
struct CommandGroup<Content> where Content : View
```

## Overview

In macOS, SwiftUI realizes command groups as collections of menu items in a menu bar menu. In iOS, iPadOS, and tvOS, SwiftUI creates key commands for each of a group’s commands that has a keyboard shortcut.

### Creating a command group

- [init(after:addition:)](/documentation/swiftui/commandgroup/init(after:addition:)): A value describing the addition of the given views to the end of the indicated group.
- [init(before:addition:)](/documentation/swiftui/commandgroup/init(before:addition:)): A value describing the addition of the given views to the beginning of the indicated group.
- [init(replacing:addition:)](/documentation/swiftui/commandgroup/init(replacing:addition:)): A value describing the complete replacement of the contents of the indicated group with the given views.

## See Also

### Defining commands

- [commands(content:)](/documentation/swiftui/scene/commands(content:)): Adds commands to the scene.
- [commandsRemoved()](/documentation/swiftui/scene/commandsremoved()): Removes all commands defined by the modified scene.
- [commandsReplaced(content:)](/documentation/swiftui/scene/commandsreplaced(content:)): Replaces all commands defined by the modified scene with the commands from the builder.
- [Commands](/documentation/swiftui/commands): Conforming types represent a group of related commands that can be exposed to the user via the main menu on macOS and key commands on iOS.
- [CommandMenu](/documentation/swiftui/commandmenu): Command menus are stand-alone, top-level containers for controls that perform related, app-specific commands.
- [CommandsBuilder](/documentation/swiftui/commandsbuilder): Constructs command sets from multi-expression closures. Like `ViewBuilder`, it supports up to ten expressions in the closure body.
- [CommandGroupPlacement](/documentation/swiftui/commandgroupplacement): The standard locations that you can place new command groups relative to.
