# withAnimation(_:_:)

Returns the result of recomputing the view’s body with the provided animation.

```swift
func withAnimation<Result>(_ animation: Animation? = .default, _ body: () throws -> Result) rethrows -> Result
```

## Discussion

This function sets the given [Animation](/documentation/swiftui/animation) as the [animation](/documentation/swiftui/transaction/animation) property of the thread’s current [Transaction](/documentation/swiftui/transaction).

## See Also

### Adding state-based animation to an action

- [withAnimation(_:completionCriteria:_:completion:)](/documentation/swiftui/withanimation(_:completioncriteria:_:completion:)): Returns the result of recomputing the view’s body with the provided animation, and runs the completion when all animations are complete.
- [AnimationCompletionCriteria](/documentation/swiftui/animationcompletioncriteria): The criteria that determines when an animation is considered finished.
- [Animation](/documentation/swiftui/animation): The way a view changes over time to create a smooth visual transition from one state to another.
