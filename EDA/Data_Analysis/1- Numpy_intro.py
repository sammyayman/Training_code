print("\033c")
import numpy as np

# ===== BOOLEAN DATA TYPES =====
# 1. Creating boolean arrays
bool_array = np.array([True, False, True, False])
print("Boolean array:", bool_array)
print("Data type:", bool_array.dtype)  # bool_

# 2. Creating boolean arrays from conditions
numbers = np.array([1, 2, 3, 4, 5])
greater_than_3 = numbers > 3
print("\nNumbers greater than 3:", greater_than_3)

# 3. Boolean operations
# Element-wise AND, OR, NOT
array1 = np.array([True, True, False, False])

array2 = np.array([0, 1, 1, 0])

print("\nArray 1:", array1)
print("Array 2:", array2)
print("AND:", np.logical_and(array1, array2))  # [True, False, False, False]
print("OR: ", np.logical_or(array1, array2))   # [True, True, True, False]
print("NOT Array 1:", np.logical_not(array1))  # [False, False, True, True]

# 4. Boolean indexing
fruits = np.array(['apple', 'banana', 'cherry', 'date'])
prices = np.array([1.2, 0.5, 2.5, 1.8])

# Select fruits cheaper than $2


cheap_fruits = fruits[prices < 2.0]
print("\nFruits cheaper than $2:", cheap_fruits)

# 5. All and Any functions
print("\nAll values True?", np.all([True, True, True]))  # True
print("Any value True?", np.any([False, True, False]))  # True

# 6. Creating boolean arrays with specific shapes
# All True
all_true = np.ones(3, dtype=bool)
# All False
all_false = np.zeros(3, dtype=bool)
print("\nAll true:", all_true)
print("All false:", all_false)


# 7. Converting to boolean
numbers = np.array([-1, 0, 1, 2, 0])
bool_numbers = numbers.astype(bool)
print("\nNumbers to boolean:", bool_numbers)  # [True, False, True, True, False]

# ===== NUMERICAL DATA TYPES =====
# 1. Basic Data Types
# Integer types
int8_array = np.array([1, 2, 3], dtype=np.int8)     # 8-bit integer
int32_array = np.array([1, 2, 3], dtype=np.int32)   # 32-bit integer
int64_array = np.array([1, 2, 3], dtype=np.int64)   # 64-bit integer

# Unsigned integers
uint8_array = np.array([1, 2, 3], dtype=np.uint8)   # 8-bit unsigned integer

# Floating point types
float32_array = np.array([1.0, 2.5, 3.7], dtype=np.float32)  # 32-bit float
float64_array = np.array([1.0, 2.5, 3.7], dtype=np.float64)  # 64-bit float

# Complex numbers
complex64_array = np.array([1 + 2j, 3 + 4j], dtype=np.complex64)
complex128_array = np.array([1 + 2j, 3 + 4j], dtype=np.complex128)

# Boolean
bool_array = np.array([True, False, True], dtype=bool)

# 2. Checking Data Types
print("Integer array type:", int32_array.dtype)
print("Float array type:", float32_array.dtype)
print("Complex array type:", complex64_array.dtype)

# 3. Type Conversion
# Convert between data types
float_to_int = float32_array.astype(np.int32)
int_to_float = int32_array.astype(np.float64)

print("\nOriginal float32:", float32_array)
print("Converted to int32:", float_to_int)

# 4. Minimum and Maximum Values
print("\nint8 range:", np.iinfo(np.int8).min, "to", np.iinfo(np.int8).max)
print("uint8 range:", np.iinfo(np.uint8).min, "to", np.iinfo(np.uint8).max)
print("float32 range:", np.finfo(np.float32).min, "to", np.finfo(np.float32).max)

# 5. Creating arrays with specified data types
zeros_int = np.zeros(3, dtype=np.int32)
ones_float = np.ones(3, dtype=np.float64)
full_complex = np.full(3, 1+2j, dtype=np.complex128)

print("\nZeros array:", zeros_int)
print("Ones array:", ones_float)
print("Complex array:", full_complex)