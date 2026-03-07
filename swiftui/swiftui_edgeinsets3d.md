# EdgeInsets3D

The inset distances for the faces of a 3D volume.

```swift
@frozen struct EdgeInsets3D
```

### Getting edge insets

- [top](/documentation/swiftui/edgeinsets3d/top): The inset distance along the top face of a 3D volume.
- [bottom](/documentation/swiftui/edgeinsets3d/bottom): The inset distance along the bottom face of a 3D volume.
- [leading](/documentation/swiftui/edgeinsets3d/leading): The inset distance along the leading face of a 3D volume.
- [trailing](/documentation/swiftui/edgeinsets3d/trailing): The inset distance along the top trailing of a 3D volume.
- [front](/documentation/swiftui/edgeinsets3d/front): The inset distance along the top front of a 3D volume.
- [back](/documentation/swiftui/edgeinsets3d/back): The inset distance along the top back of a 3D volume.

### Creating an edge inset

- [init(horizontal:vertical:depth:)](/documentation/swiftui/edgeinsets3d/init(horizontal:vertical:depth:)): Creates an `EdgeInsets3D` value with values provided for each axis.
- [init(top:leading:bottom:trailing:front:back:)](/documentation/swiftui/edgeinsets3d/init(top:leading:bottom:trailing:front:back:)): Creates an `EdgeInsets3D` value with values provided for each face.

## See Also

### Accessing edges, regions, and layouts

- [Edge](/documentation/swiftui/edge): An enumeration to indicate one edge of a rectangle.
- [Edge3D](/documentation/swiftui/edge3d): An edge or face of a 3D volume.
- [HorizontalEdge](/documentation/swiftui/horizontaledge): An edge on the horizontal axis.
- [VerticalEdge](/documentation/swiftui/verticaledge): An edge on the vertical axis.
- [EdgeInsets](/documentation/swiftui/edgeinsets): The inset distances for the sides of a rectangle.
