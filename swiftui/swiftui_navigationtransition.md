# NavigationTransition

A type that defines the transition to use when navigating to a view.

```swift
protocol NavigationTransition
```

### Getting built-in transitions

- [automatic](/documentation/swiftui/navigationtransition/automatic): A style that automatically chooses the appropriate presentation transition for the current context.
- [zoom(sourceID:in:)](/documentation/swiftui/navigationtransition/zoom(sourceid:in:)): A navigation transition that zooms the appearing view from a given source view.

### Supporting Types

- [AutomaticNavigationTransition](/documentation/swiftui/automaticnavigationtransition): A style that automatically chooses the appropriate presentation transition for the current context.
- [ZoomNavigationTransition](/documentation/swiftui/zoomnavigationtransition): A navigation transition that zooms the appearing view from a given source view. Indicate the source view using the `View/matchedTransitionSource(id:namespace:)` modifier.

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
- [matchedTransitionSource(id:in:)](/documentation/swiftui/view/matchedtransitionsource(id:in:)): Identifies this view as the source of a navigation transition, such as a zoom transition.
- [matchedTransitionSource(id:in:configuration:)](/documentation/swiftui/view/matchedtransitionsource(id:in:configuration:)): Identifies this view as the source of a navigation transition, such as a zoom transition.
- [MatchedTransitionSourceConfiguration](/documentation/swiftui/matchedtransitionsourceconfiguration): A configuration that defines the appearance of a matched transition source.
