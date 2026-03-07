# EmptyModifier

An empty, or identity, modifier, used during development to switch modifiers at compile time.

```swift
@frozen struct EmptyModifier
```

## Overview

Use the empty modifier to switch modifiers at compile time during development. In the example below, in a debug build the [Text](/documentation/swiftui/text) view inside `ContentView` has a yellow background and a red border. A non-debug build reflects the default system, or container supplied appearance.

```swift
struct EmphasizedLayout: ViewModifier {
    func body(content: Content) -> some View {
        content
            .background(Color.yellow)
            .border(Color.red)
    }
}

struct ContentView: View {
    var body: some View {
        Text("Hello, World!")
            .modifier(modifier)
    }

    var modifier: some ViewModifier {
        #if DEBUG
            return EmphasizedLayout()
        #else
            return EmptyModifier()
        #endif
    }
}
```

### Creating an empty modifier

- [init()](/documentation/swiftui/emptymodifier/init())

### Getting the identity modifier

- [identity](/documentation/swiftui/emptymodifier/identity)

## See Also

### Modifying a view

- [Configuring views](/documentation/swiftui/configuring-views): Adjust the characteristics of a view by applying view modifiers.
- [Reducing view modifier maintenance](/documentation/swiftui/reducing-view-modifier-maintenance): Bundle view modifiers that you regularly reuse into a custom view modifier.
- [modifier(_:)](/documentation/swiftui/view/modifier(_:)): Applies a modifier to a view and returns a new view.
- [ViewModifier](/documentation/swiftui/viewmodifier): A modifier that you apply to a view or another view modifier, producing a different version of the original value.
- [ModifiedContent](/documentation/swiftui/modifiedcontent): A value with a modifier applied to it.
- [EnvironmentalModifier](/documentation/swiftui/environmentalmodifier): A modifier that must resolve to a concrete modifier in an environment before use.
- [ManipulableModifier](/documentation/swiftui/manipulablemodifier)
- [ManipulableResponderModifier](/documentation/swiftui/manipulablerespondermodifier)
- [ManipulableTransformBindingModifier](/documentation/swiftui/manipulabletransformbindingmodifier)
- [ManipulationGeometryModifier](/documentation/swiftui/manipulationgeometrymodifier)
- [ManipulationGestureModifier](/documentation/swiftui/manipulationgesturemodifier)
- [ManipulationUsingGestureStateModifier](/documentation/swiftui/manipulationusinggesturestatemodifier)
- [Manipulable](/documentation/swiftui/manipulable): A namespace for various manipulable related types.
