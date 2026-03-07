# ButtonStyle

A type that applies standard interaction behavior and a custom appearance to all buttons within a view hierarchy.

```swift
@MainActor @preconcurrency protocol ButtonStyle
```

## Overview

To configure the current button style for a view hierarchy, use the [buttonStyle(_:)](/documentation/swiftui/view/buttonstyle(_:)) modifier. Specify a style that conforms to `ButtonStyle` when creating a button that uses the standard button interaction behavior defined for each platform. To create a button with custom interaction behavior, use [PrimitiveButtonStyle](/documentation/swiftui/primitivebuttonstyle) instead.

### Custom button styles

- [makeBody(configuration:)](/documentation/swiftui/buttonstyle/makebody(configuration:)): Creates a view that represents the body of a button.
- [ButtonStyle.Configuration](/documentation/swiftui/buttonstyle/configuration): The properties of a button.
- [Body](/documentation/swiftui/buttonstyle/body): A view that represents the body of a button.

## See Also

### Styling buttons

- [buttonStyle(_:)](/documentation/swiftui/view/buttonstyle(_:)): Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [ButtonStyleConfiguration](/documentation/swiftui/buttonstyleconfiguration): The properties of a button.
- [PrimitiveButtonStyle](/documentation/swiftui/primitivebuttonstyle): A type that applies custom interaction behavior and a custom appearance to all buttons within a view hierarchy.
- [PrimitiveButtonStyleConfiguration](/documentation/swiftui/primitivebuttonstyleconfiguration): The properties of a button.
- [signInWithAppleButtonStyle(_:)](/documentation/swiftui/view/signinwithapplebuttonstyle(_:)): Sets the style used for displaying the control (see `SignInWithAppleButton.Style`).
