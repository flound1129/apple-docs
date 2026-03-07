# ToggleStyleConfiguration

The properties of a toggle instance.

```swift
struct ToggleStyleConfiguration
```

## Overview

When you define a custom toggle style by creating a type that conforms to the [ToggleStyle](/documentation/swiftui/togglestyle) protocol, you implement the [makeBody(configuration:)](/documentation/swiftui/togglestyle/makebody(configuration:)) method. That method takes a `ToggleStyleConfiguration` input that has the information you need to define the behavior and appearance of a [Toggle](/documentation/swiftui/toggle).

The configuration structure’s [label](/documentation/swiftui/togglestyleconfiguration/label-swift.property) reflects the toggle’s content, which might be the value that you supply to the `label` parameter of the [init(isOn:label:)](/documentation/swiftui/toggle/init(ison:label:)) initializer. Alternatively, it could be another view that SwiftUI builds from an initializer that takes a string input, like [init(_:isOn:)](/documentation/swiftui/toggle/init(_:ison:)). In either case, incorporate the label into the toggle’s view to help the user understand what the toggle does. For example, the built-in [switch](/documentation/swiftui/togglestyle/switch) style horizontally stacks the label with the control element.

The structure’s [isOn](/documentation/swiftui/togglestyleconfiguration/ison) property provides a [Binding](/documentation/swiftui/binding) to the state of the toggle. Adjust the appearance of the toggle based on this value. For example, the built-in [button](/documentation/swiftui/togglestyle/button) style fills the button’s background when the property is `true`, but leaves the background empty when the property is `false`. Change the value when the user performs an action that’s meant to change the toggle, like the button does when tapped or clicked by the user.

### Getting the label view

- [label](/documentation/swiftui/togglestyleconfiguration/label-swift.property): A view that describes the effect of switching the toggle between states.
- [ToggleStyleConfiguration.Label](/documentation/swiftui/togglestyleconfiguration/label-swift.struct): A type-erased label of a toggle.

### Managing the toggle state

- [isMixed](/documentation/swiftui/togglestyleconfiguration/ismixed): Whether the [Toggle](/documentation/swiftui/toggle) is currently in a mixed state.
- [isOn](/documentation/swiftui/togglestyleconfiguration/ison): A binding to a state property that indicates whether the toggle is on.
- [$isOn](/documentation/swiftui/togglestyleconfiguration/$ison)

## See Also

### Styling toggles

- [toggleStyle(_:)](/documentation/swiftui/view/togglestyle(_:)): Sets the style for toggles in a view hierarchy.
- [ToggleStyle](/documentation/swiftui/togglestyle): The appearance and behavior of a toggle.
