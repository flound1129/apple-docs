# PencilHoverPose

A value describing the location and distance of an Apple Pencil hovering in the area above a view’s bounds.

```swift
struct PencilHoverPose
```

### Getting the hover characteristics

- [anchor](/documentation/swiftui/pencilhoverpose/anchor): The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a normalized anchor point relative to that view.
- [location](/documentation/swiftui/pencilhoverpose/location): The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a point in that view’s coordinate space.
- [zDistance](/documentation/swiftui/pencilhoverpose/zdistance): The normalized distance between the screen and a hovering Apple Pencil.

### Instance Properties

- [altitude](/documentation/swiftui/pencilhoverpose/altitude): A value that represents the altitude angle of the hovering Apple Pencil.
- [azimuth](/documentation/swiftui/pencilhoverpose/azimuth): A value that represents the azimuth angle of a hovering Apple Pencil.
- [roll](/documentation/swiftui/pencilhoverpose/roll): A value that represents the barrel roll angle of the hovering Apple Pencil.

## See Also

### Recognizing Apple Pencil gestures

- [onPencilDoubleTap(perform:)](/documentation/swiftui/view/onpencildoubletap(perform:)): Adds an action to perform after the user double-taps their Apple Pencil.
- [onPencilSqueeze(perform:)](/documentation/swiftui/view/onpencilsqueeze(perform:)): Adds an action to perform when the user squeezes their Apple Pencil.
- [preferredPencilDoubleTapAction](/documentation/swiftui/environmentvalues/preferredpencildoubletapaction): The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.
- [preferredPencilSqueezeAction](/documentation/swiftui/environmentvalues/preferredpencilsqueezeaction): The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.
- [PencilPreferredAction](/documentation/swiftui/pencilpreferredaction): An action that the user prefers to perform after double-tapping their Apple Pencil.
- [PencilDoubleTapGestureValue](/documentation/swiftui/pencildoubletapgesturevalue): Describes the value of an Apple Pencil double-tap gesture.
- [PencilSqueezeGestureValue](/documentation/swiftui/pencilsqueezegesturevalue): Describes the value of an Apple Pencil squeeze gesture.
- [PencilSqueezeGesturePhase](/documentation/swiftui/pencilsqueezegesturephase): Describes the phase and value of an Apple Pencil squeeze gesture.
