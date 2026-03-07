# PickerStyle

A type that specifies the appearance and interaction of all pickers within a view hierarchy.

```swift
protocol PickerStyle
```

### Getting built-in picker styles

- [automatic](/documentation/swiftui/pickerstyle/automatic): The default picker style, based on the picker’s context.
- [inline](/documentation/swiftui/pickerstyle/inline): A `PickerStyle` where each option is displayed inline with other views in the current container.
- [menu](/documentation/swiftui/pickerstyle/menu): A picker style that presents the options as a menu when the user presses a button, or as a submenu when nested within a larger menu.
- [navigationLink](/documentation/swiftui/pickerstyle/navigationlink): A picker style represented by a navigation link that presents the options by pushing a List-style picker view.
- [palette](/documentation/swiftui/pickerstyle/palette): A picker style that presents the options as a row of compact elements.
- [radioGroup](/documentation/swiftui/pickerstyle/radiogroup): A picker style that presents the options as a group of radio buttons.
- [segmented](/documentation/swiftui/pickerstyle/segmented): A picker style that presents the options in a segmented control.
- [wheel](/documentation/swiftui/pickerstyle/wheel): A picker style that presents the options in a scrollable wheel that shows the selected option and a few neighboring options.

### Supporting types

- [DefaultPickerStyle](/documentation/swiftui/defaultpickerstyle): The default picker style, based on the picker’s context.
- [InlinePickerStyle](/documentation/swiftui/inlinepickerstyle): A `PickerStyle` where each option is displayed inline with other views in the current container.
- [MenuPickerStyle](/documentation/swiftui/menupickerstyle): A picker style that presents the options as a menu when the user presses a button, or as a submenu when nested within a larger menu.
- [NavigationLinkPickerStyle](/documentation/swiftui/navigationlinkpickerstyle): A picker style represented by a navigation link that presents the options by pushing a List-style picker view.
- [PalettePickerStyle](/documentation/swiftui/palettepickerstyle): A picker style that presents the options as a row of compact elements.
- [RadioGroupPickerStyle](/documentation/swiftui/radiogrouppickerstyle): A picker style that presents the options as a group of radio buttons.
- [SegmentedPickerStyle](/documentation/swiftui/segmentedpickerstyle): A picker style that presents the options in a segmented control.
- [WheelPickerStyle](/documentation/swiftui/wheelpickerstyle): A picker style that presents the options in a scrollable wheel that shows the selected option and a few neighboring options.

### Deprecated styles

- [PopUpButtonPickerStyle](/documentation/swiftui/popupbuttonpickerstyle): A picker style that presents the options as a menu when the user presses a button.

## See Also

### Styling pickers

- [pickerStyle(_:)](/documentation/swiftui/view/pickerstyle(_:)): Sets the style for pickers within this view.
- [datePickerStyle(_:)](/documentation/swiftui/view/datepickerstyle(_:)): Sets the style for date pickers within this view.
- [DatePickerStyle](/documentation/swiftui/datepickerstyle): A type that specifies the appearance and interaction of all date pickers within a view hierarchy.
