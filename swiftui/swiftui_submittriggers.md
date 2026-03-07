# SubmitTriggers

A type that defines various triggers that result in the firing of a submission action.

```swift
struct SubmitTriggers
```

## Overview

These triggers may be provided to the [onSubmit(of:_:)](/documentation/swiftui/view/onsubmit(of:_:)) modifier to alter which types of user behaviors trigger a provided submission action.

### Getting submit triggers

- [search](/documentation/swiftui/submittriggers/search): Defines triggers originating from search fields constructed from searchable modifiers.
- [text](/documentation/swiftui/submittriggers/text): Defines triggers originating from text input controls like `TextField` and `SecureField`.

### Creating a set of options

- [init(rawValue:)](/documentation/swiftui/submittriggers/init(rawvalue:)): Creates a set of submit triggers.

## See Also

### Responding to submission events

- [onSubmit(of:_:)](/documentation/swiftui/view/onsubmit(of:_:)): Adds an action to perform when the user submits a value to this view.
- [submitScope(_:)](/documentation/swiftui/view/submitscope(_:)): Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
