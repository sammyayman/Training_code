from dateutil.tz._common import enfold
print("\033c")
print(data := "Machine Learining")
# if we want f.format : 
print(f'{data}' if (data := "Machine Learning") else None)

# n = len(data)

# print(n if len (data) > 10  else None)

# if (n := len(data)) > 10:
#     print(n)

print(n if (n:= len(data) ) > 10 else None)

print(""""
    val = 100
    message = f"Value: {val}"
    print(message)                   # Value: 100
    print(val)                          # 100
    These use explicit assignme   

""")

message = f"Value: {val}" if (val := 100) else ""
print(message) ; print(val)




print("""
    x= 25
    print(x)
    print(x**2)

""")

print(x := 42 , f'x = {x} , x^2 = {x**2}')  # Output: 42
print()        # Output: 42


# Assign and pass to function
print("""       
    a = 10
    b = 20
    result = max(a, b)
    print(result)  # Output: 20
    print(a, b)    # Output: 10 20

""")
result = max(a := 10, b := 20)
print(a, b, result)  # Output: 20
print()    # Output: 10 20

# Assign intermediate values

squares = [(y := x**2) for x in range(5)]
print(squares)  


print("""
    a = 5
    b = 10
    c = 15
    total = a + b + c
    print(total)  # 30
    print(a, b, c)  # 5 10 15

    """)
# Assign and use in calculation
total = (a := 5) + (b := 10) + (c := 15)
print(f'{a}+{b}+{c} = {total}')   

print((x := 10) + (y := 20) + (z := 30))
print(x, y, z)  # Output: 10 20 30

# Assign and format

print("""
    x = 7
    y = x + 3
    print(y)

    """)
print(y := (x := 7) + 3)

value = abs(-15)
print(value)

print("""a = 3
b = a**2 + 2*a + 1
print(b)

x = 5
t = (x, x + 1)
print(t)   \n""")

print(value := abs(-15))
print(b := (a := 3)**2 + 2*a + 1)
print(t := (x := 5, x + 1))


print("""
      x = 10
      lst = [x, x*2, x*3]
      print(lst)
      
      name = "Python"
      length = len(name)
      print(f"{name} has {length} letters")
      
      
      x = 3
      d = {"x": x, "square": x*x}
      print(d)
      
      """)


print(lst := [(x := 10), x*2, x*3])
print(f"{name} has {len(name)} letters" if (name := "Python") else "")
print(d := {"x": (x := 3), "square": x*x})


print(""" 
      def f():
    return 5

    x = f()
    y = x + 1
    print(y)
    
    x = 2
    y = x + 3
    z = y * 2
    print(z)
      """)
def f(): return 5 
print((x := f()) + 1 , end = '  ,   ');print((y := (x := 2) + 3) * 2)


print("""
        t = (4, 5)
        result = t[0] + t[1]
        print(result)
        
        
        x = 2
        y = 3
        t = (x**2, y**2)
        print(t)
        
        t = (10, 20)
        a, b = t
        print(a + b)
        
        inner = (1, 2)
        outer = (inner, inner)
        print(outer)

      """)
print((t := (4, 5))[0] + t[1] ,end = " , ")
print(t := ((x := 2)**2, (y := 3)**2),end=' , ')
print(sum(t := (10, 20)),end=' , ')
print(outer := ((inner := (1, 2)), inner*3))


   
      
 


print("""
        x = 2
        y = 3
        lst = [x**2, y**2]
        print(lst)
        
        lst = [1, 2, 3]
        total = sum(lst)
        print(total)
        
        inner = ['X', 'Y']
        outer = [inner, inner]
        print(outer)
      """)
print(lst := [(x := 2)**2, (y := 3)**2],end=' , ')
print(sum(lst := [1, 2, 3]),end=' , ')
print(outer := [(inner := ["X", "Y"]), inner])


d = {"a": 1, "b": 2,"x": 3, "y": 4}
result = d["x"] + d["y"]
print(result)

print(d := {"a": 1, "b": 2})
print((d := {"x": 3, "y": 4})["x"] + d["y"])



print("""
        x = 5
        d = {"x": x, "square": x**2}
        print(d)
        
        d = {"a": 10, "b": 20}
        keys = list(d.keys())
        print(keys)
        
        
        inner = {"value": 7}
        outer = {"first": inner, "second": inner}
        print(outer)
""")

