# SurfaceSnappingInfo

A type representing information about the window scenes snap state.

```swift
struct SurfaceSnappingInfo
```

## Overview

Use the provided [SurfaceSnappingInfo](/documentation/swiftui/surfacesnappinginfo) to modify the contents of your view.

```swift
struct LightFixtureView: View {
    @Environment(\.surfaceSnappingInfo)
    var snappingInfo: SurfaceSnappingInfo

    var body: some View {
        if snappingInfo.isSnapped {
            switch SurfaceSnappingInfo.authorizationStatus {
                case .authorized:
                    switch snappingInfo.classification {
                        case .table:
                            LampView()
                        case .floor:
                            FloorLampView()
                        default:
                            DefaultLampView()
                    }
                default:
                    DefaultLampView()
            }
        } else {
            FloatingOrbLampView()
        }
    }
}
```

The bottom of volumes may snap to horizontal surfaces and the back of windows may snap to vertical surfaces.

### Instance Properties

- [classification](/documentation/swiftui/surfacesnappinginfo/classification): A type that provides information about the surface classification the scene is snapped to. This property only has a value if the scene is snapped and `authorizationStatus` is `.authorized`.
- [isSnapped](/documentation/swiftui/surfacesnappinginfo/issnapped): A value that represents whether the scene is currently snapped to a physical surface or not.

### Type Properties

- [authorizationStatus](/documentation/swiftui/surfacesnappinginfo/authorizationstatus-swift.type.property): A value that represents whether the user has authorized providing more detailed information about the surface scenes are snapped to. To request this detailed surface information, in your `Info.plist` file, set `UIWantsDetailedSurfaceInfo` to `YES` and set `NSWorldSensingUsageDescription` to provide a description of why your app is requesting this information.

### Enumerations

- [SurfaceSnappingInfo.AuthorizationStatus](/documentation/swiftui/surfacesnappinginfo/authorizationstatus-swift.enum): A type representing whether the user has granted permissions to provide more detailed information about the surface a scene is snapped to.

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
- [WorldTrackingLimitation](/documentation/swiftui/worldtrackinglimitation): A structure to represent limitations of tracking the user’s surroundings.
