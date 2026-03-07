# AsyncImagePhase

The current phase of the asynchronous image loading operation.

```swift
enum AsyncImagePhase
```

## Overview

When you create an [AsyncImage](/documentation/swiftui/asyncimage) instance with the [init(url:scale:transaction:content:)](/documentation/swiftui/asyncimage/init(url:scale:transaction:content:)) initializer, you define the appearance of the view using a `content` closure. SwiftUI calls the closure with a phase value at different points during the load operation to indicate the current state. Use the phase to decide what to draw. For example, you can draw the loaded image if it exists, a view that indicates an error, or a placeholder:

```swift
AsyncImage(url: URL(string: "https://example.com/icon.png")) { phase in
    if let image = phase.image {
        image // Displays the loaded image.
    } else if phase.error != nil {
        Color.red // Indicates an error.
    } else {
        Color.blue // Acts as a placeholder.
    }
}
```

### Getting load phases

- [AsyncImagePhase.empty](/documentation/swiftui/asyncimagephase/empty): No image is loaded.
- [AsyncImagePhase.success(_:)](/documentation/swiftui/asyncimagephase/success(_:)): An image successfully loaded.
- [AsyncImagePhase.failure(_:)](/documentation/swiftui/asyncimagephase/failure(_:)): An image failed to load with an error.

### Getting the image

- [image](/documentation/swiftui/asyncimagephase/image): The loaded image, if any.

### Getting the error

- [error](/documentation/swiftui/asyncimagephase/error): The error that occurred when attempting to load an image, if any.

## See Also

### Loading images asynchronously

- [AsyncImage](/documentation/swiftui/asyncimage): A view that asynchronously loads and displays an image.
