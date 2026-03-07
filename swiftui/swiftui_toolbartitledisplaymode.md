# ToolbarTitleDisplayMode

A type that defines the behavior of title of a toolbar.

```swift
struct ToolbarTitleDisplayMode
```

## Overview

Use the [toolbarTitleDisplayMode(_:)](/documentation/swiftui/view/toolbartitledisplaymode(_:)) modifier to configure the title display behavior of your toolbar:

```swift
NavigationStack {
    ContentView()
        .toolbarTitleDisplayMode(.inlineLarge)
}
```

### Getting display modes

- [automatic](/documentation/swiftui/toolbartitledisplaymode/automatic): The automatic mode.
- [inline](/documentation/swiftui/toolbartitledisplaymode/inline): The inline mode.
- [inlineLarge](/documentation/swiftui/toolbartitledisplaymode/inlinelarge): The inline large mode.
- [large](/documentation/swiftui/toolbartitledisplaymode/large): The large mode.

## See Also

### Configuring the toolbar title display mode

- [toolbarTitleDisplayMode(_:)](/documentation/swiftui/view/toolbartitledisplaymode(_:)): Configures the toolbar title display mode for this view.
