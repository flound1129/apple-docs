# DefaultFocusEvaluationPriority

Prioritizations for default focus preferences when evaluating where to move focus in different circumstances.

```swift
struct DefaultFocusEvaluationPriority
```

### Getting the priorities

- [automatic](/documentation/swiftui/defaultfocusevaluationpriority/automatic): Use the default focus preference when focus moves into the affected branch automatically, but ignore it when the movement is driven by a user-initiated navigation command.
- [userInitiated](/documentation/swiftui/defaultfocusevaluationpriority/userinitiated): Always use the default focus preference when focus moves into the affected branch.

## See Also

### Controlling default focus

- [prefersDefaultFocus(_:in:)](/documentation/swiftui/view/prefersdefaultfocus(_:in:)): Indicates that the view should receive focus by default for a given namespace.
- [defaultFocus(_:_:priority:)](/documentation/swiftui/view/defaultfocus(_:_:priority:)): Defines a region of the window in which default focus is evaluated by assigning a value to a given focus state binding.
