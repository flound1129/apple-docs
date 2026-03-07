# AccessibilityTextContentType

Textual context that assistive technologies can use to improve the presentation of spoken text.

```swift
struct AccessibilityTextContentType
```

## Overview

Use an `AccessibilityTextContentType` value when setting the accessibility text content type of a view using the [accessibilityTextContentType(_:)](/documentation/swiftui/view/accessibilitytextcontenttype(_:)) modifier.

### Getting content types

- [console](/documentation/swiftui/accessibilitytextcontenttype/console): A type that represents text used for input, like in the Terminal app.
- [fileSystem](/documentation/swiftui/accessibilitytextcontenttype/filesystem): A type that represents text used by a file browser, like in the Finder app in macOS.
- [messaging](/documentation/swiftui/accessibilitytextcontenttype/messaging): A type that represents text used in a message, like in the Messages app.
- [narrative](/documentation/swiftui/accessibilitytextcontenttype/narrative): A type that represents text used in a story or poem, like in the Books app.
- [plain](/documentation/swiftui/accessibilitytextcontenttype/plain): A type that represents generic text that has no specific type.
- [sourceCode](/documentation/swiftui/accessibilitytextcontenttype/sourcecode): A type that represents text used in source code, like in Swift Playgrounds.
- [spreadsheet](/documentation/swiftui/accessibilitytextcontenttype/spreadsheet): A type that represents text used in a grid of data, like in the Numbers app.
- [wordProcessing](/documentation/swiftui/accessibilitytextcontenttype/wordprocessing): A type that represents text used in a document, like in the Pages app.

## See Also

### Describing content

- [accessibilityTextContentType(_:)](/documentation/swiftui/view/accessibilitytextcontenttype(_:)): Sets an accessibility text content type.
- [accessibilityHeading(_:)](/documentation/swiftui/view/accessibilityheading(_:)): Sets the accessibility level of this heading.
- [AccessibilityHeadingLevel](/documentation/swiftui/accessibilityheadinglevel): The hierarchy of a heading in relation to other headings.
