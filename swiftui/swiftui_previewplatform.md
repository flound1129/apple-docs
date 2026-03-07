# PreviewPlatform

Platforms that can run the preview.

```swift
enum PreviewPlatform
```

## Overview

Xcode infers the platform for a preview based on the currently selected target. If you have a multiplatform target and want to suggest a particular target for a preview, implement the [platform](/documentation/swiftui/previewprovider/platform) computed property as a hint, and specify one of the preview platforms:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
    }

    static var platform: PreviewPlatform? {
        PreviewPlatform.tvOS
    }
}
```

### Getting an operating system

- [PreviewPlatform.iOS](/documentation/swiftui/previewplatform/ios): Specifies iOS as the preview platform.
- [PreviewPlatform.macOS](/documentation/swiftui/previewplatform/macos): Specifies macOS as the preview platform.
- [PreviewPlatform.tvOS](/documentation/swiftui/previewplatform/tvos): Specifies tvOS as the preview platform.
- [PreviewPlatform.watchOS](/documentation/swiftui/previewplatform/watchos): Specifies watchOS as the preview platform.

## See Also

### Defining a preview

- [Previewable()](/documentation/swiftui/previewable()): Tag allowing a dynamic property to appear inline in a preview.
- [PreviewProvider](/documentation/swiftui/previewprovider): A type that produces view previews in Xcode.
- [previewDisplayName(_:)](/documentation/swiftui/view/previewdisplayname(_:)): Sets a user visible name to show in the canvas for a preview.
- [PreviewModifier](/documentation/swiftui/previewmodifier): A type that defines an environment in which previews can appear.
- [PreviewModifierContent](/documentation/swiftui/previewmodifiercontent): The type-erased content of a preview.
