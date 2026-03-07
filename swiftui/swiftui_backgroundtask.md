# BackgroundTask

The kinds of background tasks that your app or extension can handle.

```swift
struct BackgroundTask<Request, Response>
```

## Overview

Use a value of this type with the [backgroundTask(_:action:)](/documentation/swiftui/scene/backgroundtask(_:action:)) scene modifier to create a handler for background tasks that the system sends to your app or extension. For example, you can use [urlSession](/documentation/swiftui/backgroundtask/urlsession) to define an asynchronous closure that the system calls when it launches your app or extension to handle a response from a background [URLSession](/documentation/Foundation/URLSession).

### Refreshing the app

- [appRefresh](/documentation/swiftui/backgroundtask/apprefresh): A task that updates your app’s state in the background.
- [appRefresh(_:)](/documentation/swiftui/backgroundtask/apprefresh(_:)): A task that updates your app’s state in the background for a matching identifier.

### Preparing for a snapshot

- [snapshot](/documentation/swiftui/backgroundtask/snapshot): A background task used to update your app’s user interface in preparation for a snapshot.

### Receiving connectivity updates

- [bluetoothAlert](/documentation/swiftui/backgroundtask/bluetoothalert): A background task used to receive critical alerts from paired bluetooth accessories.
- [watchConnectivity](/documentation/swiftui/backgroundtask/watchconnectivity): A background task used to receive background updates from the Watch Connectivity framework.

### Responding to URL sessions

- [urlSession](/documentation/swiftui/backgroundtask/urlsession): A task that responds to background URL sessions.
- [urlSession(_:)](/documentation/swiftui/backgroundtask/urlsession(_:)): A task that responds to background URL sessions matching the given identifier.
- [urlSession(matching:)](/documentation/swiftui/backgroundtask/urlsession(matching:)): A task that responds to background URL sessions matching the given predicate.

### Updating intents and shortcuts

- [intentDidRun](/documentation/swiftui/backgroundtask/intentdidrun): A background task used to update your app after a SiriKit intent runs.
- [relevantShortcut](/documentation/swiftui/backgroundtask/relevantshortcut): A background task used to periodically donate relevant Siri shortcuts.

## See Also

### Handling background tasks

- [backgroundTask(_:action:)](/documentation/swiftui/scene/backgroundtask(_:action:)): Runs the specified action when the system provides a background task.
- [SnapshotData](/documentation/swiftui/snapshotdata): The associated data of a snapshot background task.
- [SnapshotResponse](/documentation/swiftui/snapshotresponse): Your application’s response to a snapshot background task.
