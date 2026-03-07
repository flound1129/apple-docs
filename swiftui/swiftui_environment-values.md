# Environment values

Share data throughout a view hierarchy using the environment.

## Overview

Views in SwiftUI can react to configuration information that they read from the environment using an [Environment](/documentation/swiftui/environment) property wrapper.

![None]

A view inherits its environment from its container view, subject to explicit changes from an [environment(_:_:)](/documentation/swiftui/view/environment(_:_:)) view modifier, or by implicit changes from one of the many modifiers that operate on environment values. As a result, you can configure a entire hierarchy of views by modifying the environment of the group’s container.

You can find many built-in environment values in the [EnvironmentValues](/documentation/swiftui/environmentvalues) structure. You can also create a custom [EnvironmentValues](/documentation/swiftui/environmentvalues) property by defining a new property in an extension to the environment values structure and applying the [Entry()](/documentation/swiftui/entry()) macro to the variable declaration.

### Accessing environment values

- [Environment](/documentation/swiftui/environment): A property wrapper that reads a value from a view’s environment.
- [EnvironmentValues](/documentation/swiftui/environmentvalues): A collection of environment values propagated through a view hierarchy.

### Creating custom environment values

- [Entry()](/documentation/swiftui/entry()): Creates an environment values, transaction, container values, or focused values entry.
- [EnvironmentKey](/documentation/swiftui/environmentkey): A key for accessing values in the environment.

### Modifying the environment of a view

- [environment(_:)](/documentation/swiftui/view/environment(_:)): Places an observable object in the view’s environment.
- [environment(_:_:)](/documentation/swiftui/view/environment(_:_:)): Sets the environment value of the specified key path to the given value.
- [transformEnvironment(_:transform:)](/documentation/swiftui/view/transformenvironment(_:transform:)): Transforms the environment value of the specified key path with the given function.

### Modifying the environment of a scene

- [environment(_:)](/documentation/swiftui/scene/environment(_:)): Places an observable object in the scene’s environment.
- [environment(_:_:)](/documentation/swiftui/scene/environment(_:_:)): Sets the environment value of the specified key path to the given value.
- [transformEnvironment(_:transform:)](/documentation/swiftui/scene/transformenvironment(_:transform:)): Transforms the environment value of the specified key path with the given function.

## See Also

### Data and storage

- [Model data](/documentation/swiftui/model-data): Manage the data that your app uses to drive its interface.
- [Preferences](/documentation/swiftui/preferences): Indicate configuration preferences from views to their container views.
- [Persistent storage](/documentation/swiftui/persistent-storage): Store data for use across sessions of your app.
