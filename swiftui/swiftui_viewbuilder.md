# ViewBuilder

A custom parameter attribute that constructs views from closures.

```swift
@resultBuilder struct ViewBuilder
```

## Overview

You typically use [ViewBuilder](/documentation/swiftui/viewbuilder) as a parameter attribute for child view-producing closure parameters, allowing those closures to provide multiple child views. For example, the following `contextMenu` function accepts a closure that produces one or more views via the view builder.

```swift
func contextMenu<MenuItems: View>(
    @ViewBuilder menuItems: () -> MenuItems
) -> some View
```

Clients of this function can use multiple-statement closures to provide several child views, as shown in the following example:

```swift
myView.contextMenu {
    Text("Cut")
    Text("Copy")
    Text("Paste")
    if isSymbol {
        Text("Jump to Definition")
    }
}
```

### Building content

- [buildBlock()](/documentation/swiftui/viewbuilder/buildblock()): Builds an empty view from a block containing no statements.
- [buildBlock(_:)](/documentation/swiftui/viewbuilder/buildblock(_:)): Passes a single view written as a child view through unmodified.
- [buildExpression(_:)](/documentation/swiftui/viewbuilder/buildexpression(_:)): Builds an expression within the builder.

### Conditionally building content

- [buildEither(first:)](/documentation/swiftui/viewbuilder/buildeither(first:)): Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [buildEither(second:)](/documentation/swiftui/viewbuilder/buildeither(second:)): Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [buildIf(_:)](/documentation/swiftui/viewbuilder/buildif(_:)): Produces an optional view for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
- [buildLimitedAvailability(_:)](/documentation/swiftui/viewbuilder/buildlimitedavailability(_:)): Processes view content for a conditional compiler-control statement that performs an availability check.

## See Also

### Creating a view

- [Declaring a custom view](/documentation/swiftui/declaring-a-custom-view): Define views and assemble them into a view hierarchy.
- [View](/documentation/swiftui/view): A type that represents part of your app’s user interface and provides modifiers that you use to configure views.
