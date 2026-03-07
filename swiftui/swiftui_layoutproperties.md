# LayoutProperties

Layout-specific properties of a layout container.

```swift
struct LayoutProperties
```

## Overview

This structure contains configuration information that’s applicable to a layout container. For example, the [stackOrientation](/documentation/swiftui/layoutproperties/stackorientation) value indicates the layout’s primary axis, if any.

You can use an instance of this type to characterize a custom layout container, which is a type that conforms to the [Layout](/documentation/swiftui/layout) protocol. Implement the protocol’s [layoutProperties](/documentation/swiftui/layout/layoutproperties) property to return an instance. For example, you can indicate that your layout has a vertical stack orientation:

```swift
extension BasicVStack {
    static var layoutProperties: LayoutProperties {
        var properties = LayoutProperties()
        properties.stackOrientation = .vertical
        return properties
    }
}
```

If you don’t implement the property in your custom layout, the protocol provides a default implementation that returns a `LayoutProperties` instance with default values.

### Creating a layout properties instance

- [init()](/documentation/swiftui/layoutproperties/init()): Creates a default set of properties.

### Getting layout properties

- [stackOrientation](/documentation/swiftui/layoutproperties/stackorientation): The orientation of the containing stack-like container.

## See Also

### Configuring a custom layout

- [ProposedViewSize](/documentation/swiftui/proposedviewsize): A proposal for the size of a view.
- [ViewSpacing](/documentation/swiftui/viewspacing): A collection of the geometric spacing preferences of a view.
