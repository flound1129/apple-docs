# SectionCollection

An opaque collection representing the sections of view.

```swift
struct SectionCollection
```

## Overview

Sections are constructed lazily, on demand, so access only as much of this collection as is necessary to create the resulting content.

You can get access to a view’s [SectionCollection](/documentation/swiftui/sectioncollection) by using the `Group/init(sectionsOf:transform:)` initializer.

Any content of the given view which is not explicitly specified as a section is grouped with its sibling content to form implicit sections, meaning the minimum number of sections in a `SectionCollection` is one.

## See Also

### Organizing views into sections

- [Section](/documentation/swiftui/section): A container view that you can use to add hierarchy within certain views.
- [SectionConfiguration](/documentation/swiftui/sectionconfiguration): Specifies the contents of a section.
