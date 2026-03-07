# FocusInteractions

Values describe different focus interactions that a view can support.

```swift
struct FocusInteractions
```

### Creating the interaction types

- [automatic](/documentation/swiftui/focusinteractions/automatic): The view supports whatever focus-driven interactions are commonly expected for interactive content on the current platform.
- [activate](/documentation/swiftui/focusinteractions/activate): The view has a primary action that can be activated via focus gestures.
- [edit](/documentation/swiftui/focusinteractions/edit): The view captures input from non-spatial sources like a keyboard or Digital Crown.

## See Also

### Indicating that a view can receive focus

- [focusable(_:)](/documentation/swiftui/view/focusable(_:)): Specifies if the view is focusable.
- [focusable(_:interactions:)](/documentation/swiftui/view/focusable(_:interactions:)): Specifies if the view is focusable, and if so, what focus-driven interactions it supports.
