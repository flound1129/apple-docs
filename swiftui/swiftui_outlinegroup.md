# OutlineGroup

A structure that computes views and disclosure groups on demand from an underlying collection of tree-structured, identified data.

```swift
struct OutlineGroup<Data, ID, Parent, Leaf, Subgroup> where Data : RandomAccessCollection, ID : Hashable
```

## Overview

Use an outline group when you need a view that can represent a hierarchy of data by using disclosure views. This allows the user to navigate the tree structure by using the disclosure views to expand and collapse branches.

In the following example, a tree structure of `FileItem` data offers a simplified view of a file system. Passing the root of this tree and the key path of its children allows you to quickly create a visual representation of the file system.

```swift
struct FileItem: Hashable, Identifiable, CustomStringConvertible {
    var id: Self { self }
    var name: String
    var children: [FileItem]? = nil
    var description: String {
        switch children {
        case nil:
            return "📄 \(name)"
        case .some(let children):
            return children.isEmpty ? "📂 \(name)" : "📁 \(name)"
        }
    }
}

let data =
  FileItem(name: "users", children:
    [FileItem(name: "user1234", children:
      [FileItem(name: "Photos", children:
        [FileItem(name: "photo001.jpg"),
         FileItem(name: "photo002.jpg")]),
       FileItem(name: "Movies", children:
         [FileItem(name: "movie001.mp4")]),
          FileItem(name: "Documents", children: [])
      ]),
     FileItem(name: "newuser", children:
       [FileItem(name: "Documents", children: [])
       ])
    ])

OutlineGroup(data, children: \.children) { item in
    Text("\(item.description)")
}
```

### Type parameters

Five generic type constraints define a specific `OutlineGroup` instance:

- `Data`: The type of a collection containing the children of an element in the tree-shaped data.
- `ID`: The type of the identifier for an element.
- `Parent`: The type of the visual representation of an element whose children property is non-`nil`
- `Leaf`: The type of the visual representation of an element whose children property is `nil`.
- `Subgroup`: A type of a view that groups a parent view and a view representing its children, typically with some mechanism for showing and hiding the children

### Creating an outline group

- [init(_:children:)](/documentation/swiftui/outlinegroup/init(_:children:)): Creates an outline group from a collection of root data elements and a key path to element’s children.
- [init(_:children:content:)](/documentation/swiftui/outlinegroup/init(_:children:content:)): Creates an outline group from a binding to a collection of root data elements and a key path to its children.
- [init(_:id:children:content:)](/documentation/swiftui/outlinegroup/init(_:id:children:content:)): Creates an outline group from a binding to a collection of root data elements, the key path to a data element’s identifier, and a key path to its children.

### Supporting types

- [OutlineSubgroupChildren](/documentation/swiftui/outlinesubgroupchildren): A type-erased view representing the children in an outline subgroup.

## See Also

### Disclosing information progressively

- [DisclosureGroup](/documentation/swiftui/disclosuregroup): A view that shows or hides another content view, based on the state of a disclosure control.
- [disclosureGroupStyle(_:)](/documentation/swiftui/view/disclosuregroupstyle(_:)): Sets the style for disclosure groups within this view.
