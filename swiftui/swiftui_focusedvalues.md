# FocusedValues

A collection of state exported by the focused scene or view and its ancestors.

```swift
struct FocusedValues
```

## Creating Custom Focused Values

Use the `Entry` macro to create custom focused values by extending `FocusedValues` with new properties:

```swift
extension FocusedValues {
    @Entry var focusedDocument: Binding<MyDocument>?
}
```

The `Entry` macro automatically generates the underlying key type and provides the getter and setter for the focused value. Since the default value for focused values is always `nil`, all focused values must be optional.

### Publishing Values in Your Views

Views publish focused values using the [focusedValue(_:_:)](/documentation/swiftui/view/focusedvalue(_:_:)) modifier:

```swift
struct DocumentCellView: View {
    @Binding var document: MyDocument

    var body: some View {
        Text("Document Content")
            .focusedValue(\.focusedDocument, $document)
    }
}
```

For scene-wide values that should be available depending on the focused scene, use [focusedSceneValue(_:_:)](/documentation/swiftui/view/focusedscenevalue(_:_:)):

```swift
struct DocumentViewer: View {
    @Binding var document: MyDocument

    var body: some View {
        Text("Document Content")
            .focusedSceneValue(\.focusedDocument, $document)
    }
}
```

### Accessing the current focused value

Use the [FocusedValue](/documentation/swiftui/focusedvalue) property wrapper in your [App](/documentation/swiftui/app) or [View](/documentation/swiftui/view) to read the current value in the `body`. The [FocusedBinding](/documentation/swiftui/focusedbinding) can be used as a convenient way to access the `wrappedValue` if the value type of the focused value is a `Binding`:

```swift
@main
struct DocumentApp: App {
    @FocusedBinding(\.focusedDocument) var currentDocument: MyDocument?

    var body: some Scene {
        DocumentGroup(newDocument: MyDocument()) { file in
            ContentView(document: file.$document)
                .focusedValue(\.focusedDocument, file.$document)
        }
        .commands {
            CommandGroup(after: .undoRedo) {
                Button("Increment") {
                    currentDocument?.value += 1
                }.disabled(currentDocument == nil)
            }
        }
    }
}
```

### Getting the value for a key

- [subscript(_:)](/documentation/swiftui/focusedvalues/subscript(_:)): Reads and writes values associated with a given focused value key.

## See Also

### Exposing value types to focused views

- [focusedValue(_:)](/documentation/swiftui/view/focusedvalue(_:)): Sets the focused value for the given object type.
- [focusedValue(_:_:)](/documentation/swiftui/view/focusedvalue(_:_:)): Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused view hierarchy.
- [focusedSceneValue(_:)](/documentation/swiftui/view/focusedscenevalue(_:)): Sets the focused value for the given object type at a scene-wide scope.
- [focusedSceneValue(_:_:)](/documentation/swiftui/view/focusedscenevalue(_:_:)): Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused scene.
