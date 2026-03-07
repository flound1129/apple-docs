# Xcode library customization

Expose custom views and modifiers in the Xcode library.

## Overview

You can add your custom SwiftUI views and view modifiers to Xcode’s library. This allows anyone developing your app or adopting your framework to access them by clicking the Library button (+) in Xcode’s toolbar. You can select and drag the custom library items into code, just like you would for system-provided items.

![None]

To add items to the library, create a structure that conforms to the [LibraryContentProvider](/documentation/DeveloperToolsSupport/LibraryContentProvider) protocol and encapsulate any items you want to add as [LibraryItem](/documentation/DeveloperToolsSupport/LibraryItem) instances. Implement the [views](/documentation/DeveloperToolsSupport/LibraryContentProvider/views) computed property to add library items containing views. Implement the [modifiers(base:)](/documentation/DeveloperToolsSupport/LibraryContentProvider/modifiers(base:)) method to add items containing view modifiers. Xcode harvests items from all of the library content providers in your project as you work, and makes them available to you in its library.

### Creating library items

- [LibraryContentProvider](/documentation/DeveloperToolsSupport/LibraryContentProvider): A source of Xcode library and code completion content.
- [LibraryItem](/documentation/DeveloperToolsSupport/LibraryItem): A single item to add to the Xcode library.

## See Also

### Tool support

- [Previews in Xcode](/documentation/swiftui/previews-in-xcode): Generate dynamic, interactive previews of your custom views.
- [Performance analysis](/documentation/swiftui/performance-analysis): Measure and improve your app’s responsiveness.
