# ShaderFunction

A reference to a function in a Metal shader library.

```swift
@dynamicCallable struct ShaderFunction
```

### Creating a shader function

- [init(library:name:)](/documentation/swiftui/shaderfunction/init(library:name:)): Creates a new function reference from the provided shader library and function name string.

### Configuring a function

- [library](/documentation/swiftui/shaderfunction/library): The shader library storing the function.
- [name](/documentation/swiftui/shaderfunction/name): The name of the shader function in the library.
- [dynamicallyCall(withArguments:)](/documentation/swiftui/shaderfunction/dynamicallycall(witharguments:)): Returns a new shader by applying the provided argument values to the referenced function.

## See Also

### Accessing Metal shaders

- [colorEffect(_:isEnabled:)](/documentation/swiftui/view/coloreffect(_:isenabled:)): Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.
- [distortionEffect(_:maxSampleOffset:isEnabled:)](/documentation/swiftui/view/distortioneffect(_:maxsampleoffset:isenabled:)): Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [layerEffect(_:maxSampleOffset:isEnabled:)](/documentation/swiftui/view/layereffect(_:maxsampleoffset:isenabled:)): Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.
- [Shader](/documentation/swiftui/shader): A reference to a function in a Metal shader library, along with its bound uniform argument values.
- [ShaderLibrary](/documentation/swiftui/shaderlibrary): A Metal shader library.
