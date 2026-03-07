# PresentationBackgroundInteraction

The kinds of interaction available to views behind a presentation.

```swift
struct PresentationBackgroundInteraction
```

## Overview

Use values of this type with the [presentationBackgroundInteraction(_:)](/documentation/swiftui/view/presentationbackgroundinteraction(_:)) modifier.

### Getting interaction types

- [automatic](/documentation/swiftui/presentationbackgroundinteraction/automatic): The default background interaction for the presentation.
- [disabled](/documentation/swiftui/presentationbackgroundinteraction/disabled): People can’t interact with the view behind a presentation.
- [enabled](/documentation/swiftui/presentationbackgroundinteraction/enabled): People can interact with the view behind a presentation.
- [enabled(upThrough:)](/documentation/swiftui/presentationbackgroundinteraction/enabled(upthrough:)): People can interact with the view behind a presentation up through a specified detent.

## See Also

### Styling a sheet and its background

- [presentationCornerRadius(_:)](/documentation/swiftui/view/presentationcornerradius(_:)): Requests that the presentation have a specific corner radius.
- [presentationBackground(_:)](/documentation/swiftui/view/presentationbackground(_:)): Sets the presentation background of the enclosing sheet using a shape style.
- [presentationBackground(alignment:content:)](/documentation/swiftui/view/presentationbackground(alignment:content:)): Sets the presentation background of the enclosing sheet to a custom view.
- [presentationBackgroundInteraction(_:)](/documentation/swiftui/view/presentationbackgroundinteraction(_:)): Controls whether people can interact with the view behind a presentation.
