# EventModifiers

A set of key modifiers that you can add to a gesture.

```swift
@frozen struct EventModifiers
```

### Getting modifier keys

- [all](/documentation/swiftui/eventmodifiers/all): All possible modifier keys.
- [capsLock](/documentation/swiftui/eventmodifiers/capslock): The Caps Lock key.
- [command](/documentation/swiftui/eventmodifiers/command): The Command key.
- [control](/documentation/swiftui/eventmodifiers/control): The Control key.
- [numericPad](/documentation/swiftui/eventmodifiers/numericpad): Any key on the numeric keypad.
- [option](/documentation/swiftui/eventmodifiers/option): The Option key.
- [shift](/documentation/swiftui/eventmodifiers/shift): The Shift key.

### Creating a set of options

- [init(rawValue:)](/documentation/swiftui/eventmodifiers/init(rawvalue:)): Creates a new set from a raw value.
- [rawValue](/documentation/swiftui/eventmodifiers/rawvalue): The raw value.

### Deprecated modifiers

- [function](/documentation/swiftui/eventmodifiers/function): The Function key.

## See Also

### Creating keyboard shortcuts

- [keyboardShortcut(_:)](/documentation/swiftui/view/keyboardshortcut(_:)): Assigns a keyboard shortcut to the modified control.
- [keyboardShortcut(_:modifiers:)](/documentation/swiftui/view/keyboardshortcut(_:modifiers:)): Defines a keyboard shortcut and assigns it to the modified control.
- [keyboardShortcut(_:modifiers:localization:)](/documentation/swiftui/view/keyboardshortcut(_:modifiers:localization:)): Defines a keyboard shortcut and assigns it to the modified control.
- [keyboardShortcut](/documentation/swiftui/environmentvalues/keyboardshortcut): The keyboard shortcut that buttons in this environment will be triggered with.
- [KeyboardShortcut](/documentation/swiftui/keyboardshortcut): Keyboard shortcuts describe combinations of keys on a keyboard that the user can press in order to activate a button or toggle.
- [KeyEquivalent](/documentation/swiftui/keyequivalent): Key equivalents consist of a letter, punctuation, or function key that can be combined with an optional set of modifier keys to specify a keyboard shortcut.
