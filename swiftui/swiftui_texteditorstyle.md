# TextEditorStyle

A specification for the appearance and interaction of a text editor.

```swift
@MainActor @preconcurrency protocol TextEditorStyle
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

### Getting built-in styles

- [automatic](/documentation/swiftui/texteditorstyle/automatic): The default text editor style, based on the text editor’s context.
- [plain](/documentation/swiftui/texteditorstyle/plain): A text editor style with no decoration.
- [roundedBorder](/documentation/swiftui/texteditorstyle/roundedborder): A text editor style with a system-defined rounded border.

### Creating custom styles

- [makeBody(configuration:)](/documentation/swiftui/texteditorstyle/makebody(configuration:)): Creates a view that represents the body of a text editor.
- [TextEditorStyle.Configuration](/documentation/swiftui/texteditorstyle/configuration): The properties of a text editor.
- [Body](/documentation/swiftui/texteditorstyle/body): A view that represents the body of a text editor.

### Supporting types

- [AutomaticTextEditorStyle](/documentation/swiftui/automatictexteditorstyle): The default text editor style, based on the text editor’s context.
- [PlainTextEditorStyle](/documentation/swiftui/plaintexteditorstyle): A text editor style with no decoration.
- [RoundedBorderTextEditorStyle](/documentation/swiftui/roundedbordertexteditorstyle): A text editor style with a system-defined rounded border.

## See Also

### Styling views that display text

- [labelStyle(_:)](/documentation/swiftui/view/labelstyle(_:)): Sets the style for labels within this view.
- [LabelStyle](/documentation/swiftui/labelstyle): A type that applies a custom appearance to all labels within a view.
- [LabelStyleConfiguration](/documentation/swiftui/labelstyleconfiguration): The properties of a label.
- [textFieldStyle(_:)](/documentation/swiftui/view/textfieldstyle(_:)): Sets the style for text fields within this view.
- [TextFieldStyle](/documentation/swiftui/textfieldstyle): A specification for the appearance and interaction of a text field.
- [textEditorStyle(_:)](/documentation/swiftui/view/texteditorstyle(_:)): Sets the style for text editors within this view.
- [TextEditorStyleConfiguration](/documentation/swiftui/texteditorstyleconfiguration): The properties of a text editor.
