# SymbolEffectTransition

Creates a transition that applies the Appear, Disappear, DrawOn or DrawOff symbol animation to symbol images within the inserted or removed view hierarchy.

```swift
@MainActor @frozen @preconcurrency struct SymbolEffectTransition
```

## Overview

Other views are unaffected by this transition.

### Creating a transition

- [init(effect:options:)](/documentation/swiftui/symboleffecttransition/init(effect:options:))

## See Also

### Managing symbol effects

- [symbolEffect(_:options:isActive:)](/documentation/swiftui/view/symboleffect(_:options:isactive:)): Returns a new view with a symbol effect added to it.
- [symbolEffect(_:options:value:)](/documentation/swiftui/view/symboleffect(_:options:value:)): Returns a new view with a symbol effect added to it.
- [symbolEffectsRemoved(_:)](/documentation/swiftui/view/symboleffectsremoved(_:)): Returns a new view with its inherited symbol image effects either removed or left unchanged.
