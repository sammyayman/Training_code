print('\033c')
print("  Function without argument   ".center(100,'-') ,'\n')
# print("Ex 1) : ")
# def test() : 
#     print("Data Analysis",end=' ------->   ') ; return 'Machine Learrning'
    
    
# print(test , test(),sep='   next    ') ; test(),print('\n')

 
 
print("Ex 2) : ")
# from pprint import pprint

# def get_video_game_info():
#     # String: Game title
#     title = "Super Mario Odyssey"
    
#     # List: Levels
#     levels = ["Cap Kingdom", "Cascade Kingdom", "Sand Kingdom"]
    
#     # Tuple: High scores (immutable)
#     high_scores = (15000, 20000, 25000)
    
#     # Set: Unique power-ups
#     power_ups = {"Super Mushroom", "Fire Flower", "Cape Feather"}
    
#     # Dictionary: Game data
#     game_data = {
#         "title": title,
#         "levels": levels,
#         "high_scores": high_scores,
#         "power_ups": power_ups
#     }
    
#     return game_data

# # Call the function
# info = get_video_game_info()
# pprint(info, sort_dicts=False)


 
# print('\nEx 3')

# def get_full_game_data():
#     # String
#     favorite_game = "The Legend of Zelda: Breath of the Wild"

#     # List
#     top_games = ["Elden Ring", "The Last of Us", "Minecraft", "Fortnite", "Valorant"]

#     # Tuple
#     console_info = ("PlayStation 5", 499, 825, "SST")
#     # (name, price, storage_gb, type)

#     # Set
#     game_genres = {"RPG", "FPS", "Strategy", "Adventure", "Puzzle", "Sports"}

#     # Dictionary
#     player_profile = {
#         "username": "ProGamer92",
#         "level": 45,
#         "playtime_hours": 320,
#         "main_game": "League of Legends",
#         "rank": "Diamond"
#     }

#     # Combine all in one dictionary
#     return {
#         "favorite_game": favorite_game,     # string
#         "top_games": top_games,             # list
#         "console_info": console_info,       # tuple
#         "game_genres": game_genres,         # set
#         "player_profile": player_profile    # dict
#     }



# data = get_full_game_data()
# pprint(data, sort_dicts=False)





print("\nEx 4) :")
# def get_math_constants_and_data():
#     # String: Approximation of pi
#     pi_approx = "3.141592653589793"
    
#     # List: First few prime numbers
#     primes = [2, 3, 5, 7, 11, 13]
    
#     # Tuple: Fundamental constants (immutable)
#     constants = (3.1415926535, 2.7182818284, 1.4142135623)  # pi, e, sqrt(2)
    
#     # Set: Basic arithmetic operations
#     operations = {"addition", "subtraction", "multiplication", "division"}
    
#     # Dictionary: Math formulas
#     formulas = {
#         "area_circle": "πr²",
#         "pythagorean": "a² + b² = c²",
#         "quadratic": "ax² + bx + c = 0"
#     }
    
#     return {
#         "pi_approx": pi_approx,
#         "primes": primes,
#         "constants": constants,
#         "operations": operations,
#         "formulas": formulas
#     }

# # Call the function
# math_info = get_math_constants_and_data()
# pprint(math_info)




print("\nEx 5) : ")
# def get_math_data():
#     # String: description of the topic
#     topic = "Basic Statistics for a Math Exam"

#     # List: list of scores
#     scores = [88, 92, 75, 91, 85, 92, 75]

#     # Tuple: (min, max, average)
#     stats = (min(scores), max(scores), f'{sum(scores) / len(scores):0.2f}')

#     # Set: unique scores (no duplicates)
#     unique_scores = set(scores)

#     # Dictionary: detailed math info
#     math_data = {
#         "topic": topic,               # string
#         "scores": scores,             # list
#         "stats": stats,               # tuple
#         "unique_scores": unique_scores,  # set
#         "passed": [s for s in scores if s >= 80],  # list of passing scores
#     }

#     return math_data

# pprint(get_math_data())


print("\nEx 6) :")
# def show_ranked_games():
#     games = ["Elden Ring", "The Last of Us", "Minecraft", "Fortnite"]

#     print(*(f"Rank {rank}: {game}" for rank, game in enumerate(games, start=1)))
#     # [print(f"Rank {rank}: {game}") for rank, game in enumerate(games, start=1)]
        
        
        
# def show_student_scores():
#     students = ["Ayman", "Sara", "Omar"]
#     math_scores = [95, 88, 76]

#     print(*(f"Student: {name}  -->  Math score: {score}"
#             for name, score in zip(students, math_scores)),sep=" || ")
    
#     [print(f"Student: {name}  -->  Math score: {score}",end = ' ') 
#      for name, score in zip(students, math_scores)]
    
    
# show_ranked_games() , print();  show_student_scores()



print('\nEx 7) :')
# def sum_even_squares():
#     # Fixed limit inside the function (no arguments)
#     limit = 10

#     # sq := n * n both computes and stores the square
#     even_squares = [sq for n in range(1, limit + 1) if (sq := n * n) % 2 == 0]

