print("\033c")  # Clear screen

print(" I - MAP and FILTER Basic".center(100,'='))

#%%
# ============ MAP EXAMPLES ============
print("\n" + " A - MAP FUNCTION ".center(100,'_'))

print("\nEx 1: Using built-in str() function with map")
numbers = [2,4,6,8,10]
squared = []
# Using list comprehension
squared = [x**2 for x in numbers]
print(squared)  

def square(x):
    return x**2
print(squared)  
squared = list(map(square, numbers))
print(squared) 


squared = list(map(lambda x:int( x/2), numbers))
print(squared)  


 


 
print("\nEx 2: Using built-in int() function with map")
string_numbers = ["10", "-20", "-30", "40"]

numbers = list(map(int, string_numbers))
print(numbers)   
for item in map(int, string_numbers):
    print(item, end=" ")
print()

negative_numbers = numbers
for item in map(lambda x: abs(x), negative_numbers):
    print(item, end=" ")
print() #OR :
for item in map(abs, negative_numbers):
    print(item, end=" ")
# for item in map(lambda x: abs(x), negative_numbers):
#     print(item, end=" ")
print()

integers = numbers
print("Mapped to floats:  ", list(map(float, integers)))
for item in map(float, integers):
    print(item, end=" ")
print()

for item in map(lambda x: float(x+0.25/0.4), integers):
    print(item, end=" ")
print( )
print( '\nBonus :')

 

decimals = [3.14159, 2.71828, 1.41421]
# rounded = list(map(round, decimals))
rounded = list(map(lambda x : round(x),decimals))
print("Original : ",decimals,"\nRounded : ",rounded)  # [3, 3, 1]





print("\nEx 3 :  Working with Set & Tuple Operations")
print(" 1 : length")
sets = [{3, 1, -2}, {-6,5}, {9, 7,-8,11},{0.114,3.14}]
# lengths = list(map(len, sets))
lengths = list(map(lambda x : len(x),sets))
print(lengths)  # [3, 2, 4]

print(" 2 : sort ")

# Example 2: Sort elements in each set (returns list)
# sorted_sets = list(map(sorted, sets))
sorted_sets = list(map(lambda x : sorted(x),sets))
print(sorted_sets)   

print(" 3 : max ")

 
# # max_values = list(map(max, sets))
max_values = list(map(lambda x : max(x),sets))
print(max_values)  # [5, 8 

print(" 4 : min  ")

 
# # min_values = list(map(min, sets))
min_values = list(map(lambda x : min(x),sets))
print(min_values) 

print(" 5 : sum ")

# Example 5: Sum elements in each set
# sums = list(map(sum, sets))
sums = list(map(lambda x : sum(x),sets))
print(sums) 

print(" 6 : length")

# # Example 6: Get length of tuples
tuples = [(3, 1, -2), [-6,5], [9, 7,-8,11],(0.114,3.14)]
lengths = list(map(len, tuples))
lengths = list(map(lambda x : len(x),tuples))
print(lengths)  # [2, 3, 4]

print(" 7 : sorted ")
 
# sorted_tuples = list(map(sorted, tuples))
sorted_tuples = list(map(lambda x : sorted(x),tuples))
print(sorted_tuples)   

print(" \n8 : Reverse each tuple")

# Example 8: Reverse each tuple
# reversed_tuples = list(map(reversed, tuples))
reversed_tuples = list(map(lambda x : reversed(x),tuples))
print()
print(*[list(item) for item in reversed_tuples], sep=' ')
# Convert back to tuples
# result = list(map(tuple, reversed_tuples))
result = list(map(lambda x : tuple(x),reversed_tuples))
print(result)  # [(3, 2, 1), (6, 5, 4), (9, 8, 7)]

 

 



print("\nEx 4 : Converting Between Set and Tuple :-")
# Example 1: Convert sets to tuples (using tuple on map object)
sets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
tuples = tuple(map(tuple, sets))
# print(tuples,end=' ')  ;print()
tuples = tuple(map(lambda x : tuple(x),sets))
print(tuples,end=' ')  ;print()

