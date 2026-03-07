# ContentMode

Constants that define how a view’s content fills the available space.

```swift
@frozen enum ContentMode
```

### Getting content modes

- [ContentMode.fill](/documentation/swiftui/contentmode/fill): An option that resizes the content so it occupies all available space, both vertically and horizontally.
- [ContentMode.fit](/documentation/swiftui/contentmode/fit): An option that resizes the content so it’s all within the available space, both vertically and horizontally.

## See Also

### Scaling, rotating, or transforming a view

- [scaledToFill()](/documentation/swiftui/view/scaledtofill()): Scales this view to fill its parent.
- [scaledToFit()](/documentation/swiftui/view/scaledtofit()): Scales this view to fit its parent.
- [scaleEffect(_:anchor:)](/documentation/swiftui/view/scaleeffect(_:anchor:)): Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.
- [scaleEffect(_:anchor:)](/documentation/swiftui/view/scaleeffect(_:anchor:)): Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.
- [scaleEffect(x:y:anchor:)](/documentation/swiftui/view/scaleeffect(x:y:anchor:)): Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [scaleEffect(x:y:z:anchor:)](/documentation/swiftui/view/scaleeffect(x:y:z:anchor:)): Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
- [aspectRatio(_:contentMode:)](/documentation/swiftui/view/aspectratio(_:contentmode:)): Constrains this view’s dimensions to the specified aspect ratio.
- [rotationEffect(_:anchor:)](/documentation/swiftui/view/rotationeffect(_:anchor:)): Rotates a view’s rendered output in two dimensions around the specified point.
- [rotation3DEffect(_:axis:anchor:anchorZ:perspective:)](/documentation/swiftui/view/rotation3deffect(_:axis:anchor:anchorz:perspective:)): Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)](/documentation/swiftui/view/perspectiverotationeffect(_:axis:anchor:anchorz:perspective:)): Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [rotation3DEffect(_:anchor:)](/documentation/swiftui/view/rotation3deffect(_:anchor:)): Rotates the view’s content by the specified 3D rotation value.
- [rotation3DEffect(_:axis:anchor:)](/documentation/swiftui/view/rotation3deffect(_:axis:anchor:)): Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.
- [transformEffect(_:)](/documentation/swiftui/view/transformeffect(_:)): Applies an affine transformation to this view’s rendered output.
- [transform3DEffect(_:)](/documentation/swiftui/view/transform3deffect(_:)): Applies a 3D transformation to this view’s rendered output.
- [projectionEffect(_:)](/documentation/swiftui/view/projectioneffect(_:)): Applies a projection transformation to this view’s rendered output.
