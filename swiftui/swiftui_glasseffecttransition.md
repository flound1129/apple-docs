# GlassEffectTransition

A structure that describes changes to apply when a glass effect is added or removed from the view hierarchy.

```swift
struct GlassEffectTransition
```

### Type Properties

- [identity](/documentation/swiftui/glasseffecttransition/identity): The identity transition specifying no changes.
- [matchedGeometry](/documentation/swiftui/glasseffecttransition/matchedgeometry): Returns the matched geometry glass effect transition.
- [materialize](/documentation/swiftui/glasseffecttransition/materialize): The materialize glass effect transition which will fade in content and animate in or out the glass material but will not attempt to match the geometry of any other glass effects.

## See Also

### Styling views with Liquid Glass

- [Applying Liquid Glass to custom views](/documentation/swiftui/applying-liquid-glass-to-custom-views): Configure, combine, and morph views using Liquid Glass effects.
- [Landmarks: Building an app with Liquid Glass](/documentation/swiftui/landmarks-building-an-app-with-liquid-glass): Enhance your app experience with system-provided and custom Liquid Glass.
- [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:)): Applies the Liquid Glass effect to a view.
- [interactive(_:)](/documentation/swiftui/glass/interactive(_:)): Returns a copy of the structure configured to be interactive.
- [GlassEffectContainer](/documentation/swiftui/glasseffectcontainer): A view that combines multiple Liquid Glass shapes into a single shape that can morph individual shapes into one another.
- [GlassButtonStyle](/documentation/swiftui/glassbuttonstyle): A button style that applies glass border artwork based on the button’s context.
- [GlassProminentButtonStyle](/documentation/swiftui/glassprominentbuttonstyle): A button style that applies prominent glass border artwork based on the button’s context.
- [DefaultGlassEffectShape](/documentation/swiftui/defaultglasseffectshape): The default shape applied by glass effects, a capsule.
