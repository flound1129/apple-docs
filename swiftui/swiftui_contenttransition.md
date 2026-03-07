# ContentTransition

A kind of transition that applies to the content within a single view, rather than to the insertion or removal of a view.

```swift
struct ContentTransition
```

## Overview

Set the behavior of content transitions within a view with the [contentTransition(_:)](/documentation/swiftui/view/contenttransition(_:)) modifier, passing in one of the defined transitions, such as [opacity](/documentation/swiftui/contenttransition/opacity) or [interpolate](/documentation/swiftui/contenttransition/interpolate) as the parameter.

> **Tip:**
> Content transitions only take effect within transactions that apply an [Animation](/documentation/swiftui/animation) to the views inside the [contentTransition(_:)](/documentation/swiftui/view/contenttransition(_:)) modifier.
>

Content transitions only take effect within the context of an [Animation](/documentation/swiftui/animation) block.

### Getting content transitions

- [identity](/documentation/swiftui/contenttransition/identity): The identity content transition, which indicates that content changes shouldn’t animate.
- [interpolate](/documentation/swiftui/contenttransition/interpolate): A content transition that indicates the views attempt to interpolate their contents during transitions, where appropriate.
- [numericText(countsDown:)](/documentation/swiftui/contenttransition/numerictext(countsdown:)): Creates a content transition intended to be used with `Text` views displaying numeric text. In certain environments changes to the text will enable a nonstandard transition tailored to numeric characters that count up or down.
- [numericText(value:)](/documentation/swiftui/contenttransition/numerictext(value:)): Creates a content transition intended to be used with `Text` views displaying numbers.
- [opacity](/documentation/swiftui/contenttransition/opacity): A content transition that indicates content fades from transparent to opaque on insertion, and from opaque to transparent on removal.
- [symbolEffect](/documentation/swiftui/contenttransition/symboleffect): A content transition that applies the default symbol effect transition to symbol images within the inserted or removed view hierarchy. Other views are unaffected by this transition.
- [symbolEffect(_:options:)](/documentation/swiftui/contenttransition/symboleffect(_:options:)): Creates a content transition that applies the symbol Replace animation to symbol images that it is applied to.

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
- [PlaceholderContentView](/documentation/swiftui/placeholdercontentview): A placeholder used to construct an inline modifier, transition, or other helper type.
- [navigationTransition(_:)](/documentation/swiftui/view/navigationtransition(_:)): Sets the navigation transition style for this view.
- [NavigationTransition](/documentation/swiftui/navigationtransition): A type that defines the transition to use when navigating to a view.
- [matchedTransitionSource(id:in:)](/documentation/swiftui/view/matchedtransitionsource(id:in:)): Identifies this view as the source of a navigation transition, such as a zoom transition.
- [matchedTransitionSource(id:in:configuration:)](/documentation/swiftui/view/matchedtransitionsource(id:in:configuration:)): Identifies this view as the source of a navigation transition, such as a zoom transition.
- [MatchedTransitionSourceConfiguration](/documentation/swiftui/matchedtransitionsourceconfiguration): A configuration that defines the appearance of a matched transition source.
