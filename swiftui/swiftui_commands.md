# Commands

Conforming types represent a group of related commands that can be exposed to the user via the main menu on macOS and key commands on iOS.

```swift
@MainActor @preconcurrency protocol Commands
```

## Overview

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

### Implementing commands

- [body](/documentation/swiftui/commands/body-swift.property): The contents of the command hierarchy.
- [Body](/documentation/swiftui/commands/body-swift.associatedtype): The type of commands that represents the body of this command hierarchy.

## See Also

### Defining commands

- [commands(content:)](/documentation/swiftui/scene/commands(content:)): Adds commands to the scene.
- [commandsRemoved()](/documentation/swiftui/scene/commandsremoved()): Removes all commands defined by the modified scene.
- [commandsReplaced(content:)](/documentation/swiftui/scene/commandsreplaced(content:)): Replaces all commands defined by the modified scene with the commands from the builder.
- [CommandMenu](/documentation/swiftui/commandmenu): Command menus are stand-alone, top-level containers for controls that perform related, app-specific commands.
- [CommandGroup](/documentation/swiftui/commandgroup): Groups of controls that you can add to existing command menus.
- [CommandsBuilder](/documentation/swiftui/commandsbuilder): Constructs command sets from multi-expression closures. Like `ViewBuilder`, it supports up to ten expressions in the closure body.
- [CommandGroupPlacement](/documentation/swiftui/commandgroupplacement): The standard locations that you can place new command groups relative to.
