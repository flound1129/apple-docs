# Bindable

A property wrapper type that supports creating bindings to the mutable properties of observable objects.

```swift
@dynamicMemberLookup @propertyWrapper struct Bindable<Value>
```

## Overview

Use this property wrapper to create bindings to mutable properties of a data model object that conforms to the [Observable](/documentation/Observation/Observable) protocol. For example, the following code wraps the `book` input with `@Bindable`. Then it uses a [TextField](/documentation/swiftui/textfield) to change the `title` property of a book, and a [Toggle](/documentation/swiftui/toggle) to change the `isAvailable` property, using the `$` syntax to pass a binding for each property to those controls.

```swift
@Observable
class Book: Identifiable {
    var title = "Sample Book Title"
    var isAvailable = true
}

struct BookEditView: View {
    @Bindable var book: Book
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        Form {
            TextField("Title", text: $book.title)

            Toggle("Book is available", isOn: $book.isAvailable)

            Button("Close") {
                dismiss()
            }
        }
    }
}
```

You can use the `Bindable` property wrapper on properties and variables to an [Observable](/documentation/Observation/Observable) object. This includes global variables, properties that exists outside of SwiftUI types, or even local variables. For example, you can create a `@Bindable` variable within a view’s [body](/documentation/swiftui/view/body-8kl5o):

```swift
struct LibraryView: View {
    @State private var books = [Book(), Book(), Book()]

    var body: some View {
        List(books) { book in
            @Bindable var book = book
            TextField("Title", text: $book.title)
        }
    }
}
```

The `@Bindable` variable `book` provides a binding that connects [TextField](/documentation/swiftui/textfield) to the `title` property of a book so that a person can make changes directly to the model data.

Use this same approach when you need a binding to a property of an observable object stored in a view’s environment. For example, the following code uses the [Environment](/documentation/swiftui/environment) property wrapper to retrieve an instance of the observable type `Book`. Then the code creates a `@Bindable` variable `book` and passes a binding for the `title` property to a [TextField](/documentation/swiftui/textfield) using the `$` syntax.

```swift
struct TitleEditView: View {
    @Environment(Book.self) private var book

    var body: some View {
        @Bindable var book = book
        TextField("Title", text: $book.title)
    }
}
```

### Creating a bindable value

- [init(_:)](/documentation/swiftui/bindable/init(_:)): Creates a bindable object from an observable object.
- [init(wrappedValue:)](/documentation/swiftui/bindable/init(wrappedvalue:)): Creates a bindable object from an observable object.
- [init(projectedValue:)](/documentation/swiftui/bindable/init(projectedvalue:)): Creates a bindable from the value of another bindable.

### Getting the value

- [wrappedValue](/documentation/swiftui/bindable/wrappedvalue): The wrapped object.
- [projectedValue](/documentation/swiftui/bindable/projectedvalue): The bindable wrapper for the object that creates bindings to its properties using dynamic member lookup.
- [subscript(dynamicMember:)](/documentation/swiftui/bindable/subscript(dynamicmember:)): Returns a binding to the value of a given key path.

## See Also

### Creating and sharing view state

- [Managing user interface state](/documentation/swiftui/managing-user-interface-state): Encapsulate view-specific data within your app’s view hierarchy to make your views reusable.
- [State](/documentation/swiftui/state): A property wrapper type that can read and write a value managed by SwiftUI.
- [Binding](/documentation/swiftui/binding): A property wrapper type that can read and write a value owned by a source of truth.
