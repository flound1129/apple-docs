# AccessibilityZoomGestureAction

Position and direction information of a zoom gesture that someone performs with an assistive technology like VoiceOver.

```swift
struct AccessibilityZoomGestureAction
```

### Getting the action’s direction

- [direction](/documentation/swiftui/accessibilityzoomgestureaction/direction-swift.property): The zoom gesture’s direction.
- [AccessibilityZoomGestureAction.Direction](/documentation/swiftui/accessibilityzoomgestureaction/direction-swift.enum): A direction that matches the movement of a zoom gesture performed by an assistive technology, such as a swipe up and down in Voiceover’s zoom rotor.

### Getting location information

- [location](/documentation/swiftui/accessibilityzoomgestureaction/location): The zoom gesture’s activation point, normalized to the accessibility element’s frame.
- [point](/documentation/swiftui/accessibilityzoomgestureaction/point): The zoom gesture’s activation point within the window’s coordinate space.

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
- [AccessibilityDirectTouchOptions](/documentation/swiftui/accessibilitydirecttouchoptions): An option set that defines the functionality of a view’s direct touch area.
