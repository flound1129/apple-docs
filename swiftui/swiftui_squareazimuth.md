# SquareAzimuth

A type describing what direction something is being viewed from along the horizontal plane and snapped to 4 directions.

```swift
@frozen enum SquareAzimuth
```

### Structures

- [SquareAzimuth.Set](/documentation/swiftui/squareazimuth/set)

### Enumeration Cases

- [SquareAzimuth.back](/documentation/swiftui/squareazimuth/back): Has an orientation with an horizontal angle equal to `180°`
- [SquareAzimuth.front](/documentation/swiftui/squareazimuth/front): Has an orientation with an horizontal angle equal to `0°`.
- [SquareAzimuth.left](/documentation/swiftui/squareazimuth/left): Has an orientation with an horizontal angle equal to `270°`.
- [SquareAzimuth.right](/documentation/swiftui/squareazimuth/right): Has an orientation with an horizontal angle equal to `90°`.

### Initializers

- [init(closestToAzimuth:)](/documentation/swiftui/squareazimuth/init(closesttoazimuth:)): Creates a [SquareAzimuth](/documentation/swiftui/squareazimuth) case with an orientation that has a horizontal angle closest to the provided azimuth.

### Instance Properties

- [orientation](/documentation/swiftui/squareazimuth/orientation): A 3D rotation that is snapped to the center of one of the four sides.

## See Also

### Interacting with volumes

- [onVolumeViewpointChange(updateStrategy:initial:_:)](/documentation/swiftui/view/onvolumeviewpointchange(updatestrategy:initial:_:)): Adds an action to perform when the viewpoint of the volume changes.
- [supportedVolumeViewpoints(_:)](/documentation/swiftui/view/supportedvolumeviewpoints(_:)): Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [VolumeViewpointUpdateStrategy](/documentation/swiftui/volumeviewpointupdatestrategy): A type describing when the action provided to [onVolumeViewpointChange(updateStrategy:initial:_:)](/documentation/swiftui/view/onvolumeviewpointchange(updatestrategy:initial:_:)) should be called.
- [Viewpoint3D](/documentation/swiftui/viewpoint3d): A type describing what direction something is being viewed from.
- [WorldAlignmentBehavior](/documentation/swiftui/worldalignmentbehavior): A type representing the world alignment behavior for a scene.
- [volumeWorldAlignment(_:)](/documentation/swiftui/scene/volumeworldalignment(_:)): Specifies how a volume should be aligned when moved in the world.
- [WorldScalingBehavior](/documentation/swiftui/worldscalingbehavior): Specifies the scaling behavior a window should have within the world.
- [defaultWorldScaling(_:)](/documentation/swiftui/scene/defaultworldscaling(_:)): Specify the world scaling behavior for the window.
- [WorldScalingCompensation](/documentation/swiftui/worldscalingcompensation): Indicates whether returned metrics will take dynamic scaling into account.
- [worldTrackingLimitations](/documentation/swiftui/environmentvalues/worldtrackinglimitations): The current limitations of the device tracking the user’s surroundings.
- [WorldTrackingLimitation](/documentation/swiftui/worldtrackinglimitation): A structure to represent limitations of tracking the user’s surroundings.
- [SurfaceSnappingInfo](/documentation/swiftui/surfacesnappinginfo): A type representing information about the window scenes snap state.
