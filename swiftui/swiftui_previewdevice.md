# PreviewDevice

A simulator device that runs a preview.

```swift
struct PreviewDevice
```

## Overview

Create a preview device by name, like “iPhone X”, or by model number, like “iPad8,1”. Use the device in a call to the [previewDevice(_:)](/documentation/swiftui/view/previewdevice(_:)) modifier to set a preview device that doesn’t change when you change the run destination in Xcode:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewDevice(PreviewDevice(rawValue: "iPad Pro (11-inch)"))
    }
}
```

You can get a list of supported preview device names by using the `xcrun` command in the Terminal app:

```swift
% xcrun simctl list devicetypes
```

Additionally, you can use the following values for macOS platform development:

- “Mac”
- “Mac Catalyst”

## See Also

### Customizing a preview

- [previewDevice(_:)](/documentation/swiftui/view/previewdevice(_:)): Overrides the device for a preview.
- [previewLayout(_:)](/documentation/swiftui/view/previewlayout(_:)): Overrides the size of the container for the preview.
- [previewInterfaceOrientation(_:)](/documentation/swiftui/view/previewinterfaceorientation(_:)): Overrides the orientation of the preview.
- [InterfaceOrientation](/documentation/swiftui/interfaceorientation): The orientation of the interface from the user’s perspective.
