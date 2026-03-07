# SidebarRowSize

The standard sizes of sidebar rows.

```swift
enum SidebarRowSize
```

## Overview

On macOS, sidebar rows have three different sizes: small, medium, and large. The size is primarily controlled by the current users’ “Sidebar Icon Size” in Appearance settings, and applies to all applications.

On all other platforms, the only supported sidebar size is `.medium`.

This size can be read or written in the environment using `EnvironmentValues.sidebarRowSize`.

### Getting row sizes

- [SidebarRowSize.small](/documentation/swiftui/sidebarrowsize/small): The standard “small” row size
- [SidebarRowSize.medium](/documentation/swiftui/sidebarrowsize/medium): The standard “medium” row size
- [SidebarRowSize.large](/documentation/swiftui/sidebarrowsize/large): The standard “large” row size

## See Also

### Configuring the sidebar

- [sidebarRowSize](/documentation/swiftui/environmentvalues/sidebarrowsize): The current size of sidebar rows.