#     return {
#         "limit": limit,
#         "even_squares": even_squares,
#         "sum_even_squares": sum(even_squares),
#     }


# print("     A):", sum_even_squares())


# def approx_sqrt_2():
#     x = 2.0          # we always compute sqrt(2)
#     tol = 1e-6       # fixed tolerance
#     guess = 1.0      # initial guess

#     # walrus stores the current error each loop
#     while (error := abs(guess * guess - x)) > tol:
#         guess = (guess + x / guess) / 2  # Newton's update formula

#     return {
#         "x": x,
#         "tolerance": tol,
#         "approx_sqrt": f'{guess:0.2}',
#         "final_error": f'{error:0.2}',
#     }


# print("     B):", approx_sqrt_2())


print('\nEx 8 ) :')
# def approximate_e():
#     e = 1.0
#     factorial = 1
#     for i in range(1, 10):
#         e += 1 / (factorial := factorial * i)
#     return e

# def fibonacci_sum():
#     a, b = 0, 1
#     total = 0
#     for _ in range(10):
#         total += a
#         a, b = b, (temp := a + b)
#     return total



# print(f"1. Approximate e (Euler's Number) = {approximate_e():0.2f}",)  # Output: ~2.718281828 (approximation of e)
# print(f'2. Sum of Fibonacci Numbers = {fibonacci_sum()}')  # Output: 88 (sum of first 10 Fibonacci numbers: 0+1+1+2+3+5+8+13+21+34)

print("\nEx 9 : ")
# def factorial_table():
#     n_max = 6
#     n = 1
#     fact = 1
#     table = []

#     # compute 1!, 2!, ..., 6! using walrus
#     while n <= n_max:
#         table.append((n, fact := fact * n))
#         n += 1

#     return {"max_n": n_max,"factorials": table }



# def running_average():
#     numbers = [10, 20, 30, 40, 50]
#     running = []
#     total = 0

#     for i, x in enumerate(numbers, start=1):
#         running.append((x, (avg := (total := total + x) / i)))

#     return { "numbers": numbers, "running_averages": running}

# print("Ex C):");pprint(factorial_table())

# print("Ex D):"); pprint(running_average())


print("\nEx 10 ) :")
# def approximate_pi_leibniz():
#     pi = 0.0
#     sign = 1
#     for i in range(10000):
#         pi += sign * 4 / (2 * i + 1)
#         sign = -sign  # Flip sign
#     return pi

# print(f'Leibniz Formula for π Approximation : {approximate_pi_leibniz() :0.2f}')  # Output: ~3.1414926535900345 (approximation of π)

# def harmonic_sum():
#     total = 0.0
#     i = 1
#     while (total := total + 1 / i) and (i := i + 1) <= 100:
#         pass  # Sum accumulates in walrus
#     return total

# print(f'Harmonic Series Sum = {harmonic_sum():0.2f}')  # Output: ~5.187377517639621 (sum of 1 + 1/2 + ... + 1/100)

















print("  Function WITH argument   ".center(100,'-') ,'\n')
#%%
print('\nEx 1  - :')
# a , b , c , d ='ayman' , 'siraj' , 'omar' , 'sami'
# def greet_person(name="Guest"): return f"Hello, {name}!"
# print(greet_person() , greet_person(d))

# def full_name(first_name, middle_name ,last_name):
#     return f"{first_name.capitalize()} {middle_name.upper()} {list(last_name)}"
# print(full_name(a, b, c))


# def details(name = 'stranger', age = "Unkown", city="Unknown"):
#     return f"{name} is {age} years old and lives in {city}."
# print(details(a,age=35)) ; print(details(city="Cairo"))


print('\nEx 2  - :')

# def addition(n1,n2) : 
#     return n1 + n2 if isinstance(n1,(int,float)) and isinstance(n2,(int,float)) else "Error: Provide numbers only"
# print('Addition = ', addition(5, 10.5))


#%%
print('\nEx 3 - :')

# def quadratic_roots(a, b, c):
#     discriminant = b**2 - 4 * a * c
#     root_part = discriminant**0.5
#     return ((-b + root_part) / (2 * a), (-b - root_part) / (2 * a))
# print('Q_R = ',quadratic_roots(1, -3, 2))



# def slope_between_points(p1, p2):
#     x1, y1 = p1
#     x2, y2 = p2
#     return (y2 - y1) / (x2 - x1)
# print('slope_between_points = ', slope_between_points((1, 2), (3, 6)))


# print('\nEx 4 - :')
# def dot_product(vec1, vec2):
#     return sum(a * b for a, b in zip(vec1, vec2))
# print('dot product  = ',dot_product((1, 2, 3), (4, 5, 6)))


print('\nEx 5 - :')
 # 1. Sum of Squares with Decrementing Counter
# def sum_of_squares(n):
#     total = 0
#     while (n := n - 1) >= 0:
#         total += n ** 2
#     return total

