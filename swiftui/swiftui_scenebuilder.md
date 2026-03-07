# SceneBuilder

A result builder for composing a collection of scenes into a single composite scene.

```swift
@resultBuilder struct SceneBuilder
```

### Building content

- [buildBlock(_:)](/documentation/swiftui/scenebuilder/buildblock(_:)): Passes a single scene written as a child scene through unmodified.
- [buildExpression(_:)](/documentation/swiftui/scenebuilder/buildexpression(_:)): Builds an expression within the builder.
- [buildLimitedAvailability(_:)](/documentation/swiftui/scenebuilder/buildlimitedavailability(_:)): Processes scene content for a conditional compiler-control statement that performs an availability check.
- [buildOptional(_:)](/documentation/swiftui/scenebuilder/buildoptional(_:)): Produces an optional scene for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.

## See Also

### Creating scenes

- [Scene](/documentation/swiftui/scene): A part of an app’s user interface with a life cycle managed by the system.
