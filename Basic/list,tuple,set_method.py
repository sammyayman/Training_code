#%%
# data = [m for m in dir(list) if not m.startswith("_")]
# for i in range(0, len(data), 7): print(data[i:i+7])

# print("\n the Object of __obj__ : ")
# data_obj = [m for m in dir(list) if  m.startswith("_")]
# for i in range(0, len(data_obj), 7):print(data_obj[i:i+7])
# print()

# """""
# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert','pop', 'remove', 'reverse', 'sort']

#  the Object of __obj__ :
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__']
# ['__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__']
# ['__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__']
# ['__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__']
# ['__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__']
# ['__subclasshook__']


# """
#%%
print("\033[2J\033[H")
mylist = list("Ayman2030@gmail.")
print("Original list:", mylist)
print("\n" + "="*70)

# Methods that don't require arguments
methods_no_args = ['sort', 'reverse', 'clear', 'copy']

print("\nMethods with NO arguments:".center(70, "-"))
for method in methods_no_args:
    mylist_copy = mylist.copy()
    print(f"\n{method}():")
    print(f"  Before: {mylist_copy}")
    result = getattr(mylist_copy, method)()
    print(f"  After:  {mylist_copy}")
    if result is not None:
        print(f"  Return: {result}")

print("\n" + "="*70)

# Methods that require arguments
methods_with_args = {
    'append': '!',
    'count': 'a',
    'index': 'y',
    'insert': (0, 'X'),
    'remove': '@',
    'pop' : 5,
    'extend': ['.', '.', '.']
}
print("\n","Methods WITH arguments:".center(70, "-"))
for method, value in methods_with_args.items():
    mylist_copy = mylist.copy()
    print(f"\n{method}({value}):")
    print(f"  Before: {mylist_copy}")
    try:
        if isinstance(value, tuple):
            result = getattr(mylist_copy, method)(*value)
        else:
            result = getattr(mylist_copy, method)(value)
        
        # If returns a number, don't show list changes
        if isinstance(result, int):
            print(f"  Return: {result}")
        else:
            print(f"  After:  {mylist_copy}")
            if result is not None:
                print(f"  Return: {result}")
    except Exception as e:
        print(f"  Error: {e}")
 
print('\033c')

#%%
l_1 = [i for i in range(1, 51,8)]
l_2 = [i/2 for i in range(0, 20,3)]  # Fixed: range() only accepts integers, so we use list comprehension with division
string = "AymanSiraj2030"
lst_str = list(string.lower())  # Convert string to list of characters
print(lst_str)  # Output: ['A', 'y', 'm', 'a
print(len(l_1) , len(l_2))



print("\n1️⃣\t Unpacking lists (Very powerful)")
a, b, c = [10, 20, 30] 
print(a, b, c)


print("Using * (catch the rest)")
first, *middle, last = l_2
print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5



print("\n2️⃣   Remove duplicates while keeping order")
unique1 = list(dict.fromkeys(lst_str))
print(unique1)
#OR : 
unique2 = list(set(lst_str))
#OR
unique3 = [x for i, x in enumerate(lst_str) if x not in lst_str[:i]]

unique = []
for item in lst_str:
    if item not in unique:
        unique.append(item) 

print(sorted(unique2) == sorted(unique1) == sorted(unique3))

print("\n 3 Reversing")
lst_str.reverse()
print(lst_str)
print(list(reversed(lst_str)) == lst_str[::-1]  )

# print(nums[::-1])



print('\n4️⃣    Flatten a 2D list')
matrix = [[1, 'a'], [3, 'c'], [5, 'f']]

flat0 = []
for row in matrix:
    for item in row:
        flat0.append(item)
flat1 = [x for row in matrix for x in row]
flat2 = sum(matrix, [])
flat3 = [item for row in matrix for item in row]

print(flat0, flat0 == flat1 == flat2 == flat3)



print('\n5️⃣    List comprehension with condition')
l_2.extend([2,150])
nums = l_2
evens = [n for n in nums if n % 2 == 0]
labels = ["even" if n % 2 == 0 else "odd" for n in nums] ; print(evens ,'\n' ,labels)
#OR : 
EVENS = list(filter(lambda n: n % 2 == 0, nums))
LABELS = list(map(lambda n: "even" if n % 2 == 0 else "odd", nums))
print(evens == EVENS , labels == LABELS)

