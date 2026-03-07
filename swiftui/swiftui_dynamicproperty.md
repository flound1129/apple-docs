# DynamicProperty

An interface for a stored variable that updates an external property of a view.

```swift
protocol DynamicProperty
```

## Overview

The view gives values to these properties prior to recomputing the view’s [body](/documentation/swiftui/view/body-8kl5o).

### Updating the value

- [update()](/documentation/swiftui/dynamicproperty/update()): Updates the underlying value of the stored value.
