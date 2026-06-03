# print("1) --- Usual for loop ---")
# numbers = [1, 2, 3, 4, 5]
# for n in numbers:
#     print(f"n={n}, square={n*n}")

# print()
# print("--- One-liner for loop ---")
# [print(f"n={n}, square={n*n}") for n in [1, 2, 3, 4, 5]]

# print()
# print("2) --- Usual for loop (strings) ---")
# words = ["apple", "banana", "cherry"]
# for w in words:
#     print(f"word={w}, upper={w.upper()}")

# print()
# print("--- One-liner for loop (strings) ---")
# [print(f"word={w}, upper={w.upper()}") for w in ["apple", "banana", "cherry"]]

# print()
# print("3) --- Usual for loop (string characters) ---")
# text = "Ayman"
# for ch in text:
#     print(f"ch={ch}, code={ord(ch)}")

# print()
# print("--- One-liner for loop (string characters) ---")
# [print(f"ch={ch}, code={ord(ch)}") for ch in "Ayman"]

# print()
# print("4) --- Usual for loop (string with if: vowels) ---")
# text = "Ayman123!"
# for ch in text:
#     if ch.isalpha() and ch.lower() in {"a","e","i","o","u"}:
#         print(f"{ch}: vowel")
#     elif ch.isalpha():
#         print(f"{ch}: consonant")
#     else:
#         print(f"{ch}: skipped")

# print()
# print("--- One-liner (string with if: vowels) ---")
# [print(f"{ch}: " + ("vowel" if ch.isalpha() and ch.lower() in {'a','e','i','o','u'} else "consonant" if ch.isalpha() else "skipped")) for ch in "Ayman123!"]

# print()
# print("5) --- Usual for loop (string with if: uppercase) ---")
# text2 = "HelloWorld"
# for ch in text2:
#     if ch.isupper():
#         print(f"{ch}: UPPER")
#     else:
#         print(f"{ch}: lower")

# print()
# print("--- One-liner (string with if: uppercase) ---")
# [print(f"{ch}: " + ("UPPER" if ch.isupper() else "lower")) for ch in "HelloWorld"]

# print()
# print("6) --- Usual for loop (email char categories) ---")
# email = "user.name+tag@example-mail.com"
# for ch in email:
#     if ch.isalpha():
#         print(f"{ch}: letter")
#     elif ch.isdigit():
#         print(f"{ch}: digit")
#     elif ch in {"@", ".", "-", "+", "_"}:
#         print(f"{ch}: special")
#     else:
#         print(f"{ch}: other")

# print()
# print("--- One-liner (email char categories) ---")
# [print(f"{ch}: " + ("letter" if ch.isalpha() else "digit" if ch.isdigit() else "special" if ch in {'@','.', '-', '+', '_'} else "other")) for ch in "user.name+tag@example-mail.com"]





# print()
# print("7) --- Usual for loop (password strength scan) ---")
# password = "P@ssw0rd#2026!"
# upper = lower = digits = specials = 0
# for ch in password:
#     if ch.isupper():
#         upper += 1; print(f"{ch}: upper")
#     elif ch.islower():
#         lower += 1; print(f"{ch}: lower")
#     elif ch.isdigit():
#         digits += 1; print(f"{ch}: digit")
#     elif ch in {"@", "#", "$", "%", "!", "*"}:
#         specials += 1; print(f"{ch}: special")
#     else:
#         print(f"{ch}: other")
# strong = (upper > 0 and lower > 0 and digits > 0 and specials > 0 and len(password) >= 8)
# if strong:
#     print("Password looks strong")
# else:
#     print("Password needs more variety or length")

# print()
# print("--- One-liner (password strength scan) ---")
# [print(f"{ch}: " + ("Upper !" if ch.isupper() else "Lower !" if ch.islower() else "Digit !" if ch.isdigit() else "special" if ch in {'@','#','$','%','!','*'} else "other"), end=", ") for ch in password]
# print()
# print("--- One-liner (password flags, walrus) ---")
# [print(
#     (u := ch.isupper(), l := ch.islower(), d := ch.isdigit(), s := ch in {'@','#','$','%','!','*'}) and
#     f"{ch}: " + ("Upper !" if u else "Lower !" if l else "Digit !" if d else "special" if s else "other") + f" [u={u},l={l},d={d},s={s}]",
#     end=", "
# ) for ch in password]




