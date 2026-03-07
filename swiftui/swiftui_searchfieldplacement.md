# SearchFieldPlacement

The placement of a search field in a view hierarchy.

```swift
struct SearchFieldPlacement
```

## Overview

You can give a preferred placement to any of the searchable modifiers, like [searchable(text:placement:prompt:)](/documentation/swiftui/view/searchable(text:placement:prompt:)):

```swift
var body: some View {
    NavigationView {
        PrimaryView()
        SecondaryView()
        Text("Select a primary and secondary item")
    }
    .searchable(text: $text, placement: .sidebar)
}
```

Depending on the containing view hierachy, SwiftUI might not be able to fulfill your request.

### Getting a search field placement

- [automatic](/documentation/swiftui/searchfieldplacement/automatic): SwiftUI places the search field automatically.
- [navigationBarDrawer](/documentation/swiftui/searchfieldplacement/navigationbardrawer): The search field appears in the navigation bar.
- [navigationBarDrawer(displayMode:)](/documentation/swiftui/searchfieldplacement/navigationbardrawer(displaymode:)): The search field appears in the navigation bar using the specified display mode.
- [sidebar](/documentation/swiftui/searchfieldplacement/sidebar): The search field appears in the sidebar of a navigation view.
- [toolbar](/documentation/swiftui/searchfieldplacement/toolbar): The search field appears in the toolbar.

### Supporting types

- [SearchFieldPlacement.NavigationBarDrawerDisplayMode](/documentation/swiftui/searchfieldplacement/navigationbardrawerdisplaymode): A mode that determines when to display a search field that appears in a navigation bar.

### Type Properties

- [toolbarPrincipal](/documentation/swiftui/searchfieldplacement/toolbarprincipal): The search field appears in the principal section of the toolbar.

## See Also

### Searching your app’s data model

- [Adding a search interface to your app](/documentation/swiftui/adding-a-search-interface-to-your-app): Present an interface that people can use to search for content in your app.
- [Performing a search operation](/documentation/swiftui/performing-a-search-operation): Update search results based on search text and optional tokens that you store.
- [searchable(text:placement:prompt:)](/documentation/swiftui/view/searchable(text:placement:prompt:)): Marks this view as searchable, which configures the display of a search field.
- [searchable(text:tokens:placement:prompt:token:)](/documentation/swiftui/view/searchable(text:tokens:placement:prompt:token:)): Marks this view as searchable with text and tokens.
- [searchable(text:editableTokens:placement:prompt:token:)](/documentation/swiftui/view/searchable(text:editabletokens:placement:prompt:token:)): Marks this view as searchable, which configures the display of a search field.
