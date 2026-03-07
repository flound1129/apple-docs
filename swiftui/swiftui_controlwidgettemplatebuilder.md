# ControlWidgetTemplateBuilder

A custom attribute that constructs a control widget template’s body.

```swift
@resultBuilder struct ControlWidgetTemplateBuilder
```

## Overview

The `@ControlWidgetTemplateBuilder` attribute allows your control template’s body closure to produce a control template after zero or more other statements:

```swift
struct GarageDoorOpener: ControlWidget {
    var body: some ControlWidgetConfiguration {
        let kind = "com.yourcompany.GarageDoorOpener"

        StaticControlConfiguration(
            kind: kind
        ) {
            let isOpen = ...

            ControlWidgetToggle(
                "Garage Door",
                isOn: isOpen,
                action: ToggleGarageDoor()
            ) {
                Label(
                    $0 ? "Open" : "Closed",
                    systemImage: $0 ?
                        "door.garage.open" : "door.garage.closed"
                )
            }
        }
    }
}
```

### Type Methods

- [buildBlock(_:)](/documentation/swiftui/controlwidgettemplatebuilder/buildblock(_:)): Passes a single control widget template written as a child view through unmodified.
- [buildExpression(_:)](/documentation/swiftui/controlwidgettemplatebuilder/buildexpression(_:)): Builds an expression within the builder.

## See Also

### Composing control widgets

- [ControlWidget](/documentation/swiftui/controlwidget): The configuration and content of a control widget to display in system spaces such as Control Center, the Lock Screen, and the Action Button.
- [ControlWidgetConfiguration](/documentation/swiftui/controlwidgetconfiguration): A type that describes a control widget’s content.
- [EmptyControlWidgetConfiguration](/documentation/swiftui/emptycontrolwidgetconfiguration): An empty control widget configuration.
- [ControlWidgetConfigurationBuilder](/documentation/swiftui/controlwidgetconfigurationbuilder): A custom attribute that constructs a control widget’s body.
- [ControlWidgetTemplate](/documentation/swiftui/controlwidgettemplate): A type that describes a control widget’s content.
- [EmptyControlWidgetTemplate](/documentation/swiftui/emptycontrolwidgettemplate): An empty control widget template.
- [controlWidgetActionHint(_:)](/documentation/swiftui/view/controlwidgetactionhint(_:)): The action hint of the control described by the modified label.
- [controlWidgetStatus(_:)](/documentation/swiftui/view/controlwidgetstatus(_:)): The status of the control described by the modified label.
