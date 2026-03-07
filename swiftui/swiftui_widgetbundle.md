# WidgetBundle

A container used to expose multiple widgets from a single widget extension.

```swift
@MainActor @preconcurrency protocol WidgetBundle
```

## Overview

To support multiple types of widgets, add the `@main` attribute to a structure that conforms to `WidgetBundle`. For example, a game might have one widget to display summary information about the game and a second widget to display detailed information about individual characters.

```swift
@main
struct GameWidgets: WidgetBundle {
   var body: some Widget {
       GameStatusWidget()
       CharacterDetailWidget()
   }
}
```

### Implementing a widget bundle

- [body](/documentation/swiftui/widgetbundle/body-swift.property): Declares the group of widgets that an app supports.
- [Body](/documentation/swiftui/widgetbundle/body-swift.associatedtype): The type of widget that represents the content of the bundle.
- [WidgetBundleBuilder](/documentation/swiftui/widgetbundlebuilder): A custom attribute that constructs a widget bundle’s body.

### Running a widget bundle

- [init()](/documentation/swiftui/widgetbundle/init()): Creates a widget bundle using the bundle’s body as its content.
- [main()](/documentation/swiftui/widgetbundle/main()): Initializes and runs the widget bundle.

## See Also

### Creating widgets

- [Building Widgets Using WidgetKit and SwiftUI](/documentation/widgetkit/building_widgets_using_widgetkit_and_swiftui): Create widgets to show your app’s content on the Home screen, with custom intents for user-customizable settings.
- [Creating a widget extension](/documentation/WidgetKit/Creating-a-Widget-Extension): Display your app’s content in a convenient, informative widget on various devices.
- [Keeping a widget up to date](/documentation/WidgetKit/Keeping-a-Widget-Up-To-Date): Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [Making a configurable widget](/documentation/WidgetKit/Making-a-Configurable-Widget): Give people the option to customize their widgets by adding a custom app intent to your project.
- [Widget](/documentation/swiftui/widget): The configuration and content of a widget to display on the Home screen or in Notification Center.
- [LimitedAvailabilityConfiguration](/documentation/swiftui/limitedavailabilityconfiguration): A type-erased widget configuration.
- [WidgetConfiguration](/documentation/swiftui/widgetconfiguration): A type that describes a widget’s content.
- [EmptyWidgetConfiguration](/documentation/swiftui/emptywidgetconfiguration): An empty widget configuration.
