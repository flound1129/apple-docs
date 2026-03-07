# TabSection

A container that you can use to add hierarchy within a tab view.

```swift
struct TabSection<Header, Content, Footer, SelectionValue>
```

## Overview

Use [TabSection](/documentation/swiftui/tabsection) to organize tab content into separate sections. Each section has custom tab content that you provide on a per-instance basis. You can also provide a header for each section.

### Creating a tab section

- [init(content:)](/documentation/swiftui/tabsection/init(content:)): Creates a section with the provided section content.
- [init(_:content:)](/documentation/swiftui/tabsection/init(_:content:)): Creates a section with the provided content.
- [init(content:header:)](/documentation/swiftui/tabsection/init(content:header:)): Creates a section with a header and the provided section content.

### Supporting types

- [DefaultTabLabel](/documentation/swiftui/defaulttablabel): The default label to use for a tab or tab section.

## See Also

### Presenting views in tabs

- [Enhancing your app’s content with tab navigation](/documentation/swiftui/enhancing-your-app-content-with-tab-navigation): Keep your app content front and center while providing quick access to navigation using the tab bar.
- [TabView](/documentation/swiftui/tabview): A view that switches between multiple child views using interactive user interface elements.
- [Tab](/documentation/swiftui/tab): The content for a tab and the tab’s associated tab item in a tab view.
- [TabRole](/documentation/swiftui/tabrole): A value that defines the purpose of the tab.
- [tabViewStyle(_:)](/documentation/swiftui/view/tabviewstyle(_:)): Sets the style for the tab view within the current environment.
