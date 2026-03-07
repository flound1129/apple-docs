# EdgeInsets

The inset distances for the sides of a rectangle.

```swift
@frozen struct EdgeInsets
```

### Getting edge insets

- [top](/documentation/swiftui/edgeinsets/top)
- [bottom](/documentation/swiftui/edgeinsets/bottom)
- [leading](/documentation/swiftui/edgeinsets/leading)
- [trailing](/documentation/swiftui/edgeinsets/trailing)

### Creating an edge inset

- [init()](/documentation/swiftui/edgeinsets/init())
- [init(top:leading:bottom:trailing:)](/documentation/swiftui/edgeinsets/init(top:leading:bottom:trailing:))
- [init(_:)](/documentation/swiftui/edgeinsets/init(_:)): Creates a 2D `EdgeInsets` from an `EdgeInsets3D`, dropping its `front` and `back` values.

### Instance Methods

- [inset(by:edges:)](/documentation/swiftui/edgeinsets/inset(by:edges:)): Returns an inset that has been modified by the corner sizes in the specified edges. When two corner insets diverge in their values for the specified edge, the maximum inset value will be used. For example, when the top edge is specified, the top inset will be adjusted by the larger of the two heights from the top leading and trailing corner inset sizes.

## See Also

### Accessing edges, regions, and layouts

- [Edge](/documentation/swiftui/edge): An enumeration to indicate one edge of a rectangle.
- [Edge3D](/documentation/swiftui/edge3d): An edge or face of a 3D volume.
- [HorizontalEdge](/documentation/swiftui/horizontaledge): An edge on the horizontal axis.
- [VerticalEdge](/documentation/swiftui/verticaledge): An edge on the vertical axis.
- [EdgeInsets3D](/documentation/swiftui/edgeinsets3d): The inset distances for the faces of a 3D volume.
