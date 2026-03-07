# AccessibilityDirectTouchOptions

An option set that defines the functionality of a view’s direct touch area.

```swift
struct AccessibilityDirectTouchOptions
```

### Getting the options

- [requiresActivation](/documentation/swiftui/accessibilitydirecttouchoptions/requiresactivation): Prevents touch passthrough with the direct touch area until an assistive technology, such as VoiceOver, has activated the direct touch area through a user action, for example a double tap.
- [silentOnTouch](/documentation/swiftui/accessibilitydirecttouchoptions/silentontouch): Allows a direct touch area to immediately receive touch events without an assitive technology, such as VoiceOver, speaking. Appropriate for apps that provide direct audio feedback on touch that would conflict with speech feedback.

### Creating a set of options

- [init(rawValue:)](/documentation/swiftui/accessibilitydirecttouchoptions/init(rawvalue:)): Create a set of direct touch options

## See Also

### Making gestures accessible

- [accessibilityActivationPoint(_:)](/documentation/swiftui/view/accessibilityactivationpoint(_:)): The activation point for an element is the location assistive technologies use to initiate gestures.
- [accessibilityActivationPoint(_:isEnabled:)](/documentation/swiftui/view/accessibilityactivationpoint(_:isenabled:)): The activation point for an element is the location assistive technologies use to initiate gestures.
- [accessibilityDragPoint(_:description:)](/documentation/swiftui/view/accessibilitydragpoint(_:description:)): The point an assistive technology should use to begin a drag interaction.
- [accessibilityDragPoint(_:description:isEnabled:)](/documentation/swiftui/view/accessibilitydragpoint(_:description:isenabled:)): The point an assistive technology should use to begin a drag interaction.
- [accessibilityDropPoint(_:description:)](/documentation/swiftui/view/accessibilitydroppoint(_:description:)): The point an assistive technology should use to end a drag interaction.
- [accessibilityDropPoint(_:description:isEnabled:)](/documentation/swiftui/view/accessibilitydroppoint(_:description:isenabled:)): The point an assistive technology should use to end a drag interaction.
- [accessibilityDirectTouch(_:options:)](/documentation/swiftui/view/accessibilitydirecttouch(_:options:)): Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [accessibilityZoomAction(_:)](/documentation/swiftui/view/accessibilityzoomaction(_:)): Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.
- [AccessibilityZoomGestureAction](/documentation/swiftui/accessibilityzoomgestureaction): Position and direction information of a zoom gesture that someone performs with an assistive technology like VoiceOver.
