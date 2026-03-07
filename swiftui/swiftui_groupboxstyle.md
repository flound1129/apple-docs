# GroupBoxStyle

A type that specifies the appearance and interaction of all group boxes within a view hierarchy.

```swift
@MainActor @preconcurrency protocol GroupBoxStyle
```

## Overview

To configure the current `GroupBoxStyle` for a view hierarchy, use the [groupBoxStyle(_:)](/documentation/swiftui/view/groupboxstyle(_:)) modifier.

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

### Getting built-in group box styles

- [automatic](/documentation/swiftui/groupboxstyle/automatic): The default style for group box views.

### Creating custom group box styles

- [makeBody(configuration:)](/documentation/swiftui/groupboxstyle/makebody(configuration:)): Creates a view representing the body of a group box.
- [GroupBoxStyle.Configuration](/documentation/swiftui/groupboxstyle/configuration): The properties of a group box instance.
- [Body](/documentation/swiftui/groupboxstyle/body): A view that represents the body of a group box.

### Supporting types

- [DefaultGroupBoxStyle](/documentation/swiftui/defaultgroupboxstyle): The default style for group box views.

## See Also

### Styling groups

- [controlGroupStyle(_:)](/documentation/swiftui/view/controlgroupstyle(_:)): Sets the style for control groups within this view.
- [ControlGroupStyle](/documentation/swiftui/controlgroupstyle): Defines the implementation of all control groups within a view hierarchy.
- [ControlGroupStyleConfiguration](/documentation/swiftui/controlgroupstyleconfiguration): The properties of a control group.
- [formStyle(_:)](/documentation/swiftui/view/formstyle(_:)): Sets the style for forms in a view hierarchy.
- [FormStyle](/documentation/swiftui/formstyle): The appearance and behavior of a form.
- [FormStyleConfiguration](/documentation/swiftui/formstyleconfiguration): The properties of a form instance.
- [groupBoxStyle(_:)](/documentation/swiftui/view/groupboxstyle(_:)): Sets the style for group boxes within this view.
- [GroupBoxStyleConfiguration](/documentation/swiftui/groupboxstyleconfiguration): The properties of a group box instance.
- [indexViewStyle(_:)](/documentation/swiftui/view/indexviewstyle(_:)): Sets the style for the index view within the current environment.
- [IndexViewStyle](/documentation/swiftui/indexviewstyle): Defines the implementation of all `IndexView` instances within a view hierarchy.
- [labeledContentStyle(_:)](/documentation/swiftui/view/labeledcontentstyle(_:)): Sets a style for labeled content.
- [LabeledContentStyle](/documentation/swiftui/labeledcontentstyle): The appearance and behavior of a labeled content instance..
- [LabeledContentStyleConfiguration](/documentation/swiftui/labeledcontentstyleconfiguration): The properties of a labeled content instance.
