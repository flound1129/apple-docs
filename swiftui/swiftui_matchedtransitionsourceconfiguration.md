# MatchedTransitionSourceConfiguration

A configuration that defines the appearance of a matched transition source.

```swift
protocol MatchedTransitionSourceConfiguration : Sendable
```

### Instance Methods

- [background(_:)](/documentation/swiftui/matchedtransitionsourceconfiguration/background(_:)): Specifies a color that will be drawn behind the content within the matched transition source.
- [clipShape(_:)](/documentation/swiftui/matchedtransitionsourceconfiguration/clipshape(_:)): Applies the specified shape as to the matched transition source, clipping its content.
- [shadow(color:radius:x:y:)](/documentation/swiftui/matchedtransitionsourceconfiguration/shadow(color:radius:x:y:)): Applies the specified shadow effect to the matched transition source.

## See Also

### Defining transitions

- [transition(_:)](/documentation/swiftui/view/transition(_:)): Associates a transition with the view.
- [Transition](/documentation/swiftui/transition): A description of view changes to apply when a view is added to and removed from the view hierarchy.
- [TransitionProperties](/documentation/swiftui/transitionproperties): The properties a `Transition` can have.
- [TransitionPhase](/documentation/swiftui/transitionphase): An indication of which the current stage of a transition.
- [AsymmetricTransition](/documentation/swiftui/asymmetrictransition): A composite `Transition` that uses a different transition for insertion versus removal.
- [AnyTransition](/documentation/swiftui/anytransition): A type-erased transition.
- [contentTransition(_:)](/documentation/swiftui/view/contenttransition(_:)): Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [contentTransition](/documentation/swiftui/environmentvalues/contenttransition): The current method of animating the contents of views.
- [contentTransitionAddsDrawingGroup](/documentation/swiftui/environmentvalues/contenttransitionaddsdrawinggroup): A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.
- [ContentTransition](/documentation/swiftui/contenttransition): A kind of transition that applies to the content within a single view, rather than to the insertion or removal of a view.
- [PlaceholderContentView](/documentation/swiftui/placeholdercontentview): A placeholder used to construct an inline modifier, transition, or other helper type.
- [navigationTransition(_:)](/documentation/swiftui/view/navigationtransition(_:)): Sets the navigation transition style for this view.
- [NavigationTransition](/documentation/swiftui/navigationtransition): A type that defines the transition to use when navigating to a view.
- [matchedTransitionSource(id:in:)](/documentation/swiftui/view/matchedtransitionsource(id:in:)): Identifies this view as the source of a navigation transition, such as a zoom transition.
- [matchedTransitionSource(id:in:configuration:)](/documentation/swiftui/view/matchedtransitionsource(id:in:configuration:)): Identifies this view as the source of a navigation transition, such as a zoom transition.
