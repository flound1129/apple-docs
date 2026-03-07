# withTransaction(_:_:_:)

Executes a closure with the specified transaction key path and value and returns the result.

```swift
func withTransaction<R, V>(_ keyPath: WritableKeyPath<Transaction, V>, _ value: V, _ body: () throws -> R) rethrows -> R
```

## Parameters

- **keyPath**: A key path that indicates the property of the [Transaction](/documentation/swiftui/transaction) structure to update.
- **value**: The new value to set for the item specified by `keyPath`.
- **body**: A closure to execute.

## Return Value

The result of executing the closure with the specified transaction value.

## See Also

### Moving an animation to another view

- [withTransaction(_:_:)](/documentation/swiftui/withtransaction(_:_:)): Executes a closure with the specified transaction and returns the result.
- [transaction(_:)](/documentation/swiftui/view/transaction(_:)): Applies the given transaction mutation function to all animations used within the view.
- [transaction(value:_:)](/documentation/swiftui/view/transaction(value:_:)): Applies the given transaction mutation function to all animations used within the view.
- [transaction(_:body:)](/documentation/swiftui/view/transaction(_:body:)): Applies the given transaction mutation function to all animations used within the `body` closure.
- [Transaction](/documentation/swiftui/transaction): The context of the current state-processing update.
- [Entry()](/documentation/swiftui/entry()): Creates an environment values, transaction, container values, or focused values entry.
- [TransactionKey](/documentation/swiftui/transactionkey): A key for accessing values in a transaction.
