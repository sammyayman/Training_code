# # import os
# # os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# # os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# # from tensorflow.python.autograph.pyct.anno import keys
# data = [m for m in dir(dict) if not m.startswith("_")]
# for i in range(0, len(data), 7): print(data[i:i+7])

# # print("\n the Object of __obj__ : ")
# # data_obj = [m for m in dir(dict) if  m.startswith("_")]
# # for i in range(0, len(data_obj), 7):print(data_obj[i:i+7])
# # print()


print("\033c")

emoji_dict = {
    "fruits": {
        "apple": "🍎",
        "banana": "🍌",
        "grapes": "🍇",
        "orange": "🍊",
        "lemon": "🍋",
        "watermelon": "🍉",
        "strawberry": "🍓"
    },
    "geometric_shapes_hollow": {
        "circle": "◯",
        "square": "□",
        "rectangle": '▱',
        "triangle_up": "△",
        "triangle_down": "▽",
        "diamond": "◇"
    },
    "colors": {
        "red": "🔴",
        "orange": "🟠",
        "yellow": "🟡",
        "green": "🟢",
        "blue": "🔵",
        "purple": "🟣",
        "brown": "🟤"
    }
}
fruits = emoji_dict["fruits"]
shapes = emoji_dict["geometric_shapes_hollow"]
colors = emoji_dict["colors"]
# print(fruits)
# print(shapes)
# print(colors)

dict_data = {
    'list': list(range(1, 12, 3)),
    'tuple': tuple(i / 2 for i in range(1, 50, 15)),
    'set': set(i * 3 for i in range(1, 20, 5))
}
# # print(dict_data)
# print(colors)  # dict.get(key) ---->value
# print(f"get('red'): {colors.get('red')}")
# print(f"get('greeb'): {colors.get('green')}")
# print(f"get('blue'): {colors.get('blue')}")
# print(f"get('black'): {colors.get('black')}")
# pairs = zip(['R', 'B', 'G'], [colors.get('red'),
#             colors.get('blue'), colors.get('green')])
# print({k: v for k, v in pairs})


# print("\n11. values() - Get all values")
# print(f"Dictionary: {fruits}")
# print(f"values(): {fruits.values()}")
# print(f"List of values: {list(fruits.values())}")
# pairs = zip(['APPLE', 'BANANA', 'GRAPE'], list(fruits.values())[:3])
# print({k: v for k, v in pairs})


# # 6. keys() - Returns view of all keys
# print("\n6. keys() - Get all keys")
# print(f"keys(): {dict_data.keys()}")
# print(f"List of keys: {list(dict_data.keys())}")
# pair = zip(list(dict_data.keys()), [
#            ['a', 'b', 'c'], (1, 2, 3), {True, False, None}])
# print({k: v for k, v in pair})


# # 5. items() - Returns view of (key, value) pairs
# print("\n5. items() - Get key-value pairs")
# print(f"Dictionary: {shapes}")
# print(f"items():\n {list(shapes.items())}")
# print("Iterating over items:")
# for key, value in shapes.items():
#     print(tuple([key, value]), end='\t')
# print()


# # 2. copy() - Returns a shallow copy of the dictionary
# print("\n2. copy() - Create a shallow copy")
# data_copy = dict_data.copy()
# print(f"Original: {dict_data}")
# print(f"Copy: data_copy {data_copy}")


# # 10. update() - Updates dictionary with key-value pairs from another dict or iterable
# print("\n10. update() - Merge/update dictionaries\n")
# print(f"Original: {data_copy}")
# data_copy.update(
#     {'list': list(fruits.values())[:3],
#      'tuple': tuple(list(fruits.values())[3:])}
# )
# print(f"After update : {data_copy}")


# # data_copy.clear()
# print((f"After clear(): {data_copy}"))
# data_copy.update([('set', set(list(colors.values())[:4])),
#                   ('marker', '+')])
# print(f"After new update : {data_copy}")
# data_copy.update(x=[1, 6], y=[7, 10], color='r', fontsize=50)
# print(f"\nAfter update: {data_copy}")


# # 3. fromkeys() - Creates a new dictionary with keys from a sequence
# print("\n3. fromkeys() - Create dict from keys")
# keys = list(data_copy.keys())[0:3]
# d3 = dict.fromkeys(keys)
# print(f"fromkeys(keys): {d3}")
# d3_with_value = dict.fromkeys(keys, 3.14)
# print(f"fromkeys(keys, 0): {d3_with_value}")
# print(data_copy.fromkeys(keys), data_fk := data_copy.fromkeys(keys, []))
# print()


