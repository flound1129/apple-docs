# TimelineView

A view that updates according to a schedule that you provide.

```swift
struct TimelineView<Schedule, Content> where Schedule : TimelineSchedule
```

## Overview

A timeline view acts as a container with no appearance of its own. Instead, it redraws the content it contains at scheduled points in time. For example, you can update the face of an analog timer once per second:

```swift
TimelineView(.periodic(from: startDate, by: 1)) { context in
    AnalogTimerView(date: context.date)
}
```

The closure that creates the content receives an input of type [TimelineView.Context](/documentation/swiftui/timelineview/context) that you can use to customize the content’s appearance. The context includes the [date](/documentation/swiftui/timelineview/context/date) that triggered the update. In the example above, the timeline view sends that date to an analog timer that you create so the timer view knows how to draw the hands on its face.

The context also includes a [cadence](/documentation/swiftui/timelineview/context/cadence-swift.property) property that you can use to hide unnecessary detail. For example, you can use the cadence to decide when it’s appropriate to display the timer’s second hand:

```swift
TimelineView(.periodic(from: startDate, by: 1.0)) { context in
    AnalogTimerView(
        date: context.date,
        showSeconds: context.cadence <= .seconds)
}
```

The system might use a cadence that’s slower than the schedule’s update rate. For example, a view on watchOS might remain visible when the user lowers their wrist, but update less frequently, and thus require less detail.

You can define a custom schedule by creating a type that conforms to the [TimelineSchedule](/documentation/swiftui/timelineschedule) protocol, or use one of the built-in schedule types:

- Use an [everyMinute](/documentation/swiftui/timelineschedule/everyminute) schedule to update at the beginning of each minute.
- Use a [periodic(from:by:)](/documentation/swiftui/timelineschedule/periodic(from:by:)) schedule to update periodically with a custom start time and interval between updates.
- Use an [explicit(_:)](/documentation/swiftui/timelineschedule/explicit(_:)) schedule when you need a finite number, or irregular set of updates.

For a schedule containing only dates in the past, the timeline view shows the last date in the schedule. For a schedule containing only dates in the future, the timeline draws its content using the current date until the first scheduled date arrives.

### Creating a timeline

- [init(_:content:)](/documentation/swiftui/timelineview/init(_:content:)-1mlmj): Creates a new timeline view that uses the given schedule.
- [TimelineView.Context](/documentation/swiftui/timelineview/context): Information passed to a timeline view’s content callback.

### Deprecated symbols

- [init(_:content:)](/documentation/swiftui/timelineview/init(_:content:)-67h35): Creates a new timeline view that uses the given schedule.

### Initializers

- [init(_:content:)](/documentation/swiftui/timelineview/init(_:content:)): Creates a new timeline view that uses the given schedule.

## See Also

### Updating a view on a schedule

- [Updating watchOS apps with timelines](/documentation/watchOS-Apps/updating-watchos-apps-with-timelines): Seamlessly schedule updates to your user interface, even while it’s inactive.
- [TimelineSchedule](/documentation/swiftui/timelineschedule): A type that provides a sequence of dates for use as a schedule.
- [TimelineViewDefaultContext](/documentation/swiftui/timelineviewdefaultcontext): Information passed to a timeline view’s content callback.
