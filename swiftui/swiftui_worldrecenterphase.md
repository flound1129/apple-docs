# WorldRecenterPhase

A type that represents information associated with a phase of a system recenter event. Values of this type are passed to the closure specified in View.onWorldRecenter(action:).

```swift
enum WorldRecenterPhase
```

### Enumeration Cases

- [WorldRecenterPhase.began](/documentation/swiftui/worldrecenterphase/began): The app has begun to fade out. It is not re-positioned yet.
- [WorldRecenterPhase.ended](/documentation/swiftui/worldrecenterphase/ended): The app has begun to fade in after it has been re-positioned.
