# ImmersiveSpace

A scene that presents its content in an unbounded space.

```swift
struct ImmersiveSpace<Content, Data> where Content : ImmersiveSpaceContent, Data : Decodable, Data : Encodable, Data : Hashable
```

## Overview

Use an immersive space as a container for a view hierarchy that your app presents. The hierarchy that you declare as the immersive space’s content serves as a template for it:

```swift
@main
struct SolarSystemApp: App {
    var body: some Scene {
        ImmersiveSpace {
            SolarSystem()
        }
    }
}
```

If you want to create a bounded scene instead, use one of the types that creates a window or a volume, like [WindowGroup](/documentation/swiftui/windowgroup) or [DocumentGroup](/documentation/swiftui/documentgroup).

### Style the immersive space

By default, immersive spaces use the [mixed](/documentation/swiftui/immersionstyle/mixed) style which places virtual content in a person’s surroundings. You can select a different style for the immersive space by adding the [immersionStyle(selection:in:)](/documentation/swiftui/scene/immersionstyle(selection:in:)) scene modifier to the scene. For example, you can completely control the visual experience using the [full](/documentation/swiftui/immersionstyle/full) immersion style:

```swift
@main
struct SolarSystemApp: App {
    @State private var style: ImmersionStyle = .full

    var body: some Scene {
        ImmersiveSpace {
            SolarSystem()
        }
        .immersionStyle(selection: $style, in: .full)
    }
}
```

You can change the immersion style after presenting the immersive space by changing the modifier’s `selection` input, although you can only use one of the values that you specify in the modifier’s second parameter. For any style of immersion, the other parts of your app’s interface — namely its windows — remain visible. However, the immersion style affects how windows interact with virtual objects in the environment:

- For the [mixed](/documentation/swiftui/immersionstyle/mixed) style, a virtual object obscures part or all of a window that’s behind the object. Similarly, a window obscures a virtual object that’s behind the window.
- For other styles, windows always render in front of virtual content, no matter how someone positions the window or the content. This helps people to avoid losing track of windows behind virtual content when passthrough is partially or completely off.

### Open an immersive space

You can programmatically open an immersive space by giving it an identifier. For example, you can label the solar system view from the previous example:

```swift
ImmersiveSpace(id: "solarSystem") {
    SolarSystem()
}
```

Elsewhere in your code, you use the [openImmersiveSpace](/documentation/swiftui/environmentvalues/openimmersivespace) environment value to get the instance of the [OpenImmersiveSpaceAction](/documentation/swiftui/openimmersivespaceaction) structure for a given [Environment](/documentation/swiftui/environment). You call the instance directly — for example, from a button’s closure, like in the following code — using the identifier:

```swift
struct NewSolarSystemImmersiveSpace: View {
    var solarSystem: SolarSystem
    @Environment(\.openImmersiveSpace) private var openImmersiveSpace

    var body: some View {
        Button("Present Solar System") {
            Task {
                await openImmersiveSpace(id: "solarSystem")
            }
        }
    }
}
```

Mark the call to the action with `await` because it executes asynchronously. When your app opens an immersive space, the system hides all other visible apps. The system allows only one immersive space to be open at a time. Be sure to close the open immersive space before opening another one.

### Dismiss an immersive space

You can dismiss an immersive space by calling the [dismissImmersiveSpace](/documentation/swiftui/environmentvalues/dismissimmersivespace) action from the environment. For example, you can define a button that dismisses an immersive space:

```swift
struct DismissImmersiveSpaceButton: View {
    @Environment(\.dismissImmersiveSpace)
    private var dismissImmersiveSpace

    var body: some View {
        Button("Close Solar System") {
            Task {
                await dismissImmersiveSpace()
            }
        }
    }
}
```

The dismiss action runs asynchronously, like the open action. You don’t need to specify an identifier when dismissing an immersive space because there can only be one immersive space open at a time.

### Present an immersive space at launch

