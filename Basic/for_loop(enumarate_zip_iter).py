# print("\033[1;97;48;2;0;0;128m\033")
# print("\033[1;93mBright Yellow (bold)\033")
print("========= (A) - Enumerate example =========")
print("----- String enumerate example -----")
String_1 , String_2 = "Machine learning" ,  "Atrificial Intelegance"
print(next(enumerate(String_1)),next(enumerate(String_2)))
enum_s2 = enumerate(String_2)
print([next(enum_s2) for _ in range(len(String_2) - 19)]) # print(list(enum_s2)[19:])
print(list(enum_s2)[2])
print("--- String_1 ---")
for index, char in enumerate(String_1):
    print(index, char)
print("\n--- String_2 ---")
for index, char in enumerate(String_2):
    print(index, char)



print("\n----- List enumerate example -----")
lst_1 , lst_2 = [1,2,3,4,5] , ["A","B","C","D","E"]
print(dict(enumerate(lst_1)))
print(set(enumerate(lst_2)))
print("\n--- lst_1 ---")
for index, item in enumerate(lst_1):
    print(index, item)
print("\n--- lst_2 ---")
for index, item in enumerate(lst_2):
    print(index, item)


print("\n----- Tupple enumerate example -----")
tupple_1 , tupple_2 = (0.1,0.2,0.3,0.4,0.5) , ("a","b","c","d","e")
print(list(enumerate(tupple_1))[2])
print(list(enumerate(tupple_2)))
print("\n--- tupple_1 ---")
for index, item in enumerate(tupple_1):
    print(index, item)
print("\n--- tupple_2 ---")
for index, item in enumerate(tupple_1):
    item_2 = tupple_2[index]
    print(index, item, item_2)


print("\n----- Set enumerate example -----")
set_1 , set_2 = {'alpha','beta','gamma','delta','epsilon'},{'α','β','γ','δ','ε'}
print(list(enumerate(set_1)))
print(list(enumerate(set_2)))
print("\n--- set_1 ---")
for index, item in enumerate(set_1):
    print(index, item)
print("\n--- set_2 ---")
for index, item in enumerate(set_2):
    print(index, item)




print("\n----- Dict enumerate example -----")
dict_1 = {"ohom": 'Ω', 'microfarad': 'μF','tesla': 'T'}
dict_2 = {'sigma': 'Σ','pi': 'π','euler': 'e'}
print(list(enumerate(dict_1.keys())))
print(list(enumerate(dict_2.items())))
print(list(enumerate(dict_2.values())) , len(dict_2.values()))

print("\n--- dict_1 ---")
for index, key in enumerate(dict_1):
    print(index, key,'----->', dict_1[key])
print("\n--- dict_2 ---")
for index, (key, value) in enumerate(dict_2.items()):
    print(index, key, value)
    
print("Method 1 - Enumerating keys:")
for index, name in enumerate(dict_1.keys()):
    print(f"{index} -- {name}")

print()

# Method 2: Enumerate key-value pairs
print("Method 2 - Enumerating key-value pairs:")
for index, (name, score) in enumerate(dict_2.items(), start=1):
    print(f"Rank {index}: {name} =======> {score}")

print()

# Method 3: Enumerate just values
print("Method 3 - Enumerating values:")
for index, score in enumerate(dict_1.values()):
    print(f"Score #{index}: {score}")






print("\n\n\t\t========= (B) - Zip example =========")
print("----- Zip String example -----")
print(list(zip(String_1, String_2))[:5])
print(tuple(zip(String_1, String_2))[5:])
print("----- Zip String with For Loop -----")
for char1, char2 in zip(String_1, String_2):
    print(f"{char1} <-> {char2}")

print("\n----- Zip List example -----")
print(dict(zip(lst_1, lst_2)))
print("\n----- Zip List with For Loop -----")
for item1, item2 in zip(lst_1, lst_2):
    print(f"List 1: {item1} | List 2: {item2}")
print("\n----- Zip Tuple example -----")
print(set(zip(tupple_1, tupple_2)))
print("\n----- Zip Tuple with For Loop -----")
for t1, t2 in zip(tupple_1, tupple_2):
    print(f"Tuple 1: {t1} | Tuple 2: {t2}")
    
    
