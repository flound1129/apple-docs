# InterfaceOrientation

The orientation of the interface from the user’s perspective.

```swift
struct InterfaceOrientation
```

## Overview

By default, device previews appear right side up, using orientation [portrait](/documentation/swiftui/interfaceorientation/portrait). You can change the orientation with a call to the [previewInterfaceOrientation(_:)](/documentation/swiftui/view/previewinterfaceorientation(_:)) modifier:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewInterfaceOrientation(.landscapeRight)
    }
}
```

### Getting an orientation

- [portrait](/documentation/swiftui/interfaceorientation/portrait): The device is in portrait mode, with the top of the device on top.
- [portraitUpsideDown](/documentation/swiftui/interfaceorientation/portraitupsidedown): The device is in portrait mode, but is upside down.
- [landscapeLeft](/documentation/swiftui/interfaceorientation/landscapeleft): The device is in landscape mode, with the top of the device on the left.
- [landscapeRight](/documentation/swiftui/interfaceorientation/landscaperight): The device is in landscape mode, with the top of the device on the right.

## See Also

### Customizing a preview

- [previewDevice(_:)](/documentation/swiftui/view/previewdevice(_:)): Overrides the device for a preview.
- [PreviewDevice](/documentation/swiftui/previewdevice): A simulator device that runs a preview.
- [previewLayout(_:)](/documentation/swiftui/view/previewlayout(_:)): Overrides the size of the container for the preview.
- [previewInterfaceOrientation(_:)](/documentation/swiftui/view/previewinterfaceorientation(_:)): Overrides the orientation of the preview.
