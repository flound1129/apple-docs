# TextRenderer

A value that can replace the default text view rendering behavior.

```swift
protocol TextRenderer : Animatable
```

### Instance Properties

- [displayPadding](/documentation/swiftui/textrenderer/displaypadding): Returns the size of the extra padding added to any drawing layer used to rasterize the text. For example when drawing the text with a shadow this may be used to extend the drawing bounds to avoid clipping the shadow.

### Instance Methods

- [draw(layout:in:)](/documentation/swiftui/textrenderer/draw(layout:in:)): Draws `layout` into `ctx`.
- [sizeThatFits(proposal:text:)](/documentation/swiftui/textrenderer/sizethatfits(proposal:text:)): Returns the size of the text in `proposal`. The provided `text` proxy value may be used to query the sizing behavior of the underlying text layout.

## See Also

### Rendering text

- [Creating visual effects with SwiftUI](/documentation/swiftui/creating-visual-effects-with-swiftui): Add scroll effects, rich color treatments, custom transitions, and advanced effects using shaders and a text renderer.
- [TextAttribute](/documentation/swiftui/textattribute): A value that you can attach to text views and that text renderers can query.
- [textRenderer(_:)](/documentation/swiftui/view/textrenderer(_:)): Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [TextProxy](/documentation/swiftui/textproxy): A proxy for a text view that custom text renderers use.
