# Preparing views for localization

Specify hints and add strings to localize your SwiftUI views.

## Overview

Localize SwiftUI views so users experience your app in their own native language, region, and culture. Xcode parses SwiftUI views for strings to localize when exporting a localization catalog. You can add hints so that Xcode generates correct, hinted strings to localize for your app.

For information about string catalogs, see [Localizing and varying text with a string catalog](/documentation/Xcode/localizing-and-varying-text-with-a-string-catalog).

### Add comments to text views

To ease the translation process, provide hints to translators that share how and where your app displays the strings of a [Text](/documentation/swiftui/text) view. To add a hint, use the optional `comment` parameter to the text view initializer [init(_:tableName:bundle:comment:)](/documentation/swiftui/text/init(_:tablename:bundle:comment:)). When you localize your app with Xcode, it includes the comment string along with the string. For example, the following text view includes a comment:

```swift
Text("Explore",
     comment: "The title of the tab bar item that navigates to the Explore screen.")
```

Xcode creates the following entry in your string catalog file for this view:

![A screenshot that shows a string catalog in Xcode for a simple app. The catalog has a single key called Explore with an English value for the key that is also the word Explore. The key also has a comment that says The title of the tab bar item that navigates to the Explore screen.]

### Provide additional information with text views

You can localize many SwiftUI views that have a string label by providing a string that SwiftUI interprets as a [LocalizedStringKey](/documentation/swiftui/localizedstringkey). The system uses the key to retrieve a localized value from your string catalog at runtime, or uses the string directly if it can’t find the key in the catalog. For example, SwiftUI uses the string input to the following [Label](/documentation/swiftui/label) initializer as a localized string key:

```swift
Label("Message", image: "msgSymbol")
```

If you additionally want to provide a comment for localization, you can use an explicit [Text](/documentation/swiftui/text) view instead:

```swift
Label {
    Text("Message",
         comment: "A label that displays 'Message' and a corresponding image.")
} icon: {
    Image("msgSymbol")
}
```

Many SwiftUI controls have view builder initializers that enable you to follow this pattern. For more information on how to make your app’s text translatable, see [Preparing your app’s text for translation](/documentation/Xcode/preparing-your-apps-text-for-translation).

## See Also

### Localizing text

- [LocalizedStringKey](/documentation/swiftui/localizedstringkey): The key used to look up an entry in a strings file or strings dictionary file.
- [locale](/documentation/swiftui/environmentvalues/locale): The current locale that views should use.
- [typesettingLanguage(_:isEnabled:)](/documentation/swiftui/view/typesettinglanguage(_:isenabled:)): Specifies the language for typesetting.
- [TypesettingLanguage](/documentation/swiftui/typesettinglanguage): Defines how typesetting language is determined for text.
