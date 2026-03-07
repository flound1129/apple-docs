# WindowPlacementContext

A type which represents contextual information used for sizing and positioning windows.

```swift
struct WindowPlacementContext
```

## Overview

The placement context provides information to be used when providing a new placement via the closure provided to the `defaultWindowPlacement(_:)` modifier.

### Instance Properties

- [defaultDisplay](/documentation/swiftui/windowplacementcontext/defaultdisplay): The display on which new windows will be presented by default.
- [windows](/documentation/swiftui/windowplacementcontext/windows): The list of current active scenes

## See Also

### Positioning a window

- [defaultPosition(_:)](/documentation/swiftui/scene/defaultposition(_:)): Sets a default position for a window.
- [WindowLevel](/documentation/swiftui/windowlevel): The level of a window.
- [windowLevel(_:)](/documentation/swiftui/scene/windowlevel(_:)): Sets the window level of this scene.
- [WindowLayoutRoot](/documentation/swiftui/windowlayoutroot): A proxy which represents the root contents of a window.
- [WindowPlacement](/documentation/swiftui/windowplacement): A type which represents a preferred size and position for a window.
- [defaultWindowPlacement(_:)](/documentation/swiftui/scene/defaultwindowplacement(_:)): Defines a function used for determining the default placement of windows.
- [windowIdealPlacement(_:)](/documentation/swiftui/scene/windowidealplacement(_:)): Provides a function which determines a placement to use when windows of a scene zoom.
- [WindowProxy](/documentation/swiftui/windowproxy): The proxy for an open window in the app.
- [DisplayProxy](/documentation/swiftui/displayproxy): A type which provides information about display hardware.