# print()
# print("8) --- Usual for loop (tuple numbers) ---")
# tnums = (1, 2, 3, 4)
# for n in tnums:
#     print(f"n={n}, cube={n**3}")

# print()
# print("--- One-liner (tuple numbers) ---")
# [print(f"n={n}, cube={n**3}") for n in (1, 2, 3, 4)]

# print()
# print("9) --- Usual for loop (tuple words, length) ---")
# twords = ("alpha", "beta", "gamma")
# for w in twords:
#     print(f"{w}: len={len(w)}")

# print()
# print("--- One-liner (tuple words, length) ---")
# [print(f"{w}: len={len(w)}") for w in ("alpha", "beta", "gamma")]

# print()
# print("10) --- Usual for loop (set categories) ---")
# s = {'A', 'b', '3', '@', 'Z', '0', '#'}
# for ch in s:
#     if ch.isalpha():
#         print(f"{ch}: letter")
#     elif ch.isdigit():
#         print(f"{ch}: digit")
#     elif ch in {'@','#','$','%','!','*'}:
#         print(f"{ch}: special")
#     else:
#         print(f"{ch}: other")

# print()
# print("--- One-liner (set categories) ---")
# [print(f"{ch}: " + ("letter" if ch.isalpha() else "digit" if ch.isdigit() else "special" if ch in {'@','#','$','%','!','*'} else "other")) for ch in {'A','b','3','@','Z','0','#'}]

# print()
# print("11) --- Usual for loop (dict items) ---")
# d = {"a": 1, "b": 2, "c": 3}
# for k, v in d.items():
#     print(f"{k} -> {v}")

# print()
# print("--- One-liner (dict items) ---")
# [print(f"{k} -> {v}") for k, v in {"a":1,"b":2,"c":3}.items()]

# print()
# print("12) --- Usual for loop (dict filter values>1) ---")
# d2 = {"x": 0, "y": 2, "z": 5}
# for k, v in d2.items():
#     if v > 1:
#         print(f"{k} -> {v}")

# print()
# print("--- One-liner (dict filter values>1) ---")
# [print(f"{k} -> {v}") for k, v in {"x":0,"y":2,"z":5}.items() if v > 1]

# print()
# print("13) --- Nested for loop (multiplication table) ---")
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} x {j} = {i*j}")
#     print()  # blank line after each row

# print()
# print("14) --- Nested for loop (matrix iteration) ---")
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in matrix:
#     for value in row:
#         print(f"value={value}", end=" ")
#     print()  # new line after each row

# print()
# print("15) --- Nested for loop (dictionary of lists) ---")
# dlist = {"group1": [1, 2], "group2": [3, 4], "group3": [5]}
# for k, vals in dlist.items():
#     for v in vals:
#         print(f"{k}:{v}", end=" ")
#     print()

# print()
# print("16) --- Nested for loop (grid coordinates) ---")
# rows, cols = 3, 4
# for i in range(rows):
#     for j in range(cols):
#         print(f"({i},{j})", end=" ")
#     print()

# print()
# print("17) --- Nested for loop (string matrix upper) ---")
# words = [["hi", "ok"], ["go", "up"], ["py", "ai"]]
# for row in words:
#     for w in row:
#         print(w.upper(), end=" ")
#     print()



# # Each sublist represents resources from a different planet
# print("17) Each sublist represents resources from a different planet ")
# resource_donators = [[8, 6, 3], [9, 2, 7], [4, 1, 5]]
# total_resources = 0
# print("--- Summing All Resources ---")
# for planet in resource_donators:
#     for resource in planet:
#         total_resources += resource
# print(f"Total resources gathered: {total_resources}")


# rows = 5
# print("18)--- Number Pyramid ---")
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()  # Moves to the next row

