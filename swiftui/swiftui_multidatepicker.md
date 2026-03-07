# MultiDatePicker

A control for picking multiple dates.

```swift
struct MultiDatePicker<Label> where Label : View
```

## Overview

Use a `MultiDatePicker` when you want to provide a view that allows the user to select multiple dates.

The following example creates a basic `MultiDatePicker`, which appears as a calendar view representing the selected dates:

```swift
@State private var dates: Set<DateComponents> = []

var body: some View {
    MultiDatePicker("Dates Available", selection: $dates)
}
```

You can limit the `MultiDatePicker` to specific ranges of dates allowing selections only before or after a certain date or between two dates. The following example shows a multi-date picker that only permits selections within the 6th and (excluding) the 16th of December 2021 (in the `UTC` time zone):

```swift
@Environment(\.calendar) var calendar
@Environment(\.timeZone) var timeZone

var bounds: Range<Date> {
    let start = calendar.date(from: DateComponents(
        timeZone: timeZone, year: 2022, month: 6, day: 6))!
    let end = calendar.date(from: DateComponents(
        timeZone: timeZone, year: 2022, month: 6, day: 16))!
    return start ..< end
}

@State private var dates: Set<DateComponents> = []

var body: some View {
    MultiDatePicker("Dates Available", selection: $dates, in: bounds)
}
```

You can also specify an alternative locale, calendar and time zone through environment values. This can be useful when using a [PreviewProvider](/documentation/swiftui/previewprovider) to see how your multi-date picker behaves in environments that differ from your own.

The following example shows a multi-date picker with a custom locale, calendar and time zone:

```swift
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        MultiDatePicker("Dates Available", selection: .constant([]))
            .environment(\.locale, Locale.init(identifier: "zh"))
            .environment(
                \.calendar, Calendar.init(identifier: .chinese))
            .environment(\.timeZone, TimeZone(abbreviation: "HKT")!)
    }
}
```

### Picking dates

- [init(_:selection:)](/documentation/swiftui/multidatepicker/init(_:selection:)): Creates an instance that selects multiple dates with an unbounded range.
- [init(selection:label:)](/documentation/swiftui/multidatepicker/init(selection:label:)): Creates an instance that selects multiple dates with an unbounded range.

### Picking dates in a range

- [init(_:selection:in:)](/documentation/swiftui/multidatepicker/init(_:selection:in:)): Creates an instance that selects multiple dates on or after some start date.
- [init(selection:in:label:)](/documentation/swiftui/multidatepicker/init(selection:in:label:)): Creates an instance that selects multiple dates on or after some start date.

## See Also

### Choosing dates

- [DatePicker](/documentation/swiftui/datepicker): A control for selecting an absolute date.
- [datePickerStyle(_:)](/documentation/swiftui/view/datepickerstyle(_:)): Sets the style for date pickers within this view.
- [calendar](/documentation/swiftui/environmentvalues/calendar): The current calendar that views should use when handling dates.
- [timeZone](/documentation/swiftui/environmentvalues/timezone): The current time zone that views should use when handling dates.
