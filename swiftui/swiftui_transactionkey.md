# TransactionKey

A key for accessing values in a transaction.

```swift
protocol TransactionKey
```

## Overview

You can create custom transaction values by extending the [Transaction](/documentation/swiftui/transaction) structure with new properties. First declare a new transaction key type and specify a value for the required [defaultValue](/documentation/swiftui/transactionkey/defaultvalue) property:

```swift
private struct MyTransactionKey: TransactionKey {
    static let defaultValue = false
}
```

The Swift compiler automatically infers the associated [Value](/documentation/swiftui/transactionkey/value) type as the type you specify for the default value. Then use the key to define a new transaction value property:

```swift
extension Transaction {
    var myCustomValue: Bool {
        get { self[MyTransactionKey.self] }
        set { self[MyTransactionKey.self] = newValue }
    }
}
```

Clients of your transaction value never use the key directly. Instead, they use the key path of your custom transaction value property. To set the transaction value for a change, wrap that change in a call to `withTransaction`:

```swift
withTransaction(\.myCustomValue, true) {
    isActive.toggle()
}
```

To use the value from inside `MyView` or one of its descendants, use the [transaction(_:)](/documentation/swiftui/view/transaction(_:)) view modifier:

```swift
MyView()
    .transaction { transaction in
        if transaction.myCustomValue {
            transaction.animation = .default.repeatCount(3)
        }
    }
```

### Setting a default value

- [defaultValue](/documentation/swiftui/transactionkey/defaultvalue): The default value for the transaction key.
- [Value](/documentation/swiftui/transactionkey/value): The associated type representing the type of the transaction key’s value.

## See Also

### Moving an animation to another view

- [withTransaction(_:_:)](/documentation/swiftui/withtransaction(_:_:)): Executes a closure with the specified transaction and returns the result.
- [withTransaction(_:_:_:)](/documentation/swiftui/withtransaction(_:_:_:)): Executes a closure with the specified transaction key path and value and returns the result.
- [transaction(_:)](/documentation/swiftui/view/transaction(_:)): Applies the given transaction mutation function to all animations used within the view.
- [transaction(value:_:)](/documentation/swiftui/view/transaction(value:_:)): Applies the given transaction mutation function to all animations used within the view.
- [transaction(_:body:)](/documentation/swiftui/view/transaction(_:body:)): Applies the given transaction mutation function to all animations used within the `body` closure.
- [Transaction](/documentation/swiftui/transaction): The context of the current state-processing update.
- [Entry()](/documentation/swiftui/entry()): Creates an environment values, transaction, container values, or focused values entry.
