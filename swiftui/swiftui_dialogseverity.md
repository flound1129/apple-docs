# DialogSeverity

The severity of an alert or confirmation dialog.

```swift
struct DialogSeverity
```

## Overview

You can use dialog severity to indicate that people need to take extra care when interacting with the dialog, like when an action taken from the dialog permanently deletes data.

### Getting severities

- [automatic](/documentation/swiftui/dialogseverity/automatic): The default dialog severity. Alerts that present an error will use `.critical` and all others will use `.standard`.
- [standard](/documentation/swiftui/dialogseverity/standard): A severity that indicates the dialog is being displayed for the purpose of presenting information to the user.
- [critical](/documentation/swiftui/dialogseverity/critical): A severity that indicates extra attention should be given to the dialog, for example when unexpected data loss may occur as a result of the action taken.
