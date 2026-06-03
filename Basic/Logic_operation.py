def xand(a, b):
    return ~(a ^ b)  # bitwise XNOR

values = [(True, True), (False, False), (False, True), (False,False)]

for a, b in values:
    print(f"A={a}, B={b} ------------>| XOR={a ^ b} | XAND={not(a ^ b)}")
    
def xand_xor(a, b):
    return f"XAND : ~({a} ^ {b}) = {~(a ^ b)}  , XOR : {a} ^ {b} = {a ^ b}"  # bitwise XNOR

# print( 5 ^ 3)       # XOR → 6 (0101 ^ 0011 = 0110)
print(xand_xor(-3, 7))  # XAND → -7 (bitwise complement of 6)


# Logical operations
A, B = [True, 0,True], [False,1, False]
for a, b in zip(A, B):
                print(f"A :{a} and B :{b}    ======> {a and b}", end = " \t")    # AND → False
                print(f"A : {a} or B : {b}   =====> {a or b}")    # OR  → True
                print(f"\t \t\tnot A:  {a}  ======>{not a} , ~B : ~{b} ======> {~b}")     # NOT → False
                print(f"\nA  :{a} ^ B : {b}  ======>", a ^ b , end = " \t")     # XOR → True (different values)
                print(f"not (A {a} ^ B {b})  =======>", not (a ^ b),'\n ------------------------------------------')  # XAND → False (XNOR)


values= [(5, 3)]
for a,b in values :
    print(f"AND : a & b = {a} & {b}   → 0101 & 0011 = 0001 =", a & b)       # AND → 0101 & 0011 = 0001 = 1
    print(f"OR : a | b = {a} | {b}   → 0101 | 0011 = 0111 = ", a | b)       # OR  → 0101 | 0011 = 0111 = 7
    print(f"NOT : ~a   = ~{a}  → ~0101 = -(5+1) =  ", ~a)           # NOT → ~0101 = -(5+1) = -6
    print(f"XOR : a ^ b = {a} ^ {b}  → 0101 ^ 0011 = 0110 =  ", a ^ b)       # XOR → 0101 ^ 0011 = 0110 = 6
    print(f"XAND : ~(a ^ b) = ~({a} ^ {b}) → ~(6) = ", ~(a ^ b)) # XAND → ~(6) = -7
    



a, b, c, x, y, z = [1, 5, 3, 7, 9, 1]

vars = [("a", a), ("b", b), ("c", c), ("x", x), ("y", y), ("z", z)]

for name, value in vars:
    output = f"""
{name} = {value}

Comparison with b:
{name} < b   : {value < b} ,    {name} <= b  : {value <= b}
{name} > b   : {value > b} ,    {name} >= b  : {value >= b}
{name} == b  : {value == b} ,   {name} != b  : {value != b}

Logical operations:
{name} and b : {bool(value and b)} ,    {name} or b  : {bool(value or b)}
not {name}   : {not value}

Bitwise operations:
{name} & b   : {value & b} ,    {name} | b   : {value | b}
~{name}      : {~value}
{name} ^ b   : {value ^ b} ,    ~({name} ^ b): {~(value ^ b)}

Combined expressions:
a < x and b >= y or c != z : {a < x and b >= y or c != z}
a < x & b >= y | c != z    : {a < x & b >= y | c != z}
----------------------------
"""
    print(output)

#%%
A = [1, 2, 3, 4, 5]        # Math
B = [4, 5, 6, 7]           # Physics
C = [5, 7, 8, 9]           # Programming

setA , setB , setC = set(A) , set(B) , set(C)
union_all = setA | setB | setC   # OR
print("Union (A ∪ B ∪ C):", union_all)

intersection_all = setA & setB & setC   # AND
print("Intersection (A ∩ B ∩ C):", intersection_all)

N = 10
p_union = f"{len(union_all)} / {N} = {len(union_all)/N}"
p_intersection = len(intersection_all) / N

print("P(A ∪ B ∪ C) = ", p_union)
print(f"P(A ∩ B ∩ C) = {p_intersection:.2f}")
print()
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
C = {5, 7, 8, 9}
U = set(range(1,11))   # Universal set {1,...,10}

# XOR: symmetric difference
xor_AB = A ^ B

print("A XOR B =", xor_AB)

# XAND: intersection (exclusive AND)
xand_AB = A & B
print("A XAND B =", xand_AB)

# NOT: complement of A
not_A = U - A
notB = U - B
notC = U - C

