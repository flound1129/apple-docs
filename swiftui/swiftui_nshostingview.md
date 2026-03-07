# NSHostingView

An AppKit view that hosts a SwiftUI view hierarchy.

```swift
@MainActor @preconcurrency class NSHostingView<Content> where Content : View
```

## Overview

You use `NSHostingView` objects to integrate SwiftUI views into your AppKit view hierarchies. A hosting view is an [NSView](/documentation/AppKit/NSView) object that manages a single SwiftUI view, which may itself contain other SwiftUI views. Because it is an [NSView](/documentation/AppKit/NSView) object, you can integrate it into your existing AppKit view hierarchies to implement portions of your UI. For example, you can use a hosting view to implement a custom control.

A hosting view acts as a bridge between your SwiftUI views and your AppKit interface. During layout, the hosting view reports the content size preferences of your SwiftUI views back to the AppKit layout system so that it can size the view appropriately. The hosting view also coordinates event delivery.

### Creating a hosting view

- [init(rootView:)](/documentation/swiftui/nshostingview/init(rootview:)): Creates a hosting view object that wraps the specified SwiftUI view.
- [init(coder:)](/documentation/swiftui/nshostingview/init(coder:)): Creates a hosting view object from the contents of the specified archive.
- [prepareForReuse()](/documentation/swiftui/nshostingview/prepareforreuse())

### Getting the root view

- [rootView](/documentation/swiftui/nshostingview/rootview): The root view of the SwiftUI view hierarchy managed by this view controller.

### Configuring the view layout behavior

- [requiresConstraintBasedLayout](/documentation/swiftui/nshostingview/requiresconstraintbasedlayout)
- [userInterfaceLayoutDirection](/documentation/swiftui/nshostingview/userinterfacelayoutdirection)
- [isFlipped](/documentation/swiftui/nshostingview/isflipped)
- [layerContentsRedrawPolicy](/documentation/swiftui/nshostingview/layercontentsredrawpolicy)
- [updateConstraints()](/documentation/swiftui/nshostingview/updateconstraints())
- [layout()](/documentation/swiftui/nshostingview/layout())
- [safeAreaRegions](/documentation/swiftui/nshostingview/safearearegions): The safe area regions that this view controller adds to its view.

### Managing keyboard interaction

- [keyDown(with:)](/documentation/swiftui/nshostingview/keydown(with:)): Called when the user presses a key on the keyboard while this view is in the responder chain.
- [keyUp(with:)](/documentation/swiftui/nshostingview/keyup(with:)): Called when the user releases a key on the keyboard while this view is in the responder chain.
- [performKeyEquivalent(with:)](/documentation/swiftui/nshostingview/performkeyequivalent(with:))
- [insertText(_:)](/documentation/swiftui/nshostingview/inserttext(_:))
- [didChangeValue(forKey:)](/documentation/swiftui/nshostingview/didchangevalue(forkey:))
- [makeTouchBar()](/documentation/swiftui/nshostingview/maketouchbar())

### Responding to mouse events

- [mouseDown(with:)](/documentation/swiftui/nshostingview/mousedown(with:))
- [mouseUp(with:)](/documentation/swiftui/nshostingview/mouseup(with:))
- [otherMouseDown(with:)](/documentation/swiftui/nshostingview/othermousedown(with:))
- [otherMouseUp(with:)](/documentation/swiftui/nshostingview/othermouseup(with:))
- [rightMouseDown(with:)](/documentation/swiftui/nshostingview/rightmousedown(with:))
- [rightMouseUp(with:)](/documentation/swiftui/nshostingview/rightmouseup(with:))
- [mouseEntered(with:)](/documentation/swiftui/nshostingview/mouseentered(with:))
- [mouseExited(with:)](/documentation/swiftui/nshostingview/mouseexited(with:))
- [mouseDragged(with:)](/documentation/swiftui/nshostingview/mousedragged(with:))
- [mouseMoved(with:)](/documentation/swiftui/nshostingview/mousemoved(with:))
- [otherMouseDragged(with:)](/documentation/swiftui/nshostingview/othermousedragged(with:))
- [rightMouseDragged(with:)](/documentation/swiftui/nshostingview/rightmousedragged(with:))
- [cursorUpdate(with:)](/documentation/swiftui/nshostingview/cursorupdate(with:))

### Responding to touch events

- [touchesBegan(with:)](/documentation/swiftui/nshostingview/touchesbegan(with:))
- [touchesCancelled(with:)](/documentation/swiftui/nshostingview/touchescancelled(with:))
- [touchesEnded(with:)](/documentation/swiftui/nshostingview/touchesended(with:))
- [touchesMoved(with:)](/documentation/swiftui/nshostingview/touchesmoved(with:))

### Responding to gestures

- [magnify(with:)](/documentation/swiftui/nshostingview/magnify(with:))
- [rotate(with:)](/documentation/swiftui/nshostingview/rotate(with:))
- [scrollWheel(with:)](/documentation/swiftui/nshostingview/scrollwheel(with:))

### Handling drag and drop

- [validRequestor(forSendType:returnType:)](/documentation/swiftui/nshostingview/validrequestor(forsendtype:returntype:))

