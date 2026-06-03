import numpy as np

def pretty_print(arr):
    # Convert everything to string
    str_arr = np.vectorize(str)(arr)

    # Find max width per column for alignment
    col_widths = np.max([[len(item) for item in col] for col in str_arr.T], axis=1)

    # Align each element
    aligned = np.array([[item.ljust(w) for item, w in zip(row, col_widths)] for row in str_arr])

    # Print formatted
    print("\nFormatted Array:\n")
    for row in aligned:
        print(" | ".join(row))

    # Reverse function (to recover original types)
    def reverse_cast(x):
        x = x.strip()
        if x.lower() == "true":
            return True
        elif x.lower() == "false":
            return False
        try:
            if "." in x:
                return float(x)
            return int(x)
        except ValueError:
            return x  # keep as string

    def recover():
        return np.vectorize(reverse_cast, otypes=[object])(aligned)  # 👈 force object dtype

    return aligned, recover


# Mixed array
arr = np.array([
    [1, 22, 333, 4444, 55555],
    [1.1, 22.22, 333.333, 4444.4444, 5.5],
    [True, False, True, False, True],
    ["short", "a bit longer", "tiny", "super very long text", "ok"]
], dtype=object)

# Pretty print
aligned, recover_func = pretty_print(arr)

# Recover original
# print("\nRecovered Array:\n", recover_func())

import numpy as np

class PrettyArray:
    def __init__(self, arr):
        self.original = arr.astype(object)  # store original array
        self.aligned = None

    def format(self):
        """Format array for pretty printing with equal spacing."""
        str_arr = np.vectorize(str)(self.original)

        # Find max width per column
        col_widths = np.max([[len(item) for item in col] for col in str_arr.T], axis=1)

        # Align values
        self.aligned = np.array([
            [item.ljust(w) for item, w in zip(row, col_widths)]
            for row in str_arr
        ])

        return self.aligned

    def print(self):
        """Print formatted array with separators."""
        if self.aligned is None:
            self.format()
        print("\nFormatted Array:\n")
        for row in self.aligned:
            print(" | ".join(row))

    def _reverse_cast(self, x):
        """Convert string back to original type."""
        x = x.strip()
        if x.lower() == "true":
            return True
        elif x.lower() == "false":
            return False
        try:
            if "." in x:
                return float(x)
            return int(x)
        except ValueError:
            return x  # keep as string

    def recover(self):
        """Recover aligned array back to original mixed types."""
        if self.aligned is None:
            self.format()
        return np.vectorize(self._reverse_cast, otypes=[object])(self.aligned)


arr = np.array([
    [1, 22, 333, 4444, 55555],
    [1.1, 22.22, 333.333, 4444.4444, 5.5],
    [True, False, True, False, True],
    ["short", "a bit longer", "tiny", "super very long text", "ok"]
], dtype=object)

pa = PrettyArray(arr)

pa.print()  # formatted view

print("\nRecovered Array:")
print(pa.recover())  # back to original values

import numpy as np

arr = np.array([
    [1, 22, 333, 4444, 55555],
    [1.1, 22.22, 333.333, 4444.4444, 5.5],
    [True, False, True, False, True],
    ["short", "a bit longer", "tiny", "super very long text", "ok"]
], dtype=object)

# Calculate max width per column (not changing data!)
extra_space = 6  # <<--- make this bigger for wider spacing
max_lens = []
for col in range(arr.shape[1]):
    col_items = arr[:, col]
    max_len = max(len(str(x)) for x in col_items)
    max_lens.append(max_len + extra_space)

def formatter(x, col_idx):
    return f"{str(x):<{max_lens[col_idx]}}"

# Build formatted rows for printing
formatted_rows = []
for row in arr:
    formatted_row = [formatter(val, i) for i, val in enumerate(row)]
    formatted_rows.append("".join(formatted_row))

# Print neatly but data is still original
print("\n".join(formatted_rows))

print("\nOriginal array dtypes preserved:")
for row in arr:
    print([type(x) for x in row])



