# PagingScrollTargetBehavior

The scroll behavior that aligns scroll targets to container-based geometry.

```swift
struct PagingScrollTargetBehavior
```

## Overview

In the following example, every view in the lazy stack is flexible in both directions and the scroll view settles to container-aligned boundaries.

```swift
ScrollView {
    LazyVStack(spacing: 0.0) {
        ForEach(items) { item in
            FullScreenItem(item)
        }
    }
}
.scrollTargetBehavior(.paging)
```

### Creating the target behavior

- [init()](/documentation/swiftui/pagingscrolltargetbehavior/init()): Creates a paging scroll behavior.

## See Also

### Defining scroll targets

- [scrollTargetBehavior(_:)](/documentation/swiftui/view/scrolltargetbehavior(_:)): Sets the scroll behavior of views scrollable in the provided axes.
- [scrollTargetLayout(isEnabled:)](/documentation/swiftui/view/scrolltargetlayout(isenabled:)): Configures the outermost layout as a scroll target layout.
- [ScrollTarget](/documentation/swiftui/scrolltarget): A type defining the target in which a scroll view should try and scroll to.
- [ScrollTargetBehavior](/documentation/swiftui/scrolltargetbehavior): A type that defines the scroll behavior of a scrollable view.
- [ScrollTargetBehaviorContext](/documentation/swiftui/scrolltargetbehaviorcontext): The context in which a scroll target behavior updates its scroll target.
- [ViewAlignedScrollTargetBehavior](/documentation/swiftui/viewalignedscrolltargetbehavior): The scroll behavior that aligns scroll targets to view-based geometry.
- [AnyScrollTargetBehavior](/documentation/swiftui/anyscrolltargetbehavior): A type-erased scroll target behavior.
- [ScrollTargetBehaviorProperties](/documentation/swiftui/scrolltargetbehaviorproperties): Properties influencing the scroll view a scroll target behavior applies to.
- [ScrollTargetBehaviorPropertiesContext](/documentation/swiftui/scrolltargetbehaviorpropertiescontext): The context in which a scroll target behavior can decide its properties.
