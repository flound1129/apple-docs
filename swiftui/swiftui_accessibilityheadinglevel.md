# AccessibilityHeadingLevel

The hierarchy of a heading in relation to other headings.

```swift
@frozen enum AccessibilityHeadingLevel
```

## Overview

Assistive technologies can use this to improve a user’s navigation through multiple headings. When users navigate through top level headings they expect the content for each heading to be unrelated.

For example, you can categorize a list of available products into sections, like Fruits and Vegetables. With only top level headings, this list requires no heading hierarchy, and you use the [AccessibilityHeadingLevel.unspecified](/documentation/swiftui/accessibilityheadinglevel/unspecified) heading level. On the other hand, if sections contain subsections, like if the Fruits section has subsections for varieties of Apples, Pears, and so on, you apply the [AccessibilityHeadingLevel.h1](/documentation/swiftui/accessibilityheadinglevel/h1) level to Fruits and Vegetables, and the [AccessibilityHeadingLevel.h2](/documentation/swiftui/accessibilityheadinglevel/h2) level to Apples and Pears.

Except for [AccessibilityHeadingLevel.h1](/documentation/swiftui/accessibilityheadinglevel/h1), be sure to precede all leveled headings by another heading with a level that’s one less.

### Getting the heading level

- [AccessibilityHeadingLevel.h1](/documentation/swiftui/accessibilityheadinglevel/h1): Level 1 heading.
- [AccessibilityHeadingLevel.h2](/documentation/swiftui/accessibilityheadinglevel/h2): Level 2 heading.
- [AccessibilityHeadingLevel.h3](/documentation/swiftui/accessibilityheadinglevel/h3): Level 3 heading.
- [AccessibilityHeadingLevel.h4](/documentation/swiftui/accessibilityheadinglevel/h4): Level 4 heading.
- [AccessibilityHeadingLevel.h5](/documentation/swiftui/accessibilityheadinglevel/h5): Level 5 heading.
- [AccessibilityHeadingLevel.h6](/documentation/swiftui/accessibilityheadinglevel/h6): Level 6 heading.
- [AccessibilityHeadingLevel.unspecified](/documentation/swiftui/accessibilityheadinglevel/unspecified): A heading without a hierarchy.

## See Also

### Describing content

- [accessibilityTextContentType(_:)](/documentation/swiftui/view/accessibilitytextcontenttype(_:)): Sets an accessibility text content type.
- [accessibilityHeading(_:)](/documentation/swiftui/view/accessibilityheading(_:)): Sets the accessibility level of this heading.
- [AccessibilityTextContentType](/documentation/swiftui/accessibilitytextcontenttype): Textual context that assistive technologies can use to improve the presentation of spoken text.
