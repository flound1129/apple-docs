# KeyboardShortcut

Keyboard shortcuts describe combinations of keys on a keyboard that the user can press in order to activate a button or toggle.

```swift
struct KeyboardShortcut
```

### Getting standard shortcuts

- [cancelAction](/documentation/swiftui/keyboardshortcut/cancelaction): The standard keyboard shortcut for cancelling the in-progress action or dismissing a prompt, consisting of the Escape (⎋) key and no modifiers.
- [defaultAction](/documentation/swiftui/keyboardshortcut/defaultaction): The standard keyboard shortcut for the default button, consisting of the Return (↩) key and no modifiers.

### Creating a shortcut

- [init(_:modifiers:)](/documentation/swiftui/keyboardshortcut/init(_:modifiers:)): Creates a new keyboard shortcut with the given key equivalent and set of modifier keys.
- [key](/documentation/swiftui/keyboardshortcut/key): The key equivalent that the user presses in conjunction with any specified modifier keys to activate the shortcut.
- [modifiers](/documentation/swiftui/keyboardshortcut/modifiers): The modifier keys that the user presses in conjunction with a key equivalent to activate the shortcut.

### Creating a localized shortcut

- [init(_:modifiers:localization:)](/documentation/swiftui/keyboardshortcut/init(_:modifiers:localization:)): Creates a new keyboard shortcut with the given key equivalent and set of modifier keys.
- [localization](/documentation/swiftui/keyboardshortcut/localization-swift.property): The localization strategy to apply to this shortcut.
- [KeyboardShortcut.Localization](/documentation/swiftui/keyboardshortcut/localization-swift.struct): Options for how a keyboard shortcut participates in automatic localization.

## See Also

### Creating keyboard shortcuts

- [keyboardShortcut(_:)](/documentation/swiftui/view/keyboardshortcut(_:)): Assigns a keyboard shortcut to the modified control.
- [keyboardShortcut(_:modifiers:)](/documentation/swiftui/view/keyboardshortcut(_:modifiers:)): Defines a keyboard shortcut and assigns it to the modified control.
- [keyboardShortcut(_:modifiers:localization:)](/documentation/swiftui/view/keyboardshortcut(_:modifiers:localization:)): Defines a keyboard shortcut and assigns it to the modified control.
- [keyboardShortcut](/documentation/swiftui/environmentvalues/keyboardshortcut): The keyboard shortcut that buttons in this environment will be triggered with.
- [KeyEquivalent](/documentation/swiftui/keyequivalent): Key equivalents consist of a letter, punctuation, or function key that can be combined with an optional set of modifier keys to specify a keyboard shortcut.
- [EventModifiers](/documentation/swiftui/eventmodifiers): A set of key modifiers that you can add to a gesture.
