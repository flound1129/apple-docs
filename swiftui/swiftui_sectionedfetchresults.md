# SectionedFetchResults

A collection of results retrieved from a Core Data persistent store, grouped into sections.

```swift
@MainActor @preconcurrency struct SectionedFetchResults<SectionIdentifier, Result> where SectionIdentifier : Hashable, Result : NSFetchRequestResult
```

## Overview

Use a `SectionedFetchResults` instance to show or edit Core Data managed objects, grouped into sections, in your app’s user interface. If you don’t need sectioning, use [FetchedResults](/documentation/swiftui/fetchedresults) instead.

You request a particular set of results by annotating the fetched results property declaration with a [SectionedFetchRequest](/documentation/swiftui/sectionedfetchrequest) property wrapper. Indicate the type of the fetched entities with a `Results` type, and the type of the identifier that distinguishes the sections with a `SectionIdentifier` type. For example, you can create a request to list all `Quake` managed objects that the [Loading and Displaying a Large Data Feed](/documentation/swiftui/loading_and_displaying_a_large_data_feed) sample code project defines to store earthquake data, sorted by their `time` property and grouped by a string that represents the days when earthquakes occurred:

```swift
@SectionedFetchRequest<String, Quake>(
    sectionIdentifier: \.day,
    sortDescriptors: [SortDescriptor(\.time, order: .reverse)]
)
private var quakes: SectionedFetchResults<String, Quake>
```

The `quakes` property acts as a collection of [SectionedFetchResults.Section](/documentation/swiftui/sectionedfetchresults/section) instances, each containing a collection of `Quake` instances. The example above depends on the `Quake` model object declaring both `time` and `day` properties, either stored or computed. For best performance with large data sets, use stored properties.

The collection of sections, as well as the collection of managed objects in each section, conforms to the [RandomAccessCollection](/documentation/Swift/RandomAccessCollection) protocol, so you can access them as you would any other collection. For example, you can create nested [ForEach](/documentation/swiftui/foreach) loops inside a [List](/documentation/swiftui/list) to iterate over the results:

```swift
List {
    ForEach(quakes) { section in
        Section(header: Text(section.id)) {
            ForEach(section) { quake in
                QuakeRow(quake: quake) // Displays information about a quake.
            }
        }
    }
}
```

Don’t confuse the [Section](/documentation/swiftui/section) view that you use to create a hierarchical display with the [SectionedFetchResults.Section](/documentation/swiftui/sectionedfetchresults/section) instances that hold the fetched results.

When you need to dynamically change the request’s section identifier, predicate, or sort descriptors, set the result instance’s [sectionIdentifier](/documentation/swiftui/sectionedfetchresults/sectionidentifier), [nsPredicate](/documentation/swiftui/sectionedfetchresults/nspredicate), and [sortDescriptors](/documentation/swiftui/sectionedfetchresults/sortdescriptors) or [nsSortDescriptors](/documentation/swiftui/sectionedfetchresults/nssortdescriptors) properties, respectively. Be sure that the sorting and sectioning work together to avoid discontinguous sections.

The fetch request and its results use the managed object context stored in the environment, which you can access using the [managedObjectContext](/documentation/swiftui/environmentvalues/managedobjectcontext) environment value. To support user interface activity, you typically rely on the [viewContext](/documentation/CoreData/NSPersistentContainer/viewContext) property of a shared [NSPersistentContainer](/documentation/CoreData/NSPersistentContainer) instance. For example, you can set a context on your top-level content view using a container that you define as part of your model:

```swift
ContentView()
    .environment(
        \.managedObjectContext,
        QuakesProvider.shared.container.viewContext)
```

### Configuring the associated sectioned fetch request

- [nsPredicate](/documentation/swiftui/sectionedfetchresults/nspredicate): The request’s predicate.
- [sortDescriptors](/documentation/swiftui/sectionedfetchresults/sortdescriptors): The request’s sort descriptors, accessed as value types.
- [nsSortDescriptors](/documentation/swiftui/sectionedfetchresults/nssortdescriptors): The request’s sort descriptors, accessed as reference types.
- [sectionIdentifier](/documentation/swiftui/sectionedfetchresults/sectionidentifier): The key path that the system uses to group fetched results into sections.
- [SectionedFetchResults.Section](/documentation/swiftui/sectionedfetchresults/section): A collection of fetched results that share a specified identifier.

### Getting indices

- [startIndex](/documentation/swiftui/sectionedfetchresults/startindex): The index of the first section in the results collection.
- [endIndex](/documentation/swiftui/sectionedfetchresults/endindex): The index that’s one greater than that of the last section.

### Getting results

- [subscript(_:)](/documentation/swiftui/sectionedfetchresults/subscript(_:)): Gets the section at the specified index.

## See Also

### Accessing Core Data

- [Loading and displaying a large data feed](/documentation/swiftui/loading-and-displaying-a-large-data-feed): Consume data in the background, and lower memory use by batching imports and preventing duplicate records.
- [managedObjectContext](/documentation/swiftui/environmentvalues/managedobjectcontext)
- [FetchRequest](/documentation/swiftui/fetchrequest): A property wrapper type that retrieves entities from a Core Data persistent store.
- [FetchedResults](/documentation/swiftui/fetchedresults): A collection of results retrieved from a Core Data store.
- [SectionedFetchRequest](/documentation/swiftui/sectionedfetchrequest): A property wrapper type that retrieves entities, grouped into sections, from a Core Data persistent store.