# print()
# print("18) --- Nested for loop (group-wise mean) ---")
# groups = [[10, 20, 30], [5, 15], [100, 200]]
# for idx, vals in enumerate(groups, start=1):
#     total = 0
#     count = 0
#     for v in vals:
#         total += v
#         count += 1
#     mean = total / count if count else 0
#     print(f"group{idx}: mean={mean}")

# print()
# print("19) --- Nested for loop (frequency table) ---")
# data = [("red", "S"), ("blue", "M"), ("red", "L"), ("green", "S"), ("red", "S"), ("blue", "L")]
# colors_order = ["red", "blue", "green"]
# sizes_order = ["S", "M", "L"]
# for sz in sizes_order:
#     for col in colors_order:
#         cnt = 0
#         for c0, s0 in data:
#             if c0 == col and s0 == sz:
#                 cnt += 1
#         print(f"{sz}-{col}:{cnt}", end=" ")
#     print()

# print()
# print("20) --- Nested for loop (shape: hollow square) ---")
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# print()
# print("21) --- Nested for loop (shape: right-aligned triangle) ---")
# rows = 5
# for i in range(rows):
#     for j in range(rows):
#         if j < rows - i - 1:
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print()

# print()
# print("22) --- Nested for loop (shape: X pattern) ---")
# size = 7
# for i in range(size):
#     for j in range(size):
#         if i == j or i + j == size - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# print()
# print("23) --- Nested for loop (math: even product mask) ---")
# for i in range(1, 6):
#     for j in range(1, 6):
#         prod = i * j
#         if prod % 2 == 0:
#             print(f"{prod:2d}", end=" ")
#         else:
#             print(" .", end=" ")
#     print()

# print()
# print("24) --- Nested for loop (math: circle threshold) ---")
# r = 3
# for y in range(-r, r + 1):
#     for x in range(-r, r + 1):
#         if x * x + y * y <= r * r:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# print()
# print("25) --- Nested for loop (math: saddle sign map) ---")
# for y in range(-3, 4):
#     for x in range(-3, 4):
#         val = x * x - y * y
#         if val > 0:
#             print("+", end="")
#         elif val == 0:
#             print("0", end="")
#         else:
#             print("-", end="")
#     print()


# print("26) creating a 5x5 matrix")
# data = list(range(1, 26))  # [1, 2, ..., 25]
# for i in range(0, len(data), 5):   # step by 5
#     row = data[i:i+5]              # slice 5 elements
#     print(row)

# data = list(range(1, 26))
# for i in range(0, len(data), 5):
#     row = data[i:i+5]
#     print(" | ".join(str(x).rjust(2) for x in row))

# # OR : 
# data = list(range(5, 30))  # [1, 2, ..., 21]

# count = 0
# for val in data:
#     print(str(val).rjust(5), end=" ")
#     count += 1

#     # Every 5th element → new row
#     if count % 5== 0:print()


print("\n"*3)
print("\t"," One Liner for loop with Numbers  ".center(100, '*'))

print("\n","Ex (0)".center(50, '-'))
result = []
"""for x in range(5):
    result.append(x + 1)"""
    

result = [x + 1 for x in range(5)]   
print(result) 
    
result = []
# for x in range(5):
#     result.append(x - 1)
    
result = [x - 1 for x in range(5)]
print(result) 


result = []
# for x in range(5):
#     result.append(x * 2)

result = [x * 2 for x in range(5)]
print(result) 


print("\n","Ex (1)".center(50, '-'))

Rang = range(0,10,2)    
for x in Rang: print(x+2, end=' ')
print("\n")
[print(x+2, end=' ') for x in Rang]
print("\n list :")
lst = []
for x in Rang: lst.append(x+2)
print(lst)
print( [str(x+2) for x in Rang])
print( list(str(x+2) for x in Rang))
print( tuple(str(x+2) for x in Rang))
print( tuple(str(x+2) for x in Rang))
print({str(x+2) for x in Rang})



print("\n","Ex (1.5)".center(50, '-'))


start = 1
cols = 4
row = []

value = start
for c in range(cols):
    row.append(value)
    value += 5
