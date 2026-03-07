# ShaderLibrary

A Metal shader library.

```swift
@dynamicMemberLookup struct ShaderLibrary
```

### Getting the default shader library

- [default](/documentation/swiftui/shaderlibrary/default): The default shader library of the main (i.e. app) bundle.
- [bundle(_:)](/documentation/swiftui/shaderlibrary/bundle(_:)): Returns the default shader library of the specified bundle.

### Creating a shader library

- [init(url:)](/documentation/swiftui/shaderlibrary/init(url:)): Creates a new Metal shader library from the contents of `url`, which must be the location  of precompiled Metal library. Functions compiled from the returned library will only be cached as long as the returned library exists.
- [init(data:)](/documentation/swiftui/shaderlibrary/init(data:)): Creates a new Metal shader library from `data`, which must be the contents of precompiled Metal library. Functions compiled from the returned library will only be cached as long as the returned library exists.

### Access shader functions

- [subscript(dynamicMember:)](/documentation/swiftui/shaderlibrary/subscript(dynamicmember:)-swift.type.subscript): Returns a new shader function representing the stitchable MSL function called `name` in the default shader library.

### Subscripts

- [subscript(dynamicMember:)](/documentation/swiftui/shaderlibrary/subscript(dynamicmember:)-swift.subscript): Returns a new shader function representing the stitchable MSL function in the library called `name`.

## See Also

### Accessing Metal shaders

- [colorEffect(_:isEnabled:)](/documentation/swiftui/view/coloreffect(_:isenabled:)): Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.
- [distortionEffect(_:maxSampleOffset:isEnabled:)](/documentation/swiftui/view/distortioneffect(_:maxsampleoffset:isenabled:)): Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [layerEffect(_:maxSampleOffset:isEnabled:)](/documentation/swiftui/view/layereffect(_:maxsampleoffset:isenabled:)): Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.
- [Shader](/documentation/swiftui/shader): A reference to a function in a Metal shader library, along with its bound uniform argument values.
- [ShaderFunction](/documentation/swiftui/shaderfunction): A reference to a function in a Metal shader library.
