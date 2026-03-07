# TableColumnCustomizationBehavior

A set of customization behaviors of a column that a table can offer to a user.

```swift
struct TableColumnCustomizationBehavior
```

## Overview

This is used as a value provided to [disabledCustomizationBehavior(_:)](/documentation/swiftui/tablecolumncontent/disabledcustomizationbehavior(_:)).

Setting any of these values as the `disabledCustomizationBehavior(_:)` doesn’t have any effect on iOS.

### Getting the customization behavior

- [all](/documentation/swiftui/tablecolumncustomizationbehavior/all): All customization behaviors.
- [reorder](/documentation/swiftui/tablecolumncustomizationbehavior/reorder): A behavior that allows the column to be reordered by the user.
- [resize](/documentation/swiftui/tablecolumncustomizationbehavior/resize): A behavior that allows the column to be resized by the user.
- [visibility](/documentation/swiftui/tablecolumncustomizationbehavior/visibility): A behavior that allows the column to be hidden or revealed by the user.

### Creating a behavior

- [init()](/documentation/swiftui/tablecolumncustomizationbehavior/init()): Creates an empty customization behavior, representing no customization

## See Also

### Customizing columns

- [tableColumnHeaders(_:)](/documentation/swiftui/view/tablecolumnheaders(_:)): Controls the visibility of a `Table`’s column header views.
- [TableColumnCustomization](/documentation/swiftui/tablecolumncustomization): A representation of the state of the columns in a table.
