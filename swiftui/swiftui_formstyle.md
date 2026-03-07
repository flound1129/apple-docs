# FormStyle

The appearance and behavior of a form.

```swift
@MainActor @preconcurrency protocol FormStyle
```

## Overview

To configure the style for a single [Form](/documentation/swiftui/form) or for all form instances in a view hierarchy, use the [formStyle(_:)](/documentation/swiftui/view/formstyle(_:)) modifier.

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

### Getting built-in form styles

- [automatic](/documentation/swiftui/formstyle/automatic): The default form style.
- [columns](/documentation/swiftui/formstyle/columns): A non-scrolling form style with a trailing aligned column of labels next to a leading aligned column of values.
- [grouped](/documentation/swiftui/formstyle/grouped): A form style with grouped rows.

### Creating custom form styles

- [makeBody(configuration:)](/documentation/swiftui/formstyle/makebody(configuration:)): Creates a view that represents the body of a form.
- [FormStyle.Configuration](/documentation/swiftui/formstyle/configuration): The properties of a form instance.
- [Body](/documentation/swiftui/formstyle/body): A view that represents the appearance and interaction of a form.

### Supporting types

- [AutomaticFormStyle](/documentation/swiftui/automaticformstyle): The default form style.
- [ColumnsFormStyle](/documentation/swiftui/columnsformstyle): A non-scrolling form style with a trailing aligned column of labels next to a leading aligned column of values.
- [GroupedFormStyle](/documentation/swiftui/groupedformstyle): A form style with grouped rows.

## See Also

### Styling groups

- [controlGroupStyle(_:)](/documentation/swiftui/view/controlgroupstyle(_:)): Sets the style for control groups within this view.
- [ControlGroupStyle](/documentation/swiftui/controlgroupstyle): Defines the implementation of all control groups within a view hierarchy.
- [ControlGroupStyleConfiguration](/documentation/swiftui/controlgroupstyleconfiguration): The properties of a control group.
- [formStyle(_:)](/documentation/swiftui/view/formstyle(_:)): Sets the style for forms in a view hierarchy.
- [FormStyleConfiguration](/documentation/swiftui/formstyleconfiguration): The properties of a form instance.
- [groupBoxStyle(_:)](/documentation/swiftui/view/groupboxstyle(_:)): Sets the style for group boxes within this view.
- [GroupBoxStyle](/documentation/swiftui/groupboxstyle): A type that specifies the appearance and interaction of all group boxes within a view hierarchy.
- [GroupBoxStyleConfiguration](/documentation/swiftui/groupboxstyleconfiguration): The properties of a group box instance.
- [indexViewStyle(_:)](/documentation/swiftui/view/indexviewstyle(_:)): Sets the style for the index view within the current environment.
- [IndexViewStyle](/documentation/swiftui/indexviewstyle): Defines the implementation of all `IndexView` instances within a view hierarchy.
- [labeledContentStyle(_:)](/documentation/swiftui/view/labeledcontentstyle(_:)): Sets a style for labeled content.
- [LabeledContentStyle](/documentation/swiftui/labeledcontentstyle): The appearance and behavior of a labeled content instance..
- [LabeledContentStyleConfiguration](/documentation/swiftui/labeledcontentstyleconfiguration): The properties of a labeled content instance.
