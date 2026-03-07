# Persistent storage

Store data for use across sessions of your app.

## Overview

The operating system provides ways to store data when your app closes, so that when people open your app again later, they can continue working without interruption. The mechanism that you use depends on factors like what and how much you need to store, whether you need serialized or random access to the data, and so on.

![None]

You use the same kinds of storage in a SwiftUI app that you use in any other app. For example, you can access files on disk using the [FileManager](/documentation/Foundation/FileManager) interface. However, SwiftUI also provides conveniences that make it easier to use certain kinds of persistent storage in a declarative environment. For example, you can use [FetchRequest](/documentation/swiftui/fetchrequest) and [FetchedResults](/documentation/swiftui/fetchedresults) to interact with a Core Data model.

### Saving state across app launches

- [Restoring your app’s state with SwiftUI](/documentation/swiftui/restoring-your-app-s-state-with-swiftui): Provide app continuity for users by preserving their current activities.
- [defaultAppStorage(_:)](/documentation/swiftui/view/defaultappstorage(_:)): The default store used by `AppStorage` contained within the view.
- [AppStorage](/documentation/swiftui/appstorage): A property wrapper type that reflects a value from `UserDefaults` and invalidates a view on a change in value in that user default.
- [SceneStorage](/documentation/swiftui/scenestorage): A property wrapper type that reads and writes to persisted, per-scene storage.

### Accessing Core Data

- [Loading and displaying a large data feed](/documentation/swiftui/loading-and-displaying-a-large-data-feed): Consume data in the background, and lower memory use by batching imports and preventing duplicate records.
- [managedObjectContext](/documentation/swiftui/environmentvalues/managedobjectcontext)
- [FetchRequest](/documentation/swiftui/fetchrequest): A property wrapper type that retrieves entities from a Core Data persistent store.
- [FetchedResults](/documentation/swiftui/fetchedresults): A collection of results retrieved from a Core Data store.
- [SectionedFetchRequest](/documentation/swiftui/sectionedfetchrequest): A property wrapper type that retrieves entities, grouped into sections, from a Core Data persistent store.
- [SectionedFetchResults](/documentation/swiftui/sectionedfetchresults): A collection of results retrieved from a Core Data persistent store, grouped into sections.

## See Also

### Data and storage

- [Model data](/documentation/swiftui/model-data): Manage the data that your app uses to drive its interface.
- [Environment values](/documentation/swiftui/environment-values): Share data throughout a view hierarchy using the environment.
- [Preferences](/documentation/swiftui/preferences): Indicate configuration preferences from views to their container views.
