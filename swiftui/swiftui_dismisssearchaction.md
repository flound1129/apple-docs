# DismissSearchAction

An action that can end a search interaction.

```swift
@MainActor @preconcurrency struct DismissSearchAction
```

## Overview

Use the [dismissSearch](/documentation/swiftui/environmentvalues/dismisssearch) environment value to get the instance of this structure for a given [Environment](/documentation/swiftui/environment). Then call the instance to dismiss the current search interaction. You call the instance directly because it defines a [callAsFunction()](/documentation/swiftui/dismisssearchaction/callasfunction()) method that Swift calls when you call the instance.

When you dismiss search, SwiftUI:

- Sets [isSearching](/documentation/swiftui/environmentvalues/issearching) to `false`.
- Clears any text from the search field.
- Removes focus from the search field.

> **Note:**
> Calling this instance has no effect if the user isn’t interacting with a search field.
>

Use this action to dismiss a search operation based on another user interaction. For example, consider a searchable view with a [Button](/documentation/swiftui/button) that presents more information about the first matching item from a collection:

```swift
struct ContentView: View {
    @State private var searchText = ""

    var body: some View {
        NavigationStack {
            SearchedView(searchText: searchText)
                .searchable(text: $searchText)
        }
    }
}

struct SearchedView: View {
    var searchText: String

    let items = ["a", "b", "c"]
    var filteredItems: [String] { items.filter { $0 == searchText.lowercased() } }

    @State private var isPresented = false
    @Environment(\.dismissSearch) private var dismissSearch

    var body: some View {
        if let item = filteredItems.first {
            Button("Details about \(item)") {
                isPresented = true
            }
            .sheet(isPresented: $isPresented) {
                NavigationStack {
                    DetailView(item: item, dismissSearch: dismissSearch)
                }
            }
        }
    }
}
```

The button becomes visible only after the user enters search text that produces a match. When the user taps the button, SwiftUI shows a sheet that provides more information about the item, including an Add button for adding the item to a stored list of items:

```swift
private struct DetailView: View {
    var item: String
    var dismissSearch: DismissSearchAction

    @Environment(\.dismiss) private var dismiss

    var body: some View {
        Text("Information about \(item).")
            .toolbar {
                Button("Add") {
                    // Store the item here...

                    dismiss()
                    dismissSearch()
                }
            }
    }
}
```

People can dismiss the sheet by dragging it down, effectively canceling the operation, leaving the in-progress search interaction intact. Alternatively, people can tap the Add button to store the item. Because the person using your app is likely to be done with both the detail view and the search interaction at this point, the button’s closure also uses the [dismiss](/documentation/swiftui/environmentvalues/dismiss) property to dismiss the sheet, and the [dismissSearch](/documentation/swiftui/environmentvalues/dismisssearch) property to reset the search field.

> **Important:**
> Access the action from inside the searched view, as the example above demonstrates, rather than from the searched view’s parent, or another hierarchy, like that of a sheet. SwiftUI sets the value in the environment of the view that you apply the searchable modifier to, and doesn’t propagate the value up the view hierarchy.
>

### Calling the action

- [callAsFunction()](/documentation/swiftui/dismisssearchaction/callasfunction()): Dismisses the current search operation, if any.

## See Also

### Detecting, activating, and dismissing search

- [Managing search interface activation](/documentation/swiftui/managing-search-interface-activation): Programmatically detect and dismiss a search field.
- [isSearching](/documentation/swiftui/environmentvalues/issearching): A Boolean value that indicates when the user is searching.
- [dismissSearch](/documentation/swiftui/environmentvalues/dismisssearch): An action that ends the current search interaction.
- [searchable(text:isPresented:placement:prompt:)](/documentation/swiftui/view/searchable(text:ispresented:placement:prompt:)): Marks this view as searchable with programmatic presentation of the search field.
- [searchable(text:tokens:isPresented:placement:prompt:token:)](/documentation/swiftui/view/searchable(text:tokens:ispresented:placement:prompt:token:)): Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [searchable(text:editableTokens:isPresented:placement:prompt:token:)](/documentation/swiftui/view/searchable(text:editabletokens:ispresented:placement:prompt:token:)): Marks this view as searchable, which configures the display of a search field.
- [searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)](/documentation/swiftui/view/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)): Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
