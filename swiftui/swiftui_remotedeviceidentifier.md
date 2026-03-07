# RemoteDeviceIdentifier

An opaque type that identifies a remote device displaying scene content in a [RemoteImmersiveSpace](/documentation/swiftui/remoteimmersivespace).

```swift
struct RemoteDeviceIdentifier
```

## Overview

Access this from the [remoteDeviceIdentifier](/documentation/swiftui/environmentvalues/remotedeviceidentifier) environment property in a remote scene to get the identifier for that scene’s device.

When accessed in a context that is being presented on the local device, this value will be `nil`.

This identifier can also be used to initialize an `ARKitSession` associated with the remote device.

```swift
struct SolarSystem: CompositorContent {
    @Environment(\.remoteDeviceIdentifier) private var deviceID

    var body: some CompositorContent {
        RemoteImmersiveSpace {
            CompositorLayer { layerRenderer in
                // Create an ARSession for the device
                let arSession = ARKitSession(deviceID)

                // Set up and run the Metal render loop.
                let renderThread = Thread {
                    let engine = solar_engine_create(
                        layerRenderer, arSession)
                    solar_engine_render_loop(engine)
                }
                renderThread.name = "Render Thread"
                renderThread.start()
            }
        }
    }
}
```

> **Note:**
> This identifier is not stable across app launches.
>

### Instance Properties

- [cDevice](/documentation/swiftui/remotedeviceidentifier/cdevice): Returns the `ar_device` associated with this device.

## See Also

### Handling remote immersive spaces

- [RemoteImmersiveSpace](/documentation/swiftui/remoteimmersivespace): A scene that presents its content in an unbounded space on a remote device.