# import numpy as np

def pretty_print(arr):
    # Convert everything to string
    str_arr = np.vectorize(str)(arr)

    # Find max width per column for alignment
    col_widths = np.max([[len(item) for item in col] for col in str_arr.T], axis=1)

    # Align each element
    aligned = np.array([[item.ljust(w) for item, w in zip(row, col_widths)] for row in str_arr])

    # Print formatted
    print("\nFormatted Array:\n")
    for row in aligned:
        print(" | ".join(row))

    # Reverse function (to recover original types)
    def reverse_cast(x):
        x = x.strip()
        if x.lower() == "true":
            return True
        elif x.lower() == "false":
            return False
        try:
            if "." in x:
                return float(x)
            return int(x)
        except ValueError:
            return x  # keep as string

    def recover():
        return np.vectorize(reverse_cast, otypes=[object])(aligned)  # 👈 force object dtype

    return aligned, recover


arr = np.array([
    [1, 22, 333, 4444, 55555],
    [1.1, 22.22, 333.333, 4444.4444, 5.5],
    [True, False, True, False, True],
    ["short", "a bit longer", "tiny", "super very long text", "ok"]
], dtype=object)

aligned, recover_func = pretty_print(arr)

print("\nRecovered Array:")
print(recover_func())



import numpy as np

class PrettyArray:
    def __init__(self, arr):
        self.original = arr.astype(object)  # store original array
        self.aligned = None

    def format(self):
        """Format array for pretty printing with equal spacing."""
        str_arr = np.vectorize(str)(self.original)

        # Find max width per column
        col_widths = np.max([[len(item) for item in col] for col in str_arr.T], axis=1)

        # Align values
        self.aligned = np.array([
            [item.ljust(w) for item, w in zip(row, col_widths)]
            for row in str_arr
        ])

        return self.aligned

    def print(self):
        """Print formatted array with separators."""
        if self.aligned is None:
            self.format()
        print("\nFormatted Array:\n")
        for row in self.aligned:
            print(" | ".join(row))

    def _reverse_cast(self, x):
        """Convert string back to original type."""
        x = x.strip()
        if x.lower() == "true":
            return True
        elif x.lower() == "false":
            return False
        try:
            if "." in x:
                return float(x)
            return int(x)
        except ValueError:
            return x  # keep as string

    def recover(self):
        """Recover aligned array back to original mixed types."""
        if self.aligned is None:
            self.format()
        return np.vectorize(self._reverse_cast, otypes=[object])(self.aligned)



print("---"*20)

arr = np.array([
    [1, 22, 333, 4444, 55555],
    [1.1, 22.22, 333.333, 4444.4444, 5.5],
    [True, False, True, False, True],
    ["short", "a bit longer", "tiny", "super very long text", "ok"]
], dtype=object)

pa = PrettyArray(arr)

pa.print()  # formatted view

print("\nRecovered Array:")
print(pa.recover())  # back to original values



import numpy as np

# 3D array: shape (3, 2, 3)
arr = np.array([
    [[1, "a", True],
     [2, "b", False]],

    [[3.5, "c", True],
     [4, "d", False]],

    [[5, "e", True],
     [6, "f", False]]
], dtype=object)

print("Original 3D array:\n", arr)

# Flatten to work easily
flat = arr.flatten()

numbers = [x for x in flat if isinstance(x, (int, float)) and not isinstance(x, bool)]
booleans = [x for x in flat if isinstance(x, bool)]
strings = [x for x in flat if isinstance(x, str)]

print("Numbers:", numbers)
print("Booleans:", booleans)
print("Strings:", strings)


block0 = np.array(numbers).reshape(2, 3)   # numbers
block1 = np.array(booleans).reshape(2, 3)  # booleans
block2 = np.array(strings).reshape(2, 3)   # strings

result = np.array([block0, block1, block2], dtype=object)
print("Final rearranged array:\n", result)

print('---'*20)

import numpy as np

