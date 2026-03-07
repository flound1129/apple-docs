# ViewAlignedScrollTargetBehavior

The scroll behavior that aligns scroll targets to view-based geometry.

```swift
struct ViewAlignedScrollTargetBehavior
```

## Overview

You use this behavior when a scroll view should always align its scroll targets to a rectangle that’s aligned to the geometry of a view. In the following example, the scroll view always picks an item view to settle on.

```swift
ScrollView(.horizontal) {
    LazyHStack(spacing: 10.0) {
        ForEach(items) { item in
          ItemView(item)
        }
    }
    .scrollTargetLayout()
}
.scrollTargetBehavior(.viewAligned)
.padding(.horizontal, 20.0)
```

You configure which views should be used for settling using the [scrollTargetLayout(isEnabled:)](/documentation/swiftui/view/scrolltargetlayout(isenabled:)) modifier. Apply this modifier to a layout container like [LazyVStack](/documentation/swiftui/lazyvstack) or [HStack](/documentation/swiftui/hstack) and each individual view in that layout will be considered for alignment.

You can customize whether the view aligned behavior limits the number of views that can be scrolled at a time by using the [ViewAlignedScrollTargetBehavior.LimitBehavior](/documentation/swiftui/viewalignedscrolltargetbehavior/limitbehavior) type. Provide a value of [always](/documentation/swiftui/viewalignedscrolltargetbehavior/limitbehavior/always) to always have the behavior only allow a few views to be scrolled at a time.

By default, the view aligned behavior will limit the number of views it scrolls when in a compact horizontal size class when scrollable in the horizontal axis, when in a compact vertical size class when scrollable in the vertical axis, and otherwise does not impose any limit on the number of views that can be scrolled.

### Creating the target behavior

- [init(limitBehavior:)](/documentation/swiftui/viewalignedscrolltargetbehavior/init(limitbehavior:)): Creates a view aligned scroll behavior.
- [ViewAlignedScrollTargetBehavior.LimitBehavior](/documentation/swiftui/viewalignedscrolltargetbehavior/limitbehavior): A type that defines the amount of views that can be scrolled at a time.

### Initializers

- [init(anchor:)](/documentation/swiftui/viewalignedscrolltargetbehavior/init(anchor:)): Creates a view aligned scroll behavior with the provided anchor.
- [init(limitBehavior:anchor:)](/documentation/swiftui/viewalignedscrolltargetbehavior/init(limitbehavior:anchor:)): Creates a view aligned scroll behavior with the provided limit behavior and anchor.

## See Also

### Defining scroll targets

- [scrollTargetBehavior(_:)](/documentation/swiftui/view/scrolltargetbehavior(_:)): Sets the scroll behavior of views scrollable in the provided axes.
- [scrollTargetLayout(isEnabled:)](/documentation/swiftui/view/scrolltargetlayout(isenabled:)): Configures the outermost layout as a scroll target layout.
- [ScrollTarget](/documentation/swiftui/scrolltarget): A type defining the target in which a scroll view should try and scroll to.
- [ScrollTargetBehavior](/documentation/swiftui/scrolltargetbehavior): A type that defines the scroll behavior of a scrollable view.
- [ScrollTargetBehaviorContext](/documentation/swiftui/scrolltargetbehaviorcontext): The context in which a scroll target behavior updates its scroll target.
- [PagingScrollTargetBehavior](/documentation/swiftui/pagingscrolltargetbehavior): The scroll behavior that aligns scroll targets to container-based geometry.
- [AnyScrollTargetBehavior](/documentation/swiftui/anyscrolltargetbehavior): A type-erased scroll target behavior.
- [ScrollTargetBehaviorProperties](/documentation/swiftui/scrolltargetbehaviorproperties): Properties influencing the scroll view a scroll target behavior applies to.
- [ScrollTargetBehaviorPropertiesContext](/documentation/swiftui/scrolltargetbehaviorpropertiescontext): The context in which a scroll target behavior can decide its properties.
