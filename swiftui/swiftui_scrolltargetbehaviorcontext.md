# ScrollTargetBehaviorContext

The context in which a scroll target behavior updates its scroll target.

```swift
@dynamicMemberLookup struct ScrollTargetBehaviorContext
```

### Getting the scroll target behavior context

- [axes](/documentation/swiftui/scrolltargetbehaviorcontext/axes): The axes in which the scrollable view is scrollable.
- [containerSize](/documentation/swiftui/scrolltargetbehaviorcontext/containersize): The size of the container of the scrollable view.
- [contentSize](/documentation/swiftui/scrolltargetbehaviorcontext/contentsize): The size of the content of the scrollable view.
- [originalTarget](/documentation/swiftui/scrolltargetbehaviorcontext/originaltarget): The original target when the scroll gesture began.
- [velocity](/documentation/swiftui/scrolltargetbehaviorcontext/velocity): The current velocity of the scrollable view’s scroll gesture.

### Accessing the context

- [subscript(dynamicMember:)](/documentation/swiftui/scrolltargetbehaviorcontext/subscript(dynamicmember:))

## See Also

### Defining scroll targets

- [scrollTargetBehavior(_:)](/documentation/swiftui/view/scrolltargetbehavior(_:)): Sets the scroll behavior of views scrollable in the provided axes.
- [scrollTargetLayout(isEnabled:)](/documentation/swiftui/view/scrolltargetlayout(isenabled:)): Configures the outermost layout as a scroll target layout.
- [ScrollTarget](/documentation/swiftui/scrolltarget): A type defining the target in which a scroll view should try and scroll to.
- [ScrollTargetBehavior](/documentation/swiftui/scrolltargetbehavior): A type that defines the scroll behavior of a scrollable view.
- [PagingScrollTargetBehavior](/documentation/swiftui/pagingscrolltargetbehavior): The scroll behavior that aligns scroll targets to container-based geometry.
- [ViewAlignedScrollTargetBehavior](/documentation/swiftui/viewalignedscrolltargetbehavior): The scroll behavior that aligns scroll targets to view-based geometry.
- [AnyScrollTargetBehavior](/documentation/swiftui/anyscrolltargetbehavior): A type-erased scroll target behavior.
- [ScrollTargetBehaviorProperties](/documentation/swiftui/scrolltargetbehaviorproperties): Properties influencing the scroll view a scroll target behavior applies to.
- [ScrollTargetBehaviorPropertiesContext](/documentation/swiftui/scrolltargetbehaviorpropertiescontext): The context in which a scroll target behavior can decide its properties.
