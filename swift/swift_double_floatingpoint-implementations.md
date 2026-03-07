# FloatingPoint Implementations

### Operators

- [*(_:_:)](/documentation/swift/double/*(_:_:)): Multiplies two values and produces their product, rounding to a representable value.
- [*=(_:_:)](/documentation/swift/double/*=(_:_:)): Multiplies two values and stores the result in the left-hand-side variable, rounding to a representable value.
- [+(_:_:)](/documentation/swift/double/+(_:_:)): Adds two values and produces their sum, rounded to a representable value.
- [+=(_:_:)](/documentation/swift/double/+=(_:_:)): Adds two values and stores the result in the left-hand-side variable, rounded to a representable value.
- [-(_:)](/documentation/swift/double/-(_:)): Calculates the additive inverse of a value.
- [-(_:_:)](/documentation/swift/double/-(_:_:)): Subtracts one value from another and produces their difference, rounded to a representable value.
- [-=(_:_:)](/documentation/swift/double/-=(_:_:)): Subtracts the second value from the first and stores the difference in the left-hand-side variable, rounding to a representable value.
- [/(_:_:)](/documentation/swift/double/_(_:_:)): Returns the quotient of dividing the first value by the second, rounded to a representable value.
- [>(_:_:)](/documentation/swift/double/_(_:_:)-552jp)
- [/=(_:_:)](/documentation/swift/double/_=(_:_:)): Divides the first value by the second and stores the quotient in the left-hand-side variable, rounding to a representable value.
- [<=(_:_:)](/documentation/swift/double/_=(_:_:)-5yoz7)
- [>=(_:_:)](/documentation/swift/double/_=(_:_:)-9o6h8)

### Initializers

- [init(_:)](/documentation/swift/double/init(_:)-5blrp): Creates a new value, rounded to the closest possible representation.
- [init(_:)](/documentation/swift/double/init(_:)-84ohu): Creates a new value, rounded to the closest possible representation.
- [init(exactly:)](/documentation/swift/double/init(exactly:)-2uexo): Creates a new value, if the given integer can be represented exactly.
- [init(sign:exponent:significand:)](/documentation/swift/double/init(sign:exponent:significand:)): Creates a new value from the given sign, exponent, and significand.
- [init(signOf:magnitudeOf:)](/documentation/swift/double/init(signof:magnitudeof:)): Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init(signOf:magnitudeOf:)](/documentation/swift/double/init(signof:magnitudeof:)-6i9uy): Creates a new floating-point value using the sign of one value and the magnitude of another.

### Instance Properties

- [exponent](/documentation/swift/double/exponent-swift.property): The exponent of the floating-point value.
- [floatingPointClass](/documentation/swift/double/floatingpointclass): The classification of this value.
- [isCanonical](/documentation/swift/double/iscanonical): A Boolean value indicating whether the instance’s representation is in its canonical form.
- [isFinite](/documentation/swift/double/isfinite): A Boolean value indicating whether this instance is finite.
- [isInfinite](/documentation/swift/double/isinfinite): A Boolean value indicating whether the instance is infinite.
- [isNaN](/documentation/swift/double/isnan): A Boolean value indicating whether the instance is NaN (“not a number”).
- [isNormal](/documentation/swift/double/isnormal): A Boolean value indicating whether this instance is normal.
- [isSignalingNaN](/documentation/swift/double/issignalingnan): A Boolean value indicating whether the instance is a signaling NaN.
- [isSubnormal](/documentation/swift/double/issubnormal): A Boolean value indicating whether the instance is subnormal.
- [isZero](/documentation/swift/double/iszero): A Boolean value indicating whether the instance is equal to zero.
- [nextDown](/documentation/swift/double/nextdown): The greatest representable value that compares less than this value.
- [nextUp](/documentation/swift/double/nextup): The least representable value that compares greater than this value.
- [sign](/documentation/swift/double/sign): The sign of the floating-point value.
- [significand](/documentation/swift/double/significand): The significand of the floating-point value.
- [ulp](/documentation/swift/double/ulp): The unit in the last place of this value.

### Instance Methods

- [addProduct(_:_:)](/documentation/swift/double/addproduct(_:_:)): Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [addingProduct(_:_:)](/documentation/swift/double/addingproduct(_:_:)): Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [formRemainder(dividingBy:)](/documentation/swift/double/formremainder(dividingby:)): Replaces this value with the remainder of itself divided by the given value.
- [formSquareRoot()](/documentation/swift/double/formsquareroot()): Replaces this value with its square root, rounded to a representable value.
- [formTruncatingRemainder(dividingBy:)](/documentation/swift/double/formtruncatingremainder(dividingby:)): Replaces this value with the remainder of itself divided by the given value using truncating division.
- [isEqual(to:)](/documentation/swift/double/isequal(to:)): Returns a Boolean value indicating whether this instance is equal to the given value.
- [isLess(than:)](/documentation/swift/double/isless(than:)): Returns a Boolean value indicating whether this instance is less than the given value.
- [isLessThanOrEqualTo(_:)](/documentation/swift/double/islessthanorequalto(_:)): Returns a Boolean value indicating whether this instance is less than or equal to the given value.
- [isTotallyOrdered(belowOrEqualTo:)](/documentation/swift/double/istotallyordered(beloworequalto:)): Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.
- [negate()](/documentation/swift/double/negate()): Replaces this value with its additive inverse.
- [remainder(dividingBy:)](/documentation/swift/double/remainder(dividingby:)): Returns the remainder of this value divided by the given value.
- [round()](/documentation/swift/double/round())
- [round(_:)](/documentation/swift/double/round(_:)): Rounds the value to an integral value using the specified rounding rule.
- [rounded()](/documentation/swift/double/rounded())
- [rounded(_:)](/documentation/swift/double/rounded(_:)): Returns this value rounded to an integral value using the specified rounding rule.
- [squareRoot()](/documentation/swift/double/squareroot()): Returns the square root of the value, rounded to a representable value.
- [truncatingRemainder(dividingBy:)](/documentation/swift/double/truncatingremainder(dividingby:)): Returns the remainder of this value divided by the given value using truncating division.

### Type Aliases

- [Double.Exponent](/documentation/swift/double/exponent-swift.typealias): A type that can represent any written exponent.

### Type Properties

- [greatestFiniteMagnitude](/documentation/swift/double/greatestfinitemagnitude): The greatest finite number representable by this type.
- [infinity](/documentation/swift/double/infinity): Positive infinity.
- [leastNonzeroMagnitude](/documentation/swift/double/leastnonzeromagnitude): The least positive number.
- [leastNormalMagnitude](/documentation/swift/double/leastnormalmagnitude): The least positive normal number.
- [nan](/documentation/swift/double/nan): A quiet NaN (“not a number”).
- [pi](/documentation/swift/double/pi): The mathematical constant pi (π), approximately equal to 3.14159.
- [radix](/documentation/swift/double/radix): The radix, or base of exponentiation, for a floating-point type.
- [signalingNaN](/documentation/swift/double/signalingnan): A signaling NaN (“not a number”).
- [ulpOfOne](/documentation/swift/double/ulpofone): The unit in the last place of 1.0.
- [ulpOfOne](/documentation/swift/double/ulpofone-1s81x): The unit in the last place of 1.0.

### Type Methods

- [maximum(_:_:)](/documentation/swift/double/maximum(_:_:)): Returns the greater of the two given values.
- [maximumMagnitude(_:_:)](/documentation/swift/double/maximummagnitude(_:_:)): Returns the value with greater magnitude.
- [minimum(_:_:)](/documentation/swift/double/minimum(_:_:)): Returns the lesser of the two given values.
- [minimumMagnitude(_:_:)](/documentation/swift/double/minimummagnitude(_:_:)): Returns the value with lesser magnitude.
