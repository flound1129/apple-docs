# ToolbarCustomizationBehavior

The customization behavior of customizable toolbar content.

```swift
struct ToolbarCustomizationBehavior
```

## Overview

Customizable toolbar content support different types of customization behaviors. For example, some customizable content may not be removed by the user. Some content may be placed in a toolbar that supports customization overall, but not for that particular content.

Use this type in conjunction with the [customizationBehavior(_:)](/documentation/swiftui/customizabletoolbarcontent/customizationbehavior(_:)) modifier.

### Getting customization behaviors

- [default](/documentation/swiftui/toolbarcustomizationbehavior/default): The default customization behavior.
- [disabled](/documentation/swiftui/toolbarcustomizationbehavior/disabled): The disabled customization behavior.
- [reorderable](/documentation/swiftui/toolbarcustomizationbehavior/reorderable): The reorderable customization behavior.

## See Also

### Populating a customizable toolbar

- [toolbar(id:content:)](/documentation/swiftui/view/toolbar(id:content:)): Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [CustomizableToolbarContent](/documentation/swiftui/customizabletoolbarcontent): Conforming types represent items that can be placed in various locations in a customizable toolbar.
- [ToolbarCustomizationOptions](/documentation/swiftui/toolbarcustomizationoptions): Options that influence the default customization behavior of customizable toolbar content.
- [SearchToolbarBehavior](/documentation/swiftui/searchtoolbarbehavior): The behavior of a search field in a toolbar.
