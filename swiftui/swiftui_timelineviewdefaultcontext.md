# TimelineViewDefaultContext

Information passed to a timeline view’s content callback.

```swift
typealias TimelineViewDefaultContext = TimelineView<EveryMinuteTimelineSchedule, Never>.Context
```

## Discussion

The context includes both the date from the schedule that triggered the callback, and a cadence that you can use to customize the appearance of your view. For example, you might choose to display the second hand of an analog clock only when the cadence is [TimelineView.Context.Cadence.seconds](/documentation/swiftui/timelineview/context/cadence-swift.enum/seconds) or faster.

> **Note:**
> This type alias uses a specific concrete instance of [TimelineView.Context](/documentation/swiftui/timelineview/context) that all timeline views can use. It does this to prevent introducing an unnecessary generic parameter dependency on the context type.
>

## See Also

### Updating a view on a schedule

- [Updating watchOS apps with timelines](/documentation/watchOS-Apps/updating-watchos-apps-with-timelines): Seamlessly schedule updates to your user interface, even while it’s inactive.
- [TimelineView](/documentation/swiftui/timelineview): A view that updates according to a schedule that you provide.
- [TimelineSchedule](/documentation/swiftui/timelineschedule): A type that provides a sequence of dates for use as a schedule.
