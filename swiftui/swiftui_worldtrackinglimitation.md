# WorldTrackingLimitation

A structure to represent limitations of tracking the user’s surroundings.

```swift
struct WorldTrackingLimitation
```

## Overview

You receive a set of world tracking limitations when you read the [worldTrackingLimitations](/documentation/swiftui/environmentvalues/worldtrackinglimitations) environment value. The value tells you which limitations the device currently is facing. If any of the limitations occur due to changing circumstances, e.g., the lighting, the set is updated accordingly. For example, the following [Text](/documentation/swiftui/text) view automatically updates when the world tracking limitations change:

```swift
@Environment(\.worldTrackingLimitations)
private var worldTrackingLimitations

var body: some View {
    Text("Can track translation?" + worldTrackingLimitations
        .contains(.translation) ? "No" : "Yes")
}
```

### Type Properties

- [orientation](/documentation/swiftui/worldtrackinglimitation/orientation): The device capabilities of tracking orientation changes in all dimensions are currently limited.
- [translation](/documentation/swiftui/worldtrackinglimitation/translation): The device capabilities of tracking translation changes in all dimensions are currently limited.

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
- [WorldScalingCompensation](/documentation/swiftui/worldscalingcompensation): Indicates whether returned metrics will take dynamic scaling into account.
- [worldTrackingLimitations](/documentation/swiftui/environmentvalues/worldtrackinglimitations): The current limitations of the device tracking the user’s surroundings.
- [SurfaceSnappingInfo](/documentation/swiftui/surfacesnappinginfo): A type representing information about the window scenes snap state.
