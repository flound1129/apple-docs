# TextSelection

Represents a selection of text.

```swift
struct TextSelection
```

## Overview

A selection is either an insertion point (e.g. a cursor in the text), a selection over a range of text or on macOS, multiple selections.

This is frequently used to represent selection of text in a `TextField` or `TextEditor`. The following example shows a text editor that leverages text selection to offer live suggestions based on the current selection.

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
    }

    private func getSubstrings(
        text: String, indices: TextSelection.Indices?
    ) -> [Substring] {
        // Resolve substrings representing the current selection...
    }
}

struct SuggestionsView: View { ... }
```

You can also use the [textSelectionAffinity(_:)](/documentation/swiftui/view/textselectionaffinity(_:)) modifier to specify a selection affinity on the given hierarchy:

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

### Initializers

- [init(insertionPoint:)](/documentation/swiftui/textselection/init(insertionpoint:)): Create a selection at a given insertion point.
- [init(range:)](/documentation/swiftui/textselection/init(range:)): Create a single selection with a given range.
- [init(ranges:)](/documentation/swiftui/textselection/init(ranges:)): Create multiple selections with a given range-set.

### Instance Properties

- [affinity](/documentation/swiftui/textselection/affinity): Return the selection affinity of the selection.
- [indices](/documentation/swiftui/textselection/indices-swift.property): Return the current text selection indices.
- [isInsertion](/documentation/swiftui/textselection/isinsertion): Return `true` if the selection is an insertion point.

### Enumerations

- [TextSelection.Indices](/documentation/swiftui/textselection/indices-swift.enum): The indices of the current selection.

## See Also

### Selecting text

- [textSelection(_:)](/documentation/swiftui/view/textselection(_:)): Controls whether people can select text within this view.
- [TextSelectability](/documentation/swiftui/textselectability): A type that describes the ability to select text.
- [textSelectionAffinity(_:)](/documentation/swiftui/view/textselectionaffinity(_:)): Sets the direction of a selection or cursor relative to a text character.
- [textSelectionAffinity](/documentation/swiftui/environmentvalues/textselectionaffinity): A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [TextSelectionAffinity](/documentation/swiftui/textselectionaffinity): A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [AttributedTextSelection](/documentation/swiftui/attributedtextselection): Represents a selection of attributed text.
