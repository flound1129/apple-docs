# OpenDocumentAction

An action that presents an existing document.

```swift
@MainActor struct OpenDocumentAction
```

## Overview

Use the [openDocument](/documentation/swiftui/environmentvalues/opendocument) environment value to get the instance of this structure for a given [Environment](/documentation/swiftui/environment). Then call the instance to present an existing document. You call the instance directly because it defines a [callAsFunction(at:)](/documentation/swiftui/opendocumentaction/callasfunction(at:)) method that Swift calls when you call the instance.

For example, you can create a button that opens the document at the specified URL:

```swift
struct OpenDocumentButton: View {
    var url: URL
    @Environment(\.openDocument) private var openDocument

    var body: some View {
        Button(url.deletingPathExtension().lastPathComponent) {
            Task {
                do {
                    try await openDocument(at: url)
                } catch {
                    // Handle error
                }
            }
        }
    }
}
```

The above example uses a `do-catch` statement to handle any errors that the open document action might throw. It also places the action inside a task and awaits the result because the action operates asynchronously.

To present an existing document, your app must define a [DocumentGroup](/documentation/swiftui/documentgroup) that handles the content type of the specified file. For a document that’s already open, the system brings the existing window to the front. Otherwise, the system opens a new window.

### Calling the action

- [callAsFunction(at:)](/documentation/swiftui/opendocumentaction/callasfunction(at:)): Opens the document at the specified file URL.

## See Also

### Opening a document programmatically

- [newDocument](/documentation/swiftui/environmentvalues/newdocument): An action in the environment that presents a new document.
- [NewDocumentAction](/documentation/swiftui/newdocumentaction): An action that presents a new document.
- [openDocument](/documentation/swiftui/environmentvalues/opendocument): An action in the environment that presents an existing document.
