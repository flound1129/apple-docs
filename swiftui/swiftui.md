# SwiftUI

Declare the user interface and behavior for your app on every platform.

## Overview

SwiftUI provides views, controls, and layout structures for declaring your app’s user interface. The framework provides event handlers for delivering taps, gestures, and other types of input to your app, and tools to manage the flow of data from your app’s models down to the views and controls that users see and interact with.

Define your app structure using the [App](/documentation/swiftui/app) protocol, and populate it with scenes that contain the views that make up your app’s user interface. Create your own custom views that conform to the [View](/documentation/swiftui/view) protocol, and compose them with SwiftUI views for displaying text, images, and custom shapes using stacks, lists, and more. Apply powerful modifiers to built-in views and your own views to customize their rendering and interactivity. Share code between apps on multiple platforms with views and controls that adapt to their context and presentation.

![An image of the Landmarks sample app on Mac, iPad, and iPhone showing the Mount Fuji landmark.]

You can integrate SwiftUI views with objects from the [UIKit](/documentation/UIKit), [AppKit](/documentation/AppKit), and [WatchKit](/documentation/WatchKit) frameworks to take further advantage of platform-specific functionality. You can also customize accessibility support in SwiftUI, and localize your app’s interface for different languages, countries, or cultural regions.

> **Tip:**
> If you’re new to SwiftUI, visit the [SwiftUI Pathway](https://developer.apple.com/swiftui/get-started/). It’s a collection of tutorials, articles, and sample projects that help you get started with SwiftUI.
>

### Featured samples

### Essentials

- [Adopting Liquid Glass](/documentation/TechnologyOverviews/adopting-liquid-glass): Find out how to bring the new material to your app.
- [Develop in Swift](/tutorials/Develop-in-Swift#explore-xcode): Develop in Swift Tutorials introduce app development with Swift and Xcode to anyone learning to build apps for Apple platforms.
- [SwiftUI updates](/documentation/Updates/SwiftUI): Learn about important changes to SwiftUI.
- [Landmarks: Building an app with Liquid Glass](/documentation/swiftui/landmarks-building-an-app-with-liquid-glass): Enhance your app experience with system-provided and custom Liquid Glass.

### App structure

- [App organization](/documentation/swiftui/app-organization): Define the entry point and top-level structure of your app.
- [Scenes](/documentation/swiftui/scenes): Declare the user interface groupings that make up the parts of your app.
- [Windows](/documentation/swiftui/windows): Display user interface content in a window or a collection of windows.
- [Immersive spaces](/documentation/swiftui/immersive-spaces): Display unbounded content in a person’s surroundings.
- [Documents](/documentation/swiftui/documents): Enable people to open and manage documents.
- [Navigation](/documentation/swiftui/navigation): Enable people to move between different parts of your app’s view hierarchy within a scene.
- [Modal presentations](/documentation/swiftui/modal-presentations): Present content in a separate view that offers focused interaction.
- [Toolbars](/documentation/swiftui/toolbars): Provide immediate access to frequently used commands and controls.
- [Search](/documentation/swiftui/search): Enable people to search for text or other content within your app.
- [App extensions](/documentation/swiftui/app-extensions): Extend your app’s basic functionality to other parts of the system, like by adding a Widget.

### Data and storage

- [Model data](/documentation/swiftui/model-data): Manage the data that your app uses to drive its interface.
- [Environment values](/documentation/swiftui/environment-values): Share data throughout a view hierarchy using the environment.
- [Preferences](/documentation/swiftui/preferences): Indicate configuration preferences from views to their container views.
- [Persistent storage](/documentation/swiftui/persistent-storage): Store data for use across sessions of your app.

### Views

- [View fundamentals](/documentation/swiftui/view-fundamentals): Define the visual elements of your app using a hierarchy of views.
- [View configuration](/documentation/swiftui/view-configuration): Adjust the characteristics of views in a hierarchy.
- [View styles](/documentation/swiftui/view-styles): Apply built-in and custom appearances and behaviors to different types of views.
- [Animations](/documentation/swiftui/animations): Create smooth visual updates in response to state changes.
- [Text input and output](/documentation/swiftui/text-input-and-output): Display formatted text and get text input from the user.
- [Images](/documentation/swiftui/images): Add images and symbols to your app’s user interface.
- [Controls and indicators](/documentation/swiftui/controls-and-indicators): Display values and get user selections.
- [Menus and commands](/documentation/swiftui/menus-and-commands): Provide space-efficient, context-dependent access to commands and controls.
- [Shapes](/documentation/swiftui/shapes): Trace and fill built-in and custom shapes with a color, gradient, or other pattern.
- [Drawing and graphics](/documentation/swiftui/drawing-and-graphics): Enhance your views with graphical effects and customized drawings.

### View layout

- [Layout fundamentals](/documentation/swiftui/layout-fundamentals): Arrange views inside built-in layout containers like stacks and grids.
- [Layout adjustments](/documentation/swiftui/layout-adjustments): Make fine adjustments to alignment, spacing, padding, and other layout parameters.
- [Custom layout](/documentation/swiftui/custom-layout): Place views in custom arrangements and create animated transitions between layout types.
- [Lists](/documentation/swiftui/lists): Display a structured, scrollable column of information.
- [Tables](/documentation/swiftui/tables): Display selectable, sortable data arranged in rows and columns.
- [View groupings](/documentation/swiftui/view-groupings): Present views in different kinds of purpose-driven containers, like forms or control groups.
- [Scroll views](/documentation/swiftui/scroll-views): Enable people to scroll to content that doesn’t fit in the current display.

### Event handling

- [Gestures](/documentation/swiftui/gestures): Define interactions from taps, clicks, and swipes to fine-grained gestures.
- [Input events](/documentation/swiftui/input-events): Respond to input from a hardware device, like a keyboard or a Touch Bar.
- [Clipboard](/documentation/swiftui/clipboard): Enable people to move or duplicate items by issuing Copy and Paste commands.
- [Drag and drop](/documentation/swiftui/drag-and-drop): Enable people to move or duplicate items by dragging them from one location to another.
- [Focus](/documentation/swiftui/focus): Identify and control which visible object responds to user interaction.
- [System events](/documentation/swiftui/system-events): React to system events, like opening a URL.

### Accessibility

- [Accessibility fundamentals](/documentation/swiftui/accessibility-fundamentals): Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Accessible appearance](/documentation/swiftui/accessible-appearance): Enhance the legibility of content in your app’s interface.
- [Accessible controls](/documentation/swiftui/accessible-controls): Improve access to actions that your app can undertake.
- [Accessible descriptions](/documentation/swiftui/accessible-descriptions): Describe interface elements to help people understand what they represent.
- [Accessible navigation](/documentation/swiftui/accessible-navigation): Enable users to navigate to specific user interface elements using rotors.

### Framework integration

- [AppKit integration](/documentation/swiftui/appkit-integration): Add AppKit views to your SwiftUI app, or use SwiftUI views in your AppKit app.
- [UIKit integration](/documentation/swiftui/uikit-integration): Add UIKit views to your SwiftUI app, or use SwiftUI views in your UIKit app.
- [WatchKit integration](/documentation/swiftui/watchkit-integration): Add WatchKit views to your SwiftUI app, or use SwiftUI views in your WatchKit app.
- [Technology-specific views](/documentation/swiftui/technology-specific-views): Use SwiftUI views that other Apple frameworks provide.

### Tool support

- [Previews in Xcode](/documentation/swiftui/previews-in-xcode): Generate dynamic, interactive previews of your custom views.
- [Xcode library customization](/documentation/swiftui/xcode-library-customization): Expose custom views and modifiers in the Xcode library.
- [Performance analysis](/documentation/swiftui/performance-analysis): Measure and improve your app’s responsiveness.
