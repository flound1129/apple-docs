# WKApplicationDelegateAdaptor

A property wrapper that is used in `App` to provide a delegate from WatchKit.

```swift
@MainActor @preconcurrency @propertyWrapper struct WKApplicationDelegateAdaptor<DelegateType> where DelegateType : NSObject, DelegateType : WKApplicationDelegate
```

### Creating a delegate adaptor

- [init(_:)](/documentation/swiftui/wkapplicationdelegateadaptor/init(_:)): Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application Delegate.

### Getting the delegate adaptor

- [projectedValue](/documentation/swiftui/wkapplicationdelegateadaptor/projectedvalue): A projection of the observed object that creates bindings to its properties using dynamic member lookup.
- [wrappedValue](/documentation/swiftui/wkapplicationdelegateadaptor/wrappedvalue): The underlying delegate.

## See Also

### Targeting watchOS

- [WKExtensionDelegateAdaptor](/documentation/swiftui/wkextensiondelegateadaptor): A property wrapper type that you use to create a WatchKit extension delegate.