print("\n----- Zip Set example -----")
print(set(zip(set_1, set_2)))    
print("\n----- Zip Set with For Loop -----")
for s1, s2 in zip(set_1, set_2):
    print(f"Set 1: {s1} | Set 2: {s2}")


print("\n----- Zip Dict example -----")
print("Zip keys:")
print(list(zip(dict_1, dict_2)))
print("Zip values:")
print(list(zip(dict_1, dict_1.values())))
print("Zip items:")
print(list(zip(dict_2.items(), dict_2.keys())))
print("\n----- Zip Dict with For Loop -----")
print("1. Zip Keys:")
for k1, k2 in zip(dict_1, dict_2):
    print(f"Key 1: {k1}, Key 2: {k2}")

print("\n2. Zip Values:")
for v1, v2 in zip(dict_1.values(), dict_2.values()):
    print(f"Value 1: {v1}, Value 2: {v2}")

print("\n3. Zip Items:")
for (k1, v1), (k2, v2) in zip(dict_1.items(), dict_2.items()):
    print(f"Dict 1 ({k1}: {v1}) <-> Dict 2 ({k2}: {v2})")


# Method 1: Zip dictionary keys
print("Method 1 - Zipping keys:")
for key1, key2 in zip(dict_1, dict_2):
    print(f"Key from dict1: {key1} \t || \t key from dict2: {key2}")

print()

# Method 2: Zip keys and values
print("Method 2 - Zipping keys with values:")
for key, value in zip(dict_1.keys(), dict_1.values()):
    print(f"{key} -> {value}",end = " \t")

print()

# Method 3: Zip values from two dictionaries
print("Method 3 - Zipping values from both dictionaries:")
for val1, val2 in zip(dict_1.values() ,dict_2.values()):
    print(f"dict1 value:{val1} \t  |\t dict2 value: {val2}")
    
    
    
    
    

print("\n\n\t\t========= (D) - Zip + Enumerate with For Loop example =========")

print("----- Zip + Enumerate String example -----")
for index, (char1, char2) in enumerate(zip(String_1, String_2)):
    print(f"{index}: {char1} <-> {char2}")

print("\n----- Zip + Enumerate List example -----")
for index, (item1, item2) in enumerate(zip(lst_1, lst_2)):
    print(f"Index {index}: List 1 -> {item1} | List 2 -> {item2}")

print("\n----- Zip + Enumerate Tuple example -----")
for index, (t1, t2) in enumerate(zip(tupple_1, tupple_2)):
    print(f"Index {index}: Tuple 1 -> {t1} | Tuple 2 -> {t2}")

print("\n----- Zip + Enumerate Set example -----")
for index, (s1, s2) in enumerate(zip(set_1, set_2)):
    print(f"Index {index}: Set 1 -> {s1} | Set 2 -> {s2}")

print("\n----- Zip + Enumerate Dict example -----")
print("Enumerate Zip Keys:")
for index, (k1, k2) in enumerate(zip(dict_1, dict_2)):
    print(f"{index}: {k1} <-> {k2}")

print("\nEnumerate Zip Values:")
for index, (v1, v2) in enumerate(zip(dict_1.values(), dict_2.values())):
    print(f"{index}: {v1} <-> {v2}")




#%%
print("\n\n\t\t========= (E) - iter() function example =========")

print("----- iter() String example -----")
str_iter = iter(String_1)
print(f"Original String: {String_1}")
print(f"1. next(str_iter) -> {next(str_iter)}")
print(f"2. next(str_iter) -> {next(str_iter)}")
print(f"3. next(str_iter) -> {next(str_iter)}")
print(f"Rest of the string: {list(str_iter)}")

print("\n----- iter() List example -----")
lst_iter = iter(lst_1)
print(f"Original List: {lst_1}")
print(f"1. next(lst_iter) -> {next(lst_iter)}")
print(f"2. next(lst_iter) -> {next(lst_iter)}")
print(f"Rest of the list: {list(lst_iter)}")

print("\n----- iter() Tuple example -----")
tuple_iter = iter(tupple_1)
print(f"Original Tuple: {tupple_1}")
print(f"1. next(tuple_iter) -> {next(tuple_iter)}")
print(f"2. next(tuple_iter) -> {next(tuple_iter)}")

print("\n----- iter() Set example -----")
set_iter = iter(set_1)
print(f"Original Set: {set_1}")
print(f"1. next(set_iter) -> {next(set_iter)}")

