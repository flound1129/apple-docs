# ControlSize

The size classes, like regular or small, that you can apply to controls within a view.

```swift
enum ControlSize
```

### Getting control sizes

- [ControlSize.mini](/documentation/swiftui/controlsize/mini): A control version that is minimally sized.
- [ControlSize.small](/documentation/swiftui/controlsize/small): A control version that is proportionally smaller size for space-constrained views.
- [ControlSize.regular](/documentation/swiftui/controlsize/regular): A control version that is the default size.
- [ControlSize.large](/documentation/swiftui/controlsize/large): A control version that is prominently sized.
- [ControlSize.extraLarge](/documentation/swiftui/controlsize/extralarge): A control version that is substantially sized. The largest control size. Resolves to [ControlSize.large](/documentation/swiftui/controlsize/large) on platforms other than visionOS.

### Initializers

- [init(_:)](/documentation/swiftui/controlsize/init(_:)): Creates a control size from its NSControl.ControlSize equivalent.

## See Also

### Sizing controls

- [controlSize(_:)](/documentation/swiftui/view/controlsize(_:)): Sets the size for controls within this view.
- [controlSize](/documentation/swiftui/environmentvalues/controlsize): The size to apply to controls within a view.
