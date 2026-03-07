# DragDropPreviewsFormation

On macOS, describes the way the dragged previews are visually composed. Both drag sources and drop destination can specify their desired preview formation.

```swift
struct DragDropPreviewsFormation
```

### Type Properties

- [default](/documentation/swiftui/dragdroppreviewsformation/default): System-determined composition.
- [list](/documentation/swiftui/dragdroppreviewsformation/list): Drag images are laid out vertically, non-overlapping, and the left edges are aligned.
- [none](/documentation/swiftui/dragdroppreviewsformation/none): Drag images maintain their set positions relative to each other.
- [pile](/documentation/swiftui/dragdroppreviewsformation/pile): Drag images are placed on top of each other with random rotations.
- [stack](/documentation/swiftui/dragdroppreviewsformation/stack): Drag images are laid out overlapping diagonally.
