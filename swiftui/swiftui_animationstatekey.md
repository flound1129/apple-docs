# AnimationStateKey

A key for accessing animation state values.

```swift
protocol AnimationStateKey
```

## Overview

To access animation state from an [AnimationContext](/documentation/swiftui/animationcontext) in a custom animation, create an `AnimationStateKey`. For example, the following code creates an animation state key named `PausableState` and sets the value for the required [defaultValue](/documentation/swiftui/animationstatekey/defaultvalue) property. The code also defines properties for state values that the custom animation needs when calculating animation values. Keeping the state values in the animation state key makes it more convenient to read and write those values in the implementation of a [CustomAnimation](/documentation/swiftui/customanimation).

```swift
private struct PausableState<Value: VectorArithmetic>: AnimationStateKey {
    var paused = false
    var pauseTime: TimeInterval = 0.0

    static var defaultValue: Self { .init() }
}
```

To make accessing the value of the animation state key more convenient, define a property for it by extending [AnimationContext](/documentation/swiftui/animationcontext):

```swift
extension AnimationContext {
    fileprivate var pausableState: PausableState<Value> {
        get { state[PausableState<Value>.self] }
        set { state[PausableState<Value>.self] = newValue }
    }
}
```

Then, you can read and write your state in an instance of `CustomAnimation` using the [AnimationContext](/documentation/swiftui/animationcontext):

```swift
struct PausableAnimation: CustomAnimation {
    let base: Animation

    func animate<V>(value: V, time: TimeInterval, context: inout AnimationContext<V>) -> V? where V : VectorArithmetic {
        let paused = context.environment.animationPaused

        let pausableState = context.pausableState
        var pauseTime = pausableState.pauseTime
        if pausableState.paused != paused {
            pauseTime = time - pauseTime
            context.pausableState = PausableState(paused: paused, pauseTime: pauseTime)
        }

        let effectiveTime = paused ? pauseTime : time - pauseTime
        let result = base.animate(value: value, time: effectiveTime, context: &context)
        return result
    }
}
```

### Setting the default value

- [defaultValue](/documentation/swiftui/animationstatekey/defaultvalue): The default value for the animation state key.
- [Value](/documentation/swiftui/animationstatekey/value): The associated type representing the type of the animation state key’s value.

## See Also

### Creating custom animations

- [CustomAnimation](/documentation/swiftui/customanimation): A type that defines how an animatable value changes over time.
- [AnimationContext](/documentation/swiftui/animationcontext): Contextual values that a custom animation can use to manage state and access a view’s environment.
- [AnimationState](/documentation/swiftui/animationstate): A container that stores the state for a custom animation.
- [UnitCurve](/documentation/swiftui/unitcurve): A  function defined by a two-dimensional curve that maps an input progress in the range [0,1] to an output progress that is also in the range [0,1]. By changing the shape of the curve, the effective speed of an animation or other interpolation can be changed.
- [Spring](/documentation/swiftui/spring): A representation of a spring’s motion.
