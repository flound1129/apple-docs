# TimeDataSource

A source of time related data.

```swift
struct TimeDataSource<Value>
```

## Overview

Instances of this type provide [Text](/documentation/swiftui/text) with live and automatically updating values in Widgets, Live Activities, watchOS Complications, and of course regular apps.

### Type Properties

- [currentDate](/documentation/swiftui/timedatasource/currentdate): A time data source that produces `Date.now`.

### Type Methods

- [dateRange(endingAt:)](/documentation/swiftui/timedatasource/daterange(endingat:)): A time data source that produces `min(date, Date.now)..<date`.
- [dateRange(startingAt:)](/documentation/swiftui/timedatasource/daterange(startingat:)): A time data source that produces `date..<max(date, Date.now)`.
- [durationOffset(to:)](/documentation/swiftui/timedatasource/durationoffset(to:)): A time data source that produces the offset between `Date.now` and the given `date` as a `Duration`.

## See Also

### Formatting date and time

- [SystemFormatStyle](/documentation/swiftui/systemformatstyle): A namespace for format styles that implement designs used across Apple’s platformes.