# print(sum_of_squares(5))  # Output: 30 (0² + 1² + 2² + 3² + 4²)
#  # 2. Factorial with Accumulating Product
# def factorial(n):
#     result = 1
#     while (n := n - 1) > 0:
#         result *= n + 1  # Adjust since n is decremented
#     return result

# print(factorial(5))  




print('\nEx 6 - :')

# def sum_of_squares(limit: int) -> int:
#     # squares list is created AND stored using walrus
#     squares = [sq for n in range(1, limit + 1) if (sq := n * n) % 2 == 0]
#     # only even squares are kept
#     return sum(squares)

# print("Sum of even squares up to 10:", sum_of_squares(10))
# Explanation:
# n: 1,2,3,...,10
# sq := n*n  -> 1,4,9,16,25,36,49,64,81,100
# keep only even sq: 4,16,36,64,100
# sum = 220


print('\nEx 7 - :')
# def approx_sqrt(x: float, *, tol: float = 1e-6) -> float:
#     guess = x / 2 or 1.0  # simple initial guess

#     # walrus stores the absolute difference each iteration
#     while (error := abs(guess * guess - x)) > tol:
#         guess = (guess + x / guess) / 2  # Newton's update

#     # You can also inspect the last error if you want
#     # print("Final error:", error)
#     return guess


# print("Approx sqrt of 2:", approx_sqrt(2))
# print("Approx sqrt of 10:", approx_sqrt(10))



print('\nEx 8 - :')


# def convert_to_decimal(number_str, base):
#     if '.' in number_str:
#         int_part_str, frac_part_str = number_str.split('.')
#     else:
#         int_part_str, frac_part_str = number_str, ''

#     # Convert integer part
#     int_part = int(int_part_str, base)

#     # Convert fractional part
#     frac_part = 0
#     for i, digit in enumerate(frac_part_str, start=1):
#         if digit.isdigit():
#             value = int(digit)
#         else:
#             value = ord(digit.upper()) - ord('A') + 10
#         frac_part += value / (base ** i)

#     return int_part + frac_part

# # Examples
# binary = "1010.101"
# octal = "12.5"
# hexa = "A.A"




# print(f"Binary {binary} → Decimal:", convert_to_decimal(binary, 2))
# print(f"Octal {octal} → Decimal:", convert_to_decimal(octal, 8))
# print(f"Hex {hexa} → Decimal:", convert_to_decimal(hexa, 16))





print('\nEx 9 - :')

# def convert_fractional_part(fraction, base, precision=10):
#     result = ""
#     count = 0
#     while fraction > 0 and count < precision:
#         fraction *= base
#         digit = int(fraction)
#         fraction -= digit
#         if base == 16 and digit >= 10:
#             result += chr(ord('A') + digit - 10)
#         else:
#             result += str(digit)
#         count += 1
#     return result





# def convert_decimal(number):
#     integer_part = int(number)
#     fractional_part = number - integer_part

#     # Binary
#     binary_int = bin(integer_part)[2:]
#     binary_frac = convert_fractional_part(fractional_part, 2)
#     binary = f"{binary_int}.{binary_frac}" if binary_frac else binary_int

#     # Octal
#     octal_int = oct(integer_part)[2:]
#     octal_frac = convert_fractional_part(fractional_part, 8)
#     octal = f"{octal_int}.{octal_frac}" if octal_frac else octal_int

#     # Hexadecimal
#     hex_int = hex(integer_part)[2:].upper()
#     hex_frac = convert_fractional_part(fractional_part, 16)
#     hexadecimal = f"{hex_int}.{hex_frac}" if hex_frac else hex_int

#     return binary, octal, hexadecimal

# # Example usage
# decimal_number = 10.625
# binary, octal, hexadecimal = convert_decimal(decimal_number)

# print(f"Decimal: {decimal_number}")
# print(f"Binary: {binary}")
# print(f"Octal: {octal}")
# print(f"Hexadecimal: {hexadecimal}")











print('||| A) def Funct(*rgs) |||'.rjust(50,' '))
#%%
print('\nEx 1  - :')
# def logical_and(*args):
#     return all(args)
# # Usage
# print(logical_and(True, True, False))  # Output: False
# print(logical_and(True, True, True))# Output: True



# def details(name , *skills):
#     skills_list = ", ".join(skills) if skills else "No skills listed"
#     return f"{name} has skills: {skills_list}"
# print(details("Ayman", "Python", "Data Analysis", "Machine Learning"))


print('\nEx 2 - :')
# def multiply_numbers(*numbers):
#     product = 1
#     # for number in numbers:
#     #     product *= number
#     [product := product * number for number in numbers]
#     return product
# print(f'Muliply numbers : {multiply_numbers(2, 3, 4)}',end = '    ')

# print('\nEx 3  - :')
# def sum_series(*terms): return sum(terms)
# print(f'Sum = {sum_series(1, 2, 3, 4, 5)}', end = '    ')


# def average_points(*points): return sum(points) / len(points) if points else 0
# print(f'AVG = {average_points(80, 90, 100)}',end = '    ')



