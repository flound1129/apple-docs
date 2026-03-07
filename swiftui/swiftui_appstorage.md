# AppStorage

A property wrapper type that reflects a value from `UserDefaults` and invalidates a view on a change in value in that user default.

```swift
@frozen @propertyWrapper struct AppStorage<Value>
```

### Storing a value

- [init(wrappedValue:_:store:)](/documentation/swiftui/appstorage/init(wrappedvalue:_:store:)): Creates a property that can save and restore tab sidebar customizations.
- [init(_:store:)](/documentation/swiftui/appstorage/init(_:store:)): Creates a property that can read and write an Optional boolean user default.

### Getting the value

- [wrappedValue](/documentation/swiftui/appstorage/wrappedvalue)
- [projectedValue](/documentation/swiftui/appstorage/projectedvalue)

## See Also

### Saving state across app launches

- [Restoring your app’s state with SwiftUI](/documentation/swiftui/restoring-your-app-s-state-with-swiftui): Provide app continuity for users by preserving their current activities.
- [defaultAppStorage(_:)](/documentation/swiftui/view/defaultappstorage(_:)): The default store used by `AppStorage` contained within the view.
- [SceneStorage](/documentation/swiftui/scenestorage): A property wrapper type that reads and writes to persisted, per-scene storage.