When an app launches, it opens an instance of the first scene that’s listed in the app’s body. However, to open an immersive space at launch, you need to provide additional configuration information in your app’s `Info.plist` file. In particular, set the [UIApplicationPreferredDefaultSceneSessionRole](/documentation/BundleResources/Information-Property-List/UIApplicationPreferredDefaultSceneSessionRole) key in the scene manifest to the value [UISceneSessionRoleImmersiveSpaceApplication](/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UISceneConfigurations/UISceneSessionRoleImmersiveSpaceApplication).

To configure the style of the immersive space that opens at launch, add a scene configuration to the scene session role. Use the [UISceneInitialImmersionStyle](/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UISceneConfigurations/UISceneSessionRoleImmersiveSpaceApplication/UISceneInitialImmersionStyle) key together with a value that indicates one of the mixed, full, or progressive styles. See the initial immersion style key for more information.

### Creating an immersive space

- [init(content:)](/documentation/swiftui/immersivespace/init(content:)): Creates an immersive space.

### Identifying an immersive space

- [init(id:content:)](/documentation/swiftui/immersivespace/init(id:content:)): Creates the immersive space associated with the specified identifier.

### Creating a data-driven immersive space

- [init(for:content:)](/documentation/swiftui/immersivespace/init(for:content:)): Creates the immersive space for a specified type of presented data.
- [init(id:for:content:)](/documentation/swiftui/immersivespace/init(id:for:content:)): Creates the immersive space associated with an identifier for a specified type of presented data.

### Providing default data to an immersive space

- [init(for:content:defaultValue:)](/documentation/swiftui/immersivespace/init(for:content:defaultvalue:)): Creates an immersive space.
- [init(id:for:content:defaultValue:)](/documentation/swiftui/immersivespace/init(id:for:content:defaultvalue:)): Creates the immersive space associated with an identifier for a specified type of presented data, and a default value, if the data is not set.

### Supporting types

- [ImmersiveSpaceViewContent](/documentation/swiftui/immersivespaceviewcontent): Immersive space content that uses a SwiftUI view hierarchy as the content.
- [ImmersiveSpaceContent](/documentation/swiftui/immersivespacecontent): A type that you can use as the content of an immersive space.

### Initializers

- [init(for:makeContent:)](/documentation/swiftui/immersivespace/init(for:makecontent:))
- [init(for:makeContent:defaultValue:)](/documentation/swiftui/immersivespace/init(for:makecontent:defaultvalue:))
- [init(foveatedStreaming:)](/documentation/swiftui/immersivespace/init(foveatedstreaming:)): Creates an immersive space to display foveated streaming content.
- [init(foveatedStreaming:content:)](/documentation/swiftui/immersivespace/init(foveatedstreaming:content:)): Creates an immersive space to display foveated streaming content alongside `RealityKit` content.
- [init(id:for:makeContent:)](/documentation/swiftui/immersivespace/init(id:for:makecontent:))
- [init(id:for:makeContent:defaultValue:)](/documentation/swiftui/immersivespace/init(id:for:makecontent:defaultvalue:))
- [init(id:makeContent:)](/documentation/swiftui/immersivespace/init(id:makecontent:)): Creates the immersive space associated with the specified identifier.
- [init(makeContent:)](/documentation/swiftui/immersivespace/init(makecontent:))

## See Also

### Creating an immersive space

- [ImmersiveSpaceContentBuilder](/documentation/swiftui/immersivespacecontentbuilder): A result builder for composing a collection of immersive space elements.
- [immersionStyle(selection:in:)](/documentation/swiftui/scene/immersionstyle(selection:in:)): Sets the style for an immersive space.
- [ImmersionStyle](/documentation/swiftui/immersionstyle): The styles that an immersive space can have.
- [immersiveSpaceDisplacement](/documentation/swiftui/environmentvalues/immersivespacedisplacement): The displacement that the system applies to the immersive space when moving the space away from its default position, in meters.
- [ImmersiveEnvironmentBehavior](/documentation/swiftui/immersiveenvironmentbehavior): The behavior of the system-provided immersive environments when a scene is opened by your app.
- [ProgressiveImmersionAspectRatio](/documentation/swiftui/progressiveimmersionaspectratio)
