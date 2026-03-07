# AccessibilityRotorContent

Content within an accessibility rotor.

```swift
@MainActor @preconcurrency protocol AccessibilityRotorContent
```

## Overview

Generally generated from control flow constructs like `ForEach` and `if`, and `AccessibilityRotorEntry`.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

### Supporting types

- [body](/documentation/swiftui/accessibilityrotorcontent/body-swift.property): The internal content of this `AccessibilityRotorContent`.
- [Body](/documentation/swiftui/accessibilityrotorcontent/body-swift.associatedtype): The type for the internal content of this `AccessibilityRotorContent`.

## See Also

### Creating rotors

- [AccessibilityRotorContentBuilder](/documentation/swiftui/accessibilityrotorcontentbuilder): Result builder you use to generate rotor entry content.
- [AccessibilityRotorEntry](/documentation/swiftui/accessibilityrotorentry): A struct representing an entry in an Accessibility Rotor.
