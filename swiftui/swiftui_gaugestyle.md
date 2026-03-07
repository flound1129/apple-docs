# GaugeStyle

Defines the implementation of all gauge instances within a view hierarchy.

```swift
@MainActor @preconcurrency protocol GaugeStyle
```

## Overview

To configure the style for all the [Gauge](/documentation/swiftui/gauge) instances in a view hierarchy, use the [gaugeStyle(_:)](/documentation/swiftui/view/gaugestyle(_:)) modifier. For example, you can configure a gauge to use the [circular](/documentation/swiftui/gaugestyle/circular) style:

```swift
Gauge(value: batteryLevel, in: 0...100) {
    Text("Battery Level")
}
.gaugeStyle(.circular)
```

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

### Getting the automatic style

- [automatic](/documentation/swiftui/gaugestyle/automatic): The default gauge view style in the current context of the view being styled.

### Getting circular gauge styles

- [circular](/documentation/swiftui/gaugestyle/circular): A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [accessoryCircular](/documentation/swiftui/gaugestyle/accessorycircular): A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [accessoryCircularCapacity](/documentation/swiftui/gaugestyle/accessorycircularcapacity): A gauge style that displays a closed ring that’s partially filled in to indicate the gauge’s current value.

### Getting linear gauge styles

- [linear](/documentation/swiftui/gaugestyle/linear): A gauge style that displays a bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [linearCapacity](/documentation/swiftui/gaugestyle/linearcapacity): A gauge style that displays a bar that fills from leading to trailing edges as the gauge’s current value increases.
- [accessoryLinear](/documentation/swiftui/gaugestyle/accessorylinear): A gauge style that displays bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [accessoryLinearCapacity](/documentation/swiftui/gaugestyle/accessorylinearcapacity): A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.

### Creating custom gauge styles

- [makeBody(configuration:)](/documentation/swiftui/gaugestyle/makebody(configuration:)): Creates a view representing the body of a gauge.
- [GaugeStyle.Configuration](/documentation/swiftui/gaugestyle/configuration): The properties of a gauge instance.
- [Body](/documentation/swiftui/gaugestyle/body): A view representing the body of a gauge.

### Supporting types

- [DefaultGaugeStyle](/documentation/swiftui/defaultgaugestyle): The default gauge view style in the current context of the view being styled.
- [CircularGaugeStyle](/documentation/swiftui/circulargaugestyle): A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [AccessoryCircularGaugeStyle](/documentation/swiftui/accessorycirculargaugestyle): A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [AccessoryCircularCapacityGaugeStyle](/documentation/swiftui/accessorycircularcapacitygaugestyle): A gauge style that displays a closed ring that’s partially filled in to indicate the gauge’s current value.
- [LinearGaugeStyle](/documentation/swiftui/lineargaugestyle): A gauge style that displays a bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [LinearCapacityGaugeStyle](/documentation/swiftui/linearcapacitygaugestyle): A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.
- [AccessoryLinearGaugeStyle](/documentation/swiftui/accessorylineargaugestyle): A gauge style that displays bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [AccessoryLinearCapacityGaugeStyle](/documentation/swiftui/accessorylinearcapacitygaugestyle): A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.

## See Also

### Styling indicators

- [gaugeStyle(_:)](/documentation/swiftui/view/gaugestyle(_:)): Sets the style for gauges within this view.
- [GaugeStyleConfiguration](/documentation/swiftui/gaugestyleconfiguration): The properties of a gauge instance.
- [progressViewStyle(_:)](/documentation/swiftui/view/progressviewstyle(_:)): Sets the style for progress views in this view.
- [ProgressViewStyle](/documentation/swiftui/progressviewstyle): A type that applies standard interaction behavior to all progress views within a view hierarchy.
- [ProgressViewStyleConfiguration](/documentation/swiftui/progressviewstyleconfiguration): The properties of a progress view instance.
