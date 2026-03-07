# TabViewBottomAccessoryPlacement

A placement of the bottom accessory in a tab view. You can use this to adjust the content of the accessory view based on the placement.

```swift
enum TabViewBottomAccessoryPlacement
```

## Overview

The following example shows playback controls when the view is inline, and an expanded slider player view when the view is expanded.

```swift
struct MusicPlaybackView: View {
    @Environment(\.tabViewBottomAccessoryPlacement) var placement

    var body: some View {
        switch placement {
        case .inline:
            ControlsPlaybackView()
        case .expanded:
            SliderPlaybackView()
    }
}
```

You can set the `TabView` bottom accessory using [tabViewBottomAccessory(content:)](/documentation/swiftui/view/tabviewbottomaccessory(content:))

```swift
TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }

    Tab("Alerts", systemImage: "bell") {
        AlertsView()
    }

    TabSection("Categories") {
        Tab("Climate", systemImage: "fan") {
            ClimateView()
        }

        Tab("Lights", systemImage: "lightbulb") {
            LightsView()
        }
    }
}
.tabViewBottomAccessory {
    HomeStatusView()
}
```

### Enumeration Cases

- [TabViewBottomAccessoryPlacement.expanded](/documentation/swiftui/tabviewbottomaccessoryplacement/expanded): The bar is expanded on top of the bottom tab bar, if there is a bottom tab bar, or at the bottom of the tab’s content view.
- [TabViewBottomAccessoryPlacement.inline](/documentation/swiftui/tabviewbottomaccessoryplacement/inline): The view is displayed in line with the bottom tab bar.

## See Also

### Configuring a tab bar

- [defaultAdaptableTabBarPlacement(_:)](/documentation/swiftui/view/defaultadaptabletabbarplacement(_:)): Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.
- [tabViewSidebarHeader(content:)](/documentation/swiftui/view/tabviewsidebarheader(content:)): Adds a custom header to the sidebar of a tab view.
- [tabViewSidebarFooter(content:)](/documentation/swiftui/view/tabviewsidebarfooter(content:)): Adds a custom footer to the sidebar of a tab view.
- [tabViewSidebarBottomBar(content:)](/documentation/swiftui/view/tabviewsidebarbottombar(content:)): Adds a custom bottom bar to the sidebar of a tab view.
- [AdaptableTabBarPlacement](/documentation/swiftui/adaptabletabbarplacement): A placement for tabs in a tab view using the adaptable sidebar style.
- [tabBarPlacement](/documentation/swiftui/environmentvalues/tabbarplacement): The current placement of the tab bar.
- [TabBarPlacement](/documentation/swiftui/tabbarplacement): A placement for tabs in a tab view.
- [isTabBarShowingSections](/documentation/swiftui/environmentvalues/istabbarshowingsections): A Boolean value that determines whether a tab view shows the expanded contents of a tab section.
- [TabBarMinimizeBehavior](/documentation/swiftui/tabbarminimizebehavior)
