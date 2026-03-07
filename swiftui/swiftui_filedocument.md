# FileDocument

A type that you use to serialize documents to and from file.

```swift
@preconcurrency protocol FileDocument : Sendable
```

## Overview

To store a document as a value type — like a structure — create a type that conforms to the `FileDocument` protocol and implement the required methods and properties. Your implementation:

- Provides a list of the content types that the document can read from and write to by defining [readableContentTypes](/documentation/swiftui/filedocument/readablecontenttypes). If the list of content types that the document can write to is different from those that it reads from, you can optionally also define [writableContentTypes](/documentation/swiftui/filedocument/writablecontenttypes).
- Loads documents from file in the [init(configuration:)](/documentation/swiftui/filedocument/init(configuration:)) initializer.
- Stores documents to file by serializing their content in the [fileWrapper(configuration:)](/documentation/swiftui/filedocument/filewrapper(configuration:)) method.

> **Important:**
> If you store your document as a reference type — like a class — use [ReferenceFileDocument](/documentation/swiftui/referencefiledocument) instead.
>

Ensure that types that conform to this protocol are `Sendable`. In particular, SwiftUI calls the protocol’s methods from different isolation domains. Don’t perform serialization and deserialization on `MainActor`.

### Reading a document

- [init(configuration:)](/documentation/swiftui/filedocument/init(configuration:)): Creates a document and initializes it with the contents of a file.
- [readableContentTypes](/documentation/swiftui/filedocument/readablecontenttypes): The file and data types that the document reads from.
- [FileDocument.ReadConfiguration](/documentation/swiftui/filedocument/readconfiguration): The configuration for reading document contents.

### Writing a document

- [fileWrapper(configuration:)](/documentation/swiftui/filedocument/filewrapper(configuration:)): Serializes a document snapshot to a file wrapper.
- [writableContentTypes](/documentation/swiftui/filedocument/writablecontenttypes): The file types that the document supports saving or exporting to.
- [FileDocument.WriteConfiguration](/documentation/swiftui/filedocument/writeconfiguration): The configuration for writing document contents.

## See Also

### Storing document data in a structure instance

- [FileDocumentConfiguration](/documentation/swiftui/filedocumentconfiguration): The properties of an open file document.
