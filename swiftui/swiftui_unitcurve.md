# UnitCurve

A  function defined by a two-dimensional curve that maps an input progress in the range [0,1] to an output progress that is also in the range [0,1]. By changing the shape of the curve, the effective speed of an animation or other interpolation can be changed.

```swift
struct UnitCurve
```

## Overview

The horizontal (x) axis defines the input progress: a single input progress value in the range [0,1] must be provided when evaluating a curve.

The vertical (y) axis maps to the output progress: when a curve is evaluated, the y component of the point that intersects the input progress is returned.

### Getting a linear curve

- [linear](/documentation/swiftui/unitcurve/linear): A linear curve.

### Getting easing curves

- [easeIn](/documentation/swiftui/unitcurve/easein): A bezier curve that starts out slowly, then speeds up as it finishes.
- [easeOut](/documentation/swiftui/unitcurve/easeout): A bezier curve that starts out quickly, then slows down as it approaches the end.
- [easeInOut](/documentation/swiftui/unitcurve/easeinout): A bezier curve that starts out slowly, speeds up over the middle, then slows down again as it approaches the end.
- [circularEaseIn](/documentation/swiftui/unitcurve/circulareasein): A curve that starts out slowly, then speeds up as it finishes.
- [circularEaseOut](/documentation/swiftui/unitcurve/circulareaseout): A circular curve that starts out quickly, then slows down as it approaches the end.
- [circularEaseInOut](/documentation/swiftui/unitcurve/circulareaseinout): A circular curve that starts out slowly, speeds up over the middle, then slows down again as it approaches the end.

### Creating a general Bezier curve

- [bezier(startControlPoint:endControlPoint:)](/documentation/swiftui/unitcurve/bezier(startcontrolpoint:endcontrolpoint:)): Creates a new curve using bezier control points.

### Inverting a curve

- [inverse](/documentation/swiftui/unitcurve/inverse): Returns a copy of the curve with its x and y components swapped.

### Getting curve characteristics

- [value(at:)](/documentation/swiftui/unitcurve/value(at:)): Returns the output value (y component) of the curve at the given time.
- [velocity(at:)](/documentation/swiftui/unitcurve/velocity(at:)): Returns the rate of change (first derivative) of the output value of the curve at the given time.

### Deprecated symbols

- [easeInEaseOut](/documentation/swiftui/unitcurve/easeineaseout): A bezier curve that starts out slowly, speeds up over the middle, then slows down again as it approaches the end.

## See Also

### Creating custom animations

- [CustomAnimation](/documentation/swiftui/customanimation): A type that defines how an animatable value changes over time.
- [AnimationContext](/documentation/swiftui/animationcontext): Contextual values that a custom animation can use to manage state and access a view’s environment.
- [AnimationState](/documentation/swiftui/animationstate): A container that stores the state for a custom animation.
- [AnimationStateKey](/documentation/swiftui/animationstatekey): A key for accessing animation state values.
- [Spring](/documentation/swiftui/spring): A representation of a spring’s motion.