# row => [1, 6, 11, 16]

start = 1
cols = 4
row = [start + c * 5 for c in range(cols)] ; print(row)

 

start = 20
cols = 5
row = []

value = start
for c in range(cols):
    row.append(value)
    value -= 3
# row => [20, 17, 14, 11, 8]
start = 20
cols = 5
row = [start - c * 3 for c in range(cols)];print(row)
# [20, 17, 14, 11, 8]

start = 1
cols = 5
row = []

value = start
for c in range(cols):
    row.append(value)
    value *= 2
# row => [1, 2, 4, 8, 16]
start = 1
cols = 5
row = [start * 2**c for c in range(cols)] ; print(row)
# [1, 2, 4, 8, 16]
 

print("""value = start
result = []
for i in range(n):
    result.append(value)
    value += step """)



print("\n","Ex (2)".center(50, '-'))

value = 3
lst = []
for _ in range(5):
    
    print(value, end=' ')
    lst.append(value * 4)
    value += 1
print(lst)

value = 3; lst = [];
[print(value, end=' ') or lst.append(value * 4) or (value := value + 1) for _ in range(5)]; print(lst)




print("\n","Ex (3)".center(50, '-'))
x = 1
for _ in range(5):
    print(x - 0.5, end=' ')
    x *= 3
print("\n")

x = 1    
[print(x - 0.5, end=' ') or (x := x * 3) for _ in range(5)]
print("\n")

x = 1; print( [(x := x * 3) / 3- 0.5 for _ in range(5)])

x = 1
print(*[(x := (x * 3 if i > 0 else x)) - 0.5 for i in range(5)])




print("\n","Ex (4)".center(50, '-'))
x = 100
result = []

for _ in range(5):
    x = x -5          # update x
    result.append(x)   # store in the list

print(result)

result = [(x := x -10) for _ in range(5)]
print(result)






print("\n","Ex (5)".center(50, '-'))
x = 0; y = 100 ;z = 1
result = []

for _ in range(5):
    x += 1.5
    y -= 4
    z *= 2
    result.append((x + z) / y)

print([f'{num:.2f}' for num in result])


x, y, z = 0, 100, 1
 

result = [round(((x := x + 1.5) + (z := z * 2)) / (y := y - 4), 4) for _ in range(5)]
x, y, z = 0, 100, 1
result = [f"{((x := x + 1.5) + (z := z * 2)) / (y := y - 4):.2f}" for _ in range(5)]
print(result)





print("\n","Ex (6)".center(50, '-'))

x, y, z = 0, 100, 1

result = []

for _ in range(5):
    result.append((y - x*10 ) / z)
    x += 1.5
    y -= 4
    z *= 2

print([f'{num:.2f}' for num in result])

x, y, z = 0, 100, 1
result = [((y - x*10) / z, x := x + 1.5, y := y - 4, z := z * 2)[0]
          for _ in range(5)]
print([f"{num:.2f}" for num in result])



x = 1

value = (x + 1, print("updating x"), x * 10)[0]

print(value)







print("\n","Ex (7)".center(50, '-'))
resistance = 0; resistors = [10, 20, 30, 40, 50]; 

"""for r in resistors:
    print(f"R_total: {resistance:.0f} ohms")
    resistance += r

print(f"Final R_total: {resistance} ohms") """


[print(f"R_total: {resistance:.0f} ohms") or (resistance := resistance + r) for r in resistors]; 
print(f"Final R_total: {resistance} ohms")







print("\n","Ex (8)".center(50, '-'))

import math; Vc = 0; V0 = 5; tau = 1; times = [0.5, 1, 1.5, 2, 2.5]; 

"""for t in times:
    print(f"t={t}s: Vc={Vc:.2f}V")
    Vc = V0 * (1 - math.exp(-t / tau))

print(f"Final Vc: {Vc:.2f}V")"""


[print(f"t={t}s: Vc={Vc:.2f}V") or (Vc := V0 * (1 - math.exp(-t / tau))) for t in times]; 
print(f"Final Vc: {Vc:.2f}V")






