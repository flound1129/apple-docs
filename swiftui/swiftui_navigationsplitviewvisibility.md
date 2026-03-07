# NavigationSplitViewVisibility

The visibility of the leading columns in a navigation split view.

```swift
struct NavigationSplitViewVisibility
```

## Overview

Use a value of this type to control the visibility of the columns of a [NavigationSplitView](/documentation/swiftui/navigationsplitview). Create a [State](/documentation/swiftui/state) property with a value of this type, and pass a [Binding](/documentation/swiftui/binding) to that state to the [init(columnVisibility:sidebar:detail:)](/documentation/swiftui/navigationsplitview/init(columnvisibility:sidebar:detail:)) or [init(columnVisibility:sidebar:content:detail:)](/documentation/swiftui/navigationsplitview/init(columnvisibility:sidebar:content:detail:)) initializer when you create the navigation split view. You can then modify the value elsewhere in your code to:

- Hide all but the trailing column with [detailOnly](/documentation/swiftui/navigationsplitviewvisibility/detailonly).
- Hide the leading column of a three-column navigation split view with [doubleColumn](/documentation/swiftui/navigationsplitviewvisibility/doublecolumn).
- Show all the columns with [all](/documentation/swiftui/navigationsplitviewvisibility/all).
- Rely on the automatic behavior for the current context with [automatic](/documentation/swiftui/navigationsplitviewvisibility/automatic).

> **Note:**
> Some platforms don’t respect every option. For example, macOS always displays the content column.
>

### Getting visibilities

- [automatic](/documentation/swiftui/navigationsplitviewvisibility/automatic): Use the default leading column visibility for the current device.
- [all](/documentation/swiftui/navigationsplitviewvisibility/all): Show all the columns of a three-column navigation split view.
- [doubleColumn](/documentation/swiftui/navigationsplitviewvisibility/doublecolumn): Show the content column and detail area of a three-column navigation split view, or the sidebar column and detail area of a two-column navigation split view.
- [detailOnly](/documentation/swiftui/navigationsplitviewvisibility/detailonly): Hide the leading two columns of a three-column navigation split view, so that just the detail area shows.

## See Also

### Presenting views in columns

- [Bringing robust navigation structure to your SwiftUI app](/documentation/swiftui/bringing-robust-navigation-structure-to-your-swiftui-app): Use navigation links, stacks, destinations, and paths to provide a streamlined experience for all platforms, as well as behaviors such as deep linking and state restoration.
- [Migrating to new navigation types](/documentation/swiftui/migrating-to-new-navigation-types): Improve navigation behavior in your app by replacing navigation views with navigation stacks and navigation split views.
- [NavigationSplitView](/documentation/swiftui/navigationsplitview): A view that presents views in two or three columns, where selections in leading columns control presentations in subsequent columns.
- [navigationSplitViewStyle(_:)](/documentation/swiftui/view/navigationsplitviewstyle(_:)): Sets the style for navigation split views within this view.
- [navigationSplitViewColumnWidth(_:)](/documentation/swiftui/view/navigationsplitviewcolumnwidth(_:)): Sets a fixed, preferred width for the column containing this view.
- [navigationSplitViewColumnWidth(min:ideal:max:)](/documentation/swiftui/view/navigationsplitviewcolumnwidth(min:ideal:max:)): Sets a flexible, preferred width for the column containing this view.
- [NavigationLink](/documentation/swiftui/navigationlink): A view that controls a navigation presentation.
