# SpacerSizing

A type which defines how spacers should size themselves.

```swift
struct SpacerSizing
```

## Overview

Use this type in coordination with the [ToolbarSpacer](/documentation/swiftui/toolbarspacer) type to define if the spacer should be a flexible size, or a fixed size using system-defined sizing rules.

For example, the following adds a fixed-size toolbar spacer between the share and more buttons in the toolbar:

```swift
ContentView()
    .toolbar(id: "main-toolbar") {
        ToolbarItem(id: "tag") {
           TagButton()
        }
        ToolbarItem(id: "share") {
           ShareButton()
        }
        ToolbarSpacer(.fixed)
        ToolbarItem(id: "more") {
           MoreButton()
        }
    }
```

### Type Properties

- [fixed](/documentation/swiftui/spacersizing/fixed): The fixed spacer sizing behavior. The spacer will use a pre-defined size determined by the system and the context in which the spacer is used.
- [flexible](/documentation/swiftui/spacersizing/flexible): The flexible spacer sizing behavior. The spacer will expand to accommodate as much space as it is given in the current context.

## See Also

### Styling a toolbar

- [toolbarBackground(_:for:)](/documentation/swiftui/view/toolbarbackground(_:for:)): Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [toolbarColorScheme(_:for:)](/documentation/swiftui/view/toolbarcolorscheme(_:for:)): Specifies the preferred color scheme of a bar managed by SwiftUI.
- [toolbarForegroundStyle(_:for:)](/documentation/swiftui/view/toolbarforegroundstyle(_:for:)): Specifies the preferred foreground style of bars managed by SwiftUI.
- [windowToolbarStyle(_:)](/documentation/swiftui/scene/windowtoolbarstyle(_:)): Sets the style for the toolbar defined within this scene.
- [WindowToolbarStyle](/documentation/swiftui/windowtoolbarstyle): A specification for the appearance and behavior of a window’s toolbar.
- [toolbarLabelStyle](/documentation/swiftui/environmentvalues/toolbarlabelstyle): The label style to apply to controls within a toolbar.
- [ToolbarLabelStyle](/documentation/swiftui/toolbarlabelstyle): The label style of a toolbar.
