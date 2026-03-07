# BackgroundProminence

The prominence of backgrounds underneath other views.

```swift
struct BackgroundProminence
```

## Overview

Background prominence should influence foreground styling to maintain sufficient contrast against the background. For example, selected rows in a `List` and `Table` can have increased prominence backgrounds with accent color fills when focused; the foreground content above the background should be adjusted to reflect that level of prominence.

This can be read and written for views with the `EnvironmentValues.backgroundProminence` property.

### Getting background prominence

- [standard](/documentation/swiftui/backgroundprominence/standard): The standard prominence of a background
- [increased](/documentation/swiftui/backgroundprominence/increased): A more prominent background that likely requires some changes to the views above it.

## See Also

### Configuring backgrounds

- [listRowBackground(_:)](/documentation/swiftui/view/listrowbackground(_:)): Places a custom background view behind a list row item.
- [alternatingRowBackgrounds(_:)](/documentation/swiftui/view/alternatingrowbackgrounds(_:)): Overrides whether lists and tables in this view have alternating row backgrounds.
- [AlternatingRowBackgroundBehavior](/documentation/swiftui/alternatingrowbackgroundbehavior): The styling of views with respect to alternating row backgrounds.
- [backgroundProminence](/documentation/swiftui/environmentvalues/backgroundprominence): The prominence of the background underneath views associated with this environment.
