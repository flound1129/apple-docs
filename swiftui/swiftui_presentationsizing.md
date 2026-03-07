# PresentationSizing

A type that defines the size of the presentation content and how the presentation size adjusts to its content’s size changing.

```swift
protocol PresentationSizing
```

## Overview

You don’t need to define your own version of this protocol. The system implementations of [form](/documentation/swiftui/presentationsizing/form), [page](/documentation/swiftui/presentationsizing/page), and [fitted](/documentation/swiftui/presentationsizing/fitted) are conveniences that automatically adapt to different device and screen sizes. If you do want to define your own sizing, first consider using the modifiers `PresenationSizing/sticky(horizontal:vertical:)` and [fitted(horizontal:vertical:)](/documentation/swiftui/presentationsizing/fitted(horizontal:vertical:)). For example, to define your own sizing that proposes a 400x400 square size:

```swift
protocol SquareSizing: PresentationSizing {
    func proposedSize(
        for subview: PresentationSizingRoot,
        context: PresentationSizingContext
    ) {
        .init(width: 400, height: 400)
    }
}

extension PresentationSizing where Self == SquareSizing {
    public static var square: Self { SquareSizing() }
}
```

Then, at the callsite, you can modify `.square` just like system sizings, for example, to fit its content vertically:

```swift
.presentationSizing(.square.fitted(horizontal: false, vertical: true))
```

> **See Also:**
> [presentationSizing(_:)](/documentation/swiftui/view/presentationsizing(_:))
>

### Getting built-in presentation size

- [automatic](/documentation/swiftui/presentationsizing/automatic): The default presentation sizing, appropriate for the platform.
- [fitted](/documentation/swiftui/presentationsizing/fitted): The presentation sizing is dictated by the ideal size of the content
- [form](/documentation/swiftui/presentationsizing/form): The size is appropriate for forms and slightly less wide than`.page`
- [page](/documentation/swiftui/presentationsizing/page): The size is roughly the size of a page of paper, appropriate for informational or compositional content.

### Creating custom presentation size

- [fitted(horizontal:vertical:)](/documentation/swiftui/presentationsizing/fitted(horizontal:vertical:))
- [proposedSize(for:context:)](/documentation/swiftui/presentationsizing/proposedsize(for:context:))
- [sticky(horizontal:vertical:)](/documentation/swiftui/presentationsizing/sticky(horizontal:vertical:)): Modifies self to be sticky in the specified dimensions — growing, but not shrinking.

### Supporting types

- [AutomaticPresentationSizing](/documentation/swiftui/automaticpresentationsizing): The default presentation sizing, appropriate for the platform.
- [FittedPresentationSizing](/documentation/swiftui/fittedpresentationsizing): The size of the presentation is dictated by the ideal size of the content.
- [FormPresentationSizing](/documentation/swiftui/formpresentationsizing): The size is appropriate for forms and slightly less wide than`.page`
- [PagePresentationSizing](/documentation/swiftui/pagepresentationsizing): The size is roughly the size of a page of paper, appropriate for informational or compositional content.

## See Also

### Adapting a presentation size

- [presentationCompactAdaptation(horizontal:vertical:)](/documentation/swiftui/view/presentationcompactadaptation(horizontal:vertical:)): Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [presentationCompactAdaptation(_:)](/documentation/swiftui/view/presentationcompactadaptation(_:)): Specifies how to adapt a presentation to compact size classes.
- [PresentationAdaptation](/documentation/swiftui/presentationadaptation): Strategies for adapting a presentation to a different size class.
- [presentationSizing(_:)](/documentation/swiftui/view/presentationsizing(_:)): Sets the sizing of the containing presentation.
- [PresentationSizingRoot](/documentation/swiftui/presentationsizingroot): A proxy to a view provided to the presentation with a defined presentation size.
- [PresentationSizingContext](/documentation/swiftui/presentationsizingcontext): Contextual information about a presentation.
