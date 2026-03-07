# FileDocumentConfiguration

The properties of an open file document.

```swift
struct FileDocumentConfiguration<Document> where Document : FileDocument
```

## Overview

You receive an instance of this structure when you create a [DocumentGroup](/documentation/swiftui/documentgroup) with a value file type. Use it to access the document in your viewer or editor.

### Getting and setting the document

- [document](/documentation/swiftui/filedocumentconfiguration/document): The current document model.
- [$document](/documentation/swiftui/filedocumentconfiguration/$document)

### Getting document properties

- [fileURL](/documentation/swiftui/filedocumentconfiguration/fileurl): The URL of the open file document.
- [isEditable](/documentation/swiftui/filedocumentconfiguration/iseditable): A Boolean that indicates whether you can edit the document.

## See Also

### Storing document data in a structure instance

- [FileDocument](/documentation/swiftui/filedocument): A type that you use to serialize documents to and from file.
