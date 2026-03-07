# KeyframeTimeline

A description of how a value changes over time, modeled using keyframes.

```swift
struct KeyframeTimeline<Value>
```

## Overview

Unlike other animations in SwiftUI (using [Animation](/documentation/swiftui/animation)), keyframes don’t interpolate between from and to values that SwiftUI provides as state changes. Instead, keyframes fully define the path that a value takes over time using the tracks that make up their body.

`Keyframes` values are roughly analogous to video clips; they have a set duration, and you can scrub and evaluate them for any time within the duration.

The `Keyframes` structure also allows you to compute an interpolated value at a specific time, which you can use when integrating keyframes into custom use cases.

For example, you can use a `Keyframes` instance to define animations for a type conforming to `Animatable:`

```swift
let keyframes = KeyframeTimeline(initialValue: CGPoint.zero) {
    CubicKeyframe(.init(x: 0, y: 100), duration: 0.3)
    CubicKeyframe(.init(x: 0, y: 0), duration: 0.7)
}

let value = keyframes.value(time: 0.45)
```

For animations that involve multiple coordinated changes, you can include multiple nested tracks:

```swift
struct Values {
    var rotation = Angle.zero
    var scale = 1.0
}

let keyframes = KeyframeTimeline(initialValue: Values()) {
    KeyframeTrack(\.rotation) {
        CubicKeyframe(.zero, duration: 0.2)
        CubicKeyframe(.degrees(45), duration: 0.3)
    }
    KeyframeTrack(\.scale) {
        CubicKeyframe(value: 1.2, duration: 0.5)
        CubicKeyframe(value: 0.9, duration: 0.2)
        CubicKeyframe(value: 1.0, duration: 0.3)
    }
}
```

Multiple nested tracks update the initial value in the order that they are declared. This means that if multiple nested plans change the same property of the root value, the value from the last competing track will be used.

### Creating a keyframe timeline

- [init(initialValue:content:)](/documentation/swiftui/keyframetimeline/init(initialvalue:content:)): Creates a new instance using the initial value and content that you provide.

### Getting the duration

- [duration](/documentation/swiftui/keyframetimeline/duration): The duration of the content in seconds.

### Getting an interpolated value

- [value(time:)](/documentation/swiftui/keyframetimeline/value(time:)): Returns the interpolated value at the given time.
- [value(progress:)](/documentation/swiftui/keyframetimeline/value(progress:)): Returns the interpolated value at the given progress in the range zero to one.

## See Also

### Creating keyframe-based animation

- [keyframeAnimator(initialValue:repeating:content:keyframes:)](/documentation/swiftui/view/keyframeanimator(initialvalue:repeating:content:keyframes:)): Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [keyframeAnimator(initialValue:trigger:content:keyframes:)](/documentation/swiftui/view/keyframeanimator(initialvalue:trigger:content:keyframes:)): Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.
- [KeyframeAnimator](/documentation/swiftui/keyframeanimator): A container that animates its content with keyframes.
- [Keyframes](/documentation/swiftui/keyframes): A type that defines changes to a value over time.
- [KeyframeTrack](/documentation/swiftui/keyframetrack): A sequence of keyframes animating a single property of a root type.
- [KeyframeTrackContentBuilder](/documentation/swiftui/keyframetrackcontentbuilder): The builder that creates keyframe track content from the keyframes that you define within a closure.
- [KeyframesBuilder](/documentation/swiftui/keyframesbuilder): A builder that combines keyframe content values into a single value.
- [KeyframeTrackContent](/documentation/swiftui/keyframetrackcontent): A group of keyframes that define an interpolation curve of an animatable value.
- [CubicKeyframe](/documentation/swiftui/cubickeyframe): A keyframe that uses a cubic curve to smoothly interpolate between values.
- [LinearKeyframe](/documentation/swiftui/linearkeyframe): A keyframe that uses simple linear interpolation.
- [MoveKeyframe](/documentation/swiftui/movekeyframe): A keyframe that immediately moves to the given value without interpolating.
- [SpringKeyframe](/documentation/swiftui/springkeyframe): A keyframe that uses a spring function to interpolate to the given value.
