# TabViewStyle

A specification for the appearance and interaction of a tab view.

```swift
@MainActor @preconcurrency protocol TabViewStyle
```

## Overview

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

### Getting built-in tab view styles

- [automatic](/documentation/swiftui/tabviewstyle/automatic): The default tab view style.
- [sidebarAdaptable](/documentation/swiftui/tabviewstyle/sidebaradaptable): A tab bar style that adapts to each platform.
- [tabBarOnly](/documentation/swiftui/tabviewstyle/tabbaronly): A tab view style that displays a tab bar when possible.
- [grouped](/documentation/swiftui/tabviewstyle/grouped): A tab view style that displays a tab bar that groups its tabs together.
- [page](/documentation/swiftui/tabviewstyle/page): A `TabViewStyle` that displays a paged scrolling `TabView`.
- [page(indexDisplayMode:)](/documentation/swiftui/tabviewstyle/page(indexdisplaymode:)): A `TabViewStyle` that implements a paged scrolling `TabView` with an index display mode.
- [verticalPage](/documentation/swiftui/tabviewstyle/verticalpage): A `TabViewStyle` that displays a vertical page `TabView` interaction and appearance.
- [verticalPage(transitionStyle:)](/documentation/swiftui/tabviewstyle/verticalpage(transitionstyle:)): A `TabViewStyle` that implements the vertical page `TabView` interaction and appearance, and performs the specified transition.
- [carousel](/documentation/swiftui/tabviewstyle/carousel): A style that implements the carousel interaction and appearance.

### Supporting types

- [DefaultTabViewStyle](/documentation/swiftui/defaulttabviewstyle): The default tab view style.
- [SidebarAdaptableTabViewStyle](/documentation/swiftui/sidebaradaptabletabviewstyle): A tab bar style that adapts to each platform.
- [TabBarOnlyTabViewStyle](/documentation/swiftui/tabbaronlytabviewstyle): A tab view style that displays a tab bar when possible.
- [GroupedTabViewStyle](/documentation/swiftui/groupedtabviewstyle): A tab view style that displays a tab bar that groups its tabs together.
- [PageTabViewStyle](/documentation/swiftui/pagetabviewstyle): A `TabViewStyle` that displays a paged scrolling `TabView`.
- [VerticalPageTabViewStyle](/documentation/swiftui/verticalpagetabviewstyle): A `TabViewStyle` that displays a vertical `TabView` interaction and appearance.
- [CarouselTabViewStyle](/documentation/swiftui/carouseltabviewstyle): A style that implements the carousel interaction and appearance.

## See Also

### Styling navigation views

- [navigationSplitViewStyle(_:)](/documentation/swiftui/view/navigationsplitviewstyle(_:)): Sets the style for navigation split views within this view.
- [NavigationSplitViewStyle](/documentation/swiftui/navigationsplitviewstyle): A type that specifies the appearance and interaction of navigation split views within a view hierarchy.
- [tabViewStyle(_:)](/documentation/swiftui/view/tabviewstyle(_:)): Sets the style for the tab view within the current environment.
