# FetchRequest

A property wrapper type that retrieves entities from a Core Data persistent store.

```swift
@MainActor @propertyWrapper @preconcurrency struct FetchRequest<Result> where Result : NSFetchRequestResult
```

## Overview

Use a `FetchRequest` property wrapper to declare a [FetchedResults](/documentation/swiftui/fetchedresults) property that provides a collection of Core Data managed objects to a SwiftUI view. The request infers the entity type from the `Result` placeholder type that you specify. Condition the request with an optional predicate and sort descriptors. For example, you can create a request to list all `Quake` managed objects that the [Loading and Displaying a Large Data Feed](/documentation/swiftui/loading_and_displaying_a_large_data_feed) sample code project defines to store earthquake data, sorted by their `time` property:

```swift
@FetchRequest(sortDescriptors: [SortDescriptor(\.time, order: .reverse)])
private var quakes: FetchedResults<Quake> // Define Quake in your model.
```

Alternatively, when you need more flexibility, you can initialize the request with a configured [NSFetchRequest](/documentation/CoreData/NSFetchRequest) instance:

```swift
@FetchRequest(fetchRequest: request)
private var quakes: FetchedResults<Quake>
```

Always declare properties that have a fetch request wrapper as private. This lets the compiler help you avoid accidentally setting the property from the memberwise initializer of the enclosing view.

The fetch request and its results use the managed object context stored in the environment, which you can access using the [managedObjectContext](/documentation/swiftui/environmentvalues/managedobjectcontext) environment value. To support user interface activity, you typically rely on the [viewContext](/documentation/CoreData/NSPersistentContainer/viewContext) property of a shared [NSPersistentContainer](/documentation/CoreData/NSPersistentContainer) instance. For example, you can set a context on your top level content view using a shared container that you define as part of your model:

```swift
ContentView()
    .environment(
        \.managedObjectContext,
        QuakesProvider.shared.container.viewContext)
```

When you need to dynamically change the predicate or sort descriptors, access the request’s [FetchRequest.Configuration](/documentation/swiftui/fetchrequest/configuration) structure. To create a request that groups the fetched results according to a characteristic that they share, use [SectionedFetchRequest](/documentation/swiftui/sectionedfetchrequest) instead.

### Creating a fetch request

- [init(sortDescriptors:predicate:animation:)](/documentation/swiftui/fetchrequest/init(sortdescriptors:predicate:animation:)): Creates a fetch request based on a predicate and reference type sort parameters.
- [init(entity:sortDescriptors:predicate:animation:)](/documentation/swiftui/fetchrequest/init(entity:sortdescriptors:predicate:animation:)): Creates a fetch request for a specified entity description, based on a predicate and sort parameters.

### Creating a fully configured fetch request

- [init(fetchRequest:animation:)](/documentation/swiftui/fetchrequest/init(fetchrequest:animation:)): Creates a fully configured fetch request that uses the specified animation when updating results.
- [init(fetchRequest:transaction:)](/documentation/swiftui/fetchrequest/init(fetchrequest:transaction:)): Creates a fully configured fetch request that uses the specified transaction when updating results.

### Configuring a request dynamically

- [FetchRequest.Configuration](/documentation/swiftui/fetchrequest/configuration): The request’s configurable properties.
- [projectedValue](/documentation/swiftui/fetchrequest/projectedvalue): A binding to the request’s mutable configuration properties.

### Getting the fetched results

- [update()](/documentation/swiftui/fetchrequest/update()): Updates the fetched results.
- [wrappedValue](/documentation/swiftui/fetchrequest/wrappedvalue): The fetched results of the fetch request.

### Default Implementations

- [DynamicProperty Implementations](/documentation/swiftui/fetchrequest/dynamicproperty-implementations)

## See Also

### Accessing Core Data

- [Loading and displaying a large data feed](/documentation/swiftui/loading-and-displaying-a-large-data-feed): Consume data in the background, and lower memory use by batching imports and preventing duplicate records.
- [managedObjectContext](/documentation/swiftui/environmentvalues/managedobjectcontext)
- [FetchedResults](/documentation/swiftui/fetchedresults): A collection of results retrieved from a Core Data store.
- [SectionedFetchRequest](/documentation/swiftui/sectionedfetchrequest): A property wrapper type that retrieves entities, grouped into sections, from a Core Data persistent store.
- [SectionedFetchResults](/documentation/swiftui/sectionedfetchresults): A collection of results retrieved from a Core Data persistent store, grouped into sections.
