# Transaction

The context of the current state-processing update.

```swift
@frozen struct Transaction
```

## Overview

Use a transaction to pass an animation between views in a view hierarchy.

The root transaction for a state change comes from the binding that changed, plus any global values set by calling [withTransaction(_:_:)](/documentation/swiftui/withtransaction(_:_:)) or [withAnimation(_:_:)](/documentation/swiftui/withanimation(_:_:)).

### Creating a transaction

- [init()](/documentation/swiftui/transaction/init()): Creates a transaction.
- [init(animation:)](/documentation/swiftui/transaction/init(animation:)): Creates a transaction and assigns its animation property.

### Managing animations

- [animation](/documentation/swiftui/transaction/animation): The animation, if any, associated with the current state change.
- [disablesAnimations](/documentation/swiftui/transaction/disablesanimations): A Boolean value that indicates whether views should disable animations.
- [addAnimationCompletion(criteria:_:)](/documentation/swiftui/transaction/addanimationcompletion(criteria:_:)): Adds a completion to run when the animations created with this transaction are all complete.

### Managing window dismissal

- [dismissBehavior](/documentation/swiftui/transaction/dismissbehavior): The behavior for how windows will dismiss programmatically when used in conjunction with [DismissWindowAction](/documentation/swiftui/dismisswindowaction).

### Getting information about a transaction

- [isContinuous](/documentation/swiftui/transaction/iscontinuous): A Boolean value that indicates whether the transaction originated from an action that produces a sequence of values.
- [scrollTargetAnchor](/documentation/swiftui/transaction/scrolltargetanchor): The preferred alignment of the view within a scroll view’s visible region when scrolling to a view.
- [tracksVelocity](/documentation/swiftui/transaction/tracksvelocity): Whether this transaction will track the velocity of any animatable properties that change.
- [subscript(_:)](/documentation/swiftui/transaction/subscript(_:)): Accesses the transaction value associated with a custom key.

### Instance Properties

- [scrollContentOffsetAdjustmentBehavior](/documentation/swiftui/transaction/scrollcontentoffsetadjustmentbehavior): The behavior a scroll view will have regarding content offset adjustments for the current transaction.
- [scrollPositionUpdatePreservesVelocity](/documentation/swiftui/transaction/scrollpositionupdatepreservesvelocity): Whether a programmatic update to the scroll position of a scroll view preserves the current velocity of any active scroll of the scroll view.

## See Also

### Moving an animation to another view

- [withTransaction(_:_:)](/documentation/swiftui/withtransaction(_:_:)): Executes a closure with the specified transaction and returns the result.
- [withTransaction(_:_:_:)](/documentation/swiftui/withtransaction(_:_:_:)): Executes a closure with the specified transaction key path and value and returns the result.
- [transaction(_:)](/documentation/swiftui/view/transaction(_:)): Applies the given transaction mutation function to all animations used within the view.
- [transaction(value:_:)](/documentation/swiftui/view/transaction(value:_:)): Applies the given transaction mutation function to all animations used within the view.
- [transaction(_:body:)](/documentation/swiftui/view/transaction(_:body:)): Applies the given transaction mutation function to all animations used within the `body` closure.
- [Entry()](/documentation/swiftui/entry()): Creates an environment values, transaction, container values, or focused values entry.
- [TransactionKey](/documentation/swiftui/transactionkey): A key for accessing values in a transaction.
