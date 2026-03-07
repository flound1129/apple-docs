# SearchSuggestionsPlacement

The ways that SwiftUI displays search suggestions.

```swift
struct SearchSuggestionsPlacement
```

## Overview

You can influence which modes SwiftUI displays search suggestions for by using the [searchSuggestions(_:for:)](/documentation/swiftui/view/searchsuggestions(_:for:)) modifier:

```swift
enum FruitSuggestion: String, Identifiable {
    case apple, banana, orange
    var id: Self { self }
}

@State private var text = ""
@State private var suggestions: [FruitSuggestion] = []

var body: some View {
    MainContent()
        .searchable(text: $text) {
            ForEach(suggestions) { suggestion in
                Text(suggestion.rawValue)
                    .searchCompletion(suggestion.rawValue)
            }
            .searchSuggestions(.hidden, for: .content)
        }
}
```

In the above example, SwiftUI only displays search suggestions in a suggestions menu. You might want to do this when you want to render search suggestions in a container, like inline with your own set of search results.

You can get the current search suggestion placement by querying the [searchSuggestionsPlacement](/documentation/swiftui/environmentvalues/searchsuggestionsplacement) environment value in your search suggestions.

### Getting placements

- [automatic](/documentation/swiftui/searchsuggestionsplacement/automatic): Search suggestions render automatically based on the surrounding context.
- [content](/documentation/swiftui/searchsuggestionsplacement/content): Search suggestions render in the main content of the app.
- [menu](/documentation/swiftui/searchsuggestionsplacement/menu): Search suggestions render inside of a menu attached to the search field.

### Supporting types

- [SearchSuggestionsPlacement.Set](/documentation/swiftui/searchsuggestionsplacement/set): An efficient set of search suggestion display modes.

## See Also

### Making search suggestions

- [Suggesting search terms](/documentation/swiftui/suggesting-search-terms): Provide suggestions to people searching for content in your app.
- [searchSuggestions(_:)](/documentation/swiftui/view/searchsuggestions(_:)): Configures the search suggestions for this view.
- [searchSuggestions(_:for:)](/documentation/swiftui/view/searchsuggestions(_:for:)): Configures how to display search suggestions within this view.
- [searchCompletion(_:)](/documentation/swiftui/view/searchcompletion(_:)): Associates a fully formed string with the value of this view when used as a search suggestion.
- [searchable(text:tokens:suggestedTokens:placement:prompt:token:)](/documentation/swiftui/view/searchable(text:tokens:suggestedtokens:placement:prompt:token:)): Marks this view as searchable with text, tokens, and suggestions.
