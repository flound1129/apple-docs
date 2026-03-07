# Shader

A reference to a function in a Metal shader library, along with its bound uniform argument values.

```swift
struct Shader
```

## Overview

Shader values can be used as filter effects on views, see the [colorEffect(_:isEnabled:)](/documentation/swiftui/view/coloreffect(_:isenabled:)), [distortionEffect(_:maxSampleOffset:isEnabled:)](/documentation/swiftui/view/distortioneffect(_:maxsampleoffset:isenabled:)), and [layerEffect(_:maxSampleOffset:isEnabled:)](/documentation/swiftui/view/layereffect(_:maxsampleoffset:isenabled:)) functions.

Shaders also conform to the [ShapeStyle](/documentation/swiftui/shapestyle) protocol, letting their MSL shader function provide per-pixel color to fill any shape or text view. For a shader function to act as a fill pattern it must have a function signature matching:

```swift
[[ stitchable ]] half4 name(float2 position, args...)
```

where `position` is the user-space coordinates of the pixel applied to the shader, and `args...` should be compatible with the uniform arguments bound to `shader`. The function should return the premultiplied color value in the color space of the destination (typically extended sRGB).

### Creating a shader

- [init(function:arguments:)](/documentation/swiftui/shader/init(function:arguments:)): Creates a new shader from a function and the uniform argument values to bind to the function.
- [Shader.Argument](/documentation/swiftui/shader/argument): A single uniform argument value to a shader function.

### Getting the shader function

- [function](/documentation/swiftui/shader/function): The shader function called by the shader.
- [arguments](/documentation/swiftui/shader/arguments): The uniform argument values passed to the shader function.

### Configuring the shader

- [dithersColor](/documentation/swiftui/shader/ditherscolor): For shader functions that return color values, whether the returned color has dither noise added to it, or is simply rounded to the output bit-depth. For shaders generating smooth gradients, dithering is usually necessary to prevent visible banding in the result.

### Structures

- [Shader.UsageType](/documentation/swiftui/shader/usagetype): The different ways in which a `Shader` may be used to render.

### Instance Methods

- [compile(as:)](/documentation/swiftui/shader/compile(as:)): Attempts to asynchronously compile a shader function, to minimize the chance of stalling when it is first used for rendering.

## See Also

### Accessing Metal shaders

- [colorEffect(_:isEnabled:)](/documentation/swiftui/view/coloreffect(_:isenabled:)): Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.
- [distortionEffect(_:maxSampleOffset:isEnabled:)](/documentation/swiftui/view/distortioneffect(_:maxsampleoffset:isenabled:)): Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [layerEffect(_:maxSampleOffset:isEnabled:)](/documentation/swiftui/view/layereffect(_:maxsampleoffset:isenabled:)): Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.
- [ShaderFunction](/documentation/swiftui/shaderfunction): A reference to a function in a Metal shader library.
- [ShaderLibrary](/documentation/swiftui/shaderlibrary): A Metal shader library.
