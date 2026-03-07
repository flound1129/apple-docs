# Accessible descriptions

Describe interface elements to help people understand what they represent.

## Overview

SwiftUI can often infer some information about your user interface elements, but you can use accessibility modifiers to provide even more information for users that need it.

![None]

For design guidance, see [Accessibility](/design/Human-Interface-Guidelines/accessibility#Content-descriptions) in the Accessibility section of the Human Interface Guidelines.

### Applying labels

- [accessibilityLabel(_:)](/documentation/swiftui/view/accessibilitylabel(_:)): Adds a label to the view that describes its contents.
- [accessibilityLabel(_:isEnabled:)](/documentation/swiftui/view/accessibilitylabel(_:isenabled:)): Adds a label to the view that describes its contents.
- [accessibilityLabel(content:)](/documentation/swiftui/view/accessibilitylabel(content:)): Adds a label to the view that describes its contents.
- [accessibilityInputLabels(_:)](/documentation/swiftui/view/accessibilityinputlabels(_:)): Sets alternate input labels with which users identify a view.
- [accessibilityInputLabels(_:isEnabled:)](/documentation/swiftui/view/accessibilityinputlabels(_:isenabled:)): Sets alternate input labels with which users identify a view.
- [accessibilityLabeledPair(role:id:in:)](/documentation/swiftui/view/accessibilitylabeledpair(role:id:in:)): Pairs an accessibility element representing a label with the element for the matching content.
- [AccessibilityLabeledPairRole](/documentation/swiftui/accessibilitylabeledpairrole): The role of an accessibility element in a label / content pair.

### Describing values

- [accessibilityValue(_:)](/documentation/swiftui/view/accessibilityvalue(_:)): Adds a textual description of the value that the view contains.
- [accessibilityValue(_:isEnabled:)](/documentation/swiftui/view/accessibilityvalue(_:isenabled:)): Adds a textual description of the value that the view contains.

### Describing content

- [accessibilityTextContentType(_:)](/documentation/swiftui/view/accessibilitytextcontenttype(_:)): Sets an accessibility text content type.
- [accessibilityHeading(_:)](/documentation/swiftui/view/accessibilityheading(_:)): Sets the accessibility level of this heading.
- [AccessibilityHeadingLevel](/documentation/swiftui/accessibilityheadinglevel): The hierarchy of a heading in relation to other headings.
- [AccessibilityTextContentType](/documentation/swiftui/accessibilitytextcontenttype): Textual context that assistive technologies can use to improve the presentation of spoken text.

### Describing charts

- [accessibilityChartDescriptor(_:)](/documentation/swiftui/view/accessibilitychartdescriptor(_:)): Adds a descriptor to a View that represents a chart to make the chart’s contents accessible to all users.
- [AXChartDescriptorRepresentable](/documentation/swiftui/axchartdescriptorrepresentable): A type to generate an `AXChartDescriptor` object that you use to provide information about a chart and its data for an accessible experience in VoiceOver or other assistive technologies.

### Adding custom descriptions

- [accessibilityCustomContent(_:_:importance:)](/documentation/swiftui/view/accessibilitycustomcontent(_:_:importance:)): Add additional accessibility information to the view.
- [AccessibilityCustomContentKey](/documentation/swiftui/accessibilitycustomcontentkey): Key used to specify the identifier and label associated with an entry of additional accessibility information.

### Assigning traits to content

- [accessibilityAddTraits(_:)](/documentation/swiftui/view/accessibilityaddtraits(_:)): Adds the given traits to the view.
- [accessibilityRemoveTraits(_:)](/documentation/swiftui/view/accessibilityremovetraits(_:)): Removes the given traits from this view.
- [AccessibilityTraits](/documentation/swiftui/accessibilitytraits): A set of accessibility traits that describe how an element behaves.

### Offering hints

- [accessibilityHint(_:)](/documentation/swiftui/view/accessibilityhint(_:)): Communicates to the user what happens after performing the view’s action.
- [accessibilityHint(_:isEnabled:)](/documentation/swiftui/view/accessibilityhint(_:isenabled:)): Communicates to the user what happens after performing the view’s action.

### Configuring VoiceOver

- [speechAdjustedPitch(_:)](/documentation/swiftui/view/speechadjustedpitch(_:)): Raises or lowers the pitch of spoken text.
- [speechAlwaysIncludesPunctuation(_:)](/documentation/swiftui/view/speechalwaysincludespunctuation(_:)): Sets whether VoiceOver should always speak all punctuation in the text view.
- [speechAnnouncementsQueued(_:)](/documentation/swiftui/view/speechannouncementsqueued(_:)): Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [speechSpellsOutCharacters(_:)](/documentation/swiftui/view/speechspellsoutcharacters(_:)): Sets whether VoiceOver should speak the contents of the text view character by character.

## See Also

### Accessibility

- [Accessibility fundamentals](/documentation/swiftui/accessibility-fundamentals): Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Accessible appearance](/documentation/swiftui/accessible-appearance): Enhance the legibility of content in your app’s interface.
- [Accessible controls](/documentation/swiftui/accessible-controls): Improve access to actions that your app can undertake.
- [Accessible navigation](/documentation/swiftui/accessible-navigation): Enable users to navigate to specific user interface elements using rotors.
