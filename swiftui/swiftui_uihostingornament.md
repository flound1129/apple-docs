# UIHostingOrnament

A model that represents an ornament suitable for being hosted in UIKit.

```swift
class UIHostingOrnament<Content> where Content : View
```

## Overview

Use a `UIHostingOrnament` when you want to add ornaments to a UIKit view controller. For example, the following adds a single bottom ornament to the current view controller:

```swift
self.ornaments = [
    UIHostingOrnament(sceneAnchor: .bottom) {
        OrnamentContent()
    }
]
```

### Creating a hosting ornament

- [init(sceneAnchor:contentAlignment:content:)](/documentation/swiftui/uihostingornament/init(sceneanchor:contentalignment:content:)): Creates an ornament with the specified alignment and content.
- [rootView](/documentation/swiftui/uihostingornament/rootview): The root view of the SwiftUI view hierarchy managed by this ornament.

### Setting the alignment

- [contentAlignment](/documentation/swiftui/uihostingornament/contentalignment): The alignment in the ornament used to position it.
- [sceneAnchor](/documentation/swiftui/uihostingornament/sceneanchor): The anchor point for aligning the ornament’s content (based on the `contentAlignment`) with the scene.

### Instance Properties

- [contentAlignment3D](/documentation/swiftui/uihostingornament/contentalignment3d)

## See Also

### Hosting an ornament in UIKit

- [UIOrnament](/documentation/swiftui/uiornament): The abstract base class that represents an ornament.