# # 9. setdefault() - Returns value if key exists, else sets key with default value
# print("\n9. setdefault() - Get or set default")
# print(f"Dictionary: {data_fk}")
# print(f"setdefault('a', 100): {data_fk.setdefault('set', [100, 200])}")
# print(f"Dictionary after: {data_fk}")
# print(f"setdefault('c', 3): {data_fk.setdefault('list_2', 3)}")
# print(f"Dictionary after: {data_fk}")


# print('\n'," Dict.update vs Dict.setdefault".center(100,'='))
# astormology = {"sun": "☀️", "moon": "🌙", "star": "⭐"}
# # update overwrites
# astormology.update({"moon": "🌚", "galaxy": "🌌"})
# print(astormology)
# astormology.setdefault("comet", "☄️")
# astormology.setdefault("moon", "🌙")  # won't overwrite 🌚
# print(astormology)

print()
# 7. pop() - Removes and returns value for key
print("\n7. pop() - Remove and return value")
d7 = fruits
print(f"Before: {d7}")
value = d7.pop('orange','ban')
print(f"pop('y') returned: {value}")
print(f"After: {d7}")
# With default value if key doesn't exist
value = d7.pop('w', 'not found')
print(f"pop('w', 'not found'): {value}")

# 8. popitem() - Removes and returns last (key, value) pair (LIFO in Python 3.7+)
print("\n8. popitem() - Remove and return last item")
d8 = dict_data
print(f"Before: {d8}")
item = d8.popitem()
print(f"popitem() returned: {item} \nAfter: {d8}")


# #%%
 

# d = {"fire": "🔥",
#      "water": "💧",
#      "stone": "⛰️",
#      "lightning": "⚡"}

# base = d.copy()

# method_names = [
#     'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'values','pop',
#     'popitem', 'setdefault', 'update'
# ]

# print("Testing dict methods with getattr".center(100, "-") )
# for name in method_names:
#     print(f"\nMethod: {name}")

#     d = base.copy()
#     print("  before:", d)

#     meth = getattr(d, name, None)
#     if not callable(meth):
#         print("  -> not found as a callable on dict")
#         continue
#     else:
#         print(f"{name:10} -> METHOD on dict (use d.{name}(...))")

#     result = None

#     if name == 'clear':
#         meth()
#     elif name == 'copy':
#         result = meth()
#     elif name == 'fromkeys':
#         result = meth(['x', 'y'], 0)
#     elif name == 'get':
#         result = meth('fire', '❓')
#     elif name in ('items', 'keys', 'values'):  # ✅ fix: use 'in' for multiple values
#         result = list(meth())
#     elif name == 'pop':
#         result = meth('water', None)
#     elif name == 'popitem':
#         result = meth()
#     elif name == 'setdefault':
#         result = meth('wind', '🌪️')
#     elif name == 'update':
#         meth({'wind': '🌪️'})

#     if result is not None:
#         print("  result:", result)
#     print(f"  after : {d}")











# #%%
# print("  Tricks of example from ChatGPT  ".center(100,'='))
# print("\n1 Create dictionaries smartly")
# keys = ["a", "b", "c"]
# values = [1, 2, 3]
# d = dict(zip(keys, values))
# print(d)

# print('\n2 Dictionary comprehension')
# squares = {x: x*x for x in range(1, 6)}
# evens = {x: x for x in squares if x % 2 == 0}
# print(evens)


# print('\n3 Swap keys and values')
# d = {"a": 1, "b": 2}
# swapped = {v: k for k, v in d.items()}
# print(swapped)


# print("\n4 Safely get values (get)")
# user = {"name": "Ali"}
# print(user.get("age", 10))
# print(user)

# data = {"a": 10, "b": 20}

# print(data.get("a"))        # 10
# print(data.get("c"))     # 0 (default)


# print('\n5 Set default values (setdefault)')
# counts = {}

# for x in ["a", "b", "a"]:
#     counts.setdefault(x, 0)
#     counts[x] += 1
# print(counts)

# print("\n7 Merge dictionaries (3 ways)")
# a = {"x": 1}
# b = {"y": 2}

# print(a | b , {**a,**b} , a.update(b))

# print('\n8 Remove keys safely')
# value = d.pop("a", None)
# print(d)


# print("\n9 Sort dictionary by value")
# scores = {"Ali": 90, "Sara": 85, "Omar": 95}

# sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1]))
# print(sorted_scores)

# scores = {"A": 90, "B": 70, "C": 85}

# sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1]))
# print(sorted_scores)


# print("\n10  Group data by key (very useful!)")
# from collections import defaultdict

# students = [("A", 90), ("B", 85), ("A", 95)]

# group = defaultdict(list)

# for name, score in students:
#     group[name].append(score)

# print(group)


# print('\n11 Dictionary as a switch-case')
# def add(x, y): return x + y
# def sub(x, y): return x - y

# ops = {
#     "+": add,
#     "-": sub
# }

# print(ops["+"](5, 3) , ops["-"](5, 3))

