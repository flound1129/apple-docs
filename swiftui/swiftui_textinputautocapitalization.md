# TextInputAutocapitalization

The kind of autocapitalization behavior applied during text input.

```swift
struct TextInputAutocapitalization
```

## Overview

Pass an instance of `TextInputAutocapitalization` to the [textInputAutocapitalization(_:)](/documentation/swiftui/view/textinputautocapitalization(_:)) view modifier.

### Getting autocapitalization options

- [characters](/documentation/swiftui/textinputautocapitalization/characters): Defines an autocapitalizing behavior that will capitalize every letter.
- [sentences](/documentation/swiftui/textinputautocapitalization/sentences): Defines an autocapitalizing behavior that will capitalize the first letter in every sentence.
- [words](/documentation/swiftui/textinputautocapitalization/words): Defines an autocapitalizing behavior that will capitalize the first letter of every word.
- [never](/documentation/swiftui/textinputautocapitalization/never): Defines an autocapitalizing behavior that will not capitalize anything.

### Creating an autocapitalization type

- [init(_:)](/documentation/swiftui/textinputautocapitalization/init(_:)): Creates a new [TextInputAutocapitalization](/documentation/swiftui/textinputautocapitalization) struct from a `UITextAutocapitalizationType` enum.

## See Also

### Managing text entry

- [autocorrectionDisabled(_:)](/documentation/swiftui/view/autocorrectiondisabled(_:)): Sets whether to disable autocorrection for this view.
- [autocorrectionDisabled](/documentation/swiftui/environmentvalues/autocorrectiondisabled): A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [keyboardType(_:)](/documentation/swiftui/view/keyboardtype(_:)): Sets the keyboard type for this view.
- [scrollDismissesKeyboard(_:)](/documentation/swiftui/view/scrolldismisseskeyboard(_:)): Configures the behavior in which scrollable content interacts with the software keyboard.
- [textContentType(_:)](/documentation/swiftui/view/textcontenttype(_:)): Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [textInputAutocapitalization(_:)](/documentation/swiftui/view/textinputautocapitalization(_:)): Sets how often the shift key in the keyboard is automatically enabled.
- [textInputCompletion(_:)](/documentation/swiftui/view/textinputcompletion(_:)): Associates a fully formed string with the value of this view when used as a text input suggestion
- [textInputSuggestions(_:)](/documentation/swiftui/view/textinputsuggestions(_:)): Configures the text input suggestions for this view.
- [textInputSuggestions(_:content:)](/documentation/swiftui/view/textinputsuggestions(_:content:)): Configures the text input suggestions for this view.
- [textInputSuggestions(_:id:content:)](/documentation/swiftui/view/textinputsuggestions(_:id:content:)): Configures the text input suggestions for this view.
- [textContentType(_:)](/documentation/swiftui/view/textcontenttype(_:)-4dqqb): Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on a watchOS device.
- [textContentType(_:)](/documentation/swiftui/view/textcontenttype(_:)-6fic1): Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [textContentType(_:)](/documentation/swiftui/view/textcontenttype(_:)-ufdv): Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.
- [TextInputFormattingControlPlacement](/documentation/swiftui/textinputformattingcontrolplacement): A structure defining the system text formatting controls available on each platform.
