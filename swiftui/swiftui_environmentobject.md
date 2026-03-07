# EnvironmentObject

A property wrapper type for an observable object that a parent or ancestor view supplies.

```swift
@MainActor @frozen @propertyWrapper @preconcurrency struct EnvironmentObject<ObjectType> where ObjectType : ObservableObject
```

## Overview

An environment object invalidates the current view whenever the observable object that conforms to [ObservableObject](/documentation/Combine/ObservableObject) changes. If you declare a property as an environment object, be sure to set a corresponding model object on an ancestor view by calling its [environmentObject(_:)](/documentation/swiftui/view/environmentobject(_:)) modifier.

> **Note:**
> If your observable object conforms to the [Observable](/documentation/Observation/Observable) protocol, use [Environment](/documentation/swiftui/environment) instead of `EnvironmentObject` and set the model object in an ancestor view by calling its [environment(_:)](/documentation/swiftui/view/environment(_:)) or [environment(_:_:)](/documentation/swiftui/view/environment(_:_:)) modifiers.
>

### Creating an environment object

- [init()](/documentation/swiftui/environmentobject/init()): Creates an environment object.

### Getting the value

- [wrappedValue](/documentation/swiftui/environmentobject/wrappedvalue): The underlying value referenced by the environment object.
- [projectedValue](/documentation/swiftui/environmentobject/projectedvalue): A projection of the environment object that creates bindings to its properties using dynamic member lookup.
- [EnvironmentObject.Wrapper](/documentation/swiftui/environmentobject/wrapper): A wrapper of the underlying environment object that can create bindings to its properties using dynamic member lookup.

## See Also

### Distributing model data throughout your app

- [environmentObject(_:)](/documentation/swiftui/view/environmentobject(_:)): Supplies an observable object to a view’s hierarchy.
- [environmentObject(_:)](/documentation/swiftui/scene/environmentobject(_:)): Supplies an `ObservableObject` to a view subhierarchy.
