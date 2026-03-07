# FileDialogBrowserOptions

The way that file dialogs present the file system.

```swift
struct FileDialogBrowserOptions
```

## Overview

Apply the options using the [fileDialogBrowserOptions(_:)](/documentation/swiftui/view/filedialogbrowseroptions(_:)) modifier.

### Getting browser options

- [displayFileExtensions](/documentation/swiftui/filedialogbrowseroptions/displayfileextensions): On iOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to show or hide file extensions. Default behavior is to hide them. On macOS, this option has no effect.
- [enumeratePackages](/documentation/swiftui/filedialogbrowseroptions/enumeratepackages): Allows enumerating packages contents in contrast to the default behavior when packages are represented flatly, similar to files.
- [includeHiddenFiles](/documentation/swiftui/filedialogbrowseroptions/includehiddenfiles): Displays the files that are hidden by default.

## See Also

### Configuring a file dialog

- [fileDialogBrowserOptions(_:)](/documentation/swiftui/view/filedialogbrowseroptions(_:)): On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to provide a refined URL search experience: include or exclude hidden files, allow searching by tag, etc.
- [fileDialogConfirmationLabel(_:)](/documentation/swiftui/view/filedialogconfirmationlabel(_:)): On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [fileDialogCustomizationID(_:)](/documentation/swiftui/view/filedialogcustomizationid(_:)): On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to persist and restore the file dialog configuration.
- [fileDialogDefaultDirectory(_:)](/documentation/swiftui/view/filedialogdefaultdirectory(_:)): Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the specified default directory.
- [fileDialogImportsUnresolvedAliases(_:)](/documentation/swiftui/view/filedialogimportsunresolvedaliases(_:)): On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` behavior when a user chooses an alias.
- [fileDialogMessage(_:)](/documentation/swiftui/view/filedialogmessage(_:)): On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom text that is presented to the user, similar to a title.
- [fileDialogURLEnabled(_:)](/documentation/swiftui/view/filedialogurlenabled(_:)): On macOS, configures the `fileImporter` or `fileMover` to conditionally disable presented URLs.
