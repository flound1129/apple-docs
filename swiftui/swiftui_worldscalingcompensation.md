# WorldScalingCompensation

Indicates whether returned metrics will take dynamic scaling into account.

```swift
struct WorldScalingCompensation
```

## Overview

On visionOS, a window scene or a volume scene with the [defaultWorldScaling(_:)](/documentation/swiftui/scene/defaultworldscaling(_:)) modifier may scale dynamically when the user repositions it. In those cases, the metrics returned by a [PhysicalMetric](/documentation/swiftui/physicalmetric) or [PhysicalMetricsConverter](/documentation/swiftui/physicalmetricsconverter) value may or may not correspond to the units of a `RealityView`.

World scale compensation lets you specify if this scaling is taken into account. If the values are [unscaled](/documentation/swiftui/worldscalingcompensation/unscaled), they will correspond to the physical metrics of the user’s surroundings, regardless of dynamic scale. If [scaled](/documentation/swiftui/worldscalingcompensation/scaled), they will be scaled appropriately for the scene, which means they will match the default coordinate system of a `RealityView` in that scene.

### Type Properties

- [scaled](/documentation/swiftui/worldscalingcompensation/scaled): Returns metrics that are scaled appropriately to match the coordinate system of their scene, including any world scaling behavior.
- [unscaled](/documentation/swiftui/worldscalingcompensation/unscaled): Returns metrics that match the scale of the user’s surroundings, regardless of the world scaling behavior of their scene.

## See Also

### Interacting with volumes

- [onVolumeViewpointChange(updateStrategy:initial:_:)](/documentation/swiftui/view/onvolumeviewpointchange(updatestrategy:initial:_:)): Adds an action to perform when the viewpoint of the volume changes.
- [supportedVolumeViewpoints(_:)](/documentation/swiftui/view/supportedvolumeviewpoints(_:)): Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [VolumeViewpointUpdateStrategy](/documentation/swiftui/volumeviewpointupdatestrategy): A type describing when the action provided to [onVolumeViewpointChange(updateStrategy:initial:_:)](/documentation/swiftui/view/onvolumeviewpointchange(updatestrategy:initial:_:)) should be called.
- [Viewpoint3D](/documentation/swiftui/viewpoint3d): A type describing what direction something is being viewed from.
- [SquareAzimuth](/documentation/swiftui/squareazimuth): A type describing what direction something is being viewed from along the horizontal plane and snapped to 4 directions.
- [WorldAlignmentBehavior](/documentation/swiftui/worldalignmentbehavior): A type representing the world alignment behavior for a scene.
- [volumeWorldAlignment(_:)](/documentation/swiftui/scene/volumeworldalignment(_:)): Specifies how a volume should be aligned when moved in the world.
- [WorldScalingBehavior](/documentation/swiftui/worldscalingbehavior): Specifies the scaling behavior a window should have within the world.
- [defaultWorldScaling(_:)](/documentation/swiftui/scene/defaultworldscaling(_:)): Specify the world scaling behavior for the window.
- [worldTrackingLimitations](/documentation/swiftui/environmentvalues/worldtrackinglimitations): The current limitations of the device tracking the user’s surroundings.
- [WorldTrackingLimitation](/documentation/swiftui/worldtrackinglimitation): A structure to represent limitations of tracking the user’s surroundings.
- [SurfaceSnappingInfo](/documentation/swiftui/surfacesnappinginfo): A type representing information about the window scenes snap state.
