# DigitalCrownEvent

An event emitted when the user rotates the Digital Crown.

```swift
struct DigitalCrownEvent
```

## Overview

Use the [digitalCrownRotation(_:)](/documentation/swiftui/view/digitalcrownrotation(_:)) modifier to receive these events.

### Getting events

- [offset](/documentation/swiftui/digitalcrownevent/offset): The offset of the digital crown when this event was sent.
- [velocity](/documentation/swiftui/digitalcrownevent/velocity): The velocity at which the offset was changing when this event was sent.

## See Also

### Interacting with the Digital Crown

- [digitalCrownAccessory(_:)](/documentation/swiftui/view/digitalcrownaccessory(_:)): Specifies the visibility of Digital Crown accessory Views on Apple Watch.
- [digitalCrownAccessory(content:)](/documentation/swiftui/view/digitalcrownaccessory(content:)): Places an accessory View next to the Digital Crown on Apple Watch.
- [digitalCrownRotation(_:from:through:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](/documentation/swiftui/view/digitalcrownrotation(_:from:through:sensitivity:iscontinuous:ishapticfeedbackenabled:onchange:onidle:)): Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(_:onChange:onIdle:)](/documentation/swiftui/view/digitalcrownrotation(_:onchange:onidle:)): Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](/documentation/swiftui/view/digitalcrownrotation(detent:from:through:by:sensitivity:iscontinuous:ishapticfeedbackenabled:onchange:onidle:)): Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(_:)](/documentation/swiftui/view/digitalcrownrotation(_:)): Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(_:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:)](/documentation/swiftui/view/digitalcrownrotation(_:from:through:by:sensitivity:iscontinuous:ishapticfeedbackenabled:)): Tracks Digital Crown rotations by updating the specified binding.
- [DigitalCrownRotationalSensitivity](/documentation/swiftui/digitalcrownrotationalsensitivity): The amount of Digital Crown rotation needed to move between two integer numbers.
