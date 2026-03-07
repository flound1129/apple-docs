# AnyTabContent

Type erased tab content.

```swift
struct AnyTabContent<SelectionValue> where SelectionValue : Hashable
```

### Initializers

- [init(_:)](/documentation/swiftui/anytabcontent/init(_:)): Create an instance that type-erases `tabContent`.

## See Also

### Configuring a tab

- [sectionActions(content:)](/documentation/swiftui/view/sectionactions(content:)): Adds custom actions to a section.
- [TabPlacement](/documentation/swiftui/tabplacement): A place that a tab can appear.
- [TabContentBuilder](/documentation/swiftui/tabcontentbuilder): A result builder that constructs tabs for a tab view that supports programmatic selection. This builder requires that all tabs in the tab view have the same selection type.
- [TabContent](/documentation/swiftui/tabcontent): A type that provides content for programmatically selectable tabs in a tab view.