# Example 2: Convert tuples to sets (using set creates one set, so iterate)
tuples = [(1, 2, 2, 3), (4, 5, 5, 6), (7, 8, 8, 9)]
print(list(map(set, tuples)))
for s in map(set, tuples): print(s,end = '  ')

 

# Example 3: Convert lists to sets (remove duplicates)
lists = [[1, 1, 2, 3], [4, 4, 5], [6, 7, 7, 8]]
unique_sets = list(map(set, lists))
unique_sets = list(map(lambda x : set(x),lists))
print(unique_sets)  # [{1, 2, 3}, {4, 5}, {6, 7, 8}]




# Example 4: Convert strings to sets
words = ['hello', 'world', 'python']
for char_set in map(set, words):print(char_set,end=' - ')
for char_set in map(lambda x : tuple(x),words) : print(char_set,end=' - ')
print('\n'*2)

 


# Example 5: Convert strings to tuples
words = ['cat', 'dog', 'bird']
for char_tuple in map(tuple, words):
    print(char_tuple,end = ' ')
for char_tuple in map(lambda x : tuple(x),words) : print(char_tuple,end=' ')
print('\n'*2)



# Example 6: Direct iteration over map object
sets = [{1, 2}, {3, 4}, {5, 6}]
map_obj = map(tuple, sets)
print(next(map_obj))  # (1, 2)
print(next(map_obj))  # (3, 4)
print(next(map_obj))  # (5, 6)
print()

# Example 7: Get max value from each tuple
tuples = [(1, 5, 3), (2, 8, 4), (6, 3, 9)]
max_values = list(map(max, tuples))
print(max_values)  # [5, 8, 9]

min_values = list(map(min, tuples))
print(min_values)  # [1, 2, 3]

sums = list(map(sum, tuples))
print(sums)  # [6, 15, 24]







print("\nEx 5 : Using String Methods :")
# # Example 1: Convert to uppercase
words = ['   hello world', '  python programming    ']
stripped = list(map(str.strip, words))
print('Before : ',words,'\nAfter :',stripped)   

words = stripped
uppercase = list(map(str.upper, words))
print(uppercase)  # ['HELLO', 'WORLD', 'PYTHON']

 
lowercase = list(map(str.lower, words))
print(lowercase)  # ['hello', 'world', 'python']

 
capitalized = list(map(str.capitalize, words))
print(capitalized)  # ['Alice', 'Bob', 'Charlie']


titled = list(map(str.title, words))
print(titled)  # ['Hello World', 'Python Programming']




print("\nEx 6 :Using Type Constructors ")

# Example 1: Convert to lists
tuples = [(1, 2), (3, 4), (5, 6), '', 'hello', [], {0,1},{()}]
lists = list(map(list, tuples))
print(lists)  # [[1, 2], [3, 4], [5, 6]]


# Example 2: Convert to tuples
tuples = list(map(tuple, lists))
print(tuples)  # [(1, 2), (3, 4), (5, 6)]


sets = list(map(set, lists))
print(sets)  # [{1, 2}, {3, 4}, {5, 6}]



booleans = list(map(bool, sets))
print(booleans)

values = [0, 1, '', 'hello', [], [1, 2],{()}]
print(lists[-2][0] , tuples[-2][1] , list(map(bool,[lists[-2][0] , tuples[-2][1]])))
# booleans = list(map(bool, values))
# print(booleans)  # [False, True, False, True, False, True]








print("\nEx 6 :Nest Operations ")

# Example 4: Flatten and convert to set
nested_lists = [[[1, 2]], [[3, 4]], [[5, 6,10]]]
# First map to get inner lists
inner = list(map(sum, nested_lists, [[]]*len(nested_lists)))
print(inner)  


# Example 5: Convert range objects to tuples
ranges = [range(5), range(3, 8), range(2, 7)]
tuples = list(map(tuple, ranges))
print(tuples)  # [(0, 1, 2), (3, 4, 5), (6, 7, 8)]


sets = list(map(set, ranges))
print(sets)  # [{0, 1, 2, 3, 4}, {3, 4, 5, 6, 7}, {2, 3, 4, 5, 6}]


