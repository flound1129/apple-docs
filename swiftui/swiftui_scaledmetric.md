# ScaledMetric

A dynamic property that scales a numeric value.

```swift
@propertyWrapper struct ScaledMetric<Value> where Value : BinaryFloatingPoint
```

### Creating the metric

- [init(wrappedValue:)](/documentation/swiftui/scaledmetric/init(wrappedvalue:)): Creates the scaled metric with an unscaled value using the default scaling.
- [init(wrappedValue:relativeTo:)](/documentation/swiftui/scaledmetric/init(wrappedvalue:relativeto:)): Creates the scaled metric with an unscaled value and a text style to scale relative to.

### Getting the metric

- [wrappedValue](/documentation/swiftui/scaledmetric/wrappedvalue): The value scaled based on the current environment.

## See Also

### Adjusting text size

- [textScale(_:isEnabled:)](/documentation/swiftui/view/textscale(_:isenabled:)): Applies a text scale to text in the view.
- [dynamicTypeSize(_:)](/documentation/swiftui/view/dynamictypesize(_:)): Sets the Dynamic Type size within the view to the given value.
- [dynamicTypeSize](/documentation/swiftui/environmentvalues/dynamictypesize): The current Dynamic Type size.
- [DynamicTypeSize](/documentation/swiftui/dynamictypesize): A Dynamic Type size, which specifies how large scalable content should be.
- [TextVariantPreference](/documentation/swiftui/textvariantpreference): A protocol for controlling the size variant of text views.
- [FixedTextVariant](/documentation/swiftui/fixedtextvariant): The default text variant preference that chooses the largest available variant.
- [SizeDependentTextVariant](/documentation/swiftui/sizedependenttextvariant): The size dependent variant preference allows the text to take the available space into account when choosing the variant to display.
