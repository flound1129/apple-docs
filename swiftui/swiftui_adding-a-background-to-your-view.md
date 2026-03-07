# Adding a background to your view

Compose a background behind your view and extend it beyond the safe area insets.

## Overview

You can add a view as a background with the [background(_:alignment:)](/documentation/swiftui/view/background(_:alignment:)) view modifier. To add a background under multiple views, or to have a background larger than an existing view, you can layer the views by placing them within a [ZStack](/documentation/swiftui/zstack), and place the view you want to be in the background at the bottom of the view stack. You can specify that a background view should ignore the safe area insets to extend the background to some or all edges.

### Add a background

If your design calls for a background, you can use the [background(_:alignment:)](/documentation/swiftui/view/background(_:alignment:)) modifier to add it underneath an existing view. The following example adds a gradient to the vertical stack using the [background(_:alignment:)](/documentation/swiftui/view/background(_:alignment:)) view modifier:

```swift
let backgroundGradient = LinearGradient(
    colors: [Color.red, Color.blue],
    startPoint: .top, endPoint: .bottom)

struct SignInView: View {
    @State private var name: String = ""

    var body: some View {
        VStack {
            Text("Welcome")
                .font(.title)
            HStack {
                TextField("Your name?", text: $name)
                    .textFieldStyle(.roundedBorder)
                Button(action: {}, label: {
                    Image(systemName: "arrow.right.square")
                        .font(.title)
                })
            }
            .padding()
        }
        .background(backgroundGradient)
    }
}
```

The [background(_:alignment:)](/documentation/swiftui/view/background(_:alignment:)) view modifier constrains the size of the background view to be the same size as the view to which it’s attached:

![A screenshot of an iPhone showing a gradient background for the welcome title, text field, and button in the horizontal stack, not filling in the rest of the phone’s background.]

### Expand the background underneath your view

To create a background that’s larger than the vertical stack, use a different technique. You could add [Spacer](/documentation/swiftui/spacer) views above and below the content in the [VStack](/documentation/swiftui/vstack) to expand it, but that would also expand the size of the stack, possibly changing it’s layout. To add in a larger background without changing the size of the stack, nest the views within a [ZStack](/documentation/swiftui/zstack) to layer the [VStack](/documentation/swiftui/vstack) over the background view:

```swift
struct SignInView: View {
    @State private var name: String = ""

    var body: some View {
        ZStack {
            backgroundGradient
            VStack {
                Text("Welcome")
                    .font(.title)
                HStack {
                    TextField("Your name?", text: $name)
                        .textFieldStyle(.roundedBorder)
                    Button(action: {}, label: {
                        Image(systemName: "arrow.right.square")
                            .font(.title)
                    })
                }
                .padding()
            }
        }
    }
}
```

View sizes within a depth stack are independent, unlike when using the background view modifier. The view from [Gradient](/documentation/swiftui/gradient) expands to fill the space available to the stack, but avoids the safe area insets by default:

![A screenshot of an iPhone showing a gradient background filling almost all of the background, excluding the top status bar and the bottom bar.]

For more information on usings stacks to combine views, see [Building layouts with stack views](/documentation/swiftui/building-layouts-with-stack-views).

### Extend the background into the safe areas

By default, SwiftUI sizes and positions views to avoid system defined safe areas to ensure that system content or the edges of the device won’t obstruct your views. If your design calls for the background to extend to the screen edges, use the [ignoresSafeArea(_:edges:)](/documentation/swiftui/view/ignoressafearea(_:edges:)) modifier to override the default.

```swift
struct SignInView: View {
    @State private var name: String = ""
    var body: some View {
        ZStack {
            backgroundGradient
            VStack {
                Text("Welcome")
                    .font(.title)
                HStack {
                    TextField("Your name?", text: $name)
                        .textFieldStyle(.roundedBorder)
                    Button(action: {}, label: {
                        Image(systemName: "arrow.right.square")
                            .font(.title)
                    })
                }
                .padding()
            }
        }
        .ignoresSafeArea()
    }
}
```

The background gradient fills the display area of the device and ignores the safe area insets.

![A screenshot of an iPhone showing a gradient background filling the entire background.]

### Adjust views when displaying the keyboard

You can ignore the keyboard’s safe area by adding the [ignoresSafeArea(_:edges:)](/documentation/swiftui/view/ignoressafearea(_:edges:)) modifier. When you activate the keyboard, the content of the vertical stack remains fixed, ignoring the space used by the keyboard:

![A screenshot of an iPhone showing a gradient background filling the entire background, with the keyboard overlaid at the bottom of the screen. The welcome title, text field, and button within the horizontal stack are centered between the top and bottom of the iPhone, with the keyboard obscuring the lower portion of the background.]

To get the contents of the vertical stack to respect the safe areas and adjust to the keyboard, move the modifier to only apply to the background view.

```swift
struct SignInView: View {
    @State private var name: String = ""
    var body: some View {
        ZStack {
            backgroundGradient
                .ignoresSafeArea()
            VStack {
                Text("Welcome")
                    .font(.title)
                HStack {
                    TextField("Your name?", text: $name)
                        .textFieldStyle(.roundedBorder)
                    Button(action: {}, label: {
                        Image(systemName: "arrow.right.square")
                            .font(.title)
                    })
                }
                .padding()
            }
        }
    }
}
```

To accommodate the keyboard, SwiftUI resizes and positions your view. Because the background view has the [ignoresSafeArea(_:edges:)](/documentation/swiftui/view/ignoressafearea(_:edges:)) modifier, it remains unchanged.

![A screenshot of an iPhone showing a gradient background filling the entire background, with the keyboard overlaid at the bottom of the screen. The welcome title, text field, and button within the horizontal stack is centered between the top of the keyboard and the top of the iPhone, and the gradient background extends underneath the keyboard for the full height of the iPhone.]

## See Also

### Layering views

- [ZStack](/documentation/swiftui/zstack): A view that overlays its subviews, aligning them in both axes.
- [zIndex(_:)](/documentation/swiftui/view/zindex(_:)): Controls the display order of overlapping views.
- [background(alignment:content:)](/documentation/swiftui/view/background(alignment:content:)): Layers the views that you specify behind this view.
- [background(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(_:ignoressafeareaedges:)): Sets the view’s background to a style.
- [background(ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(ignoressafeareaedges:)): Sets the view’s background to the default background style.
- [background(_:in:fillStyle:)](/documentation/swiftui/view/background(_:in:fillstyle:)): Sets the view’s background to an insettable shape filled with a style.
- [background(in:fillStyle:)](/documentation/swiftui/view/background(in:fillstyle:)): Sets the view’s background to an insettable shape filled with the default background style.
- [overlay(alignment:content:)](/documentation/swiftui/view/overlay(alignment:content:)): Layers the views that you specify in front of this view.
- [overlay(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/overlay(_:ignoressafeareaedges:)): Layers the specified style in front of this view.
- [overlay(_:in:fillStyle:)](/documentation/swiftui/view/overlay(_:in:fillstyle:)): Layers a shape that you specify in front of this view.
- [backgroundMaterial](/documentation/swiftui/environmentvalues/backgroundmaterial): The material underneath the current view.
- [containerBackground(_:for:)](/documentation/swiftui/view/containerbackground(_:for:)): Sets the container background of the enclosing container using a view.
- [containerBackground(for:alignment:content:)](/documentation/swiftui/view/containerbackground(for:alignment:content:)): Sets the container background of the enclosing container using a view.
- [ContainerBackgroundPlacement](/documentation/swiftui/containerbackgroundplacement): The placement of a container background.
