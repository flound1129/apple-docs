# ReferenceFileDocumentConfiguration

The properties of an open reference file document.

```swift
@MainActor @preconcurrency struct ReferenceFileDocumentConfiguration<Document> where Document : ReferenceFileDocument
```

## Overview

You receive an instance of this structure when you create a [DocumentGroup](/documentation/swiftui/documentgroup) with a reference file type. Use it to access the document in your viewer or editor.

### Getting and setting the document

- [document](/documentation/swiftui/referencefiledocumentconfiguration/document): The current document model.
- [$document](/documentation/swiftui/referencefiledocumentconfiguration/$document)

### Getting document properties

- [fileURL](/documentation/swiftui/referencefiledocumentconfiguration/fileurl): The URL of the open file document.
- [isEditable](/documentation/swiftui/referencefiledocumentconfiguration/iseditable): A Boolean that indicates whether you can edit the document.

## See Also

### Storing document data in a class instance

- [ReferenceFileDocument](/documentation/swiftui/referencefiledocument): A type that you use to serialize reference type documents to and from file.
- [undoManager](/documentation/swiftui/environmentvalues/undomanager): The undo manager used to register a view’s undo operations.
