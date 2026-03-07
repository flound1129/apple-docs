# SymbolVariants

A variant of a symbol.

```swift
struct SymbolVariants
```

## Overview

Many of the [SF Symbols](/design/Human-Interface-Guidelines/sf-symbols) that you can add to your app using an [Image](/documentation/swiftui/image) or a [Label](/documentation/swiftui/label) instance have common variants, like a filled version or a version that’s contained within a circle. The symbol’s name indicates the variant:

```swift
VStack(alignment: .leading) {
    Label("Default", systemImage: "heart")
    Label("Fill", systemImage: "heart.fill")
    Label("Circle", systemImage: "heart.circle")
    Label("Circle Fill", systemImage: "heart.circle.fill")
}
```

![A screenshot showing an outlined heart, a filled heart, a heart in]

You can configure a part of your view hierarchy to use a particular variant for all symbols in that view and its child views using `SymbolVariants`. Add the [symbolVariant(_:)](/documentation/swiftui/view/symbolvariant(_:)) modifier to a view to set a variant for that view’s environment. For example, you can use the modifier to create the same set of labels as in the example above, using only the base name of the symbol in the label declarations:

```swift
VStack(alignment: .leading) {
    Label("Default", systemImage: "heart")
    Label("Fill", systemImage: "heart")
        .symbolVariant(.fill)
    Label("Circle", systemImage: "heart")
        .symbolVariant(.circle)
    Label("Circle Fill", systemImage: "heart")
        .symbolVariant(.circle.fill)
}
```

Alternatively, you can set the variant in the environment directly by passing the [symbolVariants](/documentation/swiftui/environmentvalues/symbolvariants) environment value to the [environment(_:_:)](/documentation/swiftui/view/environment(_:_:)) modifier:

```swift
Label("Fill", systemImage: "heart")
    .environment(\.symbolVariants, .fill)
```

SwiftUI sets a variant for you in some environments. For example, SwiftUI automatically applies the [fill](/documentation/swiftui/symbolvariants/fill-swift.type.property) symbol variant for items that appear in the `content` closure of the [swipeActions(edge:allowsFullSwipe:content:)](/documentation/swiftui/view/swipeactions(edge:allowsfullswipe:content:)) method, or as the tab bar items of a [TabView](/documentation/swiftui/tabview).

### Getting symbol variants

- [none](/documentation/swiftui/symbolvariants/none): No variant for a symbol.
- [circle](/documentation/swiftui/symbolvariants/circle-swift.type.property): A variant that encapsulates the symbol in a circle.
- [square](/documentation/swiftui/symbolvariants/square-swift.type.property): A variant that encapsulates the symbol in a square.
- [rectangle](/documentation/swiftui/symbolvariants/rectangle-swift.type.property): A variant that encapsulates the symbol in a rectangle.
- [fill](/documentation/swiftui/symbolvariants/fill-swift.type.property): A variant that fills the symbol.
- [slash](/documentation/swiftui/symbolvariants/slash-swift.type.property): A variant that draws a slash through the symbol.

### Modifying a variant

- [circle](/documentation/swiftui/symbolvariants/circle-swift.property): A version of the variant that’s encapsulated in a circle.
- [square](/documentation/swiftui/symbolvariants/square-swift.property): A version of the variant that’s encapsulated in a square.
- [rectangle](/documentation/swiftui/symbolvariants/rectangle-swift.property): A version of the variant that’s encapsulated in a rectangle.
- [fill](/documentation/swiftui/symbolvariants/fill-swift.property): A filled version of the variant.
- [slash](/documentation/swiftui/symbolvariants/slash-swift.property): A slashed version of the variant.

### Comparing variants

- [contains(_:)](/documentation/swiftui/symbolvariants/contains(_:)): Returns a Boolean value that indicates whether the current variant contains the specified variant.

## See Also

### Setting a symbol variant

- [symbolVariant(_:)](/documentation/swiftui/view/symbolvariant(_:)): Makes symbols within the view show a particular variant.
- [symbolVariants](/documentation/swiftui/environmentvalues/symbolvariants): The symbol variant to use in this environment.
