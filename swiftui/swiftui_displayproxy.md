# DisplayProxy

A type which provides information about display hardware.

```swift
struct DisplayProxy
```

## Overview

You can use this type with your custom window layouts to size and position windows relative to a display’s bounds.

For example, your custom window layout can position a window 140 points from the bottom of the screen’s visible area:

```swift
Window("Status", id: "status") {
    StatusView()
}
.windowResizability(.contentSize)
.defaultWindowPlacement { content, context in
    let displayBounds = context.defaultDisplay.visibleRect
    let size = content.sizeThatFits(.unspecified)
    let position = CGPoint(
        x: displayBounds.midX - (size.width / 2),
        y: displayBounds.maxY - size.height - 140)
    return WindowPlacement(position: position, size: size)
}
```

### Instance Properties

- [bounds](/documentation/swiftui/displayproxy/bounds): The full dimensions of the display, including any space occupied by system interface elements.
- [safeAreaInsets](/documentation/swiftui/displayproxy/safeareainsets): The safe area inset of this display.
- [visibleRect](/documentation/swiftui/displayproxy/visiblerect): The portion of the display where it is safe to place windows.

## See Also

### Positioning a window

- [defaultPosition(_:)](/documentation/swiftui/scene/defaultposition(_:)): Sets a default position for a window.
- [WindowLevel](/documentation/swiftui/windowlevel): The level of a window.
- [windowLevel(_:)](/documentation/swiftui/scene/windowlevel(_:)): Sets the window level of this scene.
- [WindowLayoutRoot](/documentation/swiftui/windowlayoutroot): A proxy which represents the root contents of a window.
- [WindowPlacement](/documentation/swiftui/windowplacement): A type which represents a preferred size and position for a window.
- [defaultWindowPlacement(_:)](/documentation/swiftui/scene/defaultwindowplacement(_:)): Defines a function used for determining the default placement of windows.
- [windowIdealPlacement(_:)](/documentation/swiftui/scene/windowidealplacement(_:)): Provides a function which determines a placement to use when windows of a scene zoom.
- [WindowPlacementContext](/documentation/swiftui/windowplacementcontext): A type which represents contextual information used for sizing and positioning windows.
- [WindowProxy](/documentation/swiftui/windowproxy): The proxy for an open window in the app.