print('\nEx 4  - :')
# def polynomial_value(x, *coefficients):
#     total = 0
#     # for power, coefficient in enumerate(coefficients):
#     #     total += coefficient * (x**power)
#     [total := total + coefficient * (x ** power) 
#      for power, coefficient in enumerate(coefficients)]
#     return total
# print(f'Poly = {polynomial_value(2, 3, 0, 1)}')


print('\nEx 5  - :')
# def determinant_2x2(*rows):
    
#     if len(rows) != 2 :
#         raise ValueError("Provide exactly two rows with two elements each.")
#     (a, b), (c, d) = rows
#     return a * d - b * c
# print('determinant_2x2((1, 2), (3, 4)) = ', determinant_2x2((1, 2), (3, 4)))



print('\nEx 6  - :')
# def multiply_terms(*factors):
#     product = 1
#     for value in factors:
#         product *= value
#     return product
# print('multiply_terms(2, -3, 4) = ', multiply_terms(2, -3, 4),end= '  ')


print('\nEx 9  - :')
# def polynomial_value(x, *coefficients):
#     total = 0
#     for power, coefficient in enumerate(coefficients):
#         total += coefficient * (x**power)
#     return total
# print('polynomial_value(2, 3, 0, 1) = ', polynomial_value(2, 3, 0, 1))

print('\nEx 10 - :')
# def quadratic_formula(*coefficients):
#     a, b, c = coefficients
#     discriminant = b**2 - 4 * a * c
#     return discriminant
# print('quadratic_formula(1, -5, 6) = ', quadratic_formula(1, -5, 6))


# def distance_formula(*points):
#     x1, y1, x2, y2 = points
#     return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
# print('distance_formula(0, 0, 3, 4) = ', distance_formula(0, 0, 3, 4))










#%%
# print('| B) def Funct(**krgs) |'.rjust(50,' '))
# print('\nEx 0 : - ')
# my_skills = {'Python': 'Expert', 'Java': 'Intermediate', 'C++': 'Beginner'}
# def detail(**info):
#     return ", ".join(f"{key}: {value}" for key, value in info.items())

# def P_skills(**skills):
#     # return ", ".join(f"{key}: {value}" for key, value in skills.items())
#     return [f'{skill} ==> {prof}' for skill, prof in skills.items()]

# print(P_skills(**my_skills))


#%%
print('\nEx 0.5 - :')
# skills_dict = {'HTML': '80%', 'CSS': '70%', 'JS': '90%' , 'PHP': '60%' , 'Python': '95%'}
# skils_set = {'C' , 'C++' , 'Java' , 'Ruby' , 'Swift'}
# def detail_skills(name , *skills , **prof):
    
    
#     print(f'The skills of {name} are:\n')
#     # for sk_k, sk_v in prof.items():
#     #             print(f'{sk_k} ===> {sk_v}')
    
#     print('     '.join(f'{sk_k} ===> {sk_v}' for sk_k, sk_v in prof.items()))

    
#     print('\nBut he lacks of :',end = ' ')
    
    
    
#     # return [f' -{sk}' for sk in skills]
#     return set(f' -{sk}' for sk in skills)

# print(detail_skills('Gourge',*skils_set , **skills_dict))
    




#%%
print('\nEx 1 - :')
# def describe_person(**info):
#     description = []
#     for key, value in info.items():
#         description.append(f"{key}: {value}")
#     return ", ".join(description)
# print(describe_person(name="Ayman , A", hobby="Coding , B"))
# print(describe_person(name="Samo", hobby="Gaming"))



print('\nEx 2  - :',end = '  ')
# def configure_equation(**terms):
#     return " + ".join(f"{coef}{var}" for var, coef in terms.items())
# print('Eq = ',configure_equation(x=2, y=3, z=4))


print('\nEx 3  - :',end = '  ')
# def substitute_variables(expression: str, **values):
#     for variable, value in values.items():
#         expression = expression.replace(variable, str(value))
#     return expression
# print(substitute_variables("2x + 3y - z", x=4, y=5, z=6))


print('\nEx 4  - :')
# def mix_arguments(a, b, *args, c=0, **kwargs):
#     return {
#         "a_plus_b": a + b,"extra": args,
#         "c_value": c,"details": kwargs,
#     }
# pprint(mix_arguments(1, 2.3, 3, 4, c=5, hobby="Coding", language="Python"))




print('\nEx 5  - :')
# def weighted_linear_expression(*coefficients, **variables):
#     total = 0
#     for coefficient, (name, value) in zip(coefficients, variables.items()):
#         total += coefficient * value
#     return total
# print(weighted_linear_expression(2, 3, -1, x=4, y=5, z=6))






print('\nEx 6 - :')

# def evaluate_linear_expression(**variables):
#     return 3 * variables["x"] - 2 * variables["y"] + variables["z"]
# print(evaluate_linear_expression(x=4, y=1, z=5))




print('\nEx 7 - :')
# def plug_into_binomial(**variables):
#     a = variables["a"]
#     b = variables["b"]
#     return a**2 + 2 * a * b + b**2
# print(plug_into_binomial(a=3, b=2))




