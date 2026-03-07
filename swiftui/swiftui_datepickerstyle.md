# DatePickerStyle

A type that specifies the appearance and interaction of all date pickers within a view hierarchy.

```swift
@MainActor @preconcurrency protocol DatePickerStyle
```

## Overview

To configure the current date picker style for a view hierarchy, use the [datePickerStyle(_:)](/documentation/swiftui/view/datepickerstyle(_:)) modifier.

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

### Getting built-in date picker styles

- [automatic](/documentation/swiftui/datepickerstyle/automatic): The default style for date pickers.
- [compact](/documentation/swiftui/datepickerstyle/compact): A date picker style that displays the components in a compact, textual format.
- [field](/documentation/swiftui/datepickerstyle/field): A date picker style that displays the components in an editable field.
- [graphical](/documentation/swiftui/datepickerstyle/graphical): A date picker style that displays an interactive calendar or clock.
- [stepperField](/documentation/swiftui/datepickerstyle/stepperfield): A system style that displays the components in an editable field, with adjoining stepper that can increment/decrement the selected component.
- [wheel](/documentation/swiftui/datepickerstyle/wheel): A date picker style that displays each component as columns in a scrollable wheel.

### Creating custom date picker styles

- [makeBody(configuration:)](/documentation/swiftui/datepickerstyle/makebody(configuration:)): Returns the appearance and interaction content for a `DatePicker`.
- [DatePickerStyleConfiguration](/documentation/swiftui/datepickerstyleconfiguration): The properties of a `DatePicker`.
- [DatePickerStyle.Configuration](/documentation/swiftui/datepickerstyle/configuration): A type alias for the properties of a `DatePicker`.
- [Body](/documentation/swiftui/datepickerstyle/body): A view representing the appearance and interaction of a `DatePicker`.

### Supporting types

- [DefaultDatePickerStyle](/documentation/swiftui/defaultdatepickerstyle): The default style for date pickers.
- [CompactDatePickerStyle](/documentation/swiftui/compactdatepickerstyle): A date picker style that displays the components in a compact, textual format.
- [FieldDatePickerStyle](/documentation/swiftui/fielddatepickerstyle): A date picker style that displays the components in an editable field.
- [GraphicalDatePickerStyle](/documentation/swiftui/graphicaldatepickerstyle): A date picker style that displays an interactive calendar or clock.
- [StepperFieldDatePickerStyle](/documentation/swiftui/stepperfielddatepickerstyle): A system style that displays the components in an editable field, with adjoining stepper that can increment/decrement the selected component.
- [WheelDatePickerStyle](/documentation/swiftui/wheeldatepickerstyle): A date picker style that displays each component as columns in a scrollable wheel.

## See Also

### Styling pickers

- [pickerStyle(_:)](/documentation/swiftui/view/pickerstyle(_:)): Sets the style for pickers within this view.
- [PickerStyle](/documentation/swiftui/pickerstyle): A type that specifies the appearance and interaction of all pickers within a view hierarchy.
- [datePickerStyle(_:)](/documentation/swiftui/view/datepickerstyle(_:)): Sets the style for date pickers within this view.