### Providing a context menu

- [menu(for:)](/documentation/swiftui/nshostingview/menu(for:))

### Responding to actions

- [responds(to:)](/documentation/swiftui/nshostingview/responds(to:))
- [forwardingTarget(for:)](/documentation/swiftui/nshostingview/forwardingtarget(for:))
- [doCommand(by:)](/documentation/swiftui/nshostingview/docommand(by:))

### Configuring the responder behavior

- [acceptsFirstResponder](/documentation/swiftui/nshostingview/acceptsfirstresponder)
- [needsPanelToBecomeKey](/documentation/swiftui/nshostingview/needspaneltobecomekey)

### Managing the view hierarchy

- [viewWillMove(toWindow:)](/documentation/swiftui/nshostingview/viewwillmove(towindow:))
- [viewDidMoveToWindow()](/documentation/swiftui/nshostingview/viewdidmovetowindow())
- [viewDidChangeBackingProperties()](/documentation/swiftui/nshostingview/viewdidchangebackingproperties())
- [viewDidChangeEffectiveAppearance()](/documentation/swiftui/nshostingview/viewdidchangeeffectiveappearance())

### Modifying the frame rectangle

- [intrinsicContentSize](/documentation/swiftui/nshostingview/intrinsiccontentsize)
- [setFrameSize(_:)](/documentation/swiftui/nshostingview/setframesize(_:))
- [firstBaselineOffsetFromTop](/documentation/swiftui/nshostingview/firstbaselineoffsetfromtop)
- [lastBaselineOffsetFromBottom](/documentation/swiftui/nshostingview/lastbaselineoffsetfrombottom)
- [sizingOptions](/documentation/swiftui/nshostingview/sizingoptions): The options for how the hosting view creates and updates constraints based on the size of its SwiftUI content.
- [firstTextLineCenter](/documentation/swiftui/nshostingview/firsttextlinecenter)

### Testing for hits

- [hitTest(_:)](/documentation/swiftui/nshostingview/hittest(_:))

### Managing accessibility behaviors

- [accessibilityFocusedUIElement](/documentation/swiftui/nshostingview/accessibilityfocuseduielement)
- [accessibilityChildren()](/documentation/swiftui/nshostingview/accessibilitychildren())
- [accessibilityChildrenInNavigationOrder()](/documentation/swiftui/nshostingview/accessibilitychildreninnavigationorder())
- [accessibilityHitTest(_:)](/documentation/swiftui/nshostingview/accessibilityhittest(_:))
- [accessibilityRole()](/documentation/swiftui/nshostingview/accessibilityrole())
- [accessibilitySubrole()](/documentation/swiftui/nshostingview/accessibilitysubrole())
- [isAccessibilityElement()](/documentation/swiftui/nshostingview/isaccessibilityelement())

### Bridging with SwiftUI

- [sceneBridgingOptions](/documentation/swiftui/nshostingview/scenebridgingoptions): The options for which aspects of the window will be managed by this hosting view.

### Initializers

- [init(coder:rootView:)](/documentation/swiftui/nshostingview/init(coder:rootview:)): Creates a hosting view object from an archive and the specified SwiftUI view.

### Instance Properties

- [clipsToBounds](/documentation/swiftui/nshostingview/clipstobounds)

### Instance Methods

- [acceptsFirstMouse(for:)](/documentation/swiftui/nshostingview/acceptsfirstmouse(for:))
- [beginDocument()](/documentation/swiftui/nshostingview/begindocument())
- [didAddSubview(_:)](/documentation/swiftui/nshostingview/didaddsubview(_:))
- [endDocument()](/documentation/swiftui/nshostingview/enddocument())
- [observeValue(forKeyPath:of:change:context:)](/documentation/swiftui/nshostingview/observevalue(forkeypath:of:change:context:))
- [shouldDelayWindowOrdering(for:)](/documentation/swiftui/nshostingview/shoulddelaywindowordering(for:))
- [showContextMenuForSelection(_:)](/documentation/swiftui/nshostingview/showcontextmenuforselection(_:))
- [viewDidEndLiveResize()](/documentation/swiftui/nshostingview/viewdidendliveresize())
- [viewWillStartLiveResize()](/documentation/swiftui/nshostingview/viewwillstartliveresize())
- [willRemoveSubview(_:)](/documentation/swiftui/nshostingview/willremovesubview(_:))

## See Also

### Displaying SwiftUI views in AppKit

- [Unifying your app’s animations](/documentation/swiftui/unifying-your-app-s-animations): Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [NSHostingController](/documentation/swiftui/nshostingcontroller): An AppKit view controller that hosts SwiftUI view hierarchy.
- [NSHostingMenu](/documentation/swiftui/nshostingmenu): An AppKit menu with menu items that are defined by a SwiftUI View.
- [NSHostingSizingOptions](/documentation/swiftui/nshostingsizingoptions): Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.
- [NSHostingSceneRepresentation](/documentation/swiftui/nshostingscenerepresentation): An AppKit type that hosts and can present SwiftUI scenes
- [NSHostingSceneBridgingOptions](/documentation/swiftui/nshostingscenebridgingoptions): Options for how hosting views and controllers manage aspects of the associated window.
