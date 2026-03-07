# AnimationCompletionCriteria

The criteria that determines when an animation is considered finished.

```swift
struct AnimationCompletionCriteria
```

### Getting the completion criteria

- [logicallyComplete](/documentation/swiftui/animationcompletioncriteria/logicallycomplete): The animation has logically completed, but may still be in its long tail.
- [removed](/documentation/swiftui/animationcompletioncriteria/removed): The entire animation is finished and will now be removed.

## See Also

### Adding state-based animation to an action

- [withAnimation(_:_:)](/documentation/swiftui/withanimation(_:_:)): Returns the result of recomputing the view’s body with the provided animation.
- [withAnimation(_:completionCriteria:_:completion:)](/documentation/swiftui/withanimation(_:completioncriteria:_:completion:)): Returns the result of recomputing the view’s body with the provided animation, and runs the completion when all animations are complete.
- [Animation](/documentation/swiftui/animation): The way a view changes over time to create a smooth visual transition from one state to another.
