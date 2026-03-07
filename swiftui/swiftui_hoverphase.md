# HoverPhase

The current hovering state and value of the pointer.

```swift
@frozen enum HoverPhase
```

## Overview

When you use the [onContinuousHover(coordinateSpace:perform:)](/documentation/swiftui/view/oncontinuoushover(coordinatespace:perform:)) modifier, you can handle the hovering state using the `action` closure. SwiftUI calls the closure with a phase value to indicate the current hovering state. The following example updates `hoverLocation` and `isHovering` based on the phase provided to the closure:

```swift
@State private var hoverLocation: CGPoint = .zero
@State private var isHovering = false

var body: some View {
    VStack {
        Color.red
            .frame(width: 400, height: 400)
            .onContinuousHover { phase in
                switch phase {
                case .active(let location):
                    hoverLocation = location
                    isHovering = true
                case .ended:
                    isHovering = false
                }
            }
            .overlay {
                Rectangle()
                    .frame(width: 50, height: 50)
                    .foregroundColor(isHovering ? .green : .blue)
                    .offset(x: hoverLocation.x, y: hoverLocation.y)
            }
    }
}
```

### Getting hover phases

- [HoverPhase.active(_:)](/documentation/swiftui/hoverphase/active(_:)): The pointer’s location moved to the specified point within the view.
- [HoverPhase.ended](/documentation/swiftui/hoverphase/ended): The pointer exited the view.

## See Also

### Responding to hover events

- [onHover(perform:)](/documentation/swiftui/view/onhover(perform:)): Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [onContinuousHover(coordinateSpace:perform:)](/documentation/swiftui/view/oncontinuoushover(coordinatespace:perform:)): Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [hoverEffect(_:isEnabled:)](/documentation/swiftui/view/hovereffect(_:isenabled:)): Applies a hover effect to this view.
- [hoverEffectDisabled(_:)](/documentation/swiftui/view/hovereffectdisabled(_:)): Adds a condition that controls whether this view can display hover effects.
- [defaultHoverEffect(_:)](/documentation/swiftui/view/defaulthovereffect(_:)): Sets the default hover effect to use for views within this view.
- [isHoverEffectEnabled](/documentation/swiftui/environmentvalues/ishovereffectenabled): A Boolean value that indicates whether the view associated with this environment allows hover effects to be displayed.
- [HoverEffectPhaseOverride](/documentation/swiftui/hovereffectphaseoverride): Options for overriding a hover effect’s current phase.
- [OrnamentHoverContentEffect](/documentation/swiftui/ornamenthovercontenteffect): Presents an ornament on hover using a custom effect.
- [OrnamentHoverEffect](/documentation/swiftui/ornamenthovereffect): Presents an ornament on hover.
