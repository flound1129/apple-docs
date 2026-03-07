# FetchedResults

A collection of results retrieved from a Core Data store.

```swift
@MainActor @preconcurrency struct FetchedResults<Result> where Result : NSFetchRequestResult
```

## Overview

Use a `FetchedResults` instance to show or edit Core Data managed objects in your app’s user interface. You request a particular set of results by specifying a `Result` type as the entity type, and annotating the fetched results property declaration with a [FetchRequest](/documentation/swiftui/fetchrequest) property wrapper. For example, you can create a request to list all `Quake` managed objects that the [Loading and Displaying a Large Data Feed](/documentation/swiftui/loading_and_displaying_a_large_data_feed) sample code project defines to store earthquake data, sorted by their `time` property:

```swift
@FetchRequest(sortDescriptors: [SortDescriptor(\.time, order: .reverse)])
private var quakes: FetchedResults<Quake>
```

The results instance conforms to [RandomAccessCollection](/documentation/Swift/RandomAccessCollection), so you access it like any other collection. For example, you can create a [List](/documentation/swiftui/list) that iterates over all the results:

```swift
List(quakes) { quake in
    NavigationLink(destination: QuakeDetail(quake: quake)) {
        QuakeRow(quake: quake)
    }
}
```

When you need to dynamically change the request’s predicate or sort descriptors, set the result instance’s [nsPredicate](/documentation/swiftui/fetchedresults/nspredicate) and [sortDescriptors](/documentation/swiftui/fetchedresults/sortdescriptors) or [nsSortDescriptors](/documentation/swiftui/fetchedresults/nssortdescriptors) properties, respectively.

The fetch request and its results use the managed object context stored in the environment, which you can access using the [managedObjectContext](/documentation/swiftui/environmentvalues/managedobjectcontext) environment value. To support user interface activity, you typically rely on the [viewContext](/documentation/CoreData/NSPersistentContainer/viewContext) property of a shared [NSPersistentContainer](/documentation/CoreData/NSPersistentContainer) instance. For example, you can set a context on your top level content view using a container that you define as part of your model:

```swift
ContentView()
    .environment(
        \.managedObjectContext,
        QuakesProvider.shared.container.viewContext)
```

### Configuring the associated fetch request

- [nsPredicate](/documentation/swiftui/fetchedresults/nspredicate): The request’s predicate.
- [sortDescriptors](/documentation/swiftui/fetchedresults/sortdescriptors): The request’s sort descriptors, accessed as value types.
- [nsSortDescriptors](/documentation/swiftui/fetchedresults/nssortdescriptors): The request’s sort descriptors, accessed as reference types.

### Getting indices

- [startIndex](/documentation/swiftui/fetchedresults/startindex): The index of the first entity in the results collection.
- [endIndex](/documentation/swiftui/fetchedresults/endindex): The index that’s one greater than the last valid subscript argument.

### Getting results

- [subscript(_:)](/documentation/swiftui/fetchedresults/subscript(_:)): Gets the entity at the specified index.

## See Also

### Accessing Core Data

- [Loading and displaying a large data feed](/documentation/swiftui/loading-and-displaying-a-large-data-feed): Consume data in the background, and lower memory use by batching imports and preventing duplicate records.
- [managedObjectContext](/documentation/swiftui/environmentvalues/managedobjectcontext)
- [FetchRequest](/documentation/swiftui/fetchrequest): A property wrapper type that retrieves entities from a Core Data persistent store.
- [SectionedFetchRequest](/documentation/swiftui/sectionedfetchrequest): A property wrapper type that retrieves entities, grouped into sections, from a Core Data persistent store.
- [SectionedFetchResults](/documentation/swiftui/sectionedfetchresults): A collection of results retrieved from a Core Data persistent store, grouped into sections.
