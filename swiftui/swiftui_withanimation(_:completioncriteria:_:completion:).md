# withAnimation(_:completionCriteria:_:completion:)

Returns the result of recomputing the view’s body with the provided animation, and runs the completion when all animations are complete.

```swift
func withAnimation<Result>(_ animation: Animation? = .default, completionCriteria: AnimationCompletionCriteria = .logicallyComplete, _ body: () throws -> Result, completion: @escaping () -> Void) rethrows -> Result
```

## Discussion

This function sets the given [Animation](/documentation/swiftui/animation) as the [animation](/documentation/swiftui/transaction/animation) property of the thread’s current [Transaction](/documentation/swiftui/transaction) as well as calling `Transaction/addAnimationCompletion` with the specified completion.

The completion callback will always be fired exactly one time. If no animations are created by the changes in `body`, then the callback will be called immediately after `body`.

## See Also

### Adding state-based animation to an action

- [withAnimation(_:_:)](/documentation/swiftui/withanimation(_:_:)): Returns the result of recomputing the view’s body with the provided animation.
- [AnimationCompletionCriteria](/documentation/swiftui/animationcompletioncriteria): The criteria that determines when an animation is considered finished.
- [Animation](/documentation/swiftui/animation): The way a view changes over time to create a smooth visual transition from one state to another.
