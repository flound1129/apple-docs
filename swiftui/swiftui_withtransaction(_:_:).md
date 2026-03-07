# withTransaction(_:_:)

Executes a closure with the specified transaction and returns the result.

```swift
func withTransaction<Result>(_ transaction: Transaction, _ body: () throws -> Result) rethrows -> Result
```

## Parameters

- **body**: A closure to execute.

## Return Value

The result of executing the closure with the specified transaction.

## See Also

### Moving an animation to another view

- [withTransaction(_:_:_:)](/documentation/swiftui/withtransaction(_:_:_:)): Executes a closure with the specified transaction key path and value and returns the result.
- [transaction(_:)](/documentation/swiftui/view/transaction(_:)): Applies the given transaction mutation function to all animations used within the view.
- [transaction(value:_:)](/documentation/swiftui/view/transaction(value:_:)): Applies the given transaction mutation function to all animations used within the view.
- [transaction(_:body:)](/documentation/swiftui/view/transaction(_:body:)): Applies the given transaction mutation function to all animations used within the `body` closure.
- [Transaction](/documentation/swiftui/transaction): The context of the current state-processing update.
- [Entry()](/documentation/swiftui/entry()): Creates an environment values, transaction, container values, or focused values entry.
- [TransactionKey](/documentation/swiftui/transactionkey): A key for accessing values in a transaction.
