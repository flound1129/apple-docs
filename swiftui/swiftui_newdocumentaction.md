# NewDocumentAction

An action that presents a new document.

```swift
@MainActor @preconcurrency struct NewDocumentAction
```

## Overview

Use the [newDocument](/documentation/swiftui/environmentvalues/newdocument) environment value to get the instance of this structure for a given [Environment](/documentation/swiftui/environment). Then call the instance to present a new document. You call the instance directly because it defines a [callAsFunction(_:)](/documentation/swiftui/newdocumentaction/callasfunction(_:)) method that Swift calls when you call the instance.

For example, you can define a button that creates a new document from the selected text:

```swift
struct NewDocumentFromSelection: View {
    @FocusedBinding(\.selectedText) private var selectedText: String?
    @Environment(\.newDocument) private var newDocument

    var body: some View {
        Button("New Document With Selection") {
            newDocument(TextDocument(text: selectedText))
        }
        .disabled(selectedText?.isEmpty != false)
    }
}
```

The above example assumes that you define a `TextDocument` that conforms to the [FileDocument](/documentation/swiftui/filedocument) or [ReferenceFileDocument](/documentation/swiftui/referencefiledocument) protocol, and a [DocumentGroup](/documentation/swiftui/documentgroup) that handles the associated file type.

### Calling the action

- [callAsFunction(_:)](/documentation/swiftui/newdocumentaction/callasfunction(_:)): Presents a new document window.
- [callAsFunction(contentType:)](/documentation/swiftui/newdocumentaction/callasfunction(contenttype:)): Presents a new document window.
- [callAsFunction(contentType:prepareDocument:)](/documentation/swiftui/newdocumentaction/callasfunction(contenttype:preparedocument:)): Presents a new document window with preset contents.

## See Also

### Opening a document programmatically

- [newDocument](/documentation/swiftui/environmentvalues/newdocument): An action in the environment that presents a new document.
- [openDocument](/documentation/swiftui/environmentvalues/opendocument): An action in the environment that presents an existing document.
- [OpenDocumentAction](/documentation/swiftui/opendocumentaction): An action that presents an existing document.
