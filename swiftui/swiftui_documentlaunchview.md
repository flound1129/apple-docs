# DocumentLaunchView

A view to present when launching document-related user experience.

```swift
struct DocumentLaunchView<Actions, DocumentView> where Actions : View, DocumentView : View
```

## Overview

> **Note:**
>  An alternative to `DocumentLaunchView` is a scene variant of this API: [DocumentGroupLaunchScene](/documentation/swiftui/documentgrouplaunchscene). If the app definition contains `DocumentGroup` scenes, consider using a `DocumentGroupLaunchScene` instead of this view.
>

Configure `DocumentLaunchView` to open and display files and trigger custom actions.

For example, an application that offers writing books can present the `DocumentLaunchView` as its launch view:

```swift
public import UniformTypeIdentifiers

struct BookEditorLaunchView: View {

    var body: some View {
        DocumentLaunchView(for: [.book]) {
            NewDocumentButton("Start New Book")
        } onDocumentOpen: { url in
            BookEditor(url)
        }
    }
}

struct BookEditor: View {
    init(_ url: URL) { }
}

extension UTType {
    static let book = UTType(exportedAs: "com.example.bookEditor")
}
```

### Initializers

- [init(_:for:_:onDocumentOpen:)](/documentation/swiftui/documentlaunchview/init(_:for:_:ondocumentopen:)): Creates a view to present when launching document-related user experiences using a localized title and custom actions.
- [init(_:for:_:onDocumentOpen:background:)](/documentation/swiftui/documentlaunchview/init(_:for:_:ondocumentopen:background:)): Creates a view to present when launching document-related user experiences using a localized title, custom actions, and a background view.
- [init(_:for:_:onDocumentOpen:background:backgroundAccessoryView:)](/documentation/swiftui/documentlaunchview/init(_:for:_:ondocumentopen:background:backgroundaccessoryview:)): Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background view, and a background accessory view.
- [init(_:for:_:onDocumentOpen:background:backgroundAccessoryView:overlayAccessoryView:)](/documentation/swiftui/documentlaunchview/init(_:for:_:ondocumentopen:background:backgroundaccessoryview:overlayaccessoryview:)): Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background view, and accessory views.
- [init(_:for:_:onDocumentOpen:background:overlayAccessoryView:)](/documentation/swiftui/documentlaunchview/init(_:for:_:ondocumentopen:background:overlayaccessoryview:)): Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background view, and an overlay accessory view.
- [init(_:for:_:onDocumentOpen:backgroundAccessoryView:)](/documentation/swiftui/documentlaunchview/init(_:for:_:ondocumentopen:backgroundaccessoryview:)): Creates a view to present when launching document-related user experiences using a localized title, custom actions, and a background accessory view.
- [init(_:for:_:onDocumentOpen:backgroundAccessoryView:overlayAccessoryView:)](/documentation/swiftui/documentlaunchview/init(_:for:_:ondocumentopen:backgroundaccessoryview:overlayaccessoryview:)): Creates a view to present when launching document-related user experiences using a localized title, custom actions, and accessory views.
- [init(_:for:_:onDocumentOpen:overlayAccessoryView:)](/documentation/swiftui/documentlaunchview/init(_:for:_:ondocumentopen:overlayaccessoryview:)): Creates a view to present when launching document-related user experiences using a localized title, custom actions, and an overlay accessory view.
- [init(_:for:backgroundStyle:_:onDocumentOpen:)](/documentation/swiftui/documentlaunchview/init(_:for:backgroundstyle:_:ondocumentopen:)): Creates a view to present when launching document-related user experiences using a localized title, custom actions, and a background style.
- [init(_:for:backgroundStyle:_:onDocumentOpen:backgroundAccessoryView:)](/documentation/swiftui/documentlaunchview/init(_:for:backgroundstyle:_:ondocumentopen:backgroundaccessoryview:)): Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background style, and a background accessory view.
- [init(_:for:backgroundStyle:_:onDocumentOpen:backgroundAccessoryView:overlayAccessoryView:)](/documentation/swiftui/documentlaunchview/init(_:for:backgroundstyle:_:ondocumentopen:backgroundaccessoryview:overlayaccessoryview:)): Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background style, and accessory views.
- [init(_:for:backgroundStyle:_:onDocumentOpen:overlayAccessoryView:)](/documentation/swiftui/documentlaunchview/init(_:for:backgroundstyle:_:ondocumentopen:overlayaccessoryview:)): Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background style, and an overlay accessory view.

### Instance Properties

- [body](/documentation/swiftui/documentlaunchview/body): The body of the view.

## See Also

### Configuring the document launch experience

- [DocumentGroupLaunchScene](/documentation/swiftui/documentgrouplaunchscene): A launch scene for document-based applications.
- [DocumentLaunchGeometryProxy](/documentation/swiftui/documentlaunchgeometryproxy): A proxy for access to the frame of the scene and its title view.
- [DefaultDocumentGroupLaunchActions](/documentation/swiftui/defaultdocumentgrouplaunchactions): The default actions for the document group launch scene and the document launch view.
- [NewDocumentButton](/documentation/swiftui/newdocumentbutton): A button that creates and opens new documents.
- [DocumentBaseBox](/documentation/swiftui/documentbasebox): A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.
