# SearchScopeActivation

The ways that searchable modifiers can show or hide search scopes.

```swift
struct SearchScopeActivation
```

### Getting search scope activiation types

- [automatic](/documentation/swiftui/searchscopeactivation/automatic): The automatic activation of the scope bar.
- [onSearchPresentation](/documentation/swiftui/searchscopeactivation/onsearchpresentation): An activation where the system shows search scopes after presenting search and hides search scopes after search cancellation.
- [onTextEntry](/documentation/swiftui/searchscopeactivation/ontextentry): An activation where the system shows search scopes when typing begins in the search field and hides search scopes after search cancellation.

## See Also

### Limiting search scope

- [Scoping a search operation](/documentation/swiftui/scoping-a-search-operation): Divide the search space into a few broad categories.
- [searchScopes(_:scopes:)](/documentation/swiftui/view/searchscopes(_:scopes:)): Configures the search scopes for this view.
- [searchScopes(_:activation:_:)](/documentation/swiftui/view/searchscopes(_:activation:_:)): Configures the search scopes for this view with the specified activation strategy.
