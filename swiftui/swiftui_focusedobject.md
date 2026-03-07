# FocusedObject

A property wrapper type for an observable object supplied by the focused view or one of its ancestors.

```swift
@MainActor @frozen @propertyWrapper @preconcurrency struct FocusedObject<ObjectType> where ObjectType : ObservableObject
```

## Overview

Focused objects invalidate the current view whenever the observable object changes. If multiple views publish a focused object using the same key, the wrapped property will reflect the object that’s closest to the focused view.

### Creating the focused object

- [init()](/documentation/swiftui/focusedobject/init()): Creates a focused object.

### Getting the value

- [projectedValue](/documentation/swiftui/focusedobject/projectedvalue): A projection of the focused object that creates bindings to its properties using dynamic member lookup.
- [wrappedValue](/documentation/swiftui/focusedobject/wrappedvalue): The underlying value referenced by the focused object.
- [FocusedObject.Wrapper](/documentation/swiftui/focusedobject/wrapper): A wrapper around the underlying focused object that can create bindings to its properties using dynamic member lookup.

## See Also

### Exposing reference types to focused views

- [focusedObject(_:)](/documentation/swiftui/view/focusedobject(_:)): Creates a new view that exposes the provided object to other views whose whose state depends on the focused view hierarchy.
- [focusedSceneObject(_:)](/documentation/swiftui/view/focusedsceneobject(_:)): Creates a new view that exposes the provided object to other views whose whose state depends on the active scene.
