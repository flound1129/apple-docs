# CommandsBuilder

Constructs command sets from multi-expression closures. Like `ViewBuilder`, it supports up to ten expressions in the closure body.

```swift
@resultBuilder struct CommandsBuilder
```

### Building content

- [buildBlock()](/documentation/swiftui/commandsbuilder/buildblock()): Builds an empty command set from a block containing no statements.
- [buildBlock(_:)](/documentation/swiftui/commandsbuilder/buildblock(_:)): Passes a single command group written as a child group through modified.
- [buildBlock(_:_:)](/documentation/swiftui/commandsbuilder/buildblock(_:_:))
- [buildBlock(_:_:_:)](/documentation/swiftui/commandsbuilder/buildblock(_:_:_:))
- [buildBlock(_:_:_:_:)](/documentation/swiftui/commandsbuilder/buildblock(_:_:_:_:))
- [buildBlock(_:_:_:_:_:)](/documentation/swiftui/commandsbuilder/buildblock(_:_:_:_:_:))
- [buildBlock(_:_:_:_:_:_:)](/documentation/swiftui/commandsbuilder/buildblock(_:_:_:_:_:_:))
- [buildBlock(_:_:_:_:_:_:_:)](/documentation/swiftui/commandsbuilder/buildblock(_:_:_:_:_:_:_:))
- [buildBlock(_:_:_:_:_:_:_:_:)](/documentation/swiftui/commandsbuilder/buildblock(_:_:_:_:_:_:_:_:))
- [buildBlock(_:_:_:_:_:_:_:_:_:)](/documentation/swiftui/commandsbuilder/buildblock(_:_:_:_:_:_:_:_:_:))
- [buildBlock(_:_:_:_:_:_:_:_:_:_:)](/documentation/swiftui/commandsbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:))

### Building conditionally

- [buildEither(first:)](/documentation/swiftui/commandsbuilder/buildeither(first:)): Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [buildEither(second:)](/documentation/swiftui/commandsbuilder/buildeither(second:)): Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [buildIf(_:)](/documentation/swiftui/commandsbuilder/buildif(_:)): Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
- [buildLimitedAvailability(_:)](/documentation/swiftui/commandsbuilder/buildlimitedavailability(_:)): Processes commands for a conditional compiler-control statement that performs an availability check.
- [buildExpression(_:)](/documentation/swiftui/commandsbuilder/buildexpression(_:)): Builds an expression within the builder.

## See Also

### Defining commands

- [commands(content:)](/documentation/swiftui/scene/commands(content:)): Adds commands to the scene.
- [commandsRemoved()](/documentation/swiftui/scene/commandsremoved()): Removes all commands defined by the modified scene.
- [commandsReplaced(content:)](/documentation/swiftui/scene/commandsreplaced(content:)): Replaces all commands defined by the modified scene with the commands from the builder.
- [Commands](/documentation/swiftui/commands): Conforming types represent a group of related commands that can be exposed to the user via the main menu on macOS and key commands on iOS.
- [CommandMenu](/documentation/swiftui/commandmenu): Command menus are stand-alone, top-level containers for controls that perform related, app-specific commands.
- [CommandGroup](/documentation/swiftui/commandgroup): Groups of controls that you can add to existing command menus.
- [CommandGroupPlacement](/documentation/swiftui/commandgroupplacement): The standard locations that you can place new command groups relative to.
