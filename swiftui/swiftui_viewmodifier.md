# ViewModifier

A modifier that you apply to a view or another view modifier, producing a different version of the original value.

```swift
@MainActor @preconcurrency protocol ViewModifier
```

## Overview

Adopt the [ViewModifier](/documentation/swiftui/viewmodifier) protocol when you want to create a reusable modifier that you can apply to any view. The example below combines several modifiers to create a new modifier that you can use to create blue caption text surrounded by a rounded rectangle:

```swift
struct BorderedCaption: ViewModifier {
    func body(content: Content) -> some View {
        content
            .font(.caption2)
            .padding(10)
            .overlay(
                RoundedRectangle(cornerRadius: 15)
                    .stroke(lineWidth: 1)
            )
            .foregroundColor(Color.blue)
    }
}
```

You can apply [modifier(_:)](/documentation/swiftui/view/modifier(_:)) directly to a view, but a more common and idiomatic approach uses [modifier(_:)](/documentation/swiftui/view/modifier(_:)) to define an extension to [View](/documentation/swiftui/view) itself that incorporates the view modifier:

```swift
extension View {
    func borderedCaption() -> some View {
        modifier(BorderedCaption())
    }
}
```

You can then apply the bordered caption to any view, similar to this:

```swift
Image(systemName: "bus")
    .resizable()
    .frame(width:50, height:50)
Text("Downtown Bus")
    .borderedCaption()
```

![A screenshot showing the image of a bus with a caption reading]

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

### Creating a view modifier

- [body(content:)](/documentation/swiftui/viewmodifier/body(content:)): Gets the current body of the caller.
- [Body](/documentation/swiftui/viewmodifier/body): The type of view representing the body.
- [ViewModifier.Content](/documentation/swiftui/viewmodifier/content): The content view type passed to `body()`.

### Adding animations to a view

- [animation(_:)](/documentation/swiftui/viewmodifier/animation(_:)): Returns a new version of the modifier that will apply `animation` to all animatable values within the modifier.
- [concat(_:)](/documentation/swiftui/viewmodifier/concat(_:)): Returns a new modifier that is the result of concatenating `self` with `modifier`.

### Handling view taps and gestures

- [transaction(_:)](/documentation/swiftui/viewmodifier/transaction(_:)): Returns a new version of the modifier that will apply the transaction mutation function `transform` to all transactions within the modifier.

## See Also

### Modifying a view

- [Configuring views](/documentation/swiftui/configuring-views): Adjust the characteristics of a view by applying view modifiers.
- [Reducing view modifier maintenance](/documentation/swiftui/reducing-view-modifier-maintenance): Bundle view modifiers that you regularly reuse into a custom view modifier.
- [modifier(_:)](/documentation/swiftui/view/modifier(_:)): Applies a modifier to a view and returns a new view.
- [EmptyModifier](/documentation/swiftui/emptymodifier): An empty, or identity, modifier, used during development to switch modifiers at compile time.
- [ModifiedContent](/documentation/swiftui/modifiedcontent): A value with a modifier applied to it.
- [EnvironmentalModifier](/documentation/swiftui/environmentalmodifier): A modifier that must resolve to a concrete modifier in an environment before use.
- [ManipulableModifier](/documentation/swiftui/manipulablemodifier)
- [ManipulableResponderModifier](/documentation/swiftui/manipulablerespondermodifier)
- [ManipulableTransformBindingModifier](/documentation/swiftui/manipulabletransformbindingmodifier)
- [ManipulationGeometryModifier](/documentation/swiftui/manipulationgeometrymodifier)
- [ManipulationGestureModifier](/documentation/swiftui/manipulationgesturemodifier)
- [ManipulationUsingGestureStateModifier](/documentation/swiftui/manipulationusinggesturestatemodifier)
- [Manipulable](/documentation/swiftui/manipulable): A namespace for various manipulable related types.
