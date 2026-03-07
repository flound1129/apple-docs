# DynamicTypeSize

A Dynamic Type size, which specifies how large scalable content should be.

```swift
enum DynamicTypeSize
```

## Overview

For more information, see [Typography](/design/Human-Interface-Guidelines/typography) in the Human Interface Guidelines.

### Getting type sizes

- [DynamicTypeSize.xSmall](/documentation/swiftui/dynamictypesize/xsmall): An extra small size.
- [DynamicTypeSize.small](/documentation/swiftui/dynamictypesize/small): A small size.
- [DynamicTypeSize.medium](/documentation/swiftui/dynamictypesize/medium): A medium size.
- [DynamicTypeSize.large](/documentation/swiftui/dynamictypesize/large): A large size.
- [DynamicTypeSize.xLarge](/documentation/swiftui/dynamictypesize/xlarge): An extra large size.
- [DynamicTypeSize.xxLarge](/documentation/swiftui/dynamictypesize/xxlarge): An extra extra large size.
- [DynamicTypeSize.xxxLarge](/documentation/swiftui/dynamictypesize/xxxlarge): An extra extra extra large size.

### Getting accessibility type sizes

- [DynamicTypeSize.accessibility1](/documentation/swiftui/dynamictypesize/accessibility1): The first accessibility size.
- [DynamicTypeSize.accessibility2](/documentation/swiftui/dynamictypesize/accessibility2): The second accessibility size.
- [DynamicTypeSize.accessibility3](/documentation/swiftui/dynamictypesize/accessibility3): The third accessibility size.
- [DynamicTypeSize.accessibility4](/documentation/swiftui/dynamictypesize/accessibility4): The fourth accessibility size.
- [DynamicTypeSize.accessibility5](/documentation/swiftui/dynamictypesize/accessibility5): The fifth accessibility size.
- [isAccessibilitySize](/documentation/swiftui/dynamictypesize/isaccessibilitysize): A Boolean value indicating whether the size is one that is associated with accessibility.

### Creating a type size

- [init(_:)](/documentation/swiftui/dynamictypesize/init(_:)): Create a Dynamic Type size from its `UIContentSizeCategory` equivalent.

## See Also

### Adjusting text size

- [textScale(_:isEnabled:)](/documentation/swiftui/view/textscale(_:isenabled:)): Applies a text scale to text in the view.
- [dynamicTypeSize(_:)](/documentation/swiftui/view/dynamictypesize(_:)): Sets the Dynamic Type size within the view to the given value.
- [dynamicTypeSize](/documentation/swiftui/environmentvalues/dynamictypesize): The current Dynamic Type size.
- [ScaledMetric](/documentation/swiftui/scaledmetric): A dynamic property that scales a numeric value.
- [TextVariantPreference](/documentation/swiftui/textvariantpreference): A protocol for controlling the size variant of text views.
- [FixedTextVariant](/documentation/swiftui/fixedtextvariant): The default text variant preference that chooses the largest available variant.
- [SizeDependentTextVariant](/documentation/swiftui/sizedependenttextvariant): The size dependent variant preference allows the text to take the available space into account when choosing the variant to display.
