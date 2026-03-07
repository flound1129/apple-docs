# Unifying your app’s animations

Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.

## Overview

Many apps use a combination of SwiftUI, UIKit, and AppKit to build and animate their interfaces. In iOS 18 and later, you can use SwiftUI animations in UIKit and AppKit. SwiftUI provides a wide range of standard as well as custom animation types.

![A conceptual illustration of a disclosure indicator, shown animating frame by frame from its collapsed position to its expanded position.]

SwiftUI, UIKit, and AppKit use different underlying implementations for animation. Apps that use multiple frameworks for animation might encounter certain issues, such as syncing animation timing or other inconsistencies, that can be difficult to troubleshoot and lead to a suboptimal user experience. Use SwiftUI animations to animate UI across all of these frameworks to create a more consistent and seamless experience on every platform.

### Create a SwiftUI animation

To create a SwiftUI animation in UIKit or AppKit, import SwiftUI and create a SwiftUI [Animation](/documentation/swiftui/animation). Then, pass that animation as a parameter into the [animate(_:changes:completion:)](/documentation/UIKit/UIView/animate(_:changes:completion:)) class method on `UIView`, or the [animate(_:changes:completion:)](/documentation/AppKit/NSAnimationContext/animate(_:changes:completion:)) class method on `NSAnimationContext`. The following examples compare how you can create a basic spring animation using a SwiftUI [Animation](/documentation/swiftui/animation) type across SwiftUI, UIKit, and AppKit.

### Use completion handlers with SwiftUI animations

You can provide an optional completion handler to these animation methods, which the system calls automatically after the animations complete. The following examples show a completion handler that changes the background color of the view to indicate when the animation completes.

### Retarget a SwiftUI animation

Similar to animations in SwiftUI views, you can smoothly retarget the animations you perform using the [animate(_:changes:completion:)](/documentation/UIKit/UIView/animate(_:changes:completion:)) class method on `UIView` or the [animate(_:changes:completion:)](/documentation/AppKit/NSAnimationContext/animate(_:changes:completion:)) class method on `NSAnimationContext`. Retargeting a SwiftUI animation uses the velocity from the previous animations to carry the animation forward with continuous velocity, creating a fluid animation experience. The following examples show retargeting an in-progress animation.

### Troubleshoot animations

Syncing animations across frameworks can surface differing behavior across implementations. Keep these tips in mind when you troubleshoot animations in your app:

- SwiftUI animations run on a background thread in your app’s process.
- SwiftUI animations don’t have a backing [CAAnimation](/documentation/QuartzCore/CAAnimation), which differentiates them from [UIView](/documentation/UIKit/UIView) animations.
- SwiftUI animations aren’t compatible with [UIViewPropertyAnimator](/documentation/UIKit/UIViewPropertyAnimator) or `UIView` keyframe animations.

For more information about providing a great animation experience in your app, see [Enhance your UI animations and transitions](https://developer.apple.com/wwdc24/10145/).

## See Also

### Related Documentation

- [Animation](/documentation/swiftui/animation): The way a view changes over time to create a smooth visual transition from one state to another.
- [withAnimation(_:_:)](/documentation/swiftui/withanimation(_:_:)): Returns the result of recomputing the view’s body with the provided animation.
- [animate(_:changes:completion:)](/documentation/UIKit/UIView/animate(_:changes:completion:))
- [animate(_:changes:completion:)](/documentation/AppKit/NSAnimationContext/animate(_:changes:completion:)): Animate changes to one or more views using the specified SwiftUI animation.

### Displaying SwiftUI views in AppKit

- [NSHostingController](/documentation/swiftui/nshostingcontroller): An AppKit view controller that hosts SwiftUI view hierarchy.
- [NSHostingView](/documentation/swiftui/nshostingview): An AppKit view that hosts a SwiftUI view hierarchy.
- [NSHostingMenu](/documentation/swiftui/nshostingmenu): An AppKit menu with menu items that are defined by a SwiftUI View.
- [NSHostingSizingOptions](/documentation/swiftui/nshostingsizingoptions): Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.
- [NSHostingSceneRepresentation](/documentation/swiftui/nshostingscenerepresentation): An AppKit type that hosts and can present SwiftUI scenes
- [NSHostingSceneBridgingOptions](/documentation/swiftui/nshostingscenebridgingoptions): Options for how hosting views and controllers manage aspects of the associated window.
