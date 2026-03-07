# CustomAnimation

A type that defines how an animatable value changes over time.

```swift
@preconcurrency protocol CustomAnimation : Hashable, Sendable
```

## Overview

Use this protocol to create a type that changes an animatable value over time, which produces a custom visual transition of a view. For example, the follow code changes an animatable value using an elastic ease-in ease-out function:

```swift
struct ElasticEaseInEaseOutAnimation: CustomAnimation {
    let duration: TimeInterval

    func animate<V>(value: V, time: TimeInterval, context: inout AnimationContext<V>) -> V? where V : VectorArithmetic {
        if time > duration { return nil } // The animation has finished.

        let p = time / duration
        let s = sin((20 * p - 11.125) * ((2 * Double.pi) / 4.5))
        if p < 0.5 {
            return value.scaled(by: -(pow(2, 20 * p - 10) * s) / 2)
        } else {
            return value.scaled(by: (pow(2, -20 * p + 10) * s) / 2 + 1)
        }
    }
}
```

> **Note:**
> To maintain state during the life span of a custom animation, use the [state](/documentation/swiftui/animationcontext/state) property available on the `context` parameter value. You can also use context’s [environment](/documentation/swiftui/animationcontext/environment) property to retrieve environment values from the view that created the custom animation. For more information, see [AnimationContext](/documentation/swiftui/animationcontext).
>

To create an [Animation](/documentation/swiftui/animation) instance of a custom animation, use the [init(_:)](/documentation/swiftui/animation/init(_:)) initializer, passing in an instance of a custom animation; for example:

```swift
Animation(ElasticEaseInEaseOutAnimation(duration: 5.0))
```

To help make view code more readable, extend [Animation](/documentation/swiftui/animation) and add a static property and function that returns an `Animation` instance of a custom animation. For example, the following code adds the static property `elasticEaseInEaseOut` that returns the elastic ease-in ease-out animation with a default duration of `0.35` seconds. Next, the code adds a method that returns the animation with a specified duration.

```swift
extension Animation {
    static var elasticEaseInEaseOut: Animation { elasticEaseInEaseOut(duration: 0.35) }
    static func elasticEaseInEaseOut(duration: TimeInterval) -> Animation {
        Animation(ElasticEaseInEaseOutAnimation(duration: duration))
    }
}
```

To animate a view with the elastic ease-in ease-out animation, a view calls either `.elasticEaseInEaseOut` or `.elasticEaseInEaseOut(duration:)`. For example, the follow code includes an Animate button that, when clicked, animates a circle as it moves from one edge of the view to the other, using the elastic ease-in ease-out animation with a duration of `5` seconds:

```swift
struct ElasticEaseInEaseOutView: View {
    @State private var isActive = false

    var body: some View {
        VStack(alignment: isActive ? .trailing : .leading) {
            Circle()
                .frame(width: 100.0)
                .foregroundColor(.accentColor)

            Button("Animate") {
                withAnimation(.elasticEaseInEaseOut(duration: 5.0)) {
                    isActive.toggle()
                }
            }
            .frame(maxWidth: .infinity)
        }
        .padding()
    }
}
```

### Animating a value

- [animate(value:time:context:)](/documentation/swiftui/customanimation/animate(value:time:context:)): Calculates the value of the animation at the specified time.

### Getting the velocity

- [velocity(value:time:context:)](/documentation/swiftui/customanimation/velocity(value:time:context:)): Calculates the velocity of the animation at a specified time.

### Determining whether to merge

- [shouldMerge(previous:value:time:context:)](/documentation/swiftui/customanimation/shouldmerge(previous:value:time:context:)): Determines whether an instance of the animation can merge with other instance of the same type.

## See Also

### Creating custom animations

- [AnimationContext](/documentation/swiftui/animationcontext): Contextual values that a custom animation can use to manage state and access a view’s environment.
- [AnimationState](/documentation/swiftui/animationstate): A container that stores the state for a custom animation.
- [AnimationStateKey](/documentation/swiftui/animationstatekey): A key for accessing animation state values.
- [UnitCurve](/documentation/swiftui/unitcurve): A  function defined by a two-dimensional curve that maps an input progress in the range [0,1] to an output progress that is also in the range [0,1]. By changing the shape of the curve, the effective speed of an animation or other interpolation can be changed.
- [Spring](/documentation/swiftui/spring): A representation of a spring’s motion.
