# BadgeProminence

The visual prominence of a badge.

```swift
struct BadgeProminence
```

## Overview

Badges can be used for different kinds of information, from the passive number of items in a container to the number of required actions. The prominence of badges in Lists can be adjusted to reflect this and be made to draw more or less attention to themselves.

Badges will default to `standard` prominence unless specified.

The following example shows a [List](/documentation/swiftui/list) displaying a list of folders with an informational badge with lower prominence, showing the number of items in the folder.

```swift
List(folders) { folder in
    Text(folder.name)
        .badge(folder.numberOfItems)
}
.badgeProminence(.decreased)
```

### Getting background prominence

- [standard](/documentation/swiftui/badgeprominence/standard): The standard level of prominence for a badge.
- [increased](/documentation/swiftui/badgeprominence/increased): The highest level of prominence for a badge.
- [decreased](/documentation/swiftui/badgeprominence/decreased): The lowest level of prominence for a badge.

## See Also

### Displaying a badge on a list item

- [badge(_:)](/documentation/swiftui/view/badge(_:)): Generates a badge for the view from an integer value.
- [badgeProminence(_:)](/documentation/swiftui/view/badgeprominence(_:)): Specifies the prominence of badges created by this view.
- [badgeProminence](/documentation/swiftui/environmentvalues/badgeprominence): The prominence to apply to badges associated with this environment.
