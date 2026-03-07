# FindContext

The status of the find navigator for views which support text editing.

```swift
struct FindContext
```

## Overview

Views which support text editing can use this information to implement a a find navigator that is controlled using the modifiers used for controlling the find navigator throughout the rest of SwiftUI.

For example, the following shows a minimal find navigator implementation driven by the find context which falls back to local state if no `isPresented` binding is provided:

```swift
struct FindNavigatorDrivenTextInput: View {
    @State var text: String = ""
    @State var showFindNavigator = false
    @Environment(\.findContext) var findContext
    var body: some View {
        MyTextInputView(text: $text)
            .overlay(alignment: .topTrailing) {
                if let context = findContext &&
                    context.isPresented?.wrappedValue ?? showFindNavigator
                {
                    HStack {
                        FindInputView(text: text)
                        if context.allowedOperations == .findAndReplace {
                            ReplaceInputView(text: $text)
                        }
                        Button("Close") {
                            context.isPresented?.wrappedValue = false
                            showFindNavigator = false
                        }
                    }
                } else {
                    Button("Show Find Navigator") {
                        context.isPresented?.wrappedValue = true
                        showFindNavigator = true
                    }
                }
            }
    }
}
```

### Instance Properties

- [isPresented](/documentation/swiftui/findcontext/ispresented): A binding controlling if the find navigator is presented, or nil if no binding has been provided via the [findNavigator(isPresented:)](/documentation/swiftui/view/findnavigator(ispresented:)) modifier.
- [supportsReplace](/documentation/swiftui/findcontext/supportsreplace): If the find navigators in this context should support replacing.

## See Also

### Searching for text in a view

- [findNavigator(isPresented:)](/documentation/swiftui/view/findnavigator(ispresented:)): Programmatically presents the find and replace interface for text editor views.
- [findDisabled(_:)](/documentation/swiftui/view/finddisabled(_:)): Prevents find and replace operations in a text editor.
- [replaceDisabled(_:)](/documentation/swiftui/view/replacedisabled(_:)): Prevents replace operations in a text editor.
