# TabContentBuilder

A result builder that constructs tabs for a tab view that supports programmatic selection. This builder requires that all tabs in the tab view have the same selection type.

```swift
@resultBuilder struct TabContentBuilder<TabValue> where TabValue : Hashable
```

### Structures

- [TabContentBuilder.Content](/documentation/swiftui/tabcontentbuilder/content): A view representation of the content of a builder-based tab view with selection.

### Type Methods

- [buildBlock(_:)](/documentation/swiftui/tabcontentbuilder/buildblock(_:))
- [buildBlock(_:_:)](/documentation/swiftui/tabcontentbuilder/buildblock(_:_:))
- [buildBlock(_:_:_:)](/documentation/swiftui/tabcontentbuilder/buildblock(_:_:_:))
- [buildBlock(_:_:_:_:)](/documentation/swiftui/tabcontentbuilder/buildblock(_:_:_:_:))
- [buildBlock(_:_:_:_:_:)](/documentation/swiftui/tabcontentbuilder/buildblock(_:_:_:_:_:))
- [buildBlock(_:_:_:_:_:_:)](/documentation/swiftui/tabcontentbuilder/buildblock(_:_:_:_:_:_:))
- [buildBlock(_:_:_:_:_:_:_:)](/documentation/swiftui/tabcontentbuilder/buildblock(_:_:_:_:_:_:_:))
- [buildBlock(_:_:_:_:_:_:_:_:)](/documentation/swiftui/tabcontentbuilder/buildblock(_:_:_:_:_:_:_:_:))
- [buildBlock(_:_:_:_:_:_:_:_:_:)](/documentation/swiftui/tabcontentbuilder/buildblock(_:_:_:_:_:_:_:_:_:))
- [buildBlock(_:_:_:_:_:_:_:_:_:_:)](/documentation/swiftui/tabcontentbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:))
- [buildEither(first:)](/documentation/swiftui/tabcontentbuilder/buildeither(first:))
- [buildEither(second:)](/documentation/swiftui/tabcontentbuilder/buildeither(second:))
- [buildExpression(_:)](/documentation/swiftui/tabcontentbuilder/buildexpression(_:))
- [buildIf(_:)](/documentation/swiftui/tabcontentbuilder/buildif(_:))
- [buildLimitedAvailability(_:)](/documentation/swiftui/tabcontentbuilder/buildlimitedavailability(_:))

## See Also

### Configuring a tab

- [sectionActions(content:)](/documentation/swiftui/view/sectionactions(content:)): Adds custom actions to a section.
- [TabPlacement](/documentation/swiftui/tabplacement): A place that a tab can appear.
- [TabContent](/documentation/swiftui/tabcontent): A type that provides content for programmatically selectable tabs in a tab view.
- [AnyTabContent](/documentation/swiftui/anytabcontent): Type erased tab content.
