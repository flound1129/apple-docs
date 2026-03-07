# CommandGroupPlacement

The standard locations that you can place new command groups relative to.

```swift
struct CommandGroupPlacement
```

## Overview

The names of these placements aren’t visible in the user interface, but the discussion for each placement lists the items that it includes.

### App interactions

- [appInfo](/documentation/swiftui/commandgroupplacement/appinfo): Placement for commands that provide information about the app, the terms of the user’s license agreement, and so on.
- [appSettings](/documentation/swiftui/commandgroupplacement/appsettings): Placement for commands that expose app settings and preferences.
- [appTermination](/documentation/swiftui/commandgroupplacement/apptermination): Placement for commands that result in app termination.
- [appVisibility](/documentation/swiftui/commandgroupplacement/appvisibility): Placement for commands that control the visibility of running apps.
- [systemServices](/documentation/swiftui/commandgroupplacement/systemservices): Placement for commands that expose services other apps provide.

### File manipulation

- [importExport](/documentation/swiftui/commandgroupplacement/importexport): Placement for commands that relate to importing and exporting data using formats that the app doesn’t natively support.
- [newItem](/documentation/swiftui/commandgroupplacement/newitem): Placement for commands that create different kinds of documents.
- [printItem](/documentation/swiftui/commandgroupplacement/printitem): Placement for commands related to printing app content.
- [saveItem](/documentation/swiftui/commandgroupplacement/saveitem): Placement for commands that save open documents and close windows.

### Content updates

- [pasteboard](/documentation/swiftui/commandgroupplacement/pasteboard): Placement for commands that interact with the Clipboard and manipulate content that is currently selected in the app’s view hierarchy.
- [textEditing](/documentation/swiftui/commandgroupplacement/textediting): Placement for commands that manipulate and transform text selections.
- [textFormatting](/documentation/swiftui/commandgroupplacement/textformatting): Placement for commands that manipulate and transform the styles applied to text selections.
- [undoRedo](/documentation/swiftui/commandgroupplacement/undoredo): Placement for commands that control the Undo Manager.

### Bars

- [sidebar](/documentation/swiftui/commandgroupplacement/sidebar): Placement for commands that control the app’s sidebar and full-screen modes.
- [toolbar](/documentation/swiftui/commandgroupplacement/toolbar): Placement for commands that manipulate the toolbar.

### Windows

- [singleWindowList](/documentation/swiftui/commandgroupplacement/singlewindowlist): Placement for commands that describe and reveal any windows that the app defines.
- [windowArrangement](/documentation/swiftui/commandgroupplacement/windowarrangement): Placement for commands that arrange all of an app’s windows.
- [windowList](/documentation/swiftui/commandgroupplacement/windowlist): Placement for commands that describe and reveal the app’s open windows.
- [windowSize](/documentation/swiftui/commandgroupplacement/windowsize): Placement for commands that control the size of the window.

### Help

- [help](/documentation/swiftui/commandgroupplacement/help): Placement for commands that present documentation and helpful information to people.

## See Also

### Defining commands

- [commands(content:)](/documentation/swiftui/scene/commands(content:)): Adds commands to the scene.
- [commandsRemoved()](/documentation/swiftui/scene/commandsremoved()): Removes all commands defined by the modified scene.
- [commandsReplaced(content:)](/documentation/swiftui/scene/commandsreplaced(content:)): Replaces all commands defined by the modified scene with the commands from the builder.
- [Commands](/documentation/swiftui/commands): Conforming types represent a group of related commands that can be exposed to the user via the main menu on macOS and key commands on iOS.
- [CommandMenu](/documentation/swiftui/commandmenu): Command menus are stand-alone, top-level containers for controls that perform related, app-specific commands.
- [CommandGroup](/documentation/swiftui/commandgroup): Groups of controls that you can add to existing command menus.
- [CommandsBuilder](/documentation/swiftui/commandsbuilder): Constructs command sets from multi-expression closures. Like `ViewBuilder`, it supports up to ten expressions in the closure body.
