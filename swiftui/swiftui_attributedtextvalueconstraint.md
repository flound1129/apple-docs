# AttributedTextValueConstraint

A protocol for defining a constraint on the value of a certain attribute.

```swift
protocol AttributedTextValueConstraint : Hashable, Sendable, AttributedTextFormattingDefinition
```

## Overview

Used as an [AttributedTextFormattingDefinition](/documentation/swiftui/attributedtextformattingdefinition), this constrains the [AttributeKey](/documentation/swiftui/attributedtextvalueconstraint/attributekey)’s value using the `constrain(_:)-(Attributes)` function.

Given value constraints can read other attribute values, it is crucial to avoid mixing value constraints in a way where they create cyclic dependencies with undefined behavior. Thus, it is recommended to think about value constraints in the context of the [AttributedTextFormattingDefinition](/documentation/swiftui/attributedtextformattingdefinition) they will be used in:

A simple constraint only accesses a single attribute. It can be made generic over the attribute scope so it can be reused in different [AttributedTextFormattingDefinition](/documentation/swiftui/attributedtextformattingdefinition)s.

```swift
struct NoBlackOrWhiteForeground<Scope: AttributeScope>: AttributedTextValueConstraint {
    typealias AttributeKey = AttributeScopes.SwiftUIAttributes.ForegroundColorAttribute

    func constrain(
        _ container: inout Attributes
    ) {
        if container.foregroundColor == .white || container.foregroundColor == .black {
            container.foregroundColor = .primary
        }
    }
}
```

When the constraint needs to access other attribute values, it is recommended to define it on a specific attribute scope that is used for a single [AttributedTextFormattingDefinition](/documentation/swiftui/attributedtextformattingdefinition).

```swift
extension MyTextFormattingDefinition {
    struct Scope: AttributeScope {
        /* ... */
        let foregroundColor: AttributeScopes.SwiftUIAttributes.ForegroundColorAttribute
        let backgroundColor: AttributeScopes.SwiftUIAttributes.BackgroundColorAttribute
    }
}

struct NoEqualForegroundAndBackground: AttributedTextValueConstraint {
    typealias Scope = MyTextFormattingDefinition.Scope
    typealias AttributeKey = AttributeScopes.SwiftUIAttributes.BackgroundColorAttribute

    func constrain(
        _ container: inout Attributes
    ) {
        if let color = container.foregroundColor,
           container.backgroundColor == color
        {
            container.backgroundColor = nil
        }
    }
}
```

Constraints that access multiple attributes and are generic over the scope should document their dependencies so that the dependencies can be considered for the ordering of constraints in the [body](/documentation/swiftui/attributedtextformattingdefinition/body-1b01t).

```swift
/// Makes the background color for all Genmoji blue.
///
/// - Note: This constraint depends on a valid adaptiveImageGlyph value.
struct BlueGenmojiBackgroundConstraint<Scope: AttributeScope>: AttributedTextValueConstraint {
    typealias AttributeKey = AttributeScopes.SwiftUIAttributes
        .BackgroundColorAttribute

    func constrain(
        _ container: inout Attributes
    ) {
        if container[
            AttributeScopes.SwiftUIAttributes.AdaptiveImageGlyphAttribute.self
        ] != nil {
            container.backgroundColor = .blue
        }
    }
}
```

### Associated Types

- [AttributeKey](/documentation/swiftui/attributedtextvalueconstraint/attributekey): The attribute constrained by this constraint.

### Instance Methods

- [constrain(_:)](/documentation/swiftui/attributedtextvalueconstraint/constrain(_:)): Enforce constraints on the attribute.

### Type Aliases

- [AttributedTextValueConstraint.Attributes](/documentation/swiftui/attributedtextvalueconstraint/attributes): A proxy type for a container of partially constrained attributes.

## See Also

### Controlling text style

- [bold(_:)](/documentation/swiftui/view/bold(_:)): Applies a bold font weight to the text in this view.
- [italic(_:)](/documentation/swiftui/view/italic(_:)): Applies italics to the text in this view.
- [underline(_:pattern:color:)](/documentation/swiftui/view/underline(_:pattern:color:)): Applies an underline to the text in this view.
- [strikethrough(_:pattern:color:)](/documentation/swiftui/view/strikethrough(_:pattern:color:)): Applies a strikethrough to the text in this view.
- [textCase(_:)](/documentation/swiftui/view/textcase(_:)): Sets a transform for the case of the text contained in this view when displayed.
- [textCase](/documentation/swiftui/environmentvalues/textcase): A stylistic override to transform the case of `Text` when displayed, using the environment’s locale.
- [monospaced(_:)](/documentation/swiftui/view/monospaced(_:)): Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [monospacedDigit()](/documentation/swiftui/view/monospaceddigit()): Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [AttributedTextFormattingDefinition](/documentation/swiftui/attributedtextformattingdefinition): A protocol for defining how text can be styled in a view.
- [AttributedTextFormatting](/documentation/swiftui/attributedtextformatting): A namespace for types related to attributed text formatting definitions.
