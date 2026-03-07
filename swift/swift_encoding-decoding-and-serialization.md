# Encoding, Decoding, and Serialization

Serialize and deserialize instances of your types with implicit or customized encoding.

### Custom Encoding and Decoding

- [Encoding and Decoding Custom Types](/documentation/Foundation/encoding-and-decoding-custom-types): Make your data types encodable and decodable for compatibility with external representations such as JSON.
- [Codable](/documentation/swift/codable): A type that can convert itself into and out of an external representation.
- [Encodable](/documentation/swift/encodable): A type that can encode itself to an external representation.
- [Decodable](/documentation/swift/decodable): A type that can decode itself from an external representation.
- [CodingKey](/documentation/swift/codingkey): A type that can be used as a key for encoding and decoding.
- [CodingKeyRepresentable](/documentation/swift/codingkeyrepresentable): A type that can be converted to and from a coding key.
- [CodingUserInfoKey](/documentation/swift/codinguserinfokey): A user-defined key for providing context during encoding and decoding.

### Encoders and Decoders

- [Encoder](/documentation/swift/encoder): A type that can encode values into a native format for external representation.
- [Decoder](/documentation/swift/decoder): A type that can decode values from a native format into in-memory representations.
- [EncodingError](/documentation/swift/encodingerror): An error that occurs during the encoding of a value.
- [DecodingError](/documentation/swift/decodingerror): An error that occurs during the decoding of a value.

### Encoding Containers

- [SingleValueEncodingContainer](/documentation/swift/singlevalueencodingcontainer): A container that can support the storage and direct encoding of a single non-keyed value.
- [KeyedEncodingContainer](/documentation/swift/keyedencodingcontainer): A concrete container that provides a view into an encoder’s storage, making the encoded properties of an encodable type accessible by keys.
- [KeyedEncodingContainerProtocol](/documentation/swift/keyedencodingcontainerprotocol): A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type in a keyed manner.
- [UnkeyedEncodingContainer](/documentation/swift/unkeyedencodingcontainer): A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type sequentially, without keys.

### Decoding Containers

- [KeyedDecodingContainer](/documentation/swift/keyeddecodingcontainer): A concrete container that provides a view into a decoder’s storage, making the encoded properties of a decodable type accessible by keys.
- [SingleValueDecodingContainer](/documentation/swift/singlevaluedecodingcontainer): A container that can support the storage and direct decoding of a single nonkeyed value.
- [KeyedDecodingContainerProtocol](/documentation/swift/keyeddecodingcontainerprotocol): A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type in a keyed manner.
- [UnkeyedDecodingContainer](/documentation/swift/unkeyeddecodingcontainer): A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type sequentially, without keys.

## See Also

### Tools for Your Types

- [Basic Behaviors](/documentation/swift/basic-behaviors): Use your custom types in operations that depend on testing for equality or order and as members of sets and dictionaries.
- [Initialization with Literals](/documentation/swift/initialization-with-literals): Allow values of your type to be expressed using different kinds of literals.