print('\nEx 8 - :')
# def vector_from_components(**components):
#     return tuple(components[key] for key in ("i", "j", "k"))
# print(vector_from_components(i=2, j=-1, k=4))




print('\nEx 9 - :')
# def quadratic_formula(**coefficients):
#     a = coefficients["a"]
#     b = coefficients["b"]
#     c = coefficients["c"]
#     discriminant = b**2 - 4 * a * c
#     return discriminant
# print(quadratic_formula(a=1, b=-5, c=6))


# def evaluate_polynomial(x, *coeffs):
#     # coeffs = a0, a1, a2, ..., an for a0 + a1*x + a2*x^2 + ...
#     result = 0
#     for power, coeff in enumerate(coeffs):
#         result += coeff * (x ** power)
#     return result
# print(evaluate_polynomial(2, 1, 3, 4))  # Output: 1 + 3*2 + 4*4 = 1 + 6 + 16 = 23



print('\nEx 10 - :')
# def distance_formula(**points):
#     x1 = points["x1"]
#     y1 = points["y1"]
#     x2 = points["x2"]
#     y2 = points["y2"]
#     return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
# print(distance_formula(x1=0, y1=0, x2=3, y2=4))



print('\nEx 11 - :')
# def log_and_call(func, **kwargs):
    
#     print(f"Calling function '{func.__name__}' with arguments:")
    
#     for key, value in kwargs.items():
#         print(f"  {key}: {value}")
    
#     # Pass all received keyword arguments to the actual function
#     func(**kwargs)


print('\nEx 12 - :')
# def print_user_info(name, age, city="Unknown"):
   
#     print(f"\nUser Info:")
#     print(f"Name: {name}, Age: {age}, City: {city}")

# # The wrapper function takes the specific arguments for print_user_info as **kwargs
# log_and_call(print_user_info, name="Alice", age=30, city="New York")


print('\nEx 13 - :')
# def issue_greeting(greeting_type, **recipients):
#     print(f"--- {greeting_type} ---")
#     for name, title in recipients.items():
#         print(f"Hello, {title} {name}!")

# issue_greeting("Formal Greetings", John="Mr.", Jane="Ms.", Bob="Dr.")

 
print('\nEx 14 - :')
# def define_user_settings(**settings):
#     # Use .get() to retrieve a value safely, providing a default if not present
#     theme = settings.get('theme', 'Light')
#     font_size = settings.get('font_size', 16)
    
#     print(f"User Theme: {theme}")
#     print(f"Font Size: {font_size}px")
# define_user_settings(theme="Dark", font_size=20)
# print("-" * 10)
# define_user_settings(theme="System Default") # Only theme is provided

# #%%
# # Output:
# # User Theme: Dark
# # Font Size: 20px
# # ----------
# # User Theme: System Default
# # Font Size: 16px


print('\nEx 15 - :')
# def create_profile(username, email, **extra_info):
#     print(f"Profile for {username} ({email})")
#     if extra_info:
#         print("Extra Info:")
#         for key, value in extra_info.items():
#             print(f"- {key}: {value}")

# user_data = {
#     'username': 'coder_dave',
#     'email': 'dave@example.com',
#     'location': 'Seattle',
#     'status': 'Active'
# }

# # The ** unpacks the dictionary keys and values into the function parameters
# create_profile(**user_data) 

# # Output:
# # Profile for coder_dave (dave@example.com)
# # Extra Info:
# # - location: Seattle
# # - status: Active



print('\nEx 16 - :')
# def update_config(current_config, **new_settings):
#     print(f"Old config: {current_config}")
#     # Update the dictionary with all new settings provided via kwargs
#     current_config.update(new_settings)
#     print(f"New config: {current_config}")

# system_config = {'log_level': 'INFO', 'timeout': 30, 'max_users': 100}

# update_config(system_config, log_level="DEBUG", timeout=60, feature_flag_a=True)

# # Output:
# # Old config: {'log_level': 'INFO', 'timeout': 30, 'max_users': 100}
# # New config: {'log_level': 'DEBUG', 'timeout': 60, 'max_users': 100, 'feature_flag_a': True}


print('\nEx 17 - :')

# def label_axes(*labels):
#     for i, label in enumerate(labels, start=1):
#         print(f"Axis {i}: {label}")

# # Usage
# label_axes("Time", "Voltage", "Current")
# # Output:
# # Axis 1: Time
# # Axis 2: Voltage
# # Axis 3: Current



print('\nEx 18 - :')
# from sympy import symbols, Eq

# def substitute_expression(**kwargs):
#     x, y = symbols('x y')
#     expr = Eq(x + y, 10)
#     substituted = expr.subs(kwargs)
#     return substituted

# # Usage
# print(substitute_expression(x=3))  # Output: Eq(3 + y, 10)


print('\nEx 19 - :')

# def evaluate_ohms_law(**kwargs):
#     V = kwargs.get('V')
#     I = kwargs.get('I')
#     R = kwargs.get('R')

