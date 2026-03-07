# PhaseAnimator

A container that animates its content by automatically cycling through a collection of phases that you provide, each defining a discrete step within an animation.

```swift
struct PhaseAnimator<Phase, Content> where Phase : Equatable, Content : View
```

## Overview

Use one of the phase animator view modifiers like [phaseAnimator(_:content:animation:)](/documentation/swiftui/view/phaseanimator(_:content:animation:)) to create a phased animation in your app.

### Creating a phase animator

- [init(_:content:animation:)](/documentation/swiftui/phaseanimator/init(_:content:animation:)): Cycles through a sequence of phases continuously, animating updates to a view on each phase change.
- [init(_:trigger:content:animation:)](/documentation/swiftui/phaseanimator/init(_:trigger:content:animation:)): Cycles through a sequence of phases in response to changes in a specified value, animating updates to a view on each phase change.

## See Also

### Creating phase-based animation

- [Controlling the timing and movements of your animations](/documentation/swiftui/controlling-the-timing-and-movements-of-your-animations): Build sophisticated animations that you control using phase and keyframe animators.
- [phaseAnimator(_:content:animation:)](/documentation/swiftui/view/phaseanimator(_:content:animation:)): Animates effects that you apply to a view over a sequence of phases that change continuously.
- [phaseAnimator(_:trigger:content:animation:)](/documentation/swiftui/view/phaseanimator(_:trigger:content:animation:)): Animates effects that you apply to a view over a sequence of phases that change based on a trigger.
