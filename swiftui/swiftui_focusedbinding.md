# FocusedBinding

A convenience property wrapper for observing and automatically unwrapping state bindings from the focused view or one of its ancestors.

```swift
@propertyWrapper struct FocusedBinding<Value>
```

## Overview

If multiple views publish bindings using the same key, the wrapped property will reflect the value of the binding from the view closest to focus.

### Creating the binding

- [init(_:)](/documentation/swiftui/focusedbinding/init(_:)): A new property wrapper for the given key path.

### Getting the value

- [projectedValue](/documentation/swiftui/focusedbinding/projectedvalue): A binding to the optional value.
- [wrappedValue](/documentation/swiftui/focusedbinding/wrappedvalue): The unwrapped value for the focus key given the current scope and state of the focused view hierarchy.

## See Also

### Managing focus state

- [focused(_:equals:)](/documentation/swiftui/view/focused(_:equals:)): Modifies this view by binding its focus state to the given state value.
- [focused(_:)](/documentation/swiftui/view/focused(_:)): Modifies this view by binding its focus state to the given Boolean state value.
- [isFocused](/documentation/swiftui/environmentvalues/isfocused): Returns whether the nearest focusable ancestor has focus.
- [FocusState](/documentation/swiftui/focusstate): A property wrapper type that can read and write a value that SwiftUI updates as the placement of focus within the scene changes.
- [FocusedValue](/documentation/swiftui/focusedvalue): A property wrapper for observing values from the focused view or one of its ancestors.
- [Entry()](/documentation/swiftui/entry()): Creates an environment values, transaction, container values, or focused values entry.
- [FocusedValueKey](/documentation/swiftui/focusedvaluekey): A protocol for identifier types used when publishing and observing focused values.
- [searchFocused(_:)](/documentation/swiftui/view/searchfocused(_:)): Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [searchFocused(_:equals:)](/documentation/swiftui/view/searchfocused(_:equals:)): Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.