# print('12 Nested dictionary access safely')
# data = {"user": {"profile": {"name": "Ali"}}}

# name = data.get("user", {}).get("profile", {}).get("name")
# print(data,name)


# print("\n13 Immutable keys rule")
# print({(1, 2): "point"})
# grid = {}
# grid[(0, 1)] = "player"

# print(grid[(0, 1)])

# print("\n14 Dictionary vs if-elif chain")
# actions = {1: "one", 2: "two"}
# print(actions.get(x, "unknown"))

# print("\n15 ount items easily")
# text = "banana"

# count = {}
# for ch in text:
#     count[ch] = count.get(ch, 0) + 1

# print(count)
# # {'b': 1, 'a': 3, 'n': 2}

# print("\n16. Walrus operator with dictionary")
# numbers = [1, 2, 3, 4, 5]

# d = {n: (s := n*n) for n in numbers}
# print(d)


# print('\n',"Some Example of Dictionary".center(100,'-'))

# data = {"name": "Ayman", \
#         "age": 20, \
#         "city": "Cairo"}
# """OR:
#     data = {
#     "name": "Ayman",
#     "age": 20,
#     "city": "Cairo"
# }


# """

# print(data)

# print("\ndict.fromkeys()")
# keys = ["a", "b", "c"]
# d = dict.fromkeys(keys, 0)

# print(d)
# # {'a': 0, 'b': 0, 'c': 0}
# d = dict.fromkeys(keys, [])
# d["a"].append(1)
# print(d)
# # {'a': [1], 'b': [1], 'c': [1]}


# d ={i * 10: word
#  for i, word in enumerate(['twenty', 'thirty', 'forty'], start=2)
# }
# print(d)
# seats = ["", "Student A", "Student B", ..., "Student Z", "TA 1", "TA 2"]

# seat_map = {i: label for i, label in enumerate(seats) if i >= 1}
# print(seat_map)


# abbreviations = ["", "Jan", "Feb", "Mar", ..., "Dec"]  # First item is empty

# # Now:
# # i=0 → "" (skipped by if i>=1)
# # i=1 → 1: "Jan" ✅
# result = {i: abbr for i, abbr in enumerate(abbreviations) if i >= 1}
# print(result)
# # Output: {1: 'Jan', 2: 'Feb', ..., 12: 'Dec'}  👍

# words = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

# # Now:
# # i=0 → '' (skipped by if i>=2)
# # i=1 → '' (skipped)
# # i=2 → 20: 'twenty' ✅
# result = {i*10: word for i, word in enumerate(words) if i >= 2}
# print(result)
# # Output: {20: 'twenty', 30: 'thirty', ..., 90: 'ninety'}  👍


# print(" \n                           Dictionary wnith **                 \n".center(200,'-'))
# print("Ex 1 :")
# def func(a, b, c):
#     return a + b + c

# params = {'a': 1, 'b': 2, 'c': 3}
# result = func(**params)
# print(result)

# print("\nEx 2 :")

# defaults = {'name': 'Unknown', 'age': 0}
# user = {'name': 'Alice', **defaults}
# print(user)  # {'name': 'Alice', 'age': 0}

# print("\nEx 3 :")

# config = {'db': {'host': 'localhost', 'port': 5432}}
# settings = {**config['db'], 'timeout': 30}
# print(settings)

# print("\nEx 4 :")

# def process(name, age, city):
#     return f"{name} is {age} years old from {city}"

# people = [{'name': 'Alice', 'age': 25, 'city': 'NYC'}, {'name': 'Bob', 'age': 30, 'city': 'LA'}]

# for i, person in enumerate(people):
#     result = process(**person)
#     print(f"Person {i}: {result}")

# print("\nEx 5 :")

# # 4. Creating a copy with modifications
# original = {'x': 10, 'y': 20}
# modified = {**original, 'z': 30, 'x': 15}
# print(modified)  # {'x': 15, 'y': 20, 'z': 30}

# print("\nEx 6 :")

# # 5. Combining multiple dictionaries
# defaults = {'theme': 'dark', 'lang': 'en'}
# user_prefs = {'lang': 'fr'}
# config = {**defaults, **user_prefs, 'version': '1.0'}
# print(config)  # {'theme': 'dark', 'lang': 'fr', 'version': '1.0'}


# # 1. Using ** with enumerate to create a dictionary
# # greek = ['alpha', 'beta', 'gamma']

# print("\nEx 7 :")

# # More practical: starting index at 1
# G = {i: name for i, name in enumerate(['alpha', 'beta', 'gamma'], start=1)}
# print(G)

# print("\nEx 8 :")

