# PreferenceKey

A named value produced by a view.

```swift
protocol PreferenceKey
```

## Overview

A view with multiple children automatically combines its values for a given preference into a single value visible to its ancestors.

### Getting the default value

- [defaultValue](/documentation/swiftui/preferencekey/defaultvalue): The default value of the preference.
- [Value](/documentation/swiftui/preferencekey/value): The type of value produced by this preference.

### Combining preferences

- [reduce(value:nextValue:)](/documentation/swiftui/preferencekey/reduce(value:nextvalue:)): Combines a sequence of values by modifying the previously-accumulated value with the result of a closure that provides the next value.
