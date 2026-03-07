# TextVariantPreference

A protocol for controlling the size variant of text views.

```swift
protocol TextVariantPreference
```

### Type Properties

- [fixed](/documentation/swiftui/textvariantpreference/fixed): The default text variant preference. It always chooses the largest available variant.
- [sizeDependent](/documentation/swiftui/textvariantpreference/sizedependent): The size dependent preference allows the text to take the available space into account when choosing the size variant to display.

## See Also

### Adjusting text size

- [textScale(_:isEnabled:)](/documentation/swiftui/view/textscale(_:isenabled:)): Applies a text scale to text in the view.
- [dynamicTypeSize(_:)](/documentation/swiftui/view/dynamictypesize(_:)): Sets the Dynamic Type size within the view to the given value.
- [dynamicTypeSize](/documentation/swiftui/environmentvalues/dynamictypesize): The current Dynamic Type size.
- [DynamicTypeSize](/documentation/swiftui/dynamictypesize): A Dynamic Type size, which specifies how large scalable content should be.
- [ScaledMetric](/documentation/swiftui/scaledmetric): A dynamic property that scales a numeric value.
- [FixedTextVariant](/documentation/swiftui/fixedtextvariant): The default text variant preference that chooses the largest available variant.
- [SizeDependentTextVariant](/documentation/swiftui/sizedependenttextvariant): The size dependent variant preference allows the text to take the available space into account when choosing the variant to display.
