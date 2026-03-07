# ResetFocusAction

An environment value that provides the ability to reevaluate default focus.

```swift
struct ResetFocusAction
```

## Overview

Get the [resetFocus](/documentation/swiftui/environmentvalues/resetfocus) environment value and call it as a function to force a default focus reevaluation at runtime.

```swift
@Namespace var mainNamespace
@Environment(\.resetFocus) var resetFocus

var body: some View {
    // ...
    resetFocus(in: mainNamespace)
    // ...
}
```

### Calling the action

- [callAsFunction(in:)](/documentation/swiftui/resetfocusaction/callasfunction(in:)): Asks the focus sytem to reevaluate the default focus item.

## See Also

### Resetting focus

- [resetFocus](/documentation/swiftui/environmentvalues/resetfocus): An action that requests the focus system to reevaluate default focus.