print("\n----- iter() Dict example -----")
dict_iter = iter(dict_1)
print(f"Original Dict Keys: {list(dict_1.keys())}")
print(f"1. next(dict_iter) -> {next(dict_iter)}")




print("\n\n\t\t========= (F) - iter() with For Loop example =========")

print("----- iter() with For Loop (String) -----")
str_iter_for = iter(String_1)
print(f"Skipping first 5 chars: {[next(str_iter_for) for _ in range(5)]}")
print("Remaining chars in loop:")
for char in str_iter_for:
    print(char, end=' ')
print("\n")

print("\n----- iter() with For Loop (List) -----")
lst_iter_for = iter(lst_1)
print(f"Skipping first 2 items: {next(lst_iter_for)}, {next(lst_iter_for)}")
print("Remaining items in loop:")
for item in lst_iter_for:
    print(item, end=' ')
print("\n")

print("\n----- iter() with For Loop (Tuple) -----")
tuple_iter_for = iter(tupple_1)
print(f"Skipping first item: {next(tuple_iter_for)}")
print("Remaining items in loop:")
for item in tuple_iter_for:
    print(item, end=' ')
print("\n")

print("\n----- iter() with For Loop (Set) -----")
set_iter_for = iter(set_1)
print(f"Skipping first item: {next(set_iter_for)}")
print("Remaining items in loop:")
for item in set_iter_for:
    print(item, end=' ')
print("\n")

print("\n----- iter() with For Loop (Dict) -----")
dict_iter_for = iter(dict_1)
print(f"Skipping first key: {next(dict_iter_for)}")
print("Remaining keys in loop:")
print("\n")





print("\n\n\t\t========= (G) - Advanced Examples with enumerate, zip, and iter =========")

# Example 1: Zip Lists, Enumerate, and Skip with Iter
print("\n--- Example 1: Zip Lists, Enumerate, and Skip with Iter ---")
zipped_lists = zip(lst_1, lst_2)
iter_zipped = iter(zipped_lists)
print(f"Skipping first 2 pairs: {next(iter_zipped)}, {next(iter_zipped)}")
for i, (item1, item2) in enumerate(iter_zipped, start=1):
    print(f"Item {i}: {item1} - {item2}")

# Example 2: Zip Strings, Enumerate with a High Start Index
print("\n--- Example 2: Zip Strings, Enumerate with a High Start Index ---")
zipped_strings = zip(String_1, String_2)
for i, (char1, char2) in enumerate(zipped_strings, start=101):
    print(f"Index {i}: {char1} | {char2}")

# Example 3: Zip Tuples and Dict Values, then Enumerate
print("\n--- Example 3: Zip Tuples and Dict Values, then Enumerate ---")
zipped_tuple_dict = zip(tupple_1, dict_1.values())
for i, (t_item, d_value) in enumerate(zipped_tuple_dict):
    print(f"Pair {i}: Tuple item -> {t_item}, Dict value -> {d_value}")

# Example 4: Zip and Enumerate Iterators
print("\n--- Example 4: Zip and Enumerate Iterators ---")
iter_list = iter(lst_1)
iter_set = iter(set_1)
zipped_iters = zip(iter_list, iter_set)
for i, (l_item, s_item) in enumerate(zipped_iters):
    print(f"#{i}: List -> {l_item}, Set -> {s_item}")

# Example 5: Complex Zip with enumerate and iter
print("\n--- Example 5: Complex Zip with enumerate and iter ---")
complex_zip = zip(lst_2, tupple_2, String_1)
iter_complex = iter(complex_zip)
print(f"Skipping one element: {next(iter_complex)}")
for i, (l_item, t_item, s_item) in enumerate(iter_complex):
    print(f"Index {i}: {l_item}, {t_item}, {s_item}")

print("\n 26) creating a 5x5 matrix")
data = list(range(1, 22))  # [1, 2, ..., 21]

for i, val in enumerate(data, start=1):
    print(str(val).rjust(2), end=" ")

    # Every 5th element → new row
    if i % 5 == 0:
        print()  # line break

# OR :
data = list(range(1, 22))
it = iter(data)
count = 0

for val in it:
    print(str(val).rjust(2), end=" ")
    count += 1
    if count % 5 == 0:
        print()




# %%
