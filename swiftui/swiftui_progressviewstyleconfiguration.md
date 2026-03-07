# ProgressViewStyleConfiguration

The properties of a progress view instance.

```swift
struct ProgressViewStyleConfiguration
```

### Configuring the label

- [label](/documentation/swiftui/progressviewstyleconfiguration/label-swift.property): A view that describes the task represented by the progress view.
- [ProgressViewStyleConfiguration.Label](/documentation/swiftui/progressviewstyleconfiguration/label-swift.struct): A type-erased label describing the task represented by the progress view.

### Configuring the current value label

- [currentValueLabel](/documentation/swiftui/progressviewstyleconfiguration/currentvaluelabel-swift.property): A view that describes the current value of a progress view.
- [ProgressViewStyleConfiguration.CurrentValueLabel](/documentation/swiftui/progressviewstyleconfiguration/currentvaluelabel-swift.struct): A type-erased label that describes the current value of a progress view.

### Configuring progress completion

- [fractionCompleted](/documentation/swiftui/progressviewstyleconfiguration/fractioncompleted): The completed fraction of the task represented by the progress view, from `0.0` (not yet started) to `1.0` (fully complete), or `nil` if the progress is indeterminate or relative to a date interval.

## See Also

### Styling indicators

- [gaugeStyle(_:)](/documentation/swiftui/view/gaugestyle(_:)): Sets the style for gauges within this view.
- [GaugeStyle](/documentation/swiftui/gaugestyle): Defines the implementation of all gauge instances within a view hierarchy.
- [GaugeStyleConfiguration](/documentation/swiftui/gaugestyleconfiguration): The properties of a gauge instance.
- [progressViewStyle(_:)](/documentation/swiftui/view/progressviewstyle(_:)): Sets the style for progress views in this view.
- [ProgressViewStyle](/documentation/swiftui/progressviewstyle): A type that applies standard interaction behavior to all progress views within a view hierarchy.
