# PencilPreferredAction

An action that the user prefers to perform after double-tapping their Apple Pencil.

```swift
struct PencilPreferredAction
```

### Getting the preffered actions

- [ignore](/documentation/swiftui/pencilpreferredaction/ignore): An action that does nothing.
- [showColorPalette](/documentation/swiftui/pencilpreferredaction/showcolorpalette): An action that toggles the display of the color palette.
- [showInkAttributes](/documentation/swiftui/pencilpreferredaction/showinkattributes): An action that toggles the display of the current tool’s ink attributes.
- [switchEraser](/documentation/swiftui/pencilpreferredaction/switcheraser): An action that switches between the current tool and the eraser.
- [switchPrevious](/documentation/swiftui/pencilpreferredaction/switchprevious): An action that switches between the current tool and the last used tool.

### Type Properties

- [runSystemShortcut](/documentation/swiftui/pencilpreferredaction/runsystemshortcut): An action that runs a system shortcut.
- [showContextualPalette](/documentation/swiftui/pencilpreferredaction/showcontextualpalette): An action that toggles the display of the contextual palette, or the undo/redo panel if contextual palette is not available.

## See Also

### Recognizing Apple Pencil gestures

- [onPencilDoubleTap(perform:)](/documentation/swiftui/view/onpencildoubletap(perform:)): Adds an action to perform after the user double-taps their Apple Pencil.
- [onPencilSqueeze(perform:)](/documentation/swiftui/view/onpencilsqueeze(perform:)): Adds an action to perform when the user squeezes their Apple Pencil.
- [preferredPencilDoubleTapAction](/documentation/swiftui/environmentvalues/preferredpencildoubletapaction): The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.
- [preferredPencilSqueezeAction](/documentation/swiftui/environmentvalues/preferredpencilsqueezeaction): The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.
- [PencilDoubleTapGestureValue](/documentation/swiftui/pencildoubletapgesturevalue): Describes the value of an Apple Pencil double-tap gesture.
- [PencilSqueezeGestureValue](/documentation/swiftui/pencilsqueezegesturevalue): Describes the value of an Apple Pencil squeeze gesture.
- [PencilSqueezeGesturePhase](/documentation/swiftui/pencilsqueezegesturephase): Describes the phase and value of an Apple Pencil squeeze gesture.
- [PencilHoverPose](/documentation/swiftui/pencilhoverpose): A value describing the location and distance of an Apple Pencil hovering in the area above a view’s bounds.