first_even_index = next((i for i, n in enumerate(nums) if n % 2 == 0), -1)
print(first_even_index)



print('\n 6️⃣   Swap values using lists')
a, b = 5, 10
a, b = b, a


print('\n7️⃣    Copy list correctly (avoid bugs!)')
b = nums.copy()
# or
b = nums[:]



print("\n 8️⃣   Find index safely")

items = lst_str

if "n" in items:
    index = items.index('n')
    print(f"Found at index: {index}")
else:
    print("Element not found")
#OR :
print(items.index('x') if 'x' in items else 'no item found')

index = next((i for i, x in enumerate(items) if x == '0'), -1)
print(f"Found at index: {index}" if index != -1 else "Element not found")

#OR : 
# Using lambda with filter
indices = list(filter(lambda i: items[i] == '2', range(len(items))))
idx = indices
print(idx[0] == index)

 

print("\n9️⃣   Rotate a list : :", end= '  ')
nums = [1, 2, 3, 4, 5]

# rotate right by 2
k = 2
rotated = nums[-k:] + nums[:-k]
print( nums[-k:] , ' + ' , nums[:-k] , ' = ' , rotated )




print('\n🔟     Zip lists together :',end = ' ')
names = ["Ali", "Sara", "Omar"]
scores = [90, 85, 88]

Z = list(zip(names, scores))
r1 = []
for name, score in Z :
    r1.append(f'{name}: {score} points')
print(r1)

r2 = [f"{name}: {score} points" for name, score in Z]

r3 = list(map(lambda ns: f"{ns[0]}: {ns[1]} points", Z))

print(r3 == r2 == r3)



print("\n1️⃣ 1️⃣ Enumerate instead of index :",end= ' ')
items = ["pen", "book", "bag"]
index0 = []
for i, item in enumerate(items, start=1):
    index0.append(f'{i}: {item}')
print(index0)

index1 = [f'{i}: {item}' for i, item in enumerate(items, 1)]

index2 = list(map(lambda pair: f'{pair[0]}: {pair[1]}', enumerate(items, 1)))

print(index0 == index1 == index2)


print('\n1️⃣ 2️⃣  Any / All tricks')
nums = [2, 4, 6, 8]
e = [n % 2 == 0 for n in nums]
o = [n % 2 != 0 for n in nums]
all_even = all(e)
any_odd  = any(o)
print(all_even , any_odd)


print('\n1️⃣ 3️⃣  Nested list trick (⚠ common mistake)',end=' ')
matrix = [['']*3 for _ in range(3)]
print(matrix)


print('\n1️⃣ 4️⃣ Count items easily',end= ' ')
from collections import Counter

nums = [1, 2, 2, 3, 3, 3]
count = Counter(nums)
print(count)



print('\n1️⃣ 5️⃣ Sort with a key (very useful!)',end = ' ')
data = [(1, 3), (4, 1), (2, 2)]
data.sort(key=lambda x: x[0])
print(data)






print('\033c')
print(' Exercise on list '.center(100,' '))

print('1 - ')
a , b  = [1, 2, 3] , [2, 6, 9]

def cal(n):
    
    if  n == '+' :
        result = [x + y for x, y in zip(a, b)]
        result_ = list(map(lambda p: p[0] + p[1],zip(a,b)))
        print('[+]',result == result_, end= ' ')
        #      = list(filter(lambda )) 
        return result
    elif n == '-' :
        result = [x - y for x, y in zip(a, b)]
        result_ = list(map(lambda p: p[0] - p[1],zip(a,b)))
        print('[-]',result == result_, end = ' ')
        return result
    elif n == '*' :
        result = [x *y for x, y in zip(a, b)]
        result_ = list(map(lambda p: p[0] * p[1],zip(a,b)))
        print('[*]',result == result_)
        return result
    elif n == '/':
        result = [x / y for x, y in zip(a, b)]
        result_ = list(map(lambda p: p[0] / p[1],zip(a,b)))
        c = f"'[/]'{result == result_}"
        
        return result ,c

