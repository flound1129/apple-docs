# SymbolRenderingMode

A symbol rendering mode.

```swift
struct SymbolRenderingMode
```

### Getting symbol rendering modes

- [hierarchical](/documentation/swiftui/symbolrenderingmode/hierarchical): A mode that renders symbols as multiple layers, with different opacities applied to the foreground style.
- [monochrome](/documentation/swiftui/symbolrenderingmode/monochrome): A mode that renders symbols as a single layer filled with the foreground style.
- [multicolor](/documentation/swiftui/symbolrenderingmode/multicolor): A mode that renders symbols as multiple layers with their inherit styles.
- [palette](/documentation/swiftui/symbolrenderingmode/palette): A mode that renders symbols as multiple layers, with different styles applied to the layers.

## See Also

### Setting symbol rendering modes

- [symbolRenderingMode(_:)](/documentation/swiftui/view/symbolrenderingmode(_:)): Sets the rendering mode for symbol images within this view.
- [symbolRenderingMode](/documentation/swiftui/environmentvalues/symbolrenderingmode): The current symbol rendering mode, or `nil` denoting that the mode is picked automatically using the current image and foreground style as parameters.
- [SymbolColorRenderingMode](/documentation/swiftui/symbolcolorrenderingmode): A method of filling a layer in a symbol image.
- [SymbolVariableValueMode](/documentation/swiftui/symbolvariablevaluemode): A method of rendering the variable value of a symbol image.
