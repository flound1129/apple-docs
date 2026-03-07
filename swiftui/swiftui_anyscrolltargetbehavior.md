# AnyScrollTargetBehavior

A type-erased scroll target behavior.

```swift
@frozen struct AnyScrollTargetBehavior
```

## Overview

Provide this to the [scrollTargetBehavior(_:)](/documentation/swiftui/view/scrolltargetbehavior(_:)) modifier. When the underlying behavior changes, the scroll view to which this behavior applies will be updated.

Use this to dynamically control the scroll target behavior at runtime. For example, you could provide a paging behavior in compact size classes and a view aligned behavior otherwise.

```swift
@Environment(\.horizontalSizeClass) var sizeClass

var body: some View {
    ScrollView { ... }
        .scrollTargetBehavior(scrollTargetBehavior)
}

 var scrollTargetBehavior: some ScrollTargetBehavior {
    sizeClass == .compact
        ? AnyScrollTargetBehavior(.paging)
        : AnyScrollTargetBehavior(.viewAligned)
}
```

### Initializers

- [init(_:)](/documentation/swiftui/anyscrolltargetbehavior/init(_:)): Creates a new type-erase scroll target behavior.

### Instance Properties

- [base](/documentation/swiftui/anyscrolltargetbehavior/base): The type-erased scroll target behavior.

## See Also

### Defining scroll targets

- [scrollTargetBehavior(_:)](/documentation/swiftui/view/scrolltargetbehavior(_:)): Sets the scroll behavior of views scrollable in the provided axes.
- [scrollTargetLayout(isEnabled:)](/documentation/swiftui/view/scrolltargetlayout(isenabled:)): Configures the outermost layout as a scroll target layout.
- [ScrollTarget](/documentation/swiftui/scrolltarget): A type defining the target in which a scroll view should try and scroll to.
- [ScrollTargetBehavior](/documentation/swiftui/scrolltargetbehavior): A type that defines the scroll behavior of a scrollable view.
- [ScrollTargetBehaviorContext](/documentation/swiftui/scrolltargetbehaviorcontext): The context in which a scroll target behavior updates its scroll target.
- [PagingScrollTargetBehavior](/documentation/swiftui/pagingscrolltargetbehavior): The scroll behavior that aligns scroll targets to container-based geometry.
- [ViewAlignedScrollTargetBehavior](/documentation/swiftui/viewalignedscrolltargetbehavior): The scroll behavior that aligns scroll targets to view-based geometry.
- [ScrollTargetBehaviorProperties](/documentation/swiftui/scrolltargetbehaviorproperties): Properties influencing the scroll view a scroll target behavior applies to.
- [ScrollTargetBehaviorPropertiesContext](/documentation/swiftui/scrolltargetbehaviorpropertiescontext): The context in which a scroll target behavior can decide its properties.
