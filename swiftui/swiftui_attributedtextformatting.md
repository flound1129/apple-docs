# AttributedTextFormatting

A namespace for types related to attributed text formatting definitions.

```swift
enum AttributedTextFormatting
```

## Overview

> **See Also:**
> [AttributedTextFormattingDefinition](/documentation/swiftui/attributedtextformattingdefinition), `View/attributedTextFormattingDefinition(_:)-uc57`
>

### Structures

- [AttributedTextFormatting.AnyDefinition](/documentation/swiftui/attributedtextformatting/anydefinition): A type-erased text formatting definition.
- [AttributedTextFormatting.AttributeContainerProxy](/documentation/swiftui/attributedtextformatting/attributecontainerproxy): A proxy for a partially validated set of attributes.
- [AttributedTextFormatting.DefinitionBuilder](/documentation/swiftui/attributedtextformatting/definitionbuilder): A result builder for attributed text formatting definition.
- [AttributedTextFormatting.EmptyDefinition](/documentation/swiftui/attributedtextformatting/emptydefinition): A text formatting definition that places no constraints on the values of attributes.
- [AttributedTextFormatting.Transferable](/documentation/swiftui/attributedtextformatting/transferable): A transferable representation of an attributed string interpreted in a SwiftUI environment.
- [AttributedTextFormatting.TupleDefinition](/documentation/swiftui/attributedtextformatting/tupledefinition): A text formatting definition that enforces the constraints of a series of text formatting definitions.
- [AttributedTextFormatting.ValueConstraint](/documentation/swiftui/attributedtextformatting/valueconstraint): A text formatting definition that constrains the value of a single attribute to the members of a set.

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
- [AttributedTextValueConstraint](/documentation/swiftui/attributedtextvalueconstraint): A protocol for defining a constraint on the value of a certain attribute.
