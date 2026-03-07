# DisclosureGroupStyle

A type that specifies the appearance and interaction of disclosure groups within a view hierarchy.

```swift
@MainActor @preconcurrency protocol DisclosureGroupStyle
```

## Overview

To configure the disclosure group style for a view hierarchy, use the [disclosureGroupStyle(_:)](/documentation/swiftui/view/disclosuregroupstyle(_:)) modifier.

To create a custom disclosure group style, declare a type that conforms to `DisclosureGroupStyle`. Implement the [makeBody(configuration:)](/documentation/swiftui/disclosuregroupstyle/makebody(configuration:)) method to return a view that composes the elements of the `configuration` that SwiftUI provides to your method.

```swift
struct MyDisclosureStyle: DisclosureGroupStyle {
    func makeBody(configuration: Configuration) -> some View {
        VStack {
            Button {
                withAnimation {
                    configuration.isExpanded.toggle()
                }
            } label: {
                HStack(alignment: .firstTextBaseline) {
                    configuration.label
                    Spacer()
                    Text(configuration.isExpanded ? "hide" : "show")
                        .foregroundColor(.accentColor)
                        .font(.caption.lowercaseSmallCaps())
                        .animation(nil, value: configuration.isExpanded)
                }
                .contentShape(Rectangle())
            }
            .buttonStyle(.plain)
            if configuration.isExpanded {
                configuration.content
            }
        }
    }
}
```

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

### Getting the styles

- [automatic](/documentation/swiftui/disclosuregroupstyle/automatic): A disclosure group style that resolves its appearance automatically based on the current context.

### Creating custom disclosure group styles

- [makeBody(configuration:)](/documentation/swiftui/disclosuregroupstyle/makebody(configuration:)): Creates a view that represents the body of a disclosure group.
- [DisclosureGroupStyleConfiguration](/documentation/swiftui/disclosuregroupstyleconfiguration): The properties of a disclosure group instance.
- [DisclosureGroupStyle.Configuration](/documentation/swiftui/disclosuregroupstyle/configuration): The properties of a disclosure group instance.
- [Body](/documentation/swiftui/disclosuregroupstyle/body): A view that represents the body of a disclosure group.

### Supporting types

- [AutomaticDisclosureGroupStyle](/documentation/swiftui/automaticdisclosuregroupstyle): A disclosure group style that resolves its appearance automatically based on the current context.

## See Also

### Styling collection views

- [listStyle(_:)](/documentation/swiftui/view/liststyle(_:)): Sets the style for lists within this view.
- [ListStyle](/documentation/swiftui/liststyle): A protocol that describes the behavior and appearance of a list.
- [tableStyle(_:)](/documentation/swiftui/view/tablestyle(_:)): Sets the style for tables within this view.
- [TableStyle](/documentation/swiftui/tablestyle): A type that applies a custom appearance to all tables within a view.
- [TableStyleConfiguration](/documentation/swiftui/tablestyleconfiguration): The properties of a table.
- [disclosureGroupStyle(_:)](/documentation/swiftui/view/disclosuregroupstyle(_:)): Sets the style for disclosure groups within this view.
