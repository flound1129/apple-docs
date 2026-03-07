# PresentationAdaptation

Strategies for adapting a presentation to a different size class.

```swift
struct PresentationAdaptation
```

## Overview

Use values of this type with the [presentationCompactAdaptation(_:)](/documentation/swiftui/view/presentationcompactadaptation(_:)) and [presentationCompactAdaptation(horizontal:vertical:)](/documentation/swiftui/view/presentationcompactadaptation(horizontal:vertical:)) modifiers.

### Getting adaptation strategies

- [automatic](/documentation/swiftui/presentationadaptation/automatic): Use the default presentation adaptation.
- [none](/documentation/swiftui/presentationadaptation/none): Don’t adapt for the size class, if possible.
- [fullScreenCover](/documentation/swiftui/presentationadaptation/fullscreencover): Prefer a full-screen-cover appearance when adapting for size classes.
- [popover](/documentation/swiftui/presentationadaptation/popover): Prefer a popover appearance when adapting for size classes.
- [sheet](/documentation/swiftui/presentationadaptation/sheet): Prefer a sheet appearance when adapting for size classes.

## See Also

### Adapting a presentation size

- [presentationCompactAdaptation(horizontal:vertical:)](/documentation/swiftui/view/presentationcompactadaptation(horizontal:vertical:)): Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [presentationCompactAdaptation(_:)](/documentation/swiftui/view/presentationcompactadaptation(_:)): Specifies how to adapt a presentation to compact size classes.
- [presentationSizing(_:)](/documentation/swiftui/view/presentationsizing(_:)): Sets the sizing of the containing presentation.
- [PresentationSizing](/documentation/swiftui/presentationsizing): A type that defines the size of the presentation content and how the presentation size adjusts to its content’s size changing.
- [PresentationSizingRoot](/documentation/swiftui/presentationsizingroot): A proxy to a view provided to the presentation with a defined presentation size.
- [PresentationSizingContext](/documentation/swiftui/presentationsizingcontext): Contextual information about a presentation.
