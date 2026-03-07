# Previewable()

Tag allowing a dynamic property to appear inline in a preview.

```swift
@attached(peer) macro Previewable()
```

## Overview

Tagging a variable declaration at root scope in your `#Preview` body with ‘@Previewable’ allows you to use dynamic properties inline in previews. The `#Preview` macro will generate an embedded SwiftUI view; tagged declarations become properties on the view, and all remaining statements form the view’s body.

```swift
#Preview("toggle") {
    @Previewable @State var toggled = true
    return Toggle("Loud Noises", isOn: $toggled)
}
```

It is an error to use `@Previewable` outside of a `#Preview` body closure.

## See Also

### Defining a preview

- [PreviewProvider](/documentation/swiftui/previewprovider): A type that produces view previews in Xcode.
- [PreviewPlatform](/documentation/swiftui/previewplatform): Platforms that can run the preview.
- [previewDisplayName(_:)](/documentation/swiftui/view/previewdisplayname(_:)): Sets a user visible name to show in the canvas for a preview.
- [PreviewModifier](/documentation/swiftui/previewmodifier): A type that defines an environment in which previews can appear.
- [PreviewModifierContent](/documentation/swiftui/previewmodifiercontent): The type-erased content of a preview.
