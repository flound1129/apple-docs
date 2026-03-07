# NavigationView

A view for presenting a stack of views that represents a visible path in a navigation hierarchy.

```swift
struct NavigationView<Content> where Content : View
```

## Overview

Use a `NavigationView` to create a navigation-based app in which the user can traverse a collection of views. Users navigate to a destination view by selecting a [NavigationLink](/documentation/swiftui/navigationlink) that you provide. On iPadOS and macOS, the destination content appears in the next column. Other platforms push a new view onto the stack, and enable removing items from the stack with platform-specific controls, like a Back button or a swipe gesture.

![A diagram showing a multicolumn navigation view on macOS, and a stack of views on iOS.]

Use the [init(content:)](/documentation/swiftui/navigationview/init(content:)) initializer to create a navigation view that directly associates navigation links and their destination views:

```swift
NavigationView {
    List(model.notes) { note in
        NavigationLink(note.title, destination: NoteEditor(id: note.id))
    }
    Text("Select a Note")
}
```

Style a navigation view by modifying it with the [navigationViewStyle(_:)](/documentation/swiftui/view/navigationviewstyle(_:)) view modifier. Use other modifiers, like [navigationTitle(_:)](/documentation/swiftui/view/navigationtitle(_:)-avgj), on views presented by the navigation view to customize the navigation interface for the presented view.

### Creating a navigation view

- [init(content:)](/documentation/swiftui/navigationview/init(content:)): Creates a destination-based navigation view.

### Styling navigation views

- [navigationViewStyle(_:)](/documentation/swiftui/view/navigationviewstyle(_:)): Sets the style for navigation views within this view.
- [NavigationViewStyle](/documentation/swiftui/navigationviewstyle): A specification for the appearance and interaction of a navigation view.

## See Also

### Deprecated Types

- [tabItem(_:)](/documentation/swiftui/view/tabitem(_:)): Sets the tab bar item associated with this view.
