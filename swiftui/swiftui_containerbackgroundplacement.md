# ContainerBackgroundPlacement

The placement of a container background.

```swift
struct ContainerBackgroundPlacement
```

## Overview

This method controls where to place a background that you specify with the [containerBackground(_:for:)](/documentation/swiftui/view/containerbackground(_:for:)) or [containerBackground(for:alignment:content:)](/documentation/swiftui/view/containerbackground(for:alignment:content:)) modifier.

### Getting placements

- [navigation](/documentation/swiftui/containerbackgroundplacement/navigation): A background placement inside a [NavigationStack](/documentation/swiftui/navigationstack) or [NavigationSplitView](/documentation/swiftui/navigationsplitview).
- [tabView](/documentation/swiftui/containerbackgroundplacement/tabview): A background placement inside a [TabView](/documentation/swiftui/tabview).
- [widget](/documentation/swiftui/containerbackgroundplacement/widget): The container background placement for a widget.

### Getting StoreKit placements

- [subscriptionStore](/documentation/swiftui/containerbackgroundplacement/subscriptionstore): An automatic placement within a subscription store view, based on the view’s context.
- [subscriptionStoreFullHeight](/documentation/swiftui/containerbackgroundplacement/subscriptionstorefullheight): A background placement that spans the full height of a subscription store view.
- [subscriptionStoreHeader](/documentation/swiftui/containerbackgroundplacement/subscriptionstoreheader): A background placement behind the marketing content of a subscription store view.

### Type Properties

- [navigationSplitView](/documentation/swiftui/containerbackgroundplacement/navigationsplitview): A background placement behind the content of a [NavigationSplitView](/documentation/swiftui/navigationsplitview).
- [window](/documentation/swiftui/containerbackgroundplacement/window): A  background placement inside a [Window](/documentation/swiftui/window) or [WindowGroup](/documentation/swiftui/windowgroup)

## See Also

### Layering views

- [Adding a background to your view](/documentation/swiftui/adding-a-background-to-your-view): Compose a background behind your view and extend it beyond the safe area insets.
- [ZStack](/documentation/swiftui/zstack): A view that overlays its subviews, aligning them in both axes.
- [zIndex(_:)](/documentation/swiftui/view/zindex(_:)): Controls the display order of overlapping views.
- [background(alignment:content:)](/documentation/swiftui/view/background(alignment:content:)): Layers the views that you specify behind this view.
- [background(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(_:ignoressafeareaedges:)): Sets the view’s background to a style.
- [background(ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(ignoressafeareaedges:)): Sets the view’s background to the default background style.
- [background(_:in:fillStyle:)](/documentation/swiftui/view/background(_:in:fillstyle:)): Sets the view’s background to an insettable shape filled with a style.
- [background(in:fillStyle:)](/documentation/swiftui/view/background(in:fillstyle:)): Sets the view’s background to an insettable shape filled with the default background style.
- [overlay(alignment:content:)](/documentation/swiftui/view/overlay(alignment:content:)): Layers the views that you specify in front of this view.
- [overlay(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/overlay(_:ignoressafeareaedges:)): Layers the specified style in front of this view.
- [overlay(_:in:fillStyle:)](/documentation/swiftui/view/overlay(_:in:fillstyle:)): Layers a shape that you specify in front of this view.
- [backgroundMaterial](/documentation/swiftui/environmentvalues/backgroundmaterial): The material underneath the current view.
- [containerBackground(_:for:)](/documentation/swiftui/view/containerbackground(_:for:)): Sets the container background of the enclosing container using a view.
- [containerBackground(for:alignment:content:)](/documentation/swiftui/view/containerbackground(for:alignment:content:)): Sets the container background of the enclosing container using a view.
