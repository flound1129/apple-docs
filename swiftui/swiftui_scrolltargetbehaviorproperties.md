# ScrollTargetBehaviorProperties

Properties influencing the scroll view a scroll target behavior applies to.

```swift
struct ScrollTargetBehaviorProperties
```

### Initializers

- [init()](/documentation/swiftui/scrolltargetbehaviorproperties/init()): Creates a default set of properties.

### Instance Properties

- [limitsScrolls](/documentation/swiftui/scrolltargetbehaviorproperties/limitsscrolls): Whether this scroll target behavior should limit the distance a scroll view scrolls by default. When enabled, the scroll view prefers to scroll a shorter distance. By default, this is not enabled.

## See Also

### Defining scroll targets

- [scrollTargetBehavior(_:)](/documentation/swiftui/view/scrolltargetbehavior(_:)): Sets the scroll behavior of views scrollable in the provided axes.
- [scrollTargetLayout(isEnabled:)](/documentation/swiftui/view/scrolltargetlayout(isenabled:)): Configures the outermost layout as a scroll target layout.
- [ScrollTarget](/documentation/swiftui/scrolltarget): A type defining the target in which a scroll view should try and scroll to.
- [ScrollTargetBehavior](/documentation/swiftui/scrolltargetbehavior): A type that defines the scroll behavior of a scrollable view.
- [ScrollTargetBehaviorContext](/documentation/swiftui/scrolltargetbehaviorcontext): The context in which a scroll target behavior updates its scroll target.
- [PagingScrollTargetBehavior](/documentation/swiftui/pagingscrolltargetbehavior): The scroll behavior that aligns scroll targets to container-based geometry.
- [ViewAlignedScrollTargetBehavior](/documentation/swiftui/viewalignedscrolltargetbehavior): The scroll behavior that aligns scroll targets to view-based geometry.
- [AnyScrollTargetBehavior](/documentation/swiftui/anyscrolltargetbehavior): A type-erased scroll target behavior.
- [ScrollTargetBehaviorPropertiesContext](/documentation/swiftui/scrolltargetbehaviorpropertiescontext): The context in which a scroll target behavior can decide its properties.