print(d := {"x": (x := 5), "square": x**2})
print(list((d := {"a": 10, "b": 20}).keys()))
print(outer := {"first": (inner := {"value": 7}), "second": inner.values()})








print(
    """
      
        length = len("hello")
        if length > 3:
             print(f"Length: {length}")  # Output: Length: 5
        
        
      value = 42
        if value % 2 == 0: print(f"Even: {value}")
            
            
        def get_number():
            return 10

        num = get_number()
        if num > 5:
            print(f"Number: {num}")  # Output: Number: 10
      
      
      items = [1, 2, 3]
      if items and len(items) > 2: print(f"Items: {items}")
            
            
      text = "Python"
      if text == "Python":  print(f"Text: {text}") 
      
      data = [1, 2, 3, 4]
      first = data[0]
    if first > 0:
            print(f"First: {first}")  
      
      """)

print(f"Length: {length}" if (length := len("hello")) > 3 else "")

print(f"Even: {value} " if (value := 42) % 2 == 0 else 0)

def get_number():
    return 10


print(f"Number: {num}"  if (num := get_number()) > 5 else 0)

print(f"Items: {items} " if (items := [1, 2, 3]) and len(items) > 2 else 0) 

if (text := "Python") == "Python":  print(f"Text: {text}") 
#OR 
print(f"Text: {text}" if (text := "Python") == "Python" else "")


print()
# if (first := data[0]) > 0:
#     print(f"First: {first}") 
#OR
print(data if (data := [1, 2, 3] ) else 0,
      f"First: {first}" if (first := data[0]) > 0 else 0)



print("""
      
        total = 0
        for x in [1, 2, 3, 4, 5]:
            total += x
        print(total)   # 15
        
        
        
        fact = 1
        for i in range(1, 6):
            fact *= i
        print(fact)   # 120

      """)


 
        
sums = [(T := T + x) for x in [1, 2, 3, 4, 5]] if not (T := 0) else None
print('+'.join(str(i) for i in sums) +' = ' , T)   # [1, 2, 6, 24, 120]


steps = [(fact := fact * i) for i in range(1, 6)] if (fact := 1) else None

print('*'.join(str(i) for i in steps) +' = ' , fact)   # [1, 2, 6, 24, 120]





print("""
1. Accumulate Until Threshold
        total = 0; i = 1
        while total < 10:
            total = total + i
            print(f"Added {i}, total: {total}")
            i += 1


 2. Read Input Until Condition
        inputs = []
        line = input("Enter number (0 to stop): ")
        while line != "0":
            inputs.append(int(line))
            line = input("Enter number (0 to stop): ")
        print(f"Inputs: {inputs}")
        # (Simulated; stops on "0")
        
        
        
        
3. Process List Elements
        data = [1, 2, 3, 4, 5]; i = 0
        while i < len(data) and data[i] < 4:
            item = data[i]
            print(f"Processing: {item}")
            i += 1


4. Factorial Calculation
        n = 5; fact = 1; i = 1
        while fact <= 120 and i < n:
            fact = fact * i
            print(f"i={i}, fact={fact}")
            i += 1
      """)


total = 0; i = 1
while (total := total + i) < 10:
    print(f"Added {i}, total: {total}")
    i += 1
print()
# Output: Added 1, total: 1\nAdded 2, total: 3\nAdded 3, total: 6\nAdded 4, total: 10



inputs = []
while (line := input("Enter number (0 to stop): ")) != "0":
    inputs.append(int(line))
print(f"Inputs: {inputs}")
# (Simulated; stops on "0")
print()



data = [1, 2, 3, 4, 5]; i = 0
while (item := data[i] if i < len(data) else None) and item < 4:
    print(f"Processing: {item}")
    i += 1
# Output: Processing: 1\nProcessing: 2\nProcessing: 3
print()



n = 5; fact = 1; i = 1
while (fact := fact * i) <= 120 and i < n:
    print(f"i={i}, fact={fact}")
    i += 1
# Output: i=1, fact=1\ni=2, fact=2\ni=3, fact=6\ni=4, fact=24
print()


# print("""""")