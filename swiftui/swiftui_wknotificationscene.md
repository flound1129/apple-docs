# WKNotificationScene

A scene which appears in response to receiving the specified category of remote or local notifications.

```swift
struct WKNotificationScene<Content, Controller> where Content : View, Controller : WKUserNotificationHostingController<Content>
```

### Creating a notification scene

- [init(controller:category:)](/documentation/swiftui/wknotificationscene/init(controller:category:)): Creates a scene that appears in response to receiving a specific category of remote or local notifications.
