# Toolbars

Provide immediate access to frequently used commands and controls.

## Overview

The system might present toolbars above or below your app’s content, depending on the platform and the context.

![None]

Add items to a toolbar by applying the [toolbar(content:)](/documentation/swiftui/view/toolbar(content:)) view modifier to a view in your app. You can also configure the toolbar using view modifiers. For example, you can set the visibility of a toolbar with the [toolbar(_:for:)](/documentation/swiftui/view/toolbar(_:for:)) modifier.

For design guidance, see [Toolbars](/design/Human-Interface-Guidelines/toolbars) in the Human Interface Guidelines.

### Populating a toolbar

- [toolbar(content:)](/documentation/swiftui/view/toolbar(content:)): Populates the toolbar or navigation bar with the specified items.
- [ToolbarItem](/documentation/swiftui/toolbaritem): A model that represents an item which can be placed in the toolbar or navigation bar.
- [ToolbarItemGroup](/documentation/swiftui/toolbaritemgroup): A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [ToolbarItemPlacement](/documentation/swiftui/toolbaritemplacement): A structure that defines the placement of a toolbar item.
- [ToolbarContent](/documentation/swiftui/toolbarcontent): Conforming types represent items that can be placed in various locations in a toolbar.
- [ToolbarContentBuilder](/documentation/swiftui/toolbarcontentbuilder): Constructs a toolbar item set from multi-expression closures.
- [ToolbarSpacer](/documentation/swiftui/toolbarspacer): A standard space item in toolbars.
- [DefaultToolbarItem](/documentation/swiftui/defaulttoolbaritem): A toolbar item that represents a system component.

### Populating a customizable toolbar

- [toolbar(id:content:)](/documentation/swiftui/view/toolbar(id:content:)): Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [CustomizableToolbarContent](/documentation/swiftui/customizabletoolbarcontent): Conforming types represent items that can be placed in various locations in a customizable toolbar.
- [ToolbarCustomizationBehavior](/documentation/swiftui/toolbarcustomizationbehavior): The customization behavior of customizable toolbar content.
- [ToolbarCustomizationOptions](/documentation/swiftui/toolbarcustomizationoptions): Options that influence the default customization behavior of customizable toolbar content.
- [SearchToolbarBehavior](/documentation/swiftui/searchtoolbarbehavior): The behavior of a search field in a toolbar.

### Removing default items

- [toolbar(removing:)](/documentation/swiftui/view/toolbar(removing:)): Remove a toolbar item present by default
- [ToolbarDefaultItemKind](/documentation/swiftui/toolbardefaultitemkind): A kind of toolbar item a `View` adds by default.

### Setting toolbar visibility

- [toolbar(_:for:)](/documentation/swiftui/view/toolbar(_:for:)): Specifies the visibility of a bar managed by SwiftUI.
- [toolbarVisibility(_:for:)](/documentation/swiftui/view/toolbarvisibility(_:for:)): Specifies the visibility of a bar managed by SwiftUI.
- [toolbarBackgroundVisibility(_:for:)](/documentation/swiftui/view/toolbarbackgroundvisibility(_:for:)): Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [ToolbarPlacement](/documentation/swiftui/toolbarplacement): The placement of a toolbar.
- [ContentToolbarPlacement](/documentation/swiftui/contenttoolbarplacement)

### Specifying the role of toolbar content

- [toolbarRole(_:)](/documentation/swiftui/view/toolbarrole(_:)): Configures the semantic role for the content populating the toolbar.
- [ToolbarRole](/documentation/swiftui/toolbarrole): The purpose of content that populates the toolbar.

### Styling a toolbar

- [toolbarBackground(_:for:)](/documentation/swiftui/view/toolbarbackground(_:for:)): Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [toolbarColorScheme(_:for:)](/documentation/swiftui/view/toolbarcolorscheme(_:for:)): Specifies the preferred color scheme of a bar managed by SwiftUI.
- [toolbarForegroundStyle(_:for:)](/documentation/swiftui/view/toolbarforegroundstyle(_:for:)): Specifies the preferred foreground style of bars managed by SwiftUI.
- [windowToolbarStyle(_:)](/documentation/swiftui/scene/windowtoolbarstyle(_:)): Sets the style for the toolbar defined within this scene.
- [WindowToolbarStyle](/documentation/swiftui/windowtoolbarstyle): A specification for the appearance and behavior of a window’s toolbar.
- [toolbarLabelStyle](/documentation/swiftui/environmentvalues/toolbarlabelstyle): The label style to apply to controls within a toolbar.
- [ToolbarLabelStyle](/documentation/swiftui/toolbarlabelstyle): The label style of a toolbar.
- [SpacerSizing](/documentation/swiftui/spacersizing): A type which defines how spacers should size themselves.

### Configuring the toolbar title display mode

- [toolbarTitleDisplayMode(_:)](/documentation/swiftui/view/toolbartitledisplaymode(_:)): Configures the toolbar title display mode for this view.
- [ToolbarTitleDisplayMode](/documentation/swiftui/toolbartitledisplaymode): A type that defines the behavior of title of a toolbar.

### Setting the toolbar title menu

- [toolbarTitleMenu(content:)](/documentation/swiftui/view/toolbartitlemenu(content:)): Configure the title menu of a toolbar.
- [ToolbarTitleMenu](/documentation/swiftui/toolbartitlemenu): The title menu of a toolbar.

### Creating an ornament

- [ornament(visibility:attachmentAnchor:contentAlignment:ornament:)](/documentation/swiftui/view/ornament(visibility:attachmentanchor:contentalignment:ornament:)): Presents an ornament.
- [OrnamentAttachmentAnchor](/documentation/swiftui/ornamentattachmentanchor): An attachment anchor for an ornament.

## See Also

### App structure

- [App organization](/documentation/swiftui/app-organization): Define the entry point and top-level structure of your app.
- [Scenes](/documentation/swiftui/scenes): Declare the user interface groupings that make up the parts of your app.
- [Windows](/documentation/swiftui/windows): Display user interface content in a window or a collection of windows.
- [Immersive spaces](/documentation/swiftui/immersive-spaces): Display unbounded content in a person’s surroundings.
- [Documents](/documentation/swiftui/documents): Enable people to open and manage documents.
- [Navigation](/documentation/swiftui/navigation): Enable people to move between different parts of your app’s view hierarchy within a scene.
- [Modal presentations](/documentation/swiftui/modal-presentations): Present content in a separate view that offers focused interaction.
- [Search](/documentation/swiftui/search): Enable people to search for text or other content within your app.
- [App extensions](/documentation/swiftui/app-extensions): Extend your app’s basic functionality to other parts of the system, like by adding a Widget.
