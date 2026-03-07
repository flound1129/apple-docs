# TextEditor

A view that can display and edit long-form text.

```swift
struct TextEditor
```

## Overview

A text editor view allows you to display and edit multiline, scrollable text in your app’s user interface. By default, the text editor view styles the text using characteristics inherited from the environment, like [font(_:)](/documentation/swiftui/view/font(_:)), [foregroundColor(_:)](/documentation/swiftui/view/foregroundcolor(_:)), and [multilineTextAlignment(_:)](/documentation/swiftui/view/multilinetextalignment(_:)).

You create a text editor by adding a `TextEditor` instance to the body of your view, and initialize it by passing in a [Binding](/documentation/swiftui/binding) to a string variable in your app:

```swift
struct TextEditingView: View {
    @State private var fullText: String = "This is some editable text..."

    var body: some View {
        TextEditor(text: $fullText)
    }
}
```

To style the text, use the standard view modifiers to configure a system font, set a custom font, or change the color of the view’s text.

In this example, the view renders the editor’s text in gray with a custom font:

```swift
struct TextEditingView: View {
    @State private var fullText: String = "This is some editable text..."

    var body: some View {
        TextEditor(text: $fullText)
            .foregroundColor(Color.gray)
            .font(.custom("HelveticaNeue", size: 13))
    }
}
```

If you want to change the spacing or font scaling aspects of the text, you can use modifiers like [lineLimit(_:)](/documentation/swiftui/view/linelimit(_:)), [lineSpacing(_:)](/documentation/swiftui/view/linespacing(_:)), and [minimumScaleFactor(_:)](/documentation/swiftui/view/minimumscalefactor(_:)) to configure how the view displays text depending on the space constraints. For example, here the [lineSpacing(_:)](/documentation/swiftui/view/linespacing(_:)) modifier sets the spacing between lines to 5 points:

```swift
struct TextEditingView: View {
    @State private var fullText: String = "This is some editable text..."

    var body: some View {
        TextEditor(text: $fullText)
            .foregroundColor(Color.gray)
            .font(.custom("HelveticaNeue", size: 13))
            .lineSpacing(5)
    }
}
```

### Creating a text editor

- [init(text:)](/documentation/swiftui/texteditor/init(text:)): Creates a plain text editor.

### Initializers

- [init(text:selection:)](/documentation/swiftui/texteditor/init(text:selection:)): Creates a styled text editor.

## See Also

### Getting text input

- [Building rich SwiftUI text experiences](/documentation/swiftui/building-rich-swiftui-text-experiences): Build an editor for formatted text using SwiftUI text editor views and attributed strings.
- [TextField](/documentation/swiftui/textfield): A control that displays an editable text interface.
- [textFieldStyle(_:)](/documentation/swiftui/view/textfieldstyle(_:)): Sets the style for text fields within this view.
- [SecureField](/documentation/swiftui/securefield): A control into which people securely enter private text.
