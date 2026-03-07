# CustomizableToolbarContent

Conforming types represent items that can be placed in various locations in a customizable toolbar.

```swift
protocol CustomizableToolbarContent : ToolbarContent where Self.Body : CustomizableToolbarContent
```

### Using default options

- [defaultCustomization()](/documentation/swiftui/customizabletoolbarcontent/defaultcustomization()): Configures customizable toolbar content with the default visibility and options.
- [defaultCustomization(_:options:)](/documentation/swiftui/customizabletoolbarcontent/defaultcustomization(_:options:)): Configures the way customizable toolbar items with the default behavior behave.

### Customizing the behavior

- [customizationBehavior(_:)](/documentation/swiftui/customizabletoolbarcontent/customizationbehavior(_:)): Configures the customization behavior of customizable toolbar content.

### Instance Methods

- [hidden(_:)](/documentation/swiftui/customizabletoolbarcontent/hidden(_:)): Hides a toolbar item within its toolbar.
- [matchedTransitionSource(id:in:)](/documentation/swiftui/customizabletoolbarcontent/matchedtransitionsource(id:in:)): Identifies this toolbar content as the source of a navigation transition, such as a zoom transition.
- [sharedBackgroundVisibility(_:)](/documentation/swiftui/customizabletoolbarcontent/sharedbackgroundvisibility(_:)): Controls the visibility of the glass background effect on items in the toolbar. In certain contexts, such as the navigation bar on iOS and the window toolbar on macOS, toolbar items will be given a glass background effect that is shared with other items in the same logical grouping.

## See Also

### Populating a customizable toolbar

- [toolbar(id:content:)](/documentation/swiftui/view/toolbar(id:content:)): Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [ToolbarCustomizationBehavior](/documentation/swiftui/toolbarcustomizationbehavior): The customization behavior of customizable toolbar content.
- [ToolbarCustomizationOptions](/documentation/swiftui/toolbarcustomizationoptions): Options that influence the default customization behavior of customizable toolbar content.
- [SearchToolbarBehavior](/documentation/swiftui/searchtoolbarbehavior): The behavior of a search field in a toolbar.