add = cal('+') ; sub = cal('-') ; mul = cal('*') 
d , c = cal('/'); print(c)
div = [round(n,2) for n in d] # result = list(map(lambda n: round(n, 2), nums))
# div_map =  list(map(lambda n: round(n,2),d)) ; print(div == div_map , c)
print([round(n,2) for n in d]  ==  list(map(lambda n: round(n, 2),  d)) )
print(f'{add} + {mul} = {add + mul} ,\
      \n{sub} + {div}  = {sub + div}')
print()


numbers =sub + div
i = []; f = []
for n in numbers: 
    if type(n).__name__ == 'int' :
        i.append(n)
    elif type(n).__name__ == 'float' : 
        f.append(n)
# print(i , f)

# i = list(filter(lambda n: isinstance(n, int), numbers))
# f = list(filter(lambda n: isinstance(n, float), numbers))
i, f = [list(filter(lambda x: isinstance(x, t ), numbers)) for t in (int, float)]

print(i, f)

    
        
        
print('\n 2 - : ')
data = [
    10,                     # int
    3.14,                   # float
    2 + 5j,                 # complex
    True,                   # bool
    "Python",               # str
    None,                   # NoneType
    [1, 2, 3],              # list
    (4, 5, 6),              # tuple
    {7, 8, 9},              # set
    {"a": 1, "b": 2},       # dict
    range(5),               # range
    b"ABC",                 # bytes
    bytearray(b"XYZ"),     # bytearray
    frozenset({1, 2, 3}),   # frozenset
    lambda x: x**2          # function
]
for i,item in enumerate (data,start = 1):
        print(f'{i:>6}-{item}', end = '\n'if i % 2 == 0 else " ")
          
print('\n')  
for i, item in enumerate(data, start=1):
    print(f"{i:>2}:{type(item).__name__:<10}", end="\n" if i % 4 == 0 else '  ')
    
print('\n')
types = list(map(lambda x: type(x).__name__, data))
for i, t in enumerate(map(lambda x: type(x).__name__, data), 1):
    print(f"({i}) {t:<12}", end="\n" if i % 5 == 0 else " ")
    
 


print('\n 3 - : ')

text = 'samiayman2030@gmail.com'

chars, digits = [], []
smb = []
for c in text:
    if c.isalpha():
        chars.append(c)
    elif c.isdigit():
        c = int(c)
        digits.append(c)
    else : 
        smb.append(c)


#OR : 
ch = list(filter(str.isalpha, text))
dig = list(map(int, filter(lambda x: x.isdigit(), text)))
symbols = [c for c in text if not c.isalnum()]


print(chars , ch == chars)
print(digits , dig == digits)
print(smb , symbols == smb)

print("\nTo turn back from list to string : ")
dig = list(map(str , digits))
print(TEXT := ch + dig + smb ,"----->" ,"".join(TEXT))
 

print('\n4 - : ')
data = TEXT

count_a = data.count('a')

first_pos = data.index('m')
print(f"First position of 'm' is in index {first_pos}")

positions = [str(i) for i, v in enumerate(data) if v == 'a']
print( f"There're {count_a} of 'a' located in index :",','.join(positions))

#OR
positions_ = list(
    map(lambda x: str(x[0]),
        filter(lambda x: x[1] == 'a', enumerate(data)))
)

print(positions == positions_)
print("Count:", len(positions))

#OR : 
def locate(lst, target):
    pos = [i for i, v in enumerate(lst) if v == target]
    return pos, len(pos)

positions, count = locate(data, 'm')
print(positions, count)



print('\n5 - : ')
index_m = None
for i, v in enumerate(data):
    if v == 'm':
        index_m = i


print(index_m)
#OR
#OR
lengnth = len(data)-1 ; sort_re= data[::-1] ; index_re = sort_re.index('m')
print(f"Last index = {lengnth} - {index_re} = ",lengnth-index_re == index_m)
index_m = max([i for i, v in enumerate(data) if v == 'm'])
index_m = next((i for i, v in reversed(list(enumerate(data))) if v == 'm'), None)



print("\n6 - : ")
duplicates = []

for x in data:
    if data.count(x) > 1 and x not in duplicates:
        duplicates.append(x)

print(duplicates.sort() )
D = list({x for x in data if data.count(x) > 1})
print(D.sort() == duplicates.sort())



print("\n7 - : ")

from collections import defaultdict

# positions = defaultdict(list) ; print(positions)
print(positions := defaultdict(list))

for i, v in enumerate(data):
    positions[v].append(i)

