# ControlGroupStyle

Defines the implementation of all control groups within a view hierarchy.

```swift
@MainActor @preconcurrency protocol ControlGroupStyle
```

## Overview

To configure the current `ControlGroupStyle` for a view hierarchy, use the [controlGroupStyle(_:)](/documentation/swiftui/view/controlgroupstyle(_:)) modifier.

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

### Getting built-in control group styles

- [automatic](/documentation/swiftui/controlgroupstyle/automatic): The default control group style.
- [compactMenu](/documentation/swiftui/controlgroupstyle/compactmenu): A control group style that presents its content as a compact menu when the user presses the control, or as a submenu when nested within a larger menu.
- [menu](/documentation/swiftui/controlgroupstyle/menu): A control group style that presents its content as a menu when the user presses the control, or as a submenu when nested within a larger menu.
- [navigation](/documentation/swiftui/controlgroupstyle/navigation): The navigation control group style.
- [palette](/documentation/swiftui/controlgroupstyle/palette): A control group style that presents its content as a palette.

### Creating custom control group styles

- [makeBody(configuration:)](/documentation/swiftui/controlgroupstyle/makebody(configuration:)): Creates a view representing the body of a control group.
- [ControlGroupStyle.Configuration](/documentation/swiftui/controlgroupstyle/configuration): The properties of a `ControlGroup` instance being created.
- [Body](/documentation/swiftui/controlgroupstyle/body): A view representing the body of a control group.

### Supporting types

- [AutomaticControlGroupStyle](/documentation/swiftui/automaticcontrolgroupstyle): The default control group style.
- [CompactMenuControlGroupStyle](/documentation/swiftui/compactmenucontrolgroupstyle): A control group style that presents its content as a compact menu when the user presses the control, or as a submenu when nested within a larger menu.
- [MenuControlGroupStyle](/documentation/swiftui/menucontrolgroupstyle): A control group style that presents its content as a menu when the user presses the control, or as a submenu when nested within a larger menu.
- [NavigationControlGroupStyle](/documentation/swiftui/navigationcontrolgroupstyle): The navigation control group style.
- [PaletteControlGroupStyle](/documentation/swiftui/palettecontrolgroupstyle): A control group style that presents its content as a palette.

## See Also

### Styling groups

- [controlGroupStyle(_:)](/documentation/swiftui/view/controlgroupstyle(_:)): Sets the style for control groups within this view.
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
- [LabeledContentStyle](/documentation/swiftui/labeledcontentstyle): The appearance and behavior of a labeled content instance..
- [LabeledContentStyleConfiguration](/documentation/swiftui/labeledcontentstyleconfiguration): The properties of a labeled content instance.
