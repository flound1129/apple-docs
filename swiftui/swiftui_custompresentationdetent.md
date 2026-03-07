# CustomPresentationDetent

The definition of a custom detent with a calculated height.

```swift
protocol CustomPresentationDetent
```

## Overview

You can create and use a custom detent with built-in detents.

```swift
extension PresentationDetent {
    static let bar = Self.custom(BarDetent.self)
    static let small = Self.height(100)
    static let extraLarge = Self.fraction(0.75)
}

private struct BarDetent: CustomPresentationDetent {
    static func height(in context: Context) -> CGFloat? {
        max(44, context.maxDetentValue * 0.1)
    }
}

struct ContentView: View {
    @State private var showSettings = false
    @State private var selectedDetent = PresentationDetent.bar

    var body: some View {
        Button("View Settings") {
            showSettings = true
        }
        .sheet(isPresented: $showSettings) {
            SettingsView(selectedDetent: $selectedDetent)
                .presentationDetents(
                    [.bar, .small, .medium, .large, .extraLarge],
                    selection: $selectedDetent)
        }
    }
}
```

### Getting the height

- [height(in:)](/documentation/swiftui/custompresentationdetent/height(in:)): Calculates and returns a height based on the context.
- [CustomPresentationDetent.Context](/documentation/swiftui/custompresentationdetent/context): Information that you can use to calculate the height of a custom detent.

## See Also

### Configuring a sheet’s height

- [presentationDetents(_:)](/documentation/swiftui/view/presentationdetents(_:)): Sets the available detents for the enclosing sheet.
- [presentationDetents(_:selection:)](/documentation/swiftui/view/presentationdetents(_:selection:)): Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [presentationContentInteraction(_:)](/documentation/swiftui/view/presentationcontentinteraction(_:)): Configures the behavior of swipe gestures on a presentation.
- [presentationDragIndicator(_:)](/documentation/swiftui/view/presentationdragindicator(_:)): Sets the visibility of the drag indicator on top of a sheet.
- [PresentationDetent](/documentation/swiftui/presentationdetent): A type that represents a height where a sheet naturally rests.
- [PresentationContentInteraction](/documentation/swiftui/presentationcontentinteraction): A behavior that you can use to influence how a presentation responds to swipe gestures.
