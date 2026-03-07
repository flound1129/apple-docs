# SymbolVariableValueMode

A method of rendering the variable value of a symbol image.

```swift
struct SymbolVariableValueMode
```

### Type Properties

- [color](/documentation/swiftui/symbolvariablevaluemode/color): The “color” variable value mode. Sets the opacity of each variable layer to either on or off depending on how its threshold compared to the current value.
- [draw](/documentation/swiftui/symbolvariablevaluemode/draw): The “draw” variable value mode. Changes the drawn length of each variable layer to either based on how its range relates to the current value.

## See Also

### Setting symbol rendering modes

- [symbolRenderingMode(_:)](/documentation/swiftui/view/symbolrenderingmode(_:)): Sets the rendering mode for symbol images within this view.
- [symbolRenderingMode](/documentation/swiftui/environmentvalues/symbolrenderingmode): The current symbol rendering mode, or `nil` denoting that the mode is picked automatically using the current image and foreground style as parameters.
- [SymbolRenderingMode](/documentation/swiftui/symbolrenderingmode): A symbol rendering mode.
- [SymbolColorRenderingMode](/documentation/swiftui/symbolcolorrenderingmode): A method of filling a layer in a symbol image.
