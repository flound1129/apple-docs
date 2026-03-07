# AnyTransition

A type-erased transition.

```swift
@frozen struct AnyTransition
```

## Overview

- See Also: `Transition`

### Getting built-in transitions

- [identity](/documentation/swiftui/anytransition/identity): A transition that returns the input view, unmodified, as the output view.
- [move(edge:)](/documentation/swiftui/anytransition/move(edge:)): Returns a transition that moves the view away, towards the specified edge of the view.
- [offset(_:)](/documentation/swiftui/anytransition/offset(_:))
- [offset(x:y:)](/documentation/swiftui/anytransition/offset(x:y:))
- [opacity](/documentation/swiftui/anytransition/opacity): A transition from transparent to opaque on insertion, and from opaque to transparent on removal.
- [push(from:)](/documentation/swiftui/anytransition/push(from:)): Creates a transition that when added to a view will animate the view’s insertion by moving it in from the specified edge while fading it in, and animate its removal by moving it out towards the opposite edge and fading it out.
- [scale](/documentation/swiftui/anytransition/scale): Returns a transition that scales the view.
- [scale(scale:anchor:)](/documentation/swiftui/anytransition/scale(scale:anchor:)): Returns a transition that scales the view by the specified amount.
- [slide](/documentation/swiftui/anytransition/slide): A transition that inserts by moving in from the leading edge, and removes by moving out towards the trailing edge.

### Combining and configuring transitions

- [animation(_:)](/documentation/swiftui/anytransition/animation(_:)): Attaches an animation to this transition.
- [asymmetric(insertion:removal:)](/documentation/swiftui/anytransition/asymmetric(insertion:removal:)): Provides a composite transition that uses a different transition for insertion versus removal.
- [combined(with:)](/documentation/swiftui/anytransition/combined(with:)): Combines this transition with another, returning a new transition that is the result of both transitions being applied.

### Creating a custom transition

- [init(_:)](/documentation/swiftui/anytransition/init(_:)): Create an instance that type-erases `transition`.
- [modifier(active:identity:)](/documentation/swiftui/anytransition/modifier(active:identity:)): Returns a transition defined between an active modifier and an identity modifier.

## See Also

### Defining transitions

- [transition(_:)](/documentation/swiftui/view/transition(_:)): Associates a transition with the view.
- [Transition](/documentation/swiftui/transition): A description of view changes to apply when a view is added to and removed from the view hierarchy.
- [TransitionProperties](/documentation/swiftui/transitionproperties): The properties a `Transition` can have.
- [TransitionPhase](/documentation/swiftui/transitionphase): An indication of which the current stage of a transition.
- [AsymmetricTransition](/documentation/swiftui/asymmetrictransition): A composite `Transition` that uses a different transition for insertion versus removal.
- [contentTransition(_:)](/documentation/swiftui/view/contenttransition(_:)): Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [contentTransition](/documentation/swiftui/environmentvalues/contenttransition): The current method of animating the contents of views.
- [contentTransitionAddsDrawingGroup](/documentation/swiftui/environmentvalues/contenttransitionaddsdrawinggroup): A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.
- [ContentTransition](/documentation/swiftui/contenttransition): A kind of transition that applies to the content within a single view, rather than to the insertion or removal of a view.
- [PlaceholderContentView](/documentation/swiftui/placeholdercontentview): A placeholder used to construct an inline modifier, transition, or other helper type.
- [navigationTransition(_:)](/documentation/swiftui/view/navigationtransition(_:)): Sets the navigation transition style for this view.
- [NavigationTransition](/documentation/swiftui/navigationtransition): A type that defines the transition to use when navigating to a view.
- [matchedTransitionSource(id:in:)](/documentation/swiftui/view/matchedtransitionsource(id:in:)): Identifies this view as the source of a navigation transition, such as a zoom transition.
- [matchedTransitionSource(id:in:configuration:)](/documentation/swiftui/view/matchedtransitionsource(id:in:configuration:)): Identifies this view as the source of a navigation transition, such as a zoom transition.
- [MatchedTransitionSourceConfiguration](/documentation/swiftui/matchedtransitionsourceconfiguration): A configuration that defines the appearance of a matched transition source.