duplicates = {k: v for k, v in positions.items() if len(v) > 1}

print(duplicates)


#OR :  
positions = {}
for i, v in enumerate(data):
    if v not in positions:
        positions[v] = []
    positions[v].append(i)
# OR : 
pos = {v: [i for i, x in enumerate(data) if x == v] for v in data}
print(pos ==  positions)

# duplicates = {k: v for k, v in positions.items() if len(v) > 1}
print(dup :=  {k: v for k, v in positions.items() if len(v) > 1})

#OR : 
positions = {}
for i, v in enumerate(data):
    positions.setdefault(v, []).append(i)
print(positions)
#OR: 
pos = {}; [pos.setdefault(v, []).append(i) for i, v in enumerate(data)]
print(pos == positions )

duplicates = {k: v for k, v in positions.items() if len(v) > 1}


#OR :
# unique_vals = list(set(data))
# positions = dict(map(lambda v: (v, list(filter(lambda i: data[i] == v, range(len(data))))), unique_vals))

# duplicates = dict(filter(lambda item: len(item[1]) > 1, positions.items()))


unique_vals = list(set(data)) ; r = range(len(data))
f =   lambda v : list(filter(lambda i: data[i] == v, r))
m = map(lambda v: (v, f(v)), unique_vals)
pos = dict(m)
print(pos == positions )
duplicates = dict(filter(lambda item: len(item[1]) > 1, positions.items()))



unique_vals = list(set(data))
r = range(len(data))

def match_index(i, v):
    return data[i] == v

def indexes_of(v):
    return list(filter(lambda i: match_index(i, v), r))

def make_pair(v):
    return (v, indexes_of(v))

pos = dict(map(make_pair, unique_vals))

print(pos == positions)





 




# # %%
# print("All method of Function in tuple (tuple) :")
# data = [m for m in dir(tuple) if not m.startswith("_")]
# for i in range(0, len(data), 7): print(data[i:i+7])

# print("\n the Object of __obj__ : ")
# data_obj = [m for m in dir(tuple) if  m.startswith("_")]
# for i in range(0, len(data_obj), 7):print(data_obj[i:i+7])
# print()

# """ 
# ['count', 'index']
#  the Object of __obj__ :
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__']
# ['__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__']
# ['__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__']
# ['__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__']
# ['__setattr__', '__sizeof__', '__str__', '__subclasshook__']

# """

# # Practical examples with tuple methods
# mytuple = tuple("Ayman2030")
# print("Original tuple:", mytuple)
# print("\n" + "="*70)

# # Tuple methods that require arguments
# tuple_methods_with_args = {
#     'count': 'a',
#     'index': 'y'
# }

# print("\nTuple Methods WITH arguments:".center(70, "-"))
# for method, value in tuple_methods_with_args.items():
#     mytuple_copy = mytuple
#     print(f"\n{method}('{value}'):")
#     print(f"  Tuple: {mytuple_copy}")
#     try:
#         result = getattr(mytuple_copy, method)(value)
#         print(f"  Return: {result}")
#     except Exception as e:
#         print(f"  Error: {e}")

# print("\n" + "="*70)







# print("✅ 1. Swapping values without a temporary variable")
# a, b = 5, 10
# a, b = b, a
# print(a, b)  # 10 5


# print('✅ 2. Tuple unpacking')

# t = (1, 2, 3)
# a, b, c = t
# print(a, b, c)  # 1 2 3


# print("✅ 3. Unpack with * (catch remaining values)")

# t = (1, 2, 3, 4, 5)
# a, b, *rest = t
# print(a, b, rest)  # 1 2 [3, 4, 5]


# print('✅ 4. Swap multiple variable')

# a, b, c = 1, 2, 3
# a, b, c = c, a, b
# print(a, b, c)  # 3 1 2


# print('✅ 5. Use tuples as dictionary keys')

# d = {}
# d[(1, 2)] = "value"
# print(d[(1, 2)])  # value

# print("✅ 6. Tuple slicing")

# t = (1, 2, 3, 4, 5)
# print(t[1:4])  # (2, 3, 4)



# print('✅ 7. Convert list to tuple and vice versa')
# l = [1, 2, 3]
# t = tuple(l)
# print(t)  # (1, 2, 3)

# l2 = list(t)
# print(l2)  # [1, 2, 3]

