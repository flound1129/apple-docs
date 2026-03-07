# LabeledContentStyle

The appearance and behavior of a labeled content instance..

```swift
@MainActor @preconcurrency protocol LabeledContentStyle
```

## Overview

Use [labeledContentStyle(_:)](/documentation/swiftui/view/labeledcontentstyle(_:)) to set a style on a view.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

### Getting built-in labeled content styles

- [automatic](/documentation/swiftui/labeledcontentstyle/automatic): A labeled content style that resolves its appearance automatically based on the current context.

### Creating custom labeled content styles

- [makeBody(configuration:)](/documentation/swiftui/labeledcontentstyle/makebody(configuration:)): Creates a view that represents the body of labeled content.
- [LabeledContentStyle.Configuration](/documentation/swiftui/labeledcontentstyle/configuration): The properties of a labeled content instance.
- [Body](/documentation/swiftui/labeledcontentstyle/body): A view that represents the appearance and behavior of labeled content.

### Supporting types

- [AutomaticLabeledContentStyle](/documentation/swiftui/automaticlabeledcontentstyle): The default labeled content style.

## See Also

### Styling groups

- [controlGroupStyle(_:)](/documentation/swiftui/view/controlgroupstyle(_:)): Sets the style for control groups within this view.
- [ControlGroupStyle](/documentation/swiftui/controlgroupstyle): Defines the implementation of all control groups within a view hierarchy.
- [ControlGroupStyleConfiguration](/documentation/swiftui/controlgroupstyleconfiguration): The properties of a control group.
- [formStyle(_:)](/documentation/swiftui/view/formstyle(_:)): Sets the style for forms in a view hierarchy.
- [FormStyle](/documentation/swiftui/formstyle): The appearance and behavior of a form.
- [FormStyleConfiguration](/documentation/swiftui/formstyleconfiguration): The properties of a form instance.
- [groupBoxStyle(_:)](/documentation/swiftui/view/groupboxstyle(_:)): Sets the style for group boxes within this view.
- [GroupBoxStyle](/documentation/swiftui/groupboxstyle): A type that specifies the appearance and interaction of all group boxes within a view hierarchy.
- [GroupBoxStyleConfiguration](/documentation/swiftui/groupboxstyleconfiguration): The properties of a group box instance.
- [indexViewStyle(_:)](/documentation/swiftui/view/indexviewstyle(_:)): Sets the style for the index view within the current environment.
- [IndexViewStyle](/documentation/swiftui/indexviewstyle): Defines the implementation of all `IndexView` instances within a view hierarchy.
- [labeledContentStyle(_:)](/documentation/swiftui/view/labeledcontentstyle(_:)): Sets a style for labeled content.
- [LabeledContentStyleConfiguration](/documentation/swiftui/labeledcontentstyleconfiguration): The properties of a labeled content instance.
