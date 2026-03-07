# AccessibilityTraits

A set of accessibility traits that describe how an element behaves.

```swift
struct AccessibilityTraits
```

### Getting traits

- [allowsDirectInteraction](/documentation/swiftui/accessibilitytraits/allowsdirectinteraction): The accessibility element allows direct touch interaction for VoiceOver users.
- [causesPageTurn](/documentation/swiftui/accessibilitytraits/causespageturn): The accessibility element causes an automatic page turn when VoiceOver finishes reading the text within it.
- [isButton](/documentation/swiftui/accessibilitytraits/isbutton): The accessibility element is a button.
- [isHeader](/documentation/swiftui/accessibilitytraits/isheader): The accessibility element is a header that divides content into sections, like the title of a navigation bar.
- [isImage](/documentation/swiftui/accessibilitytraits/isimage): The accessibility element is an image.
- [isKeyboardKey](/documentation/swiftui/accessibilitytraits/iskeyboardkey): The accessibility element behaves as a keyboard key.
- [isLink](/documentation/swiftui/accessibilitytraits/islink): The accessibility element is a link.
- [isModal](/documentation/swiftui/accessibilitytraits/ismodal): The accessibility element is modal.
- [isSearchField](/documentation/swiftui/accessibilitytraits/issearchfield): The accessibility element is a search field.
- [isSelected](/documentation/swiftui/accessibilitytraits/isselected): The accessibility element is currently selected.
- [isStaticText](/documentation/swiftui/accessibilitytraits/isstatictext): The accessibility element is a static text that cannot be modified by the user.
- [isSummaryElement](/documentation/swiftui/accessibilitytraits/issummaryelement): The accessibility element provides summary information when the application starts.
- [isToggle](/documentation/swiftui/accessibilitytraits/istoggle): The accessibility element is a toggle.
- [playsSound](/documentation/swiftui/accessibilitytraits/playssound): The accessibility element plays its own sound when activated.
- [startsMediaSession](/documentation/swiftui/accessibilitytraits/startsmediasession): The accessibility element starts a media session when it is activated.
- [updatesFrequently](/documentation/swiftui/accessibilitytraits/updatesfrequently): The accessibility element frequently updates its label or value.

### Type Properties

- [isTabBar](/documentation/swiftui/accessibilitytraits/istabbar): The accessibility element is a tab bar.

## See Also

### Assigning traits to content

- [accessibilityAddTraits(_:)](/documentation/swiftui/view/accessibilityaddtraits(_:)): Adds the given traits to the view.
- [accessibilityRemoveTraits(_:)](/documentation/swiftui/view/accessibilityremovetraits(_:)): Removes the given traits from this view.