# print('✅ 8. Tuple in for loop')
# t = (10, 20, 30)
# for x in t:
#     print(x)



# print('✅ 9. zip() returns tuples')
# names = ("Ayman", "Sammy", "John")
# scores = (90, 85, 88)

# z = zip(names, scores)
# print(tuple(z))
# # (('Ayman', 90), ('Sammy', 85), ('John', 88))


# print('✅ 10. min, max, sum')
# t = (10, 5, 20)
# print(min(t))  # 5
# print(max(t))  # 20
# print(sum(t))  # 35


# print('✅ 11. Using tuple in functions (return multiple values)')
# def stats(x, y):
#     return x+y, x-y, x*y

# result = stats(5, 2)
# print(result)        # (7, 3, 10)
# a, b, c = result
# print(a, b, c)       # 7 3 10

# print('✅ 12. Check if value exists')
# t = (1, 2, 3)
# print(2 in t)  # True



# print('✅ 13. Immutable but you can replace using conversion')
# t = (1, 2, 3)
# l = list(t)
# l[0] = 10
# t = tuple(l)
# print(t)  # (10, 2, 3)



# print('🔥 Bonus Trick: Tuple + List for Fast Swapping')
# t = (1, 2, 3)
# t = (t[2], t[0], t[1])
# print(t)  # (3, 1, 2)














# class Unprintable:
#     pass  # No __str__ or __repr__ defined properly

# t = ("hello", Unprintable(), 42)

# # print(f"t[0]: {t[0]}, t[2]: {t[2]}")


# for i, item in enumerate(t):
#     try:
#         print(f"t[{i}]: {item}")
#     except Exception as e:
#         print(f"t[{i}]: <not printable - {type(item).__name__}>")
        
# # print(f"Printable: {[str(item) for item in [t[0], t[2]]]}")
# # Example tuple with a non-printable element at index 1
# t = ("hello", lambda x: x + 1, 42)

 

# # Option 3: Use repr() or str() which works on most objects
# print(f"t[0]: {t[0]}, t[1]: {repr(t[1])}, t[2]: {t[2]}")
# # Output: t[0]: hello, t[1]: <function <lambda> at 0x...>, t[2]: 42

# # Option 4: Handle with try-except
# for i, item in enumerate(t):
#     try:
#         print(f"t[{i}]: {item}")
#     except Exception as e:
#         print(f"t[{i}]: <unprintable - {type(item).__name__}>")

# # Option 5: Check if element is printable before printing
# for i, item in enumerate(t):
#     if isinstance(item, (str, int, float, bool)):
#         print(f"t[{i}]: {item}")
#     else:
#         print(f"t[{i}]: <{type(item).__name__} object>")
        
        
        
        
# t = (x := 10, 20, 30)
# print(t)   # (10, 20, 30)
# print(x)   # 10

# t = (x := 5 + 3, 2*x, 3*x)
# print(t)   # (8, 16, 24)

# t = (x := int(input("Enter a number: ")), x+1, x+2)
# print(t)


# numbers = [1, 2, 3]
# t = tuple(x := n for n in numbers)
# print(t)  # (1, 2, 3)


# numbers = [1, 2, 3, 4, 5, 6]

# t = tuple(x := n for n in numbers if (x := n) % 2 == 0)
# print(t)  # (2, 4, 6)


# numbers = [1, 2, 3, 4]

# t = tuple((x := n, x**2) for n in numbers)
# print(t)
# # ((1, 1), (2, 4), (3, 9), (4, 16))

# numbers = [1, 2, 3, 4]

# t = tuple((s := (s if 's' in globals() else 0) + n) for n in numbers)
# print(t)  # (1, 3, 6, 10)

# import random

# numbers = [random.randint(1, 20) for _ in range(10)]

# t = tuple(x := n for n in numbers if (x := n) > 10)
# print(numbers)
# print(t)











#%%
# print("All method of Function in set (set) :")
# data = [m for m in dir(set) if not m.startswith("_")]
# for i in range(0, len(data), 7): print(data[i:i+7])

# print("\n the Object of __obj__ : ")
# data_obj = [m for m in dir(set) if  m.startswith("_")]
# for i in range(0, len(data_obj), 7):print(data_obj[i:i+7])
# print()
# Practical examples with set methods
# myset = set("Ayman2030")
# print("Original set:", myset)
# print("\n" + "="*70)

