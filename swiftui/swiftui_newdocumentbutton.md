# NewDocumentButton

A button that creates and opens new documents.

```swift
struct NewDocumentButton<Label> where Label : View
```

## Overview

Use a new document button to give people the option to create documents in your app. In the following example, there are two new document buttons, both support [Text](/documentation/swiftui/text) labels. When the user taps or clicks the first button, the system creates a new document in the directory currently open in the document browser. The second button presents a template picker, where a document can be prepopulated or preconfigured using a template.

```swift
@State private var isTemplatePickerPresented = false
@State private var documentCreationContinuation:
    CheckedContinuation<TextDocument?, any Error>?

var body: some Scene {
    DocumentGroupLaunchScene("My Documents") {
        NewDocumentButton(Text("Start Writing…"))
        NewDocumentButton(Text("Choose a Template"), for: TextDocument.self) {
            try await withCheckedThrowingContinuation { continuation in
                documentCreationContinuation = continuation
                isTemplatePickerPresented = true
            }
        }
        .fullScreenCover(isPresented: $isTemplatePickerPresented) {
            TemplatePicker(
                continuation: $documentCreationContinuation
            )
        }
    }

    DocumentGroup(newDocument: TextDocument()) { configuration in
        MyDocumentView(document: configuration.$document))
    }
}

struct TemplatePicker: View {
    @Binding var continuation:
        CheckedContinuation<TextDocument?, any Error>?
    @Environment(\.dismiss) var dismiss

    var body: some View {
        VStack {
            Text("Choose a template")
                .font(.title)
            Button("Meeting minutes") {
                let document = makeMeetingMinutes()
                documentCreationContinuation?.resume(returning: document)
                dismiss()
            }
            Button("Letter") {
                let document = makeLetter()
                documentCreationContinuation?.resume(returning: document)
                dismiss()
            }
            Button("Cancel") {
                documentCreationContinuation?.resume(throwing: CancellationError())
                dismiss()
            }
        }
    }

    private func makeMeetingMinutes() -> TextDocument { ... }
    private func makeLetter() -> TextDocument { ... }
}

struct TextDocument: FileDocument { ... }
```

If you don’t provide a custom label, the system provides a button with the default “Create Document” label.

### Initializers

- [init(_:contentType:)](/documentation/swiftui/newdocumentbutton/init(_:contenttype:)): Creates and opens new documents.
- [init(_:contentType:prepareDocumentURL:)](/documentation/swiftui/newdocumentbutton/init(_:contenttype:preparedocumenturl:)): Creates and opens new documents.
- [init(_:for:contentType:prepareDocument:)](/documentation/swiftui/newdocumentbutton/init(_:for:contenttype:preparedocument:)): Creates and opens new documents.

## See Also

### Configuring the document launch experience

- [DocumentGroupLaunchScene](/documentation/swiftui/documentgrouplaunchscene): A launch scene for document-based applications.
- [DocumentLaunchView](/documentation/swiftui/documentlaunchview): A view to present when launching document-related user experience.
- [DocumentLaunchGeometryProxy](/documentation/swiftui/documentlaunchgeometryproxy): A proxy for access to the frame of the scene and its title view.
- [DefaultDocumentGroupLaunchActions](/documentation/swiftui/defaultdocumentgrouplaunchactions): The default actions for the document group launch scene and the document launch view.
- [DocumentBaseBox](/documentation/swiftui/documentbasebox): A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.
