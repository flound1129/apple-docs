# FocusedValue

A property wrapper for observing values from the focused view or one of its ancestors.

```swift
@propertyWrapper struct FocusedValue<Value>
```

## Overview

If multiple views publish values using the same key, the wrapped property will reflect the value from the view closest to focus.

### Creating the value

- [init(_:)](/documentation/swiftui/focusedvalue/init(_:)): A new property wrapper for the given key path.

### Getting the value

- [wrappedValue](/documentation/swiftui/focusedvalue/wrappedvalue): The value for the focus key given the current scope and state of the focused view hierarchy.

## See Also

### Managing focus state

- [focused(_:equals:)](/documentation/swiftui/view/focused(_:equals:)): Modifies this view by binding its focus state to the given state value.
- [focused(_:)](/documentation/swiftui/view/focused(_:)): Modifies this view by binding its focus state to the given Boolean state value.
- [isFocused](/documentation/swiftui/environmentvalues/isfocused): Returns whether the nearest focusable ancestor has focus.
- [FocusState](/documentation/swiftui/focusstate): A property wrapper type that can read and write a value that SwiftUI updates as the placement of focus within the scene changes.
- [Entry()](/documentation/swiftui/entry()): Creates an environment values, transaction, container values, or focused values entry.
- [FocusedValueKey](/documentation/swiftui/focusedvaluekey): A protocol for identifier types used when publishing and observing focused values.
- [FocusedBinding](/documentation/swiftui/focusedbinding): A convenience property wrapper for observing and automatically unwrapping state bindings from the focused view or one of its ancestors.
- [searchFocused(_:)](/documentation/swiftui/view/searchfocused(_:)): Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [searchFocused(_:equals:)](/documentation/swiftui/view/searchfocused(_:equals:)): Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.