# Randomly mixed data (27 items = 3x3x3)
data = [
    1, "a", True,
    5, False, "b",
    "c", 9, True,
    
    2, "d", False,
    7.5, True, "e",
    "f", 4, False,
    
    "g", 6, True,
    8, "h", False,
    True, "i", 3
]

arr = np.array(data, dtype=object).reshape(3, 3, 3)

print("Original random 3D array:\n", arr)
flat = arr.flatten()

numbers = [x for x in flat if isinstance(x, (int, float)) and not isinstance(x, bool)]
booleans = [x for x in flat if isinstance(x, bool)]
strings = [x for x in flat if isinstance(x, str)]

print("Numbers:", numbers)
print("Booleans:", booleans)
print("Strings:", strings)

block0 = np.array(numbers).reshape(3, 3)   # numbers
block1 = np.array(booleans).reshape(3, 3)  # booleans
block2 = np.array(strings).reshape(3, 3)   # strings

result = np.array([block0, block1, block2], dtype=object)
print("Final rearranged array:\n", result)


print('---'*20 , '\n with OOP : \n') 

import numpy as np

class MixedArrayHandler:
    def __init__(self, arr):
        self.arr = np.array(arr, dtype=object).reshape(3, 3, 3)
        self.numbers, self.booleans, self.strings = [], [], []
        self.result = None

    def split_by_type(self):
        flat = self.arr.flatten()
        self.numbers = [x for x in flat if isinstance(x, (int, float)) and not isinstance(x, bool)]
        self.booleans = [x for x in flat if isinstance(x, bool)]
        self.strings = [x for x in flat if isinstance(x, str)]

    def rearrange(self):
        block0 = np.array(self.numbers).reshape(3, 3)
        block1 = np.array(self.booleans).reshape(3, 3)
        block2 = np.array(self.strings).reshape(3, 3)
        self.result = np.array([block0, block1, block2], dtype=object)
        return self.result

    def __str__(self):
        return f"Original Array:\n{self.arr}\n\nRearranged (Num, Bool, Str):\n{self.result}"


# 🔹 Example Usage
data = [
    1, "a", True,
    5, False, "b",
    "c", 9, True,
    
    2, "d", False,
    7.5, True, "e",
    "f", 4, False,
    
    "g", 6, True,
    8, "h", False,
    True, "i", 3
]

handler = MixedArrayHandler(data)
handler.split_by_type()
handler.rearrange()

print(handler)


import numpy as np

class MixedArrayHandler:
    def __init__(self, arr):
        self.arr = np.array(arr, dtype=object).reshape(3, 3, 3)
        self.numbers, self.booleans, self.strings = [], [], []
        self.result = None

    def split_by_type(self):
        flat = self.arr.flatten()
        self.numbers = [x for x in flat if isinstance(x, (int, float)) and not isinstance(x, bool)]
        self.booleans = [x for x in flat if isinstance(x, bool)]
        self.strings = [x for x in flat if isinstance(x, str)]

    def get_numbers_block(self):
        return np.array(self.numbers).reshape(3, 3)

    def get_booleans_block(self):
        return np.array(self.booleans).reshape(3, 3)

    def get_strings_block(self):
        return np.array(self.strings).reshape(3, 3)

    def rearrange(self):
        block0 = self.get_numbers_block()
        block1 = self.get_booleans_block()
        block2 = self.get_strings_block()
        self.result = np.array([block0, block1, block2], dtype=object)
        return self.result

    def __str__(self):
        return f"""
Original Array:
{self.arr}

Numbers Block:
{self.get_numbers_block()}

Booleans Block:
{self.get_booleans_block()}

Strings Block:
{self.get_strings_block()}

Final Rearranged 3D Array:
{self.result}
"""


# 🔹 Example Usage
data = [
    1, "a", True,
    5, False, "b",
    "c", 9, True,
    
    2, "d", False,
    7.5, True, "e",
    "f", 4, False,
    
    "g", 6, True,
    8, "h", False,
    True, "i", 3
]

handler = MixedArrayHandler(data)
handler.split_by_type()
handler.rearrange()

print(handler)