#     if I is not None and R is not None:
#         return I * R
#     elif  V is not None and R is not None:
#         return V / R
#     elif  V is not None and I is not None:
#         return V / I
#     else:
#         return "Insufficient data"

# # Usage
# print(evaluate_ohms_law(V=12, R=4))  # Output: 3.0 (I = V / R)




print('\nEx 20 - :')
# def build_expression(**kwargs):
#     terms = [f"{v}{k}" for k, v in kwargs.items()]
#     return " + ".join(terms)

# # Usage
# print(build_expression(x=3, y=4, z=5))  
# # Output: 3x + 4y + 5z




print('\nEx 21 - :')
# def evaluate_linear(**kwargs):
#     # Expecting kwargs like a=2, b=3, x=5 for ax + b
#     a = kwargs.get('a', 1)
#     b = kwargs.get('b', 0)
#     x = kwargs.get('x', 0)
#     return a * x + b

# # Usage
# print(evaluate_linear(a=2, b=3, x=5))   # Output: 13
# print(evaluate_linear(x=4))            # Output: 4 (uses default a=1, b=0)






print('\nEx 22 - :')
# def evaluate_poly(x, *coeffs, **options):
#     result = sum(c * x**i for i, c in enumerate(coeffs))
#     if options.get("verbose"):
#         print(f"Evaluating at x={x} with coeffs={coeffs}: result={result}")
#     return result

# # Usage
# evaluate_poly(2, 1, 3, 4, verbose=True)  # Output: 1 + 3*2 + 4*4 = 23





print('\nEx 23 - :')
# def validate_conditions(*args, **kwargs):
#     if kwargs.get("mode") == "strict":
#         return all(args)
#     else:
#         return any(args)
# # Usage
# print(validate_conditions(True, False, True, mode="strict"))  # Output: False
# print(validate_conditions(False, False, True))                # Output: True





print('\nEx 24 - :')

# def label_plot(*axes, **styles):
#     for i, label in enumerate(axes, start=1):
#         style = styles.get(f"axis{i}", "default")
#         print(f"Axis {i}: {label} [{style}]")

# # Usage
# label_plot("Time", "Voltage", axis1="bold", axis2="italic")





print('\nEx 25 - :')

# def apply_operation(*numbers, **kwargs):
#     op = kwargs.get("operation", "add")
#     if op == "add":
#         return sum(numbers)
#     elif op == "multiply":
#         result = 1
#         for n in numbers:
#             result *= n
#         return result
#     else:
#         return "Unknown operation"

# # Usage
# print(apply_operation(2, 3, 4, operation="multiply"))  # Output: 24



print('\nEx 26 - :')
# def simulate_physics(*forces, **params):
#     mass = params.get("mass", 1)
#     net_force = sum(forces)
#     acceleration = net_force / mass
#     return acceleration

# # Usage
# print(simulate_physics(10, -2, mass=4))  # Output: 2.0


print('\nEx 1 - :')
# %%

# def Alpha(name = 'Stranger'): return f'Hello {name}\t'
# Beta  = lambda name = 'Stranger' :  f'Hello {name}\t'
# print(Alpha() == Beta()) ; print(Alpha.__name__ ,type(Alpha))
# print(Beta.__name__ , type(Beta)) 


# # %%
# print('\nEx 2  - :')

# from sympy import symbols
# from sympy import pprint as pp
# x, y, z = symbols("x y z")

# def Sigma(a,b,c) :return pp((a+b)/c)
# print(Sigma(x,y,z)) 

# Omega = lambda a,b,c :  pp(( a-c/b )**2)
# print(Omega(x,y,z))



# %%
print('\nEx 3  - :')
# Example 1: Lambda with *args - sum all arguments
# sum_all = lambda *args: sum(args)
# print(sum_all(1, 2, 3, 4))  # Output: 10
 
# # Example 2: Lambda with **kwargs - create a dictionary with specific keys
# greet = lambda **kwargs: f"Hello {kwargs.get('name', 'Guest')}, you are {kwargs.get('age', '?')} years old"
# print(greet(name="Alice", age=30))  # Output: Hello Alice, you are 30 years old

# # Example 3: Lambda with both *args and **kwargs - flexible function
# process = lambda *args, **kwargs: {"args": args, "kwargs": kwargs}
# print(process(1, 2, 3, name="test", value=42))
# # Output: {'args': (1, 2, 3), 'kwargs': {'name': 'test', 'value': 42}}
# # %%
# print('\nEx 4  - :')
# keys_list = lambda **kwargs: list(kwargs.keys())
# print(keys_list(a=1, b=2, c=3))  

# count_args = lambda *args, **kwargs: len(args) + len(kwargs)
# print(count_args(1, 2, x=3, y=4))





#%%
print('\nEx 5 - :')
# 3 lambda examples using *args and **kwargs

# Example 1: Sum all positional numbers, with an optional 'bias' added via kwargs
# sum_with_bias = lambda *args, **kwargs: sum(args) + kwargs.get('bias', 0)

