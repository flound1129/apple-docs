# AccessibilityChildBehavior

Defines the behavior for the child elements of the new parent element.

```swift
struct AccessibilityChildBehavior
```

### Getting behaviors

- [combine](/documentation/swiftui/accessibilitychildbehavior/combine): Any child accessibility element’s properties are merged into the new accessibility element.
- [contain](/documentation/swiftui/accessibilitychildbehavior/contain): Any child accessibility elements become children of the new accessibility element.
- [ignore](/documentation/swiftui/accessibilitychildbehavior/ignore): Any child accessibility elements become hidden.

## See Also

### Creating accessible elements

- [accessibilityElement(children:)](/documentation/swiftui/view/accessibilityelement(children:)): Creates a new accessibility element, or modifies the [AccessibilityChildBehavior](/documentation/swiftui/accessibilitychildbehavior) of the existing accessibility element.
- [accessibilityChildren(children:)](/documentation/swiftui/view/accessibilitychildren(children:)): Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.
- [accessibilityRepresentation(representation:)](/documentation/swiftui/view/accessibilityrepresentation(representation:)): Replaces one or more accessibility elements for this view with new accessibility elements.
