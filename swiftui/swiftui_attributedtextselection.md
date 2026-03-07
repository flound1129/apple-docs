# AttributedTextSelection

Represents a selection of attributed text.

```swift
struct AttributedTextSelection
```

## Overview

A selection is either an insertion point (e.g. a cursor in the text), or spans over a range of characters. While that range is always visually contiguous, it may not be logically contiguous in the text storage. Specifically, a single selection value cannot represent multiple cursors.

This is frequently used to represent selection of text in a `TextEditor`. The following example shows a text editor that leverages text selection to offer live suggestions based on the current selection.

```swift
struct SuggestionTextEditor: View {
    @State var text: AttributedString = ""
    @State var selection = AttributedTextSelection()

    var body: some View {
        VStack {
            TextEditor(text: $text, selection: $selection)
            // A helper view that offers live suggestions based on selection.
            SuggestionsView(substrings: getSubstrings(
                text: text, indices: selection.indices(in: text))
        }
    }

    private func getSubstrings(
        text: String, indices: AttributedTextSelection.Indices
    ) -> [Substring] {
        // Resolve substrings representing the current selection...
    }
}

struct SuggestionsView: View { ... }
```

You can also use the [textSelectionAffinity(_:)](/documentation/swiftui/view/textselectionaffinity(_:)) modifier to specify a selection affinity on the given hierarchy:

```swift
struct SuggestionTextEditor: View {
    @State var text: AttributedString = ""
    @State var selection = AttributedTextSelection()

    var body: some View {
        VStack {
            TextEditor(text: $text, selection: $selection)
            // A helper view that offers live suggestions based on selection.
            SuggestionsView(substrings: getSubstrings(
                text: text, indices: selection.indices(in: text))
        }
        .textSelectionAffinity(.upstream)
    }

    private func getSubstrings(
        text: String, indices: AttributedTextSelection.Indices
    ) -> [Substring] {
        // Resolve substrings representing the current selection...
    }
}

struct SuggestionsView: View { ... }
```

> **See Also:**
> [TextSelectionAffinity](/documentation/swiftui/textselectionaffinity), [TextEditor](/documentation/swiftui/texteditor)
>

### Structures

- [AttributedTextSelection.Attributes](/documentation/swiftui/attributedtextselection/attributes): A sequence of all attribute values a selection has in a certain text.

### Initializers

- [init()](/documentation/swiftui/attributedtextselection/init()): Initialize the default selection for a new text editor.
- [init(insertionPoint:typingAttributes:)](/documentation/swiftui/attributedtextselection/init(insertionpoint:typingattributes:)): Initialize a selection to a single insertion point.
- [init(range:)](/documentation/swiftui/attributedtextselection/init(range:)): Initialize a selection to a character range.
- [init(ranges:)](/documentation/swiftui/attributedtextselection/init(ranges:)): Initialize a selection to character ranges.

### Instance Methods

- [affinity(in:)](/documentation/swiftui/attributedtextselection/affinity(in:)): Return the selection affinity of the selection.
- [attributes(in:)](/documentation/swiftui/attributedtextselection/attributes(in:)): Obtain a lazy sequence of all attribute values the selection has in a given text.
- [indices(in:)](/documentation/swiftui/attributedtextselection/indices(in:)): The current text selection indices.
- [typingAttributes(in:)](/documentation/swiftui/attributedtextselection/typingattributes(in:)): Returns the typing attributes for a corresponding text.

### Enumerations

- [AttributedTextSelection.Indices](/documentation/swiftui/attributedtextselection/indices): The indices of the current selection.

## See Also

### Selecting text

- [textSelection(_:)](/documentation/swiftui/view/textselection(_:)): Controls whether people can select text within this view.
- [TextSelectability](/documentation/swiftui/textselectability): A type that describes the ability to select text.
- [TextSelection](/documentation/swiftui/textselection): Represents a selection of text.
- [textSelectionAffinity(_:)](/documentation/swiftui/view/textselectionaffinity(_:)): Sets the direction of a selection or cursor relative to a text character.
- [textSelectionAffinity](/documentation/swiftui/environmentvalues/textselectionaffinity): A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [TextSelectionAffinity](/documentation/swiftui/textselectionaffinity): A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