print("\nEx 7 : Conmbining Uing zip ")
# Example 1: Zip and convert to tuples
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipping = zip(list1, list2)
print([i for i in zipping])

zipping = zip(list1, list2)
zipped = list(map(list, zipping))
print(zipped)  # [(1, 'a'), (2, 'b'), (3, 'c')]

zipping = zip(list1, list2)
zipped_sets = list(map(lambda x : set(x),zipping ))
print(zipped_sets)   

for x,(y ,z) in enumerate(zip(zipped,zipped_sets)):
    print(x,y,z)

print("\nEx 8 : Converting differnt type :")
# Example 1: Convert to strings
numbers = (1, 2, 3, 4, 5)
for s in map(str, numbers):
    print(s)
# '1'
# '2'
# '3'
# '4'
# '5'


# # Example 2: Convert to integers
# strings = ('10', '20', '30')
# for num in map(int, strings):
#     print(num)
# # 10
# # 20
# # 30


# # Example 3: Convert to absolute values
# numbers = {-5, -3, 0, 2, 7}
# for abs_val in map(abs, numbers):
#     print(abs_val)
# # 0
# # 2
# # 3
# # 5
# # 7


# # Example 4: Convert range to tuple
ranges = [range(3), range(3, 6,2), range(6,9,3)]
print(ranges)
l = []
for r in map(tuple, ranges):l.append(r)
print(l)
print(list(map(tuple, ranges)) == l)
print([r for r in map(set, ranges)] == list(map(lambda x : set(x),ranges)))

 


print("Unpacking : ")
# Example 1: Unpack map results
a, b, c = map(tuple, l)
print(a,b,c,sep="\t")  # (1, 2) (3, 4) (5, 6)
 
x, y, z = map(len, l)
print(x, y, z)  # 2 3 4

[m1, m2, m3] , [n1,n2,n3] = map(max, l) , map(min,l)
print(m1, m2, m3 , n1,n2,n3)  # 5 8 9






print("\nEx9: Getting items one at a time with next()")
nums = [i for i in range(0,20,3)]
mapped = map(str, nums)
print(f"Original: {nums}")

print(f"First item: {next(mapped)}")
print(f"Second item: {next(mapped)}")
print(f"Third item: {next(mapped)}")

print("Remaining items: ", end="")
for item in mapped:
    print(item, end=" ")
