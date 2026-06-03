data = [m for m in dir(int) if not m.startswith("_")]
for i in range(0, len(data), 7): print(data[i:i+7])

# print("\n the Object of __obj__ : ")
# data_obj = [m for m in dir(int) if  m.startswith("_")]
# for i in range(0, len(data_obj), 7):print(data_obj[i:i+7])
# print()


data = [m for m in dir(float) if not m.startswith("_")]
for i in range(0, len(data), 7): print(data[i:i+7])

# print("\n the Object of __obj__ : ")
# data_obj = [m for m in dir(dict) if  m.startswith("_")]
# for i in range(0, len(data_obj), 7):print(data_obj[i:i+7])
print('\033c')


num = 0.123456789012345
print(f"{num:.4f}")  # Output:

num = 0.000123456789
print(f"{num:.2e}")  # Output: 1.23e-04


long_decimal = 123.456789012345
rounded = round(long_decimal, 4)  # Round to 4 decimal places
print(rounded)  # Output: 123.4568



 

num = 0.123456789
print(f"{num:.2%}" , round(num, 4) ,  f"{num:>.3f}",sep='\t  \t')  # Output: 12.35%

import math
num = 0.123456789
ceiled = math.ceil(num);print(ceiled)
floored = math.floor(num);print(floored)


num = 1.7135660062
print(f"ceil({num}): {math.ceil(num)}")   # 2
print(f"floor({num}): {math.floor(num)}") # 1
print(f"trunc({num}): {math.trunc(num)}") # 1

num = -1.7135660062
print(f"ceil({num}): {math.ceil(num)}")   # 2
print(f"floor({num}): {math.floor(num)}") # 1
print(f"trunc({num}): {math.trunc(num)}") # 1




print('     [] / ( ) / {}   Row Data    '.center(70,'_'))
### 1. Formatting to Strings (List)
numbers = [1.23456789, 2.987654321, 0.123456789]
formatted_list = [f"{x:.2f}" for x in numbers]
print(formatted_list)  # ['1.23', '2.99', '0.12']

### 2. Rounding (Tuple)
numbers = (1.23456789, 2.987654321, 0.123456789)
rounded_tuple = tuple(round(x, 3) for x in numbers)
print(rounded_tuple)  # (1.235, 2.988, 0.123)

### 3. Applying Math Function (Set)
import math
numbers = {1.23456789, 2.987654321, 0.123456789}
ceiled_set = {math.ceil(x) for x in numbers}
print(ceiled_set)  # {2, 3, 1}

### 4. Using `map()` for Formatting

numbers = [1.23456789, 2.987654321]
formatted = list(map(lambda x: f"{x:.2f}", numbers))
print(formatted)  # ['1.23', '2.99']




### 1. Formatting Values to Strings
data = {'a': 1.23456789, 'b': 2.987654321, 'c': 0.123456789}
formatted_dict = {k: f"{v:.2f}" for k, v in data.items()}
print(formatted_dict)  # {'a': '1.23', 'b': '2.99', 'c': '0.12'}

### 2. Rounding Values
data = {'a': 1.23456789, 'b': 2.987654321, 'c': 0.123456789}
rounded_dict = {k: round(v, 3) for k, v in data.items()}
print(rounded_dict)  # {'a': 1.235, 'b': 2.988, 'c': 0.123}

### 3. Applying Math Function to Values
data = {'a': 1.23456789, 'b': 2.987654321, 'c': 0.123456789}
ceiled_dict = {k: math.ceil(v) for k, v in data.items()}
print(ceiled_dict)  # {'a': 2, 'b': 3, 'c': 1}

### 4. Using `map()` on Values
data = {'a': 1.23456789, 'b': 2.987654321}
formatted_values = dict(zip(data.keys(), map(lambda x: f"{x:.2f}", data.values())))
print(formatted_values)  # {'a': '1.23', 'b': '2.99'}


print('     [] / ( ) / {}   Mixed Data    '.center(70,'_'))
data = [1.23456789, "hello", True, 2.987654321]
processed = [round(x, 2) if isinstance(x, (int, float)) else x for x in data]
print(processed)  # [1.23, 'hello', True, 2.99]


data = (1.23456789, "world", False, 0.123456789)
processed = tuple(f"{x:.2f}" if isinstance(x, (int, float)) else str(x) for x in data)
print(processed)  # ('1.23', 'world', 'False', '0.12')


data = {1.23456789, "test", True, 2.987654321}
processed = {round(x, 2) if isinstance(x, (int, float)) else x for x in data}
print(processed)  # {1.23, 'test', True, 2.99}


data = [1.23456789, "hello", 2.987654321]
processed = []
for x in data:
    try:
        processed.append(round(x, 2))
    except TypeError:
        processed.append(x)
print(processed)  # [1.23, 'hello', 2.99]
