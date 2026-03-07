# ButtonRole

A value that describes the purpose of a button.

```swift
struct ButtonRole
```

## Overview

A button role provides a description of a button’s purpose.  For example, the [destructive](/documentation/swiftui/buttonrole/destructive) role indicates that a button performs a destructive action, like delete user data:

```swift
Button("Delete", role: .destructive) { delete() }
```

### Getting button roles

- [cancel](/documentation/swiftui/buttonrole/cancel): A role that indicates a button that cancels an operation.
- [destructive](/documentation/swiftui/buttonrole/destructive): A role that indicates a destructive button.

### Type Properties

- [close](/documentation/swiftui/buttonrole/close): A role that indicates a button that closes the current operation.
- [confirm](/documentation/swiftui/buttonrole/confirm): A role that indicates a button that confirms an operation.

## See Also

### Creating buttons

- [Button](/documentation/swiftui/button): A control that initiates an action.
- [buttonStyle(_:)](/documentation/swiftui/view/buttonstyle(_:)): Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [buttonBorderShape(_:)](/documentation/swiftui/view/buttonbordershape(_:)): Sets the border shape for buttons in this view.
- [buttonRepeatBehavior(_:)](/documentation/swiftui/view/buttonrepeatbehavior(_:)): Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.
- [buttonRepeatBehavior](/documentation/swiftui/environmentvalues/buttonrepeatbehavior): Whether buttons with this associated environment should repeatedly trigger their actions on prolonged interactions.
- [ButtonBorderShape](/documentation/swiftui/buttonbordershape): A shape used to draw a button’s border.
- [ButtonRepeatBehavior](/documentation/swiftui/buttonrepeatbehavior): The options for controlling the repeatability of button actions.
- [ButtonSizing](/documentation/swiftui/buttonsizing): The sizing behavior of `Button`s and other button-like controls.
