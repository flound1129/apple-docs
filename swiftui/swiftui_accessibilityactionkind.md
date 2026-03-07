# AccessibilityActionKind

The structure that defines the kinds of available accessibility actions.

```swift
struct AccessibilityActionKind
```

### Getting the kind of action

- [default](/documentation/swiftui/accessibilityactionkind/default): The value that represents the default accessibility action.
- [delete](/documentation/swiftui/accessibilityactionkind/delete)
- [escape](/documentation/swiftui/accessibilityactionkind/escape): The value that represents an accessibility action that dismisses a modal view or cancels an operation.
- [magicTap](/documentation/swiftui/accessibilityactionkind/magictap)
- [showMenu](/documentation/swiftui/accessibilityactionkind/showmenu)

### Creating an action type

- [init(named:)](/documentation/swiftui/accessibilityactionkind/init(named:))

## See Also

### Adding actions to views

- [accessibilityAction(_:_:)](/documentation/swiftui/view/accessibilityaction(_:_:)): Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityActions(_:)](/documentation/swiftui/view/accessibilityactions(_:)): Adds multiple accessibility actions to the view.
- [accessibilityAction(named:_:)](/documentation/swiftui/view/accessibilityaction(named:_:)): Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityAction(action:label:)](/documentation/swiftui/view/accessibilityaction(action:label:)): Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityAction(intent:label:)](/documentation/swiftui/view/accessibilityaction(intent:label:)): Adds an accessibility action labeled by the contents of `label` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAction(_:intent:)](/documentation/swiftui/view/accessibilityaction(_:intent:)): Adds an accessibility action representing `actionKind` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAction(named:intent:)](/documentation/swiftui/view/accessibilityaction(named:intent:)): Adds an accessibility action labeled `name` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAdjustableAction(_:)](/documentation/swiftui/view/accessibilityadjustableaction(_:)): Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityScrollAction(_:)](/documentation/swiftui/view/accessibilityscrollaction(_:)): Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityActions(category:_:)](/documentation/swiftui/view/accessibilityactions(category:_:)): Adds multiple accessibility actions to the view with a specific category. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action and are grouped by their category. When multiple action modifiers with an equal category are applied to the view, the actions are combined together.
- [AccessibilityAdjustmentDirection](/documentation/swiftui/accessibilityadjustmentdirection): A directional indicator you use when making an accessibility adjustment.
- [AccessibilityActionCategory](/documentation/swiftui/accessibilityactioncategory): Designates an accessibility action category that is provided and named by the system.