# # Example 2: Keep only values within [min, max] provided via kwargs (defaults are -inf to +inf)
# filter_range = lambda *args, **kwargs: [
#     x for x in args
#     if kwargs.get('min', float('-inf')) <= x <= kwargs.get('max', float('inf'))
# ]

# # Example 3: Join positional args as strings with a configurable separator, plus optional prefix/suffix
# join_with_options = lambda *args, **kwargs: (
#     kwargs.get('prefix', '')
#     + kwargs.get('sep', ',').join(map(str, args))
#     + kwargs.get('suffix', '')
# )

# if __name__ == '__main__':
#     # Demo for Example 1
#     print('Example a - sum_with_bias:')
#     print(sum_with_bias(1, 2, 3))                  # 6
#     print(sum_with_bias(1, 2, 3, bias=10))         # 16
#     print()

#     # Demo for Example 2
#     print('Example b - filter_range:')
#     print(filter_range(5, 2, 9, 4, min=4))         # [5, 9, 4]
#     print(filter_range(5, 2, 9, 4, min=3, max=5))  # [5, 4]
    # print()

    # Demo for Example 3
#     print('Example c - join_with_options:')
#     print(join_with_options('a', 'b', 'c'))                            # a,b,c
#     print(join_with_options('a', 'b', 'c', sep=' | '))                 # a | b | c
#     print(join_with_options('a', 'b', 'c', sep='-', prefix='[', suffix=']'))  # [a-b-c]
# #



print('\nEx 6  - :')
# filter_range = lambda *args, **kwargs: [
#     x for x in args
#     if kwargs.get('min', float('-inf')) <= x <= kwargs.get('max', float('inf'))
# ]
# print(filter_range(2,65,22))
# print(filter_range(2, 65, 22, min=10, max=50))




#%%
print('\nEx 7  - :')
# double_add = lambda x: (temp := x * 2) + temp
# print('Double = ' , double_add(5),end= ' ')  # Output: 15 (5*2 + 5*2)

# average = lambda lst: (avg := sum(lst) / len(lst)) if lst else 0
# print('agv(1,2,3,4) = ',average([1, 2, 3, 4]))  # Output: 2.5
# # print(average([]))            # Output: 0


# is_upper = lambda s: (upper := s.upper()) == s
# print(is_upper("HELLO"),is_upper("Hello"))  # Output: True
# print()  # Output: False

# fact_approx = lambda n: (f := 1) and [f := f * i for i in range(1, n+1)] and f
# print('F  =  ',fact_approx(5))  # Output: 120



#%%

print('\nEx 8  - :')
# Example 1: Walrus in lambda - assign and use value
# get_double = lambda x: (y := x * 2) and y
# print(get_double(5))  # Output: 10

# # Example 2: Walrus in lambda - conditional with assignment
# check_range = lambda x: (n := x * 2) and (n if n > 10 else n)
# print(check_range(6), check_range(3))  # Output: 12 6


# # Example 3: Walrus in lambda - using assigned value multiple times
# calculate = lambda x: (squared := x ** 2) + squared
# print(calculate(4))  # Output: 32 (16 + 16)

# # Example 4: Walrus in lambda with list comprehension
# filter_and_count = lambda nums: [(x, count) for x in nums if (count := len([n for n in nums if n == x])) > 1]
# print(filter_and_count([1, 2, 2, 3, 3, 3]))  # Output: [(2, 2), (2, 2), (3, 3), (3, 3), (3, 3)]

# # Example 5: Walrus in lambda - simplify nested calls
# process = lambda text: (trimmed := text.strip()) or "empty"
# print(process("  hello  ") , process("   "))  # Output: hello
# print()        # Output: empty



print('\nEx 9  - :')
# from sympy import solve, sin, diff , Eq
# x = symbols('x')

# eval_sin = lambda val: sin(x).subs(x, val)
# print(eval_sin(0) , eval_sin(3.14159/2))  # Output: 0
# print()  # Output: 1.0

# derivative = lambda expr: diff(expr, x)
# result = derivative(x**3 + 2*x**2 + 5)
# print('result = ',result)  ; pp(result)


# x = symbols('x')
# solve_equation = lambda eq: solve(eq, x)
# equation = Eq(x**2 - 5*x + 6, 0)

# # Display the equation
# print("Equation:") ; pp(equation)

# # Display the solution
# print("\nSolution:",solve_equation(equation))


print('\nEx 10  - :')
# mean = lambda lst: sum(lst) / len(lst) if lst else 0
# print(mean([1.5, 2.3, 3.247, 4.34, 5.9]))

# median = lambda lst: sorted(lst)[len(lst) // 2] if lst else 0
# print(median([1, 2, 3, 4, 5]) , median([1, 12, 33, 4]))  # Output: 3

# mode = lambda lst: max(set(lst), key=lst.count) if lst else None
# print(mode([1, 2, 2, 3, 3, 3 ,5]))  # Output: 3


