# KeyEquivalent

Key equivalents consist of a letter, punctuation, or function key that can be combined with an optional set of modifier keys to specify a keyboard shortcut.

```swift
struct KeyEquivalent
```

## Overview

Key equivalents are used to establish keyboard shortcuts to app functionality. Any key can be used as a key equivalent as long as pressing it produces a single character value. Key equivalents are typically initialized using a single-character string literal, with constants for unprintable or hard-to-type values.

The modifier keys necessary to type a key equivalent are factored in to the resulting keyboard shortcut. That is, a key equivalent whose raw value is the capitalized string “A” corresponds with the keyboard shortcut Command-Shift-A. The exact mapping may depend on the keyboard layout—for example, a key equivalent with the character value “}” produces a shortcut equivalent to Command-Shift-] on ANSI keyboards, but would produce a different shortcut for keyboard layouts where punctuation characters are in different locations.

### Getting arrow keys

- [upArrow](/documentation/swiftui/keyequivalent/uparrow): Up Arrow (U+F700)
- [downArrow](/documentation/swiftui/keyequivalent/downarrow): Down Arrow (U+F701)
- [leftArrow](/documentation/swiftui/keyequivalent/leftarrow): Left Arrow (U+F702)
- [rightArrow](/documentation/swiftui/keyequivalent/rightarrow): Right Arrow (U+F703)

### Getting other special keys

- [clear](/documentation/swiftui/keyequivalent/clear): Clear (U+F739)
- [delete](/documentation/swiftui/keyequivalent/delete): Delete (U+0008)
- [deleteForward](/documentation/swiftui/keyequivalent/deleteforward): Delete Forward (U+F728)
- [end](/documentation/swiftui/keyequivalent/end): End (U+F72B)
- [escape](/documentation/swiftui/keyequivalent/escape): Escape (U+001B)
- [home](/documentation/swiftui/keyequivalent/home): Home (U+F729)
- [pageDown](/documentation/swiftui/keyequivalent/pagedown): Page Down (U+F72D)
- [pageUp](/documentation/swiftui/keyequivalent/pageup): Page Up (U+F72C)
- [return](/documentation/swiftui/keyequivalent/return): Return (U+000D)
- [space](/documentation/swiftui/keyequivalent/space): Space (U+0020)
- [tab](/documentation/swiftui/keyequivalent/tab): Tab (U+0009)

### Creating a key equivalent

- [init(_:)](/documentation/swiftui/keyequivalent/init(_:)): Creates a new key equivalent from the given character value.
- [character](/documentation/swiftui/keyequivalent/character): The character value that the key equivalent represents.

## See Also

### Creating keyboard shortcuts

- [keyboardShortcut(_:)](/documentation/swiftui/view/keyboardshortcut(_:)): Assigns a keyboard shortcut to the modified control.
- [keyboardShortcut(_:modifiers:)](/documentation/swiftui/view/keyboardshortcut(_:modifiers:)): Defines a keyboard shortcut and assigns it to the modified control.
- [keyboardShortcut(_:modifiers:localization:)](/documentation/swiftui/view/keyboardshortcut(_:modifiers:localization:)): Defines a keyboard shortcut and assigns it to the modified control.
- [keyboardShortcut](/documentation/swiftui/environmentvalues/keyboardshortcut): The keyboard shortcut that buttons in this environment will be triggered with.
- [KeyboardShortcut](/documentation/swiftui/keyboardshortcut): Keyboard shortcuts describe combinations of keys on a keyboard that the user can press in order to activate a button or toggle.
- [EventModifiers](/documentation/swiftui/eventmodifiers): A set of key modifiers that you can add to a gesture.
