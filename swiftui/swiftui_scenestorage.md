# SceneStorage

A property wrapper type that reads and writes to persisted, per-scene storage.

```swift
@frozen @propertyWrapper struct SceneStorage<Value>
```

## Overview

You use `SceneStorage` when you need automatic state restoration of the value.  `SceneStorage` works very similar to `State`, except its initial value is restored by the system if it was previously saved, and the value is shared with other `SceneStorage` variables in the same scene.

The system manages the saving and restoring of `SceneStorage` on your behalf. The underlying data that backs `SceneStorage` is not available to you, so you must access it via the `SceneStorage` property wrapper. The system makes no guarantees as to when and how often the data will be persisted.

Each `Scene` has its own notion of `SceneStorage`, so data is not shared between scenes.

Ensure that the data you use with `SceneStorage` is lightweight. Data of a large size, such as model data, should not be stored in `SceneStorage`, as poor performance may result.

If the `Scene` is explicitly destroyed (e.g. the switcher snapshot is destroyed on iPadOS or the window is closed on macOS), the data is also destroyed. Do not use `SceneStorage` with sensitive data.

### Storing a value

- [init(wrappedValue:_:)](/documentation/swiftui/scenestorage/init(wrappedvalue:_:)): Creates a property that can save and restore an integer, transforming it to a `RawRepresentable` data type.
- [init(_:)](/documentation/swiftui/scenestorage/init(_:)): Creates a property that can save and restore an Optional boolean.

### Getting the value

- [wrappedValue](/documentation/swiftui/scenestorage/wrappedvalue): The underlying value referenced by the state variable.
- [projectedValue](/documentation/swiftui/scenestorage/projectedvalue): A binding to the state value.

### Initializers

- [init(wrappedValue:_:store:)](/documentation/swiftui/scenestorage/init(wrappedvalue:_:store:)): Creates a property that can save and restore tab sidebar customizations.

## See Also

### Saving state across app launches

- [Restoring your app’s state with SwiftUI](/documentation/swiftui/restoring-your-app-s-state-with-swiftui): Provide app continuity for users by preserving their current activities.
- [defaultAppStorage(_:)](/documentation/swiftui/view/defaultappstorage(_:)): The default store used by `AppStorage` contained within the view.
- [AppStorage](/documentation/swiftui/appstorage): A property wrapper type that reflects a value from `UserDefaults` and invalidates a view on a change in value in that user default.
