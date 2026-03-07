# ControlWidgetTemplate

A type that describes a control widget’s content.

```swift
@MainActor @preconcurrency protocol ControlWidgetTemplate
```

## Overview

Controls are defined using templates in order to ensure that they control will work at all sizes and in all system spaces in which they might be displayed. These templates define images (specifically, symbol images) and text using simple SwiftUI views like [Label](/documentation/swiftui/label), [Text](/documentation/swiftui/text), and [Image](/documentation/swiftui/image); and tint colors using the [tint(_:)](/documentation/swiftui/controlwidgettemplate/tint(_:)) modifier.

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

### Associated Types

- [Body](/documentation/swiftui/controlwidgettemplate/body-swift.associatedtype): The type of control widget template representing the body of this template.

### Instance Properties

- [body](/documentation/swiftui/controlwidgettemplate/body-swift.property): The content and behavior of this control widget.

### Instance Methods

- [disabled(_:)](/documentation/swiftui/controlwidgettemplate/disabled(_:)): Determines whether people can interact with this control.
- [privacySensitive(_:)](/documentation/swiftui/controlwidgettemplate/privacysensitive(_:)): Marks the control template as containing sensitive, private user data.
- [tint(_:)](/documentation/swiftui/controlwidgettemplate/tint(_:)): Sets the tint color within this control template.

## See Also

### Composing control widgets

- [ControlWidget](/documentation/swiftui/controlwidget): The configuration and content of a control widget to display in system spaces such as Control Center, the Lock Screen, and the Action Button.
- [ControlWidgetConfiguration](/documentation/swiftui/controlwidgetconfiguration): A type that describes a control widget’s content.
- [EmptyControlWidgetConfiguration](/documentation/swiftui/emptycontrolwidgetconfiguration): An empty control widget configuration.
- [ControlWidgetConfigurationBuilder](/documentation/swiftui/controlwidgetconfigurationbuilder): A custom attribute that constructs a control widget’s body.
- [EmptyControlWidgetTemplate](/documentation/swiftui/emptycontrolwidgettemplate): An empty control widget template.
- [ControlWidgetTemplateBuilder](/documentation/swiftui/controlwidgettemplatebuilder): A custom attribute that constructs a control widget template’s body.
- [controlWidgetActionHint(_:)](/documentation/swiftui/view/controlwidgetactionhint(_:)): The action hint of the control described by the modified label.
- [controlWidgetStatus(_:)](/documentation/swiftui/view/controlwidgetstatus(_:)): The status of the control described by the modified label.
