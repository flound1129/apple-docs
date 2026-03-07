# PhysicalMetric

Provides access to a value in points that corresponds to the specified physical measurement.

```swift
@propertyWrapper @frozen struct PhysicalMetric<Value>
```

## Overview

Use this property wrapper inside a [View](/documentation/swiftui/view) or a type that inherits a `View`’s environment, like a [ViewModifier](/documentation/swiftui/viewmodifier). Its value will be the equivalent in points of the physical measurement of length you specify.

For example, to have a variable that contains the amount of points corresponding to one meter, you can do the following:

```swift
struct MyView: View {
    @PhysicalMetric(from: .meters)
    var twoAndAHalfMeters = 2.5
    …
}
```

Using this wrapper for a property of a type not associated with a scene’s view contents, like an  [App](/documentation/swiftui/app) or a [Scene](/documentation/swiftui/scene), is unsupported.

## Compensating for World Scaling

Starting with apps built against the visionOS 2.0 SDK, the default behavior of `PhysicalMetric` is to produce values that match the distances used by `RealityView`s in the same scene, by scaling its returned values to match the world scaling of the current scene. Previously, the values were not scaled, and they were suitable for measuring distances and lengths within the user’s surroundings, outside of any scene. Unscaled values could produce unexpected behavior if used in conjunction with `RealityView`s within the scene.

To modify the behavior of `PhysicalMetric` and obtain unscaled values, use the [transformEnvironment(_:transform:)](/documentation/swiftui/view/transformenvironment(_:transform:)) modifier, transforming the [physicalMetrics](/documentation/swiftui/environmentvalues/physicalmetrics) key path, to edit the converter used by `PhysicalMetric` within the modified views to use a new [WorldScalingCompensation](/documentation/swiftui/worldscalingcompensation) mode. For example:

```swift
struct RulerView: View {
    @PhysicalMetric(from: .meters)
    var oneMeter = 1

    var body: some View {
        /* implement a size-accurate ruler */
    }
}

struct ContentView: View {
    var body: some View {
        RulerView()
            .transformEnvironment(\.physicalMetrics) { metrics in
                metrics = metrics.worldScalingCompensation(.unscaled)
            }
    }
}
```

> **See Also:**
> [PhysicalMetricsConverter](/documentation/swiftui/physicalmetricsconverter)
>

> **See Also:**
> [WorldScalingCompensation](/documentation/swiftui/worldscalingcompensation)
>

### Creating a metric

- [init(wrappedValue:from:)](/documentation/swiftui/physicalmetric/init(wrappedvalue:from:)): Creates a value that maps the specified point, whose dimensions are specified in physical length measurements in the given unit, to the corresponding value in points in the associated scene.

### Getting the value

- [wrappedValue](/documentation/swiftui/physicalmetric/wrappedvalue): A value in points in the coordinate system of the associated scene.

## See Also

### Measuring a view

- [GeometryReader](/documentation/swiftui/geometryreader): A container view that defines its content as a function of its own size and coordinate space.
- [GeometryReader3D](/documentation/swiftui/geometryreader3d): A container view that defines its content as a function of its own size and coordinate space.
- [GeometryProxy](/documentation/swiftui/geometryproxy): A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
- [GeometryProxy3D](/documentation/swiftui/geometryproxy3d): A proxy for access to the size and coordinate space of the container view.
- [coordinateSpace(_:)](/documentation/swiftui/view/coordinatespace(_:)): Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [CoordinateSpace](/documentation/swiftui/coordinatespace): A resolved coordinate space created by the coordinate space protocol.
- [CoordinateSpaceProtocol](/documentation/swiftui/coordinatespaceprotocol): A frame of reference within the layout system.
- [PhysicalMetricsConverter](/documentation/swiftui/physicalmetricsconverter): A physical metrics converter provides conversion between point values and their extent in 3D space, in the form of physical length measurements.
