# FocusedValueKey

A protocol for identifier types used when publishing and observing focused values.

```swift
protocol FocusedValueKey
```

## Overview

Unlike [EnvironmentKey](/documentation/swiftui/environmentkey), `FocusedValueKey` has no default value requirement, because the default value for a key is always `nil`.

Use the `Entry` macro to create custom focused values by extending `FocusedValues` with new properties:

```swift
extension FocusedValues {
    @Entry var selectedItem: Item?
}
```

Alternatively it is possible to create a focused value key by manually creating a type that conforms to this protocol:

```swift
struct SelectedItemKey: FocusedValueKey {
    typealias Value = Item
}
```

Then extend [FocusedValues](/documentation/swiftui/focusedvalues) to add a computed property for your key:

```swift
extension FocusedValues {
    var selectedItem: Item? {
        get { self[SelectedItemKey.self] }
        set { self[SelectedItemKey.self] = newValue }
    }
}
```

### Specifying the value type

- [Value](/documentation/swiftui/focusedvaluekey/value)

## See Also

### Managing focus state

- [focused(_:equals:)](/documentation/swiftui/view/focused(_:equals:)): Modifies this view by binding its focus state to the given state value.
- [focused(_:)](/documentation/swiftui/view/focused(_:)): Modifies this view by binding its focus state to the given Boolean state value.
- [isFocused](/documentation/swiftui/environmentvalues/isfocused): Returns whether the nearest focusable ancestor has focus.
- [FocusState](/documentation/swiftui/focusstate): A property wrapper type that can read and write a value that SwiftUI updates as the placement of focus within the scene changes.
- [FocusedValue](/documentation/swiftui/focusedvalue): A property wrapper for observing values from the focused view or one of its ancestors.
- [Entry()](/documentation/swiftui/entry()): Creates an environment values, transaction, container values, or focused values entry.
- [FocusedBinding](/documentation/swiftui/focusedbinding): A convenience property wrapper for observing and automatically unwrapping state bindings from the focused view or one of its ancestors.
- [searchFocused(_:)](/documentation/swiftui/view/searchfocused(_:)): Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [searchFocused(_:equals:)](/documentation/swiftui/view/searchfocused(_:equals:)): Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.
