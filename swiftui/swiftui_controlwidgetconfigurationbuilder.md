# ControlWidgetConfigurationBuilder

A custom attribute that constructs a control widget’s body.

```swift
@resultBuilder struct ControlWidgetConfigurationBuilder
```

## Overview

The `@ControlWidgetConfigurationBuilder` attribute allows your control widget’s body closure to produce a control widget configuration after zero or more other statements:

```swift
struct GarageDoorOpener: ControlWidget {
    var body: some ControlWidgetConfiguration {
        let kind = "com.yourcompany.GarageDoorOpener"

        StaticControlConfiguration(
            kind: kind
        ) {
            ...
        }
    }
}
```

### Type Methods

- [buildBlock(_:)](/documentation/swiftui/controlwidgetconfigurationbuilder/buildblock(_:)): Passes a single control widget configuration written as a child control through unmodified.
- [buildExpression(_:)](/documentation/swiftui/controlwidgetconfigurationbuilder/buildexpression(_:)): Builds an expression within the builder.

## See Also

### Composing control widgets

- [ControlWidget](/documentation/swiftui/controlwidget): The configuration and content of a control widget to display in system spaces such as Control Center, the Lock Screen, and the Action Button.
- [ControlWidgetConfiguration](/documentation/swiftui/controlwidgetconfiguration): A type that describes a control widget’s content.
- [EmptyControlWidgetConfiguration](/documentation/swiftui/emptycontrolwidgetconfiguration): An empty control widget configuration.
- [ControlWidgetTemplate](/documentation/swiftui/controlwidgettemplate): A type that describes a control widget’s content.
- [EmptyControlWidgetTemplate](/documentation/swiftui/emptycontrolwidgettemplate): An empty control widget template.
- [ControlWidgetTemplateBuilder](/documentation/swiftui/controlwidgettemplatebuilder): A custom attribute that constructs a control widget template’s body.
- [controlWidgetActionHint(_:)](/documentation/swiftui/view/controlwidgetactionhint(_:)): The action hint of the control described by the modified label.
- [controlWidgetStatus(_:)](/documentation/swiftui/view/controlwidgetstatus(_:)): The status of the control described by the modified label.
