# PencilSqueezeGesturePhase

Describes the phase and value of an Apple Pencil squeeze gesture.

```swift
@frozen enum PencilSqueezeGesturePhase
```

## Overview

When you use the [onPencilSqueeze(perform:)](/documentation/swiftui/view/onpencilsqueeze(perform:)) view modifier, you can handle the Apple Pencil squeeze gesture’s phase in the `action` closure.

### Enumeration Cases

- [PencilSqueezeGesturePhase.active(_:)](/documentation/swiftui/pencilsqueezegesturephase/active(_:)): The user started squeezing their Apple Pencil.
- [PencilSqueezeGesturePhase.ended(_:)](/documentation/swiftui/pencilsqueezegesturephase/ended(_:)): The user successfully completed a squeeze gesture.
- [PencilSqueezeGesturePhase.failed](/documentation/swiftui/pencilsqueezegesturephase/failed): The user started squeezing their Apple Pencil but failed to successfully complete the gesture.

## See Also

### Recognizing Apple Pencil gestures

- [onPencilDoubleTap(perform:)](/documentation/swiftui/view/onpencildoubletap(perform:)): Adds an action to perform after the user double-taps their Apple Pencil.
- [onPencilSqueeze(perform:)](/documentation/swiftui/view/onpencilsqueeze(perform:)): Adds an action to perform when the user squeezes their Apple Pencil.
- [preferredPencilDoubleTapAction](/documentation/swiftui/environmentvalues/preferredpencildoubletapaction): The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.
- [preferredPencilSqueezeAction](/documentation/swiftui/environmentvalues/preferredpencilsqueezeaction): The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.
- [PencilPreferredAction](/documentation/swiftui/pencilpreferredaction): An action that the user prefers to perform after double-tapping their Apple Pencil.
- [PencilDoubleTapGestureValue](/documentation/swiftui/pencildoubletapgesturevalue): Describes the value of an Apple Pencil double-tap gesture.
- [PencilSqueezeGestureValue](/documentation/swiftui/pencilsqueezegesturevalue): Describes the value of an Apple Pencil squeeze gesture.
- [PencilHoverPose](/documentation/swiftui/pencilhoverpose): A value describing the location and distance of an Apple Pencil hovering in the area above a view’s bounds.
