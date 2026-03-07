# TextSelectionAffinity

A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).

```swift
enum TextSelectionAffinity
```

## Overview

This type also determines whether, for example, the insertion point appears after the last character on a line or before the first character on the following line in cases where text wraps across line boundaries.

Given the scenario `hello|مرحبا`, where `|` represents the cursor & `مرحبا` represents “hello” in Arabic, the ambiguity arises because:

- If the cursor is associated with the end of the English word, it would be as if you’re continuing to type in English (LTR).
- If the cursor is associated with the beginning of the Arabic word, it would also be as if you’re continuing to type in Arabic (RTL).

`TextSelectionAffinity` helps resolve this ambiguity by determining the direction or association of the cursor relative to the surrounding text.

You can configure the selection affinity on a given hierarchy by using the [textSelectionAffinity(_:)](/documentation/swiftui/view/textselectionaffinity(_:)) modifier:

```swift
struct SuggestionTextEditor: View {
    @State var text: String = ""
    @State var selection: TextSelection? = nil

    var body: some View {
        VStack {
            TextEditor(text: $text, selection: $selection)
            // A helper view that offers live suggestions based on selection.
            SuggestionsView(
                substrings: getSubstrings(text: text, indices: selection?.indices))
        }
        .textSelectionAffinity(.upstream)
    }

    private func getSubstrings(
        text: String, indices: TextSelection.Indices?
    ) -> [Substring] {
        // Resolve substrings representing the current selection...
    }
}

struct SuggestionsView: View { ... }
```

### Enumeration Cases

- [TextSelectionAffinity.automatic](/documentation/swiftui/textselectionaffinity/automatic): A selection affinity determined by the framework based on the current context.
- [TextSelectionAffinity.downstream](/documentation/swiftui/textselectionaffinity/downstream): An downstream selection affinity. In this case, the cursor is associated with the character immediately after it.
- [TextSelectionAffinity.upstream](/documentation/swiftui/textselectionaffinity/upstream): An upstream selection affinity. In this case, the cursor is associated with the character immediately before it.

## See Also

### Selecting text

- [textSelection(_:)](/documentation/swiftui/view/textselection(_:)): Controls whether people can select text within this view.
- [TextSelectability](/documentation/swiftui/textselectability): A type that describes the ability to select text.
- [TextSelection](/documentation/swiftui/textselection): Represents a selection of text.
- [textSelectionAffinity(_:)](/documentation/swiftui/view/textselectionaffinity(_:)): Sets the direction of a selection or cursor relative to a text character.
- [textSelectionAffinity](/documentation/swiftui/environmentvalues/textselectionaffinity): A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [AttributedTextSelection](/documentation/swiftui/attributedtextselection): Represents a selection of attributed text.