print("\n","Ex (9)".center(50, '-'))

import math; area = 0; radii = [1, 2, 3, 4, 5]; 

"""for r in radii:
    print(f"Total Area: {area:.2f} sq units")
    area += math.pi * r**2 """


[print(f"Total Area: {area:.2f} sq units") or (area := area + math.pi * r**2) for r in radii]; 
print(f"Final Area: {area:.2f} sq units")




print("\n","Ex (10)".center(50, '-'))


perimeter = 0; sides = [1, 2, 3, 4, 5]; 

"""for s in sides:
    print(f"Total Perimeter: {perimeter} units")
    perimeter += 4 * s 

print(f"Final Perimeter: {perimeter} units") """

[print(f"Total Perimeter: {perimeter} units") or (perimeter := perimeter + 4 * s) for s in sides]; 
print(f"Final Perimeter: {perimeter} units")






print("")
print("\n","Ex (11)".center(50, '-'))

import numpy as np

rows, cols = 4, 4 ; data = []  ; value = 1        # will become a list of rows
"""for r in range(rows):
    row = []
    for c in range(cols):
        row.append(value)
        value += 1
    data.append(row)

arr_for = np.array(data)
print(arr_for)

print(arr_for.shape)"""




""" for r in range(rows):
    row = [r * cols + c + 1 for c in range(cols)]
    data.append(row)

print(np.array(data)) """



data = [[r * cols + c + 1 for c in range(cols)] for r in range(rows)]

print(np.array(data))



print("\n","Ex (12)".center(50, '-'))

rows, cols = 4, 4
data = []

for r in range(rows):
    row = []
    value = 1 + r * cols       # starting value for this row
    for c in range(cols):
        row.append(value)
        value += 1
    data.append(row)
print(np.array(data))
   
    
rows, cols = 4, 4
data = []

for r in range(rows):
    value_start = 1 + r * cols
    row = [value_start + c for c in range(cols)]
    data.append(row)    
print(data)

data = [[1 + r * cols + c for c in range(cols)] for r in range(rows)]
print(np.array(data))

print([[value_start + c for c in range(cols)] for r in range(rows) if (value_start := 1 + r * cols)])





print("\n","Ex (12)".center(50, '-'))
rows, cols = 3, 4
data = []

for r in range(rows):
    row = []
    value = 2          # inner loop starts from 2 (same for every row)
    for c in range(cols):
        row.append(value)
        value += 5
    data.append(row)
print(np.array(data))

data = []
for r in range(rows):
    row = [2 + c*5 for c in range(cols)]   # 2 is the starting value in the inner loop
    data.append(row)
print(data)
data = [[2 + c * 5 for c in range(cols)] for r in range(rows)]; print(data)









print("\n","Ex (13)".center(50, '-'))
rows, cols = 3, 4
data = []
value = 2          # shared across all rows

for r in range(rows):
    row = []
    for c in range(cols):
        row.append(value)
        value += 5
    data.append(row)
print(data)

rows, cols = 3, 4
data = []

for r in range(rows):
    row = [2 + 5 * (r * cols + c) for c in range(cols)]
    data.append(row)

print(np.array(data))

print(*[[2 + 5 * (r * cols + c) for c in range(cols)] for r in range(rows)][0:2])








print("\n","Ex (14)".center(50, '-'))


fact = 1 ; n = 5

for i in range(n):
    print(f"n! = {fact}  ", end=' ')
    fact *= (i + 1)

print(f"\n∏_(k=1)^n k{n}!: {fact}")


# One-liner
fact = 1; n = 5; 
[print(f"n! = {fact}  ", end=' ') or (fact := fact * (i + 1)) for i in range(n)]; 
print(f"\n∏_(k=1)^n k{n}!: {fact}")

print("\n","Ex (15)".center(50, '-'))


total = 0  ; n = 5

for i in range(n):
    print(f"Sum: {total}", end=' ')
    total += (i + 1)

print(f"\n∑_(i=1)^n i ,n = {n}  =   {total}")

