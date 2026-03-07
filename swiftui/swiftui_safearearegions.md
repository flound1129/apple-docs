# SafeAreaRegions

A set of symbolic safe area regions.

```swift
@frozen struct SafeAreaRegions
```

### Getting safe area regions

- [all](/documentation/swiftui/safearearegions/all): All safe area regions.
- [container](/documentation/swiftui/safearearegions/container): The safe area defined by the device and containers within the user interface, including elements such as top and bottom bars.
- [keyboard](/documentation/swiftui/safearearegions/keyboard): The safe area matching the current extent of any software keyboard displayed over the view content.

## See Also

### Staying in the safe areas

- [ignoresSafeArea(_:edges:)](/documentation/swiftui/view/ignoressafearea(_:edges:)): Expands the safe area of a view.
- [safeAreaInset(edge:alignment:spacing:content:)](/documentation/swiftui/view/safeareainset(edge:alignment:spacing:content:)): Shows the specified content beside the modified view.
- [safeAreaPadding(_:)](/documentation/swiftui/view/safeareapadding(_:)): Adds the provided insets into the safe area of this view.
- [safeAreaPadding(_:_:)](/documentation/swiftui/view/safeareapadding(_:_:)): Adds the provided insets into the safe area of this view.
