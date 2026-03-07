# UIHostingConfiguration

A content configuration suitable for hosting a hierarchy of SwiftUI views.

```swift
struct UIHostingConfiguration<Content, Background> where Content : View, Background : View
```

## Overview

Use a value of this type, which conforms to the [UIContentConfiguration](/documentation/UIKit/UIContentConfiguration-9eib5) protocol, with a [UICollectionViewCell](/documentation/UIKit/UICollectionViewCell) or [UITableViewCell](/documentation/UIKit/UITableViewCell) to host a hierarchy of SwiftUI views in a collection or table view, respectively. For example, the following shows a stack with an image and text inside the cell:

```swift
myCell.contentConfiguration = UIHostingConfiguration {
    HStack {
        Image(systemName: "star").foregroundStyle(.purple)
        Text("Favorites")
        Spacer()
    }
}
```

You can also customize the background of the containing cell. The following example draws a blue background:

```swift
myCell.contentConfiguration = UIHostingConfiguration {
    HStack {
        Image(systemName: "star").foregroundStyle(.purple)
        Text("Favorites")
        Spacer()
    }
}
.background {
    Color.blue
}
```

When used in a list layout, certain APIs are bridged automatically, like swipe actions and separator alignment. The following example shows a trailing yellow star swipe action:

```swift
cell.contentConfiguration = UIHostingConfiguration {
    HStack {
        Image(systemName: "airplane")
        Text("Flight 123")
        Spacer()
    }
    .swipeActions {
        Button { ... } label: {
            Label("Favorite", systemImage: "star")
        }
        .tint(.yellow)
    }
}
```

### Creating and updating a configuration

- [init(content:)](/documentation/swiftui/uihostingconfiguration/init(content:)): Creates a hosting configuration with the given contents.

### Setting the background

- [background(_:)](/documentation/swiftui/uihostingconfiguration/background(_:)): Sets the background contents for the hosting configuration’s enclosing cell.
- [background(content:)](/documentation/swiftui/uihostingconfiguration/background(content:)): Sets the background contents for the hosting configuration’s enclosing cell.

### Setting margins

- [margins(_:_:)](/documentation/swiftui/uihostingconfiguration/margins(_:_:)): Sets the margins around the content of the configuration.

### Setting a size

- [minSize(width:height:)](/documentation/swiftui/uihostingconfiguration/minsize(width:height:)): Sets the minimum size for the configuration.
- [minSize()](/documentation/swiftui/uihostingconfiguration/minsize()): Sets the minimum size for the configuration.

## See Also

### Displaying SwiftUI views in UIKit

- [Using SwiftUI with UIKit](/documentation/UIKit/using-swiftui-with-uikit): Learn how to incorporate SwiftUI views into a UIKit app.
- [Unifying your app’s animations](/documentation/swiftui/unifying-your-app-s-animations): Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [UIHostingController](/documentation/swiftui/uihostingcontroller): A UIKit view controller that manages a SwiftUI view hierarchy.
- [UIHostingControllerSizingOptions](/documentation/swiftui/uihostingcontrollersizingoptions): Options for how a hosting controller tracks its content’s size.
- [UIHostingSceneDelegate](/documentation/swiftui/uihostingscenedelegate): Extends `UIKit/UISceneDelegate` to bridge SwiftUI scenes.