print()
mapped1 = map(lambda x : x/2 , [i for i in range(1,20,3)])
mapped2 = map(lambda x : float(x//2) , [i for i in range(1,20,3)])
mapped3 = map(lambda x : x%5 , [i for i in range(1,20,3)])

print([a for a in mapped1])
print([a for a in mapped2])
print([a for a in mapped3])



















#%%
# ============ FILTER EXAMPLES ============
print("\n" + " B - FILTER FUNCTION ".center(100,'_'))
print("\nEx0 : ")
numbers = [1, 2, 3, 4, 5, 6, 7, 8] 

def get_evens(lst: list[int]) -> list[int]:
    if not lst:  # Base case: list is empty
        return []
    
    # Check the first item
    current = [lst[0]] if lst[0] % 2 == 0 else []
    
    # Add it to the result of checking the rest of the list
    return current + get_evens(lst[1:])

evens1 = get_evens(numbers)
# print(evens1)  # Output: [2, 4, 6, 8]

#OR :
#  Using for loop Using list comprehension
evens2 = [x for x in numbers if x % 2 == 0]
# print(evens2)  # Output: [2, 4, 6, 8]

# filter method 1 : using def
def is_even(x: int) : return x % 2 == 0
evens3 = list(filter(is_even, numbers))
# print(evens3)  # Output: [2, 4, 6, 8]

# filter method 2 : usibg lambda :
evens4 = list(filter(lambda x : x%2==0, numbers))
print(evens4 == evens1 == evens2 == evens3 , evens4)  # Output: [2, 4, 6, 8]




 

print("\nEx 1: Using built-in bool() function with filter")
mixed_values = [0, 1, "", "hello", None, 42, False, True, [], [1,2]]

 
filterd_bool_str = [x for x in mixed_values if type(x) is bool or type(x) is str]
print(*filterd_bool_str)
# print(*[x for x in filter(int, mixed_values)])------ ValueError

def is_list_or_int(x: object) -> bool: return type(x) is list or type(x) is int
filterd_list_int = list(filter(is_list_or_int, mixed_values))
print(*filterd_list_int)

# Fix: type(x) is not type(None)
filterd_not_none = list(filter(lambda x :type(x) is not type(None) , mixed_values))
print(*filterd_not_none)

filterd_none = [item for item in filter(None, mixed_values)]

Bool_1 = list(filter(bool , mixed_values)) 

# To get the opposite (Falsy values: 0, None, False, [], etc.):
# Method 1: Using lambda with 'not'
Bool_2 = list(filter(lambda x:  x, mixed_values)) 
print(filterd_none == Bool_1 == Bool_2 , f" ------> {Bool_1}")

# Method 2: Using list comprehension (often easier to read)

Not_bool_1 = [x for x in mixed_values if not x]

Not_bool_2 = list(filter(lambda x: not bool(x), mixed_values))


import operator
Not_bool_3 = list(filter(operator.not_, mixed_values))
print( Not_bool_2 == Not_bool_1 == Not_bool_3, f"So The Falsy only (operator): {Not_bool_3}")






print("\nEx 2: Using str.isdigit method with filter")
mixed_strings = ["123", "abc", "456", "xyz", "789" ,"123a"]
print(f"Original: {mixed_strings}")
digit = [x for x in mixed_strings if x.isdigit()]
print(*digit)

alpha = list(filter(str.isalpha, mixed_strings))
print(*alpha)

alnum = set(filter(lambda x : str.isalnum(x) and not str.isdigit(x) and not str.isalpha(x), mixed_strings))
print(*alnum)
 
 
#  alnum = set(filter(str.isalnum and not str.isdigit and not str.isalpha, mixed_strings))
# print(*alnum)  -------> Error
 



# 
print("\nEx 3: Using str.is method with filter")

# # Example 6: Filter strings that are title case
# values = ('Hello World', 'hello world', 'Python Programming', 'test' , "AI")
# for val in filter(str.istitle, values):
#     print(val)
# # 'Hello World'
# # 'Python Programming'    
# print()

 



 
print("\nEx 4 : Using str.isupper method with filter")

# Example 2: Filter None values from set
values = {1, None, 2, None, 3,'hello', '', 'world', '', 'python', ''}
for val in filter(None, values):
    print(val)
 
 

print("----")
  

 
for values in filter(bool, values):
    print(values)
# # 'hello'
# # 'world'
# # 'python'
 


 

print("\nEx 5 Unpacking :")
# Using next()
values = ('123', 'abc', '456', 'xyz', '789')
filter_obj = filter(str.isalpha, values)
print(next(filter_obj))  # '123'
print(next(filter_obj))  # '456'

 
# Example 1: Unpack filtered values
a, b, c = filter(str.isdigit, values)
print(a, b, c)  # '123' '456' '789'

 
 

print("\nEx 6 : Combining Filter with Other Operations ")

# Example 1: Filter then convert to set
values = ('123', '456', 'abc', '789', 'xyz', '123')
result = set(filter(str.isdigit, values))
print(result,"\tNote : Set does not have duplicate items")
# {'123', '456', '789'}
count = sum(1 for _ in filter(str.isdigit, values))
print(count)  # 4




print("\nEx 7 : Type checking :")
# Example 1: Filter integers (using isinstance)
values = (1, 'hello', 2, 'world', 3, 'python', 4.5)
for val in filter(int.__instancecheck__, values):
    print(val,end = ' ')
print()
 
# Example 2: Filter strings
print(*[val for val in filter(str.__instancecheck__, values)])
 



print("\nEx 9 : With Enumerate : ")
words = ['hello', '', 'world', '', 'python']


# Enumerate, filter non-empty strings, map to get uppercase
enumerated = list(enumerate(words))
print([(i,word) for i,word in enumerate(words)] == enumerated)

# enumerated = enumerate(words)
# Filter keeps (index, word) tuples where word is truthy
filtered = filter(lambda x: x[1], enumerated)
print(list(filtered))

words = ['hi', 'welcome', 'to', 'the', 'python', 'ok']
# Filter words with length > 3, then show their positions
filtered_with_idx = filter(lambda x: len(x[1]) >= 3, enumerate(words))
for idx, word in filtered_with_idx:
    print(f"Index: {idx}, Word: {word}")














 















# %%
# # ============ COMBINED EXAMPLE ============
# print("\n" + " C - COMBINING MAP and FILTER ".center(100,'_'))


# # Example 4: Filter strings then get lengths
# words = ('hello', '', 'world', '', 'python', '')
# filtered = filter(bool, words)
# for length in map(len, filtered):
#     print(length)
# # 5
# # 5
# # 6

# print("Ex 1 : Filter with strings : ")
# text = "hello world python"

# # Filter out spaces, then convert to uppercase
# filtered = filter(str.isalpha, text)
# uppercase = map(str.upper, filtered)

# for char in uppercase:
#     print(char,end = ' ')
# # H
# # E
# # L
# # L
# # O
# # W
# # O
# # R
# # L
# # D
# # P
# # Y
# # T
# # H
# # O
# # N
# text = "abc123xyz456test789"

# # Filter only digit characters, then convert to integers
# digits = filter(str.isdigit, text)
# numbers = map(int, digits)

# for num in numbers:
#     print(num)
# # 1
# # 2
# # 3
# # 4
# # 5
# # 6
# # 7
# # 8
# # 9


# # Example 3: Filter alphabetic characters, then get their ASCII values
# text = "hello123world456"
# alphabetic = filter(str.isalpha, text)
# ascii_values = map(ord, alphabetic)

# for value in ascii_values:
#     print(value)
# # 104 (h)
# # 101 (e)
# # 108 (l)
# # 108 (l)
# # 111 (o)
# # 119 (w)
# # 111 (o)
# # 114 (r)
# # 108 (l)
# # 100 (d)


# # Example 4: Filter lowercase letters, then convert to uppercase
# text = "Hello World Python"
# lowercase = filter(str.islower, text)
# uppercase = map(str.upper, lowercase)

# for char in uppercase:
#     print(char)
# # E
# # L
# # L
# # O
# # O
# # R
# # L
# # D
# # Y
# # T
# # H
# # O
# # N
# result = ''.join(filter(str.isalpha, text))
# print(f"Result: {result}")


# # Example 5: Filter uppercase letters, then convert to lowercase
# text = "HELLO world PYTHON"
# uppercase_chars = filter(str.isupper, text)
# lowercase = map(str.lower, uppercase_chars)

# for char in lowercase:
#     print(char)
# # h
# # e
# # l
# # l
# # o
# # p
# # y
# # t
# # h
# # o
# # n
# result = '.'.join(filter(str.isupper, text))
# print(f"Result: {result}")

# result = '-'.join(filter(str.islower, text))
# print(f"Result: {result}")




# text = "abc123def456ghi789"
# print(f"Original: {text}")
# result = ''.join(filter(str.isdigit, text))
# print(f"Result: {result}")
# # 123456789
# result = '_'.join(map(str.upper, filter(str.isalpha, text)))
# print(f"Result: {result}")


# text = "HelloWorldPython"
# print(f"Original: {text}")
# result = ' '.join(filter(str.isupper, text))
# print(f"Result: {result}")
# # H W P

# text = "a1b2c3d4e5"
# print(f"Original: {text}")
# # Extract digits, convert to int (validates), back to str, join with arrow
# result = ' → '.join(map(str, map(int, filter(str.isdigit, text))))
# print(f"Result: {result}")
# # 1 → 2 → 3 → 4 → 5




# text = "hello@world#python!2024"
# print(f"Original: {text}")
# result = ''.join(filter(str.isalnum, text))
# print(f"Result: {result}")









# print("\nEx 2: Filter truthy values, then convert to strings")
# texts = ["  hello  ", "", "  world  ", "", "  python  "]
# print(f"Original: {texts}")
# result = ', '.join(map(str.strip, filter(bool, texts)))
# print(f"Result: {result}") 
      
# data = [0, 5, "", 10, None, 15, False, 20]
# print(f"Original: {data}")
# print("Process: filter(None) → map(str)")
# print("Result: ", end="")
# for item in map(str, filter(None, data)):
#     print(f"'{item}'", end=" ")
# print()

# #Example 1: Filter non-empty strings, then convert to uppercase

# words = ['hello', '', 'world', '', 'python', '', 'code']

# # Filter out empty strings, then convert to uppercase
# filtered = filter(bool, words)
# uppercase = map(str.upper, filtered)

# for word in uppercase:
#     print(word)
# # HELLO
# # WORLD
# # PYTHON
# # CODE

# # Example 2: Filter alphabetic strings, then get their lengths
# values = ['hello', '123', 'world', '456', 'python', '789', 'code']

# # Filter only alphabetic strings, then get their lengths
# alphabetic = filter(str.isalpha, values)
# lengths = map(len, alphabetic)

# for length in lengths:
#     print(length)
# # 5
# # 5
# # 6
# # 4

# # Example 3: Filter digit strings, then convert to integers
# strings = ['abc', '123', 'xyz', '456', 'hello', '789']
# digits = filter(str.isdigit, strings)
# numbers = map(int, digits)

# for num in numbers:
#     print(num)
# # 123
# # 456
# # 789


# # Example 4: Filter non-empty, then strip whitespace
# texts = ['  hello  ', '', '  world  ', '', '  python  ']
# non_empty = filter(bool, texts)
# stripped = map(str.strip, non_empty)

# for text in stripped:
#     print(text)
# # hello
# # world
# # python


# # Example 5: Filter lowercase strings, then capitalize
# words = ['hello', 'WORLD', 'python', 'CODE', 'test', "456", "123"]
# lowercase = filter(str.islower, words)
# capitalized = map(str.capitalize, lowercase)

# for word in capitalized:
#     print(word)
# # Hello
# # Python
# # Test
# result = ' '.join(map(str.upper, filter(bool, words)))
# print(f"Result: {result}")



# result = ', '.join(map(str.title, filter(str.isalpha, words)))
# print(f"Result: {result}")
# # Hello, World, Python

# strings = ["abc", "123", "xyz", "456", "789"]
# print(f"Original: {strings}")
# result = '+'.join(map(str, map(int, filter(str.isdigit, strings))))
# print(f"Result: {result}")
# # 123+456+789



# values = [0, 5, "", 10, None, 15, False, 20]
# print(f"Original: {values}")
# result = '|'.join(map(str, filter(None, values)))
# print(f"Result: {result}")
# # 5|10|15|20




# words = ["HELLO", "world", "PYTHON", "code", "TEST"]
# print(f"Original: {words}")
# result = '\n'.join(filter(str.islower, words))
# print(f"Result:\n{result}")



# print("\nEx 4: Filter lowercase letters, join with dash")
# text = "HelloWorldPython"
# print(f"Original: {text}")

# # e-l-l-o-o-r-l-d-y-t-h-o-n

# words = ["Hello", "World!", "Python@", "2024", "Code#"]
# print(f"Original: {words}")
# result = '-'.join(map(str.lower, filter(str.isalnum, words)))
# print(f"Result: {result}")
 



  
 








































# #%%
# # ============ USING NEXT() TO GET ITEMS ============
# print("\n" + " II - USING def/lambda  WITH MAP/FILTER ".center(100,'='))
# print("\n" + " A - USING map()".center(100,'_'))
# text = "abc1def2ghi3jkl4"

# # Enumerate to get (index, char) tuples
# enumerated = enumerate(text)

# # Filter only tuples where the character is a digit
# filtered = filter(lambda x: x[1].isdigit(), enumerated)

# # Map to format output
# mapped = map(lambda x: f"Index {x[0]}: {int(x[1])}", filtered)

# for result in mapped:
#     print(result)
# # Index 3: 1
# # Index 7: 2
# # Index 11: 3
# # Index 15: 4



# print("\n" + " B - USING filter()".center(100,'_'))
# print("\n" + " C - USING map() + filter".center(100,'_'))
# #%%






























