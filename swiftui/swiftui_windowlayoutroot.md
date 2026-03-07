# WindowLayoutRoot

A proxy which represents the root contents of a window.

```swift
struct WindowLayoutRoot
```

## Overview

This type acts like a proxy for the contents of the window defined by a SwiftUI [Scene](/documentation/swiftui/scene). The `Scene.defaultWindowPlacement(_:)` modifier receives an instance of this type, representing the contents of the window being created.

Use this proxy to get information about the window’s contents, like it’s size.

### Instance Methods

- [sizeThatFits(_:)](/documentation/swiftui/windowlayoutroot/sizethatfits(_:)): Asks the window’s content for its size.

## See Also

### Positioning a window

- [defaultPosition(_:)](/documentation/swiftui/scene/defaultposition(_:)): Sets a default position for a window.
- [WindowLevel](/documentation/swiftui/windowlevel): The level of a window.
- [windowLevel(_:)](/documentation/swiftui/scene/windowlevel(_:)): Sets the window level of this scene.
- [WindowPlacement](/documentation/swiftui/windowplacement): A type which represents a preferred size and position for a window.
- [defaultWindowPlacement(_:)](/documentation/swiftui/scene/defaultwindowplacement(_:)): Defines a function used for determining the default placement of windows.
- [windowIdealPlacement(_:)](/documentation/swiftui/scene/windowidealplacement(_:)): Provides a function which determines a placement to use when windows of a scene zoom.
- [WindowPlacementContext](/documentation/swiftui/windowplacementcontext): A type which represents contextual information used for sizing and positioning windows.
- [WindowProxy](/documentation/swiftui/windowproxy): The proxy for an open window in the app.
- [DisplayProxy](/documentation/swiftui/displayproxy): A type which provides information about display hardware.