print("NOT A =", not_A)
print("NOT B =", notB)
print("NOT C =", notC)



# Probabilities
N = len(U)
p_xor = len(xor_AB)/N
p_xand = len(xand_AB)/N
p_notA = len(not_A)/N

print(f"P(A XOR B) = {p_xor:.2f}")
print(f"P(A XAND B) = {p_xand:.2f}")
print(f"P(NOT A) = {p_notA:.2f} , P(NOT B) = {len(notB)/N:.2f} , P(NOT C) = {len(notC)/N:.2f}")



# %%
A = {1, 2, 3}          # Event A: rolling ≤ 3
B = {2, 4, 6}          # Event B: rolling even
C = {frozenset({1, 3}), frozenset({5})}   # Event C: rolling odd (nested sets)
U = {frozenset({1, 2, 3}), 4, 5, 6}       # Universal set with nested

# Union and intersection
union_all = A | B        # works fine with normal sets
intersection_all = A & B # intersection of A and B

print("Union (A ∪ B):", union_all)
print("Intersection (A ∩ B):", intersection_all)

# Subset checks
print("Is A ⊆ {1..6}?", A.issubset({1,2,3,4,5,6}))
print("Is B ⊂ {1..6}?", B < {1,2,3,4,5,6})
print("Is 2 ∈ A?", 2 in A)

# Nested membership
print("Is {1,3} ∈ C?", frozenset({1,3}) in C)
print("Is {1,2,3} ∈ U?", frozenset({1,2,3}) in intersection_all)


# Define sets
D = {"Mickey", "Donald", "Goofy",  "Mini", "Deyziy", "Pete"}
SEx = {"Cloud", "Sephiroth", "Zack"}
KH = {"Sora", "Riku", "Kairi",  "Donald", "Goofy","Mickey"}  # include Mickey/King Mickey to show overlap

# Union of origin sets

U = D | SEx | KH

# KH_crossover defined using intersection (characters from Disney or SquareEnix that are also KH main)
KH_crossover = (D | SEx) & KH

# Intersections with each source set
cross_with_disney = KH_crossover & D
cross_with_sqex = KH_crossover & SEx
cross_with_khmain = KH_crossover & KH

# Print results
print("Disney =", D)
print("SquareEnix =", SEx)
print("KH_main =", KH)
print()
print("Union U =", U)
print("KH_crossover = (D ∪ SEx) ∩ KH =", KH_crossover)
print()
print("KH_crossover ∩ D =", cross_with_disney)
print("KH_crossover ∩ SEx =", cross_with_sqex)
print("KH_crossover ∩ KH =", cross_with_khmain)
print()
# Relations using set methods
print("KH_crossover ⊆ U ?", KH_crossover.issubset(U))
print("KH_crossover ⊂ U ? (proper subset)", KH_crossover < U)
print("D ⊆ U ?", D.issubset(U))
print("SEx ⊆ U ?", SEx.issubset(U))
print("KH ⊆ U ?", KH.issubset(U))
print("U ⊇ KH_crossover ?", U.issuperset(KH_crossover))
print("'Mickey' ∈ KH_crossover ?", "Mickey" in KH_crossover)
print("'Cloud' ∈ KH_crossover ?", "Cloud" in KH_crossover)


U = set(range(1,13))
A = set(range(1,7))            # {1,2,3,4,5,6}
B = {2,4,6,8,10,12}
C = {3,6,9,12}
print()
def P(s): return len(s)/len(U)

print("U =", U , '\n')

print("A =", A, "P(A) =", P(A) , "B =", B, "P(B) =", P(B) , "C =", C, "P(C) =", P(C))
print()
print("A ∪ B =", A|B, "P =", P(A|B), "A ∩ B =", A&B, "P =", P(A&B),"A ∩ B ∩ C =", A&B&C, "P =", P(A&B&C),sep= "  ") 
print()
print("A ⊆ U ? : ", A.issubset(U),"A ⊂ U ? : ", A < U,"C ⊆ B ? : ", C.issubset(B), "C ⊂ B ? : ", C < B , sep= " ")
print()
 
print("B ⊇ {2,4,6} ? : ", B.issuperset({2,4,6}), "B ⊃ {2,4} : ?", B > {2,4},"A ⊇ C ? : ", A.issuperset(C) , sep= " ")
print()

print("A ⊃ C ? : ", A > C, "2 ∈ A ? : ", 2 in A, "9 ∉ A ? : ", 9 not in A , sep = "  ")
