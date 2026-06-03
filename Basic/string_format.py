from math import pi
from this import d
var = 100 ; g = 9.8 ; name = 'Neo'
print(f'{var = } , {isinstance(var, int) = } , {pi * 100  =   }')
print(f'{pi = :.2f}  , {pi = :.4%} , {.561475 = :0.3%}')
print(f'{pi:.2e} , {pi:.2f} , {pi:.2%} ')
print(f'{g + pi = :.2f}')
print(f'{name = !s}')
print()

big_number = 123456789.24681012
print(f'{big_number:_} , {big_number = :,}')
print(f'{big_number:_.2f}, {big_number = :,.4f} , {big_number:e} , {big_number:.2e}')

space = ',.3f'
print(f'{big_number :{space}}')

print()


from datetime import datetime , date
now = datetime.now() ; today = datetime.now().date()
print(now , today, sep = '\t')
banana =' 🍌 ' ;apple = '🍎' ; pear = '🍐 pear'
print(f'{now = :%Y-%m-%d %H:%M:%S} ')
print(f'{now:%x} , {now:%X} , {now:%c}')

print(f'[{today!s}] {name!s} says : {banana!s}')
print(f'[{today!r}] {name!r} says : {apple!r}')
print(f'[{today!a}] {name!a} says : {pear!a}')



# print()

# user = "Gourge" ; n = 25
# path = fr'C:\Users\{user}\Desktop'
# print( r'C:\Users\{user}\Desktop', path )
# print(f'user = {user:^{n}} : {path}')

# l = 'left' ; r = 'right' ; c = 'center'
# print(f'{l:,<10}')
# print(f'{r:.>{n}}')
# print(f'{c:_^{n}}')










# #%%
# n = 251

# # % formatting (C-style)
# print("Decimal: %d, Hex: %X, Binary: %s, Octal: %o" % (n, n, bin(n), n))

# # .format() method
# print("Decimal: {}, Hex: {:X}, Binary: {}, Octal: {:o}".format(n, n, bin(n), n))

# # f-string (modern)
# print(f"Decimal: {n}, Hex: {n:X}, Binary: {bin(n)}, Octal: {n:o}")






# I, R = 2.5, 10

# # Calculate values
# V = I * R
# P = V * I
# PF = P / (V * I)   # In DC circuits this will always be 1.0

# # % formatting
# print("Voltage = %.2f V, Power = %.2f W, PF = %.2f" % (V, P, PF))

# # .format()
# print("Voltage = {:.2f} V, Power = {:.2f} W, PF = {:.2f}".format(V, P, PF))

# # f-string
# print(f"Voltage = {V:.2f} V, Power = {P:.2f} W, PF = {PF:.2f}\n")



# import math

# r = 3.0
# h = 10.0   # height of cylinder

# # Circle calculations
# circle_perimeter = 2 * math.pi * r
# circle_area = math.pi * r**2

# # Cylinder calculations
# cylinder_perimeter = 2 * math.pi * r   # base circumference
# cylinder_area_lateral = 2 * math.pi * r * h
# cylinder_area_total = 2 * math.pi * r * (r + h)

# # % formatting
# print("Circle: Perimeter = %.3f m, Area = %.3f m^2" % (circle_perimeter, circle_area))

# # .format()
# print("Cylinder: Base Perimeter = {:.3f} m, Lateral Area = {:.3f} m^2, Total Area = {:.3f} m^2"
#       .format(cylinder_perimeter, cylinder_area_lateral, cylinder_area_total))

# print(" Result ".center(70, '_') )
# # f-string
# result = f"""
# Circle: Perimeter = {circle_perimeter:.3f} m, Area = {circle_area:.3f} m^2"
# Cylinder: Base Perimeter = {cylinder_perimeter:.3f} m
# Lateral Area = {cylinder_area_lateral:.3f} m^2
# Total Area = {cylinder_area_total:.3f} m^2


# """
# print(result)
# # %%

# class Text : 
#       def __init__(self, text):
#             self.text = text
            
#       def __format__(self, format_spec):
#             match format_spec:
#                   case 'U':
#                         return self.text.upper()
#                   case 'L':
#                         return self.text.lower()
#                   case 'T':
#                         return self.text.title()
#                   case 'CAP':
#                         return self.text.capitalize()
#                   case 'leng':
#                         return str(len(self.text))
#                   case _:
#                         raise ValueError(f'"{format_spec }" does not exist')
                  

# my_text = Text(user)
# print(f'{my_text:U} , {my_text:L} , {my_text:CAP}')
# print(f'{my_text:leng}')
