
# %%
BiF = [f for f in dir(__builtins__) if callable(getattr(__builtins__, f))]
# List all built-in functions and constants
for i in BiF:
    if 'Error' not in i and 'Warning' not in i and 'Exception' not in i:
        if not i.startswith("_"):
            print(i, end='   ')

        
# %%
print("\n"*2)
for i in BiF:
    if 'Error' in i or 'Warning' in i:
        print(i, end='   ')
# %%

# Examples of Built-in Functions

# abs: Absolute value
print(abs(-5))  # 5

# all: True if all elements are truthy
print(all([True, 1, "hello"]))  # True

# any: True if any element is truthy
print(any([False, 0, "hello"]))  # True

# ascii: ASCII representation
print(ascii("café  أيمن"))  # 'caf\\xe9'

# bin: Binary representation
print(bin(10))  # '0b1010'

# bool: Boolean value
print(bool(0))  # False

# chr: Character from Unicode code
print(chr(65))  # 'A'

# complex: Complex number
print(complex(1, 2))  # (1+2j)

# dict: Dictionary
print(dict(a=1, b=2))  # {'a': 1, 'b': 2}

# divmod: Quotient and remainder
print(divmod(10, 3))  # (3, 1)

# enumerate: Index and value
for i, v in enumerate(['a', 'b']):
    print(i, v)  # 0 a \n 1 b

# eval: Evaluate expression
print(eval('2 + 3'))  # 5

# filter: Filter elements
print(list(filter(lambda x: x > 0, [-1, 0, 1])))  # [1]

# float: Floating point number
print(float('3.14'))  # 3.14

# format: Format string
print(format(123, '04d'))  # 0123

# frozenset: Immutable set
print(frozenset([1, 2, 3]))  # frozenset({1, 2, 3})

# hex: Hexadecimal
print(hex(255))  # '0xff'

# id: Object identity
x = 5
print(id(x))  # Some memory address

# int: Integer
print(int('42'))  # 42

# isinstance: Check type
print(isinstance(5, int))  # True
print(type(5),type(5).__name__)  # <class 'int'>


# iter: Iterator
it = iter([1, 2, 3])
print(next(it) , next(it))  # 1

# len: Length
print(len([1, 2, 3]) , list((1, 2, 3)) , list(reversed([1, 2, 3])))  # 3



# map: Apply function
print(list(map(lambda x: x*2, [1, 2, 3])))  # [2, 4, 6]

# max: Maximum min: Minimum
print(max([1, 2, 3]) ,  min([1, 2, 3]))  # 3




# ord: Unicode code oct: Octal
print(ord('A') , oct(8))  # 65 '0o10'


# repr: String representation
print(repr("hello\n"))  # "'hello'"


# round: Round number
print(round(3.14159, 2))  # 3.14

# set: Set

# slice: Slice object
s = slice(1, 3)
print([1, 2, 3, 4][s])  # [2, 3]

# sorted: Sorted list
print(sorted([3, 1, 2]))  # [1, 2, 3]

# str: String
print(str(123))  # '123'

# sum: Sum of iterables
print(sum([1, 2, 3]))  # 6

# tuple: Tuple
print(tuple([1, 2, 3]))  # (1, 2, 3)

# type: Type of object

# zip: Zip iterables
print(list(zip([1, 2], ['a', 'b'])))  # [(1, 'a'), (2, 'b')]




#%%
print('🔢 Numbers & Math')
print(f"{abs(-5)}, {divmod(7, 3)}\
      {pow(2, 3)}, {round(3.14159, 2)}\
      {float('3.5')}, {int('10')}, {complex(2, 3)}")

print('\n✅ Logic / Boolean')
print(f'''{bool(0)} | { all([True, True, False]) } | {any([False, False, True])}  ''')


print('\n🔠 Strings & Characters')
print(f"""{ascii("café") } |  {chr(60)}  |   {ord('A') }     
{str(123) }   |    {repr("hi\n") } |  {format(3.14159, ".2f")  }  
""")

print('\n📦 Collections')
print( f"""{list((1, 2, 3))} | {tuple([1, 2])  }| {set([1, 1, 2])} | {frozenset([1, 2, 2]) }     
{dict(a=1, b=2) } | {list(zip([1,2], ['a','b']))} | {sum([1, 2, 3])  }| {max([1, 5, 3])} | {min([1, 5, 3])}           
{sorted([3, 1, 2])}  | {list(reversed([1, 2, 3])) }  | {slice(1, 4)}    """     )     

    
print("\n🔁 Iteration & Iterators")
print(f"""{list(iter([1, 2.14, 'Z'])) }  |  {next(iter([1, 2, 3])) } | {list(enumerate(['a','b']))  }   
{range(5) } | {tuple(filter(lambda x: x>2, [1,2,3,4]) ) } | {set(map(lambda x: x*2, [1,2,3]) )}      
""")



# %%
print("\n🔍 Attribute Handling")
print('''getattr(obj, "x") , setattr(obj, "x", 10)
hasattr(obj, "x") , delattr(obj, "x")''')


print("\n 🧰 Bytes & Memory")
print(f'''{bytes([65, 66])} | {bytearray([65, 66]) }     
{memoryview(b"ABC")}                 
{bin(10)} | {hex(255)}  | {oct(8)}  '''  )           

print('\n🧪 Code Execution & Debugging')
print(compile("x+1", "", "eval"))
print( eval("2+3")   , exec("x=5"))
# print(breakpoint()   )        
     

# %%
print("\n🧠 Objects & Classes")
print("""
object()                 # base object
type(3)                  # <class 'int'>
isinstance(3, int)       # True
issubclass(bool, int)    # True
id(3)                    # memory identity
callable(print)          # True
super()                  # access parent class
vars(obj)                # object's __dict__
dir(obj)                 # attributes list
hash("abc")              # hash value
""")