# # 2. Using ** with zip to create a dictionary
# keys = ['name', 'age', 'city']
# values = ['Alice', 30, 'NYC']
# person = {**dict(zip(keys, values))}
# print(person)  # {'name': 'Alice', 'age': 30, 'city': 'NYC'}


# print("\nEx 9 :")

# # 3. Merging multiple zipped dictionaries
# keys1 = ['a', 'b']
# values1 = [1, 2]
# keys2 = ['c', 'd']
# values2 = [3, 4]

# combined = {**dict(zip(keys1, values1)), **dict(zip(keys2, values2))}
# print(combined)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# print("\nEx 10 :")

# # 4. Combining enumerate with zip
# names = ['Alice', 'Bob', 'Charlie']
# scores = [95, 87, 92]

# # Create dictionary with enumerated keys
# student_data = {**{i: (name, score) for i, (name, score) in enumerate(zip(names, scores))}}
# print(student_data)  # {0: ('Alice', 95), 1: ('Bob', 87), 2: ('Charlie', 92)}

# print("\nEx 11 :")

# # 5. Using ** to merge dictionaries created from enumerate
# list1 = ['x', 'y', 'z']
# list2 = ['p', 'q', 'r']

# dict1 = dict(enumerate(list1))
# dict2 = dict(enumerate(list2, start=len(list1)))
# merged = {**dict1, **dict2}
# print(merged)  # {0: 'x', 1: 'y', 2: 'z', 3: 'p', 4: 'q', 5: 'r'}


# print(" \n                           Dictionary wnith Warlus                 \n".center(200,'-'))

# print("\nEx 1 :")

# names = ["Ali", "Sara", "Omar"]
# index_by_name = {i: name for i, name in enumerate(names, start=1)} if (n := len(names)) else {}


# print("\nEx 2 :")
# values = [10, -3, 7, -1, 5]
# pos_dict = {i: (v := val) for i, val in enumerate(values) if (v := val) > 0}
# print(pos_dict)


# print("\nEx 3 :")

# x = 3
# poly = {"x": x, "x^2": (sq := x**2), "2x^2+1": 2*sq + 1}
# print(poly)


# print("\nEx 4 :")

# print("""

#         text = "apple banana apple orange banana apple"
#         freq = {}

#         for word in text.split():
#             current = freq.get(word, 0)
#             new_count = current + 1
#             freq[word] = new_count

#       """)


# text = "apple banana apple orange apple banana apple"
# freq = {}

# for word in text.split():
#     # get current count (default 0), then store it back + 1
#     freq[word] = (count := freq.get(word, 0) + 1)

# print(freq)  # {'apple': 3, 'banana': 2, 'orange': 1}


# scores = {"Ali": 90, "Sara": 85, "Omar": 95}

# keys_list = []
# values_list = []

# for name in scores:              # same as: for name in scores.keys():
#     keys_list.append(name)       # collect keys
#     values_list.append(scores[name])  # collect values

# print("Keys  :", keys_list)      # ['Ali', 'Sara', 'Omar']
# print("Values:", values_list)    # [90, 85, 95]

# items_list = []

# for key, value in scores.items():
#     items_list.append((key, value))

# print("Items :", items_list)     # [('Ali', 90), ('Sara', 85), ('Omar', 95)]


# numbers = {1: 1, 2: 4, 3: 9, 4: 16}

# keys_list = []
# values_list = []
# check_list = []   # to verify value = key^2

# for x, x2 in numbers.items():     # x is key, x2 is value
#     keys_list.append(x)
#     values_list.append(x2)
#     check_list.append((x*2, x**2 +1))

# print("Keys   :", keys_list)      # [1, 2, 3, 4]
# print("Values :", values_list)    # [1, 4, 9, 16]
# print("Check  :", check_list)     # [(1, True), (2, True), (3, True), (4, True)]


# Dictionary Methods Examples

# # Sample dictionary for demonstrations
# print("=" * 50)
# print("DICTIONARY METHODS EXAMPLES")
# print("=" * 50)


# # 7. pop() - Removes and returns value for key
# print("\n7. pop() - Remove and return value")
# d7 = {'x': 10, 'y': 20, 'z': 30}
# print(f"Before: {d7}")
# value = d7.pop('y')
# print(f"pop('y') returned: {value}")
# print(f"After: {d7}")
# # With default value if key doesn't exist
# value = d7.pop('w', 'not found')
# print(f"pop('w', 'not found'): {value}")

# # 8. popitem() - Removes and returns last (key, value) pair (LIFO in Python 3.7+)
# print("\n8. popitem() - Remove and return last item")
# d8 = {'first': 1, 'second': 2, 'third': 3}
# print(f"Before: {d8}")
# item = d8.popitem()
# print(f"popitem() returned: {item}")
# print(f"After: {d8}")


# print("\n" + "=" * 50)
# print("END OF EXAMPLES")
# print("=" * 50)
