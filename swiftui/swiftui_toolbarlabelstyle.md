# ToolbarLabelStyle

The label style of a toolbar.

```swift
struct ToolbarLabelStyle
```

## Overview

Use this type in conjunction with modifiers like [windowToolbarLabelStyle(fixed:)](/documentation/swiftui/scene/windowtoolbarlabelstyle(fixed:)) and [windowToolbarLabelStyle(_:)](/documentation/swiftui/scene/windowtoolbarlabelstyle(_:)) to customize the appearance of window toolbars managed by SwiftUI.

### Type Properties

- [automatic](/documentation/swiftui/toolbarlabelstyle/automatic): The automatic label style. The toolbar will use a labelStyle that best fits the `Scene` it is applied to.
- [iconOnly](/documentation/swiftui/toolbarlabelstyle/icononly): The icon only label style. The toolbar contents will only display the control
- [titleAndIcon](/documentation/swiftui/toolbarlabelstyle/titleandicon): The title and icon label style. The toolbar contents will display both a control and title
- [titleOnly](/documentation/swiftui/toolbarlabelstyle/titleonly): The title only label style. The toolbar contents will only display the title

## See Also

### Styling a toolbar

- [toolbarBackground(_:for:)](/documentation/swiftui/view/toolbarbackground(_:for:)): Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [toolbarColorScheme(_:for:)](/documentation/swiftui/view/toolbarcolorscheme(_:for:)): Specifies the preferred color scheme of a bar managed by SwiftUI.
- [toolbarForegroundStyle(_:for:)](/documentation/swiftui/view/toolbarforegroundstyle(_:for:)): Specifies the preferred foreground style of bars managed by SwiftUI.
- [windowToolbarStyle(_:)](/documentation/swiftui/scene/windowtoolbarstyle(_:)): Sets the style for the toolbar defined within this scene.
- [WindowToolbarStyle](/documentation/swiftui/windowtoolbarstyle): A specification for the appearance and behavior of a window’s toolbar.
- [toolbarLabelStyle](/documentation/swiftui/environmentvalues/toolbarlabelstyle): The label style to apply to controls within a toolbar.
- [SpacerSizing](/documentation/swiftui/spacersizing): A type which defines how spacers should size themselves.