# One-liner
total = 0; n = 5; 
[print(f"Sum: {total}", end=' ') or (total := total + (i + 1)) for i in range(n)]
print(f"\n∑_(i=1)^n i ,n = {n}  =   {total}")


print("\n","Ex (16)".center(50, '-'))

print("\nSummation\n")
steps = [1, 2, 6, 24, 120]
result = []
S = 0
for item in steps:
    S += item
    result.append(str(item))

print('+'.join(result) + ' = ', S)  # Output: 1+2+6+24+120 = 153



print("\n--- One-liner (walrus operator) ---")
steps = [1, 2, 6, 24, 120]
result = []
S = 0
A = [result.append(str(item)) or (S := S + item) for item in steps]

print(result , A[-1])
print('+'.join(result) + ' = ', S)  # Output: 1+2+6+24+120 = 153
print(A[-1] == S)


steps = [1, 2, 6, 24, 120]
S = 0
R = [str(item) if  (S := S + item) else  "" for item in steps]

print(result == R)



print("\n","Ex (17)".center(50, '-'))

steps = [1, 2, 6, 24, 120]
result = []
F = 1
for item in steps:
    F *= item
    result.append(str(item))
print('*'.join(result) + ' = ', F)  # Output: 1*2*6*24*120 = 34560

print("\n--- One-liner (walrus operator) ---")
steps = [1, 2, 6, 24, 120]
result = []
F = 1
B = [result.append(str(item)) or (F := F * item) for item in steps]
print(B , result)
print('*'.join(result) + ' = ', F)  # Output: 1+2+6+24+120 = 153
print(B[-1] == F)


F = 1
R = [str(item) if  (F := F * item) else  None for item in steps]
print(R == result)


print()
print("\n","Ex (18)".center(50, '-'))

voltages = [5, 9, 12]          # V in volts
resistances = [100, 220, 330]  # R in ohms
currents = [v / r for v, r in zip(voltages, resistances)] # I = V / R (amps)
print([round(x, 3) for x in currents])


print("\n","Ex (19)".center(50, '-'))

caps = [1e-6, 4.7e-6, 10e-6]  ; V=5  # capacitances in farads
energies = [0.5 * C * V**2 for C in caps]  # energy in joules
print(np.array(energies))

print("\n","Ex (20)".center(50, '-'))

voltages = [5, 9, 12]          # volts
resistances = [100, 220, 330]  # ohms

power_table = [[V**2 / R for R in resistances] for V in voltages]
# rows: each V, columns: each R : 

print( np.array([[f"{p:.3f}" for p in row] for row in power_table]))

print("\n","Ex (21)".center(50, '-'))


R_values = [1e3, 4.7e3, 10e3]      # resistances in ohms
C_values = [1e-6, 4.7e-6, 10e-6]   # capacitances in farads

tau_table = [[R * C for C in C_values] for R in R_values]
# rows: each R, columns: each C
print( np.array([[f"{p:.3f}" for p in row] for row in tau_table]))





print("\n","Ex (22)".center(50, '-'))


principals = [1000, 2000, 5000]          # P
rates = [0.05, 0.08]                     # i (per year)
years = [1, 3, 5]                        # n (years)

FV_table = [[[P * (1 + i * n) for n in years] for i in rates] for P in principals]
np.set_printoptions(precision=2, suppress=True, floatmode="fixed")

print(np.array(FV_table))

print("\n","Ex (23)".center(50, '-'))


rates = [0.03, 0.05, 0.07]       # interest rates
periods = [1, 5, 10]             # years

FP_factors = np.array([[(1 + i)**n for n in periods] for i in rates])
print(FP_factors)

print("\n","Ex (24)".center(50, '-'))


rates = [0.04, 0.06, 0.1]
periods = [1, 3, 5, 10]

PF_factors = [[1 / (1 + i)**n for n in periods] for i in rates]
print(np.array(PF_factors))


print("\n","Ex (25)".center(50, '-'))


P = 10000      # initial cost
S = 1000       # salvage
N = 5          # life in years
years = range(N + 1)

BV_table = [[P - k * (P - S) / N for k in years]]  
print(BV_table )# single row, all book values