# stdev = lambda lst: (sum((x - (m := sum(lst) / len(lst))) ** 2 for x in lst) / len(lst)) ** 0.5 if lst else 0
# print(stdev([1, 2, 3, 4, 5]))  # Output: ~1.414 (population std dev)


print('\nEx 11  - :')
# def convert_fractional_part(fraction, base, precision=10):
#     result = ""
#     count = 0
#     while fraction > 0 and count < precision:
#         fraction *= base
#         digit = int(fraction)
#         fraction -= digit
#         if base == 16 and digit >= 10:
#             result += chr(ord('A') + digit - 10)
#         else:
#             result += str(digit)
#         count += 1
#     return result

# convert_decimal = lambda number: (
#     (binary_int := bin(int(number))[2:]),
#     (binary_frac := convert_fractional_part(number - int(number), 2)),
#     (octal_int := oct(int(number))[2:]),
#     (octal_frac := convert_fractional_part(number - int(number), 8)),
#     (hex_int := hex(int(number))[2:].upper()),
#     (hex_frac := convert_fractional_part(number - int(number), 16)),
#     f"{binary_int}.{binary_frac}" if binary_frac else binary_int,
#     f"{octal_int}.{octal_frac}" if octal_frac else octal_int,
#     f"{hex_int}.{hex_frac}" if hex_frac else hex_int
# )[-3:]  # Return last 3 (binary, octal, hex)

# # Example usage
# decimal_number = 10.625
# binary, octal, hexadecimal = convert_decimal(decimal_number)

# print(f"Decimal: {decimal_number}")
# print(f"Binary: {binary}")
# print(f"Octal: {octal}")
# print(f"Hexadecimal: {hexadecimal}")

print('\nEx 12  - :')
# convert_to_decimal = lambda number_str, base: (
#     lambda parts: 
#         int(parts[0], base) + 
#         sum(
#             (int(digit) if digit.isdigit() else ord(digit.upper()) - ord('A') + 10) / (base ** i)
#             for i, digit in enumerate(parts[1], start=1)
#         )
# )(number_str.split('.') if '.' in number_str else [number_str, ''])

# # Examples
# binary = "1010.101"
# octal = "12.5"
# hexa = "A.A"
# print(f"Binary {binary} → Decimal:", convert_to_decimal(binary, 2))
# print(f"Octal {octal} → Decimal:", convert_to_decimal(octal, 8))
# print(f"Hex {hexa} → Decimal:", convert_to_decimal(hexa, 16))

# # 
print('\nEx 13 - :')
# Example 1: enumerate + lambda to format indexed items
# items = ['a', 'b', 'c']
# format_item = lambda i, v: f"Index {i}: {v}"

# result = [format_item(i, v) for i, v in enumerate(items)]
# print(result)  # ['Index 0: a', 'Index 1: b', 'Index 2: c']

# Example 2: filter elements with even index using enumerate + lambda
# nums = [10, 20, 30, 40, 50]
# is_even_index = lambda i, v: i % 2 == 0

# even_index_values = [v for i, v in enumerate(nums) if is_even_index(i, v)]
# print(*even_index_values)  # [10, 30, 50]


# # Evaluate a polynomial a0 + a1*x + a2*x^2 + ...
# coeffs = [2, -3, 5]   # 2 - 3x + 5x^2
# x = 2
# term = lambda i, a: a * (x ** i)

# value = sum(term(i, a) for i, a in enumerate(coeffs))
# print(value)  # 2 - 3*2 + 5*4 = 16


# coeffs = [1, 0, -2, 3]   # 1 - 2x^2 + 3x^3
# format_term = lambda i, a: f"{a}*x^{i}"

# poly_str = " + ".join(
#     format_term(i, a) for i, a in enumerate(coeffs) if a != 0
# )
# print(poly_str)  # 1*x^0 + -2*x^2 + 3*x^3






print('\nEx 14 - :')
# Example 3: zip + lambda to add pairs elementwise
# a = [1, 2, 3]   ; b = [4, 5, 6]
# add_pair = lambda x, y: x + y
# sums = [add_pair(x, y) for x, y in zip(a, b)]
# print(*sums , sums)  # [5, 7, 9]



# Example 4: zip + lambda to combine name and age into a string
# L = ['A', 'B', 'C']  ; N = [25, 30, 35]
# format_person = lambda letter, number: f"{letter} is {number} "
# result = {L : format_person(L ,N) for L, N in zip(L, N)}
# print(result ,*result , *result.values() , *result.items() ,sep = '\n')   


# u = [1, 2, 3]
# v = [4, 5, 6]
# prod = lambda a, b: a * b
# dot = sum(prod(a, b) for a, b in zip(u, v))
# print(dot)  # 1*4 + 2*5 + 3*6 = 32


# u = [1, 0, -1]
# v = [2, 2, 2]
# c1, c2 = 3, -1
# combine = lambda a, b: c1 * a + c2 * b
# result = [combine(a, b) for a, b in zip(u, v)]
# print(result)  # [3*1 - 1*2, 3*0 - 1*2, 3*(-1) - 1*2] = [1, -2, -5]









# %%


 
