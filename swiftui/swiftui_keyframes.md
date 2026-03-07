# Keyframes

A type that defines changes to a value over time.

```swift
protocol Keyframes<Value>
```

### Creating a keyframe

- [body](/documentation/swiftui/keyframes/body-swift.property): The composition of content that comprise the keyframes.
- [Body](/documentation/swiftui/keyframes/body-swift.associatedtype): The type of keyframes representing the body of this type.
- [Value](/documentation/swiftui/keyframes/value): The type of value animated by this keyframes type

## See Also

### Creating keyframe-based animation

- [keyframeAnimator(initialValue:repeating:content:keyframes:)](/documentation/swiftui/view/keyframeanimator(initialvalue:repeating:content:keyframes:)): Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [keyframeAnimator(initialValue:trigger:content:keyframes:)](/documentation/swiftui/view/keyframeanimator(initialvalue:trigger:content:keyframes:)): Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.
- [KeyframeAnimator](/documentation/swiftui/keyframeanimator): A container that animates its content with keyframes.
- [KeyframeTimeline](/documentation/swiftui/keyframetimeline): A description of how a value changes over time, modeled using keyframes.
- [KeyframeTrack](/documentation/swiftui/keyframetrack): A sequence of keyframes animating a single property of a root type.
- [KeyframeTrackContentBuilder](/documentation/swiftui/keyframetrackcontentbuilder): The builder that creates keyframe track content from the keyframes that you define within a closure.
- [KeyframesBuilder](/documentation/swiftui/keyframesbuilder): A builder that combines keyframe content values into a single value.
- [KeyframeTrackContent](/documentation/swiftui/keyframetrackcontent): A group of keyframes that define an interpolation curve of an animatable value.
- [CubicKeyframe](/documentation/swiftui/cubickeyframe): A keyframe that uses a cubic curve to smoothly interpolate between values.
- [LinearKeyframe](/documentation/swiftui/linearkeyframe): A keyframe that uses simple linear interpolation.
- [MoveKeyframe](/documentation/swiftui/movekeyframe): A keyframe that immediately moves to the given value without interpolating.
- [SpringKeyframe](/documentation/swiftui/springkeyframe): A keyframe that uses a spring function to interpolate to the given value.
