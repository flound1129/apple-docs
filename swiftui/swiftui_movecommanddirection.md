# MoveCommandDirection

Specifies the direction of an arrow key movement.

```swift
enum MoveCommandDirection
```

### Getting move command directions

- [MoveCommandDirection.up](/documentation/swiftui/movecommanddirection/up)
- [MoveCommandDirection.down](/documentation/swiftui/movecommanddirection/down)
- [MoveCommandDirection.left](/documentation/swiftui/movecommanddirection/left)
- [MoveCommandDirection.right](/documentation/swiftui/movecommanddirection/right)

## See Also

### Responding to commands

- [onMoveCommand(perform:)](/documentation/swiftui/view/onmovecommand(perform:)): Adds an action to perform in response to a move command, like when the user presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote when controlling an Apple TV.
- [onDeleteCommand(perform:)](/documentation/swiftui/view/ondeletecommand(perform:)): Adds an action to perform in response to the system’s Delete command, or pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view has focus.
- [pageCommand(value:in:step:)](/documentation/swiftui/view/pagecommand(value:in:step:)): Steps a value through a range in response to page up or page down commands.
- [onExitCommand(perform:)](/documentation/swiftui/view/onexitcommand(perform:)): Sets up an action that triggers in response to receiving the exit command while the view has focus.
- [onPlayPauseCommand(perform:)](/documentation/swiftui/view/onplaypausecommand(perform:)): Adds an action to perform in response to the system’s Play/Pause command.
- [onCommand(_:perform:)](/documentation/swiftui/view/oncommand(_:perform:)): Adds an action to perform in response to the given selector.
