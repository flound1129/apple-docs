# Using Delegates to Customize Object Behavior

Respond to events on behalf of a delegator.

## Overview

You use delegates to interact with Cocoa objects that inform you of events in an app.

### Adopt a Delegate Protocol

Cocoa APIs often provide protocols that include delegate methods. When an event occurs—such as a user resizing a window—a class that’s a delegator will detect the event and call delegate methods on the class you specify as the delegate. Delegate methods can customize how an app responds to an event.

The example below adopts the [NSWindowDelegate](/documentation/AppKit/NSWindowDelegate) protocol and implements its [window(_:willUseFullScreenContentSize:)](/documentation/AppKit/NSWindowDelegate/window(_:willUseFullScreenContentSize:)) method:

```swift
class MyDelegate: NSObject, NSWindowDelegate {
    func window(_ window: NSWindow, willUseFullScreenContentSize proposedSize: NSSize) -> NSSize {
        return proposedSize
    }
}
```

### Check That Delegates Exist

The Cocoa delegation pattern doesn’t require that delegates are instantiated. If you don’t need to respond to events, you don’t need to create a delegate. Before you call a method on an object’s delegate, make sure that the delegate isn’t `nil`.

The example below creates an [NSWindow](/documentation/AppKit/NSWindow) and uses optional chaining to check that the window’s delegate exists before sending a message to the delegate.

```swift
let myWindow = NSWindow(
    contentRect: NSRect(x: 0, y: 0, width: 5120, height: 2880),
    styleMask: .fullScreen,
    backing: .buffered,
    defer: false
)

myWindow.delegate = MyDelegate()
if let fullScreenSize = myWindow.delegate?.window(myWindow, willUseFullScreenContentSize: mySize) {
    print(NSStringFromSize(fullScreenSize))
}
```

## See Also

### Common Patterns

- [Using Key-Value Observing in Swift](/documentation/swift/using-key-value-observing-in-swift): Notify objects about changes to the properties of other objects.
- [Managing a Shared Resource Using a Singleton](/documentation/swift/managing-a-shared-resource-using-a-singleton): Provide access to a shared resource using a single, shared class instance.
- [About Imported Cocoa Error Parameters](/documentation/swift/about-imported-cocoa-error-parameters): Learn how Cocoa error parameters are converted to Swift throwing methods.
- [Handling Cocoa Errors in Swift](/documentation/swift/handling-cocoa-errors-in-swift): Throw and catch errors that use Cocoa’s error types.
