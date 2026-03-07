# ControlWidgetConfiguration

A type that describes a control widget’s content.

```swift
@MainActor @preconcurrency protocol ControlWidgetConfiguration
```

## Overview

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

- [Body](/documentation/swiftui/controlwidgetconfiguration/body-swift.associatedtype): The type of control widget configuration representing the body of this configuration.

### Instance Properties

- [body](/documentation/swiftui/controlwidgetconfiguration/body-swift.property): The content and behavior of the control.

### Instance Methods

- [description(_:)](/documentation/swiftui/controlwidgetconfiguration/description(_:)): Sets the description shown for the control when a user adds or edits it, using the specified string.
- [displayName(_:)](/documentation/swiftui/controlwidgetconfiguration/displayname(_:)): Sets the name shown for the control when a user adds or edits it, using the specified string.
- [promptsForUserConfiguration()](/documentation/swiftui/controlwidgetconfiguration/promptsforuserconfiguration()): Specifies that a control’s configuration UI should be automatically presented after the widget is added.
- [pushHandler(_:)](/documentation/swiftui/controlwidgetconfiguration/pushhandler(_:)): Register a type that can handle push tokens changing for controls of this type.

## See Also

### Composing control widgets

- [ControlWidget](/documentation/swiftui/controlwidget): The configuration and content of a control widget to display in system spaces such as Control Center, the Lock Screen, and the Action Button.
- [EmptyControlWidgetConfiguration](/documentation/swiftui/emptycontrolwidgetconfiguration): An empty control widget configuration.
- [ControlWidgetConfigurationBuilder](/documentation/swiftui/controlwidgetconfigurationbuilder): A custom attribute that constructs a control widget’s body.
- [ControlWidgetTemplate](/documentation/swiftui/controlwidgettemplate): A type that describes a control widget’s content.
- [EmptyControlWidgetTemplate](/documentation/swiftui/emptycontrolwidgettemplate): An empty control widget template.
- [ControlWidgetTemplateBuilder](/documentation/swiftui/controlwidgettemplatebuilder): A custom attribute that constructs a control widget template’s body.
- [controlWidgetActionHint(_:)](/documentation/swiftui/view/controlwidgetactionhint(_:)): The action hint of the control described by the modified label.
- [controlWidgetStatus(_:)](/documentation/swiftui/view/controlwidgetstatus(_:)): The status of the control described by the modified label.