# # Methods that don't require arguments
# set_methods_no_args = ['clear', 'copy', 'pop']

# print("\nSet Methods with NO arguments:".center(70, "-"))
# for method in set_methods_no_args:
#     myset_copy = myset.copy()
#     print(f"\n{method}():")
#     print(f"  Before: {myset_copy}")
#     result = getattr(myset_copy, method)()
#     print(f"  After:  {myset_copy}")
#     if result is not None:
#         print(f"  Return: {result}")

# print("\n" + "="*70)

# # Methods that require arguments
# set_methods_with_args = {
#     'add': '!',
#     'discard': 'A',
#     'remove': 'y',
#     'difference': {'2', '0', '3'},
#     'difference_update': {'2', '0'},
#     'intersection': {'A', 'y', 'm'},
#     'intersection_update': {'A', 'y', 'm', '2'},
#     'isdisjoint': {'x', 'z'},
#     'issubset': {'A', 'y', 'm', 'a', 'n', '2', '0', '3'},
#     'issuperset': {'A'},
#     'symmetric_difference': {'A', 'x', 'y'},
#     'symmetric_difference_update': {'A', 'x'},
#     'union': {'x', 'y', 'z'},
#     'update': ['@', '#']
# }
# print("\nSet Methods WITH arguments:".center(70, "-"))
# for method, value in set_methods_with_args.items():
#     myset_copy = myset.copy()
#     print(f"\n{method}({value}):")
#     print(f"  Before: {myset_copy}")
#     try:
#         result = getattr(myset_copy, method)(value)
        
#         # If returns a value, show it
#         if result is not None:
#             if isinstance(result, (set, bool)):
#                 print(f"  Return: {result}")
#             else:
#                 print(f"  After:  {myset_copy}")
#                 print(f"  Return: {result}")
#         else:
#             print(f"  After:  {myset_copy}")
#     except Exception as e:
#         print(f"  Error: {e}")

# print("\n" + "="*70)

# """  
# ['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection','intersection_update', 'isdisjoint', 
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference','symmetric_difference_update', 'union', 'update']



# the Object of __obj__ :
# ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__']
# ['__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__']
# ['__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__']
# ['__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__']
# ['__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__']
# ['__str__', '__sub__', '__subclasshook__', '__xor__']


# """
# print('1 Remove duplicates  instantly')
# nums = [1, 2, 2, 5,3, 4, 4]
# unique = set(nums)
# print(unique)

# print('2 Fast membership test (🔥)')
# items = {1, 2, 3, 4, 5}

# print(3 in items)   # O(1)


# print('3 Union, Intersection, Difference')
# A = {1, 2, 3}
# B = {3, 4, 5}

# print(f"""{A | B}    # union
# {A & B }   # intersection
# {A - B}    # difference
# {A ^ B }   # symmetric difference """)


# print('4 Remove duplicates between two lists')
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# unique = list(set(list1) - set(list2))
# print(unique)


# print("5 Check subset & superset")
# A = {1, 2}
# B = {1, 2, 3, 4}

# print(A.issubset(B)  ,B.issuperset(A) )  # True
# #OR
# print(A <= B , B >= A)


# print('6 Set comprehension')
# squares = {x*x for x in range(1, 10)}
# print('squares:', squares)   

# evens = {x for x in squares if x % 2 == 0}
# print('evens:', evens)  

# primes = {x for x in range(2, 20) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))}
# print(primes) 

# print('7 Remove items safely')
# s= set(range(1,7))
# print(s)
# s.remove(2)     # error if missing
# s.discard(5)    # safe (no error)
# print(s)

# print('8 Pop random element')
# s = {10, 20, 30}
# x = s.pop()

# print('9 Freeze a set (immutable)')
# a = frozenset([1, 2, 3])

# print('10 Find common elements across many lists')
# lists = [
#     [1, 2, 3],
#     [2, 3, 4],
#     [2, 5, 3]
# ]

# common = set(lists[0]).intersection(*lists[1:])
# print(common)

# print('11  Check if all elements are unique')
# items = [1, 2, 3, 4]
# is_unique = len(items) == len(set(items))


# print("12 Convert set back to sorted list")
# nums = {5, 3, 1, 4}
# sorted_nums = sorted(nums)
# print(sorted_nums)

