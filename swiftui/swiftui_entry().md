# Entry()

Creates an environment values, transaction, container values, or focused values entry.

```swift
@attached(accessor) @attached(peer, names: prefixed(__Key_)) macro Entry()
```

## Environment Values

Create [EnvironmentValues](/documentation/swiftui/environmentvalues) entries by extending the [EnvironmentValues](/documentation/swiftui/environmentvalues) structure with new properties and attaching the @Entry macro to the variable declarations:

```swift
extension EnvironmentValues {
    @Entry var myCustomValue: String = "Default value"
    @Entry var anotherCustomValue = true
}
```

## Transaction Values

Create [Transaction](/documentation/swiftui/transaction) entries by extending the [Transaction](/documentation/swiftui/transaction) structure with new properties and attaching the @Entry macro to the variable declarations:

```swift
extension Transaction {
    @Entry var myCustomValue: String = "Default value"
}
```

## Container Values

Create [ContainerValues](/documentation/swiftui/containervalues) entries by extending the [ContainerValues](/documentation/swiftui/containervalues) structure with new properties and attaching the @Entry macro to the variable declarations:

```swift
extension ContainerValues {
    @Entry var myCustomValue: String = "Default value"
}
```

## Focused Values

Since the default value for [FocusedValues](/documentation/swiftui/focusedvalues) is always `nil`, [FocusedValues](/documentation/swiftui/focusedvalues) entries cannot specify a different default value and must have an Optional type.

Create [FocusedValues](/documentation/swiftui/focusedvalues) entries by extending the [FocusedValues](/documentation/swiftui/focusedvalues) structure with new properties and attaching the @Entry macro to the variable declarations:

```swift
extension FocusedValues {
    @Entry var myCustomValue: String?
}
```

## See Also

### Moving an animation to another view

- [withTransaction(_:_:)](/documentation/swiftui/withtransaction(_:_:)): Executes a closure with the specified transaction and returns the result.
- [withTransaction(_:_:_:)](/documentation/swiftui/withtransaction(_:_:_:)): Executes a closure with the specified transaction key path and value and returns the result.
- [transaction(_:)](/documentation/swiftui/view/transaction(_:)): Applies the given transaction mutation function to all animations used within the view.
- [transaction(value:_:)](/documentation/swiftui/view/transaction(value:_:)): Applies the given transaction mutation function to all animations used within the view.
- [transaction(_:body:)](/documentation/swiftui/view/transaction(_:body:)): Applies the given transaction mutation function to all animations used within the `body` closure.
- [Transaction](/documentation/swiftui/transaction): The context of the current state-processing update.
- [TransactionKey](/documentation/swiftui/transactionkey): A key for accessing values in a transaction.
