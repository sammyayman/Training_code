
#%%
# print("Global and Local function".center(100,'-'))
# print("\nEx (1) :")
# # Global variable
# counter = 10
# try :
#     def increment_wrong():
#         counter = counter + 10  # ❌ ERROR: UnboundLocalError
#         return counter
#     print(increment_wrong())  # Output: 1

# except Exception as e: print(e)
# def increment_correct():
#     global counter         # ✅ Declare we're using global counter
#     counter = counter + 1
#     return counter
# print(increment_correct())  # Output: 1
# print(counter)              # Output: 1 (global variable modified)






# print("\nEx (2) : Global, Local Scope")
# # Global variable
# balance = 1000
# def withdraw(amount):
#     global balance
#     if balance >= amount:
#         balance -= amount
#         return f"Withdrew {amount}. New balance: {balance}"
#     else:
#         return "Insufficient funds"
# print(withdraw(200),end = '            ')  # Output: Withdrew 200. New balance: 800
# print(f"Global balance: {balance}")  # Output: Global balance: 800




# # Nested function with nonlocal


# print("\n\nEx (3) : Global Scope - Game Score System")
# # Global variables
# player_score = 0
# high_score = 100
# def add_points(*points):  # ✅ Accept multiple point values
#     global player_score
      
#     """  total = sum(points)  # Add all points together
#       player_score += total
#       print(f"Added {points} = {total} points. Current score: {player_score}")
#       """
#     ##OR : 
#     player_score += (total := sum(points))  # Walrus operator assigns and returns
#     print(f"Added {points} = {total} points. Current score: {player_score}")

# # Now you can pass multiple values at once!
# add_points(5)           # Single value
# add_points(30, 20)       # Multiple values
# add_points(10, 5, 15)    # Even more values!



# def reset_score():
#     global player_score
#     player_score = 0
#     print("Score reset to 0")
# def check_high_score():
#     global high_score
#     if player_score > high_score:
#         high_score = player_score
#         print(f"🎉 New high score: {high_score}!")
#     else:
#         print(f"Current: {player_score}, High score: {high_score}")


# check_high_score() ; add_points(25)
# check_high_score() ; reset_score()











# print("\n\nEx (4) : Local Scope - Variable Isolation")
# # Global variable
# temperature = 25  # Room temperature in Celsius

# def convert_to_fahrenheit(celsius):
#     # Local variables - only exist inside this function
#     fahrenheit = (celsius * 9/5) + 32
#     message = f"{celsius}°C = {fahrenheit}°F"
#     print(message)
#     return fahrenheit

# def convert_to_kelvin(celsius):
#     # Different local variable with same name - no conflict!
#     kelvin = celsius + 273.15
#     message = f"{celsius}°C = {kelvin}K"
#     print(message)
#     return kelvin

# # Each function has its own local 'message' and result variables
# result1 = convert_to_fahrenheit(temperature)
# result2 = convert_to_kelvin(temperature)

# # Try to access local variable from outside - will cause error if uncommented
# # print(message)  # ❌ NameError: 'message' is not defined
# # print(fahrenheit)  # ❌ NameError: 'fahrenheit' is not defined

# print(f"Global temperature unchanged: {temperature}°C")






# print("\n\nEx (5) : Global and Local with Strings - 3 Functions")
# print("="*60)

# # Global string variables
# user_name = "Guest"
# greeting_message = "Hello"
# status = "offline"
# print("📌 INITIAL STATE (Global Variables):  user_name = '{user_name}\
#     greeting_message = '{greeting_message}' status = '{status}'")
 
# print()

# # ============ FUNCTION 1: Modify global user_name ============
# def login_user(name):
#     global user_name  # ✅ Modify global variable
#     print(f"1️⃣  login_user() called with: '{name}'")
#     print(f"   Before: user_name = '{user_name}'")
#     user_name = name
#     print(f"   After:  user_name = '{user_name}'")
#     return f"Logged in as {user_name}"

# # ============ FUNCTION 2: Use local variable (doesn't modify global) ============
# def create_custom_greeting(name):
#     # Local variable - doesn't modify global greeting_message
#     greeting_message = f"Welcome back, {name}!"  # ❌ Local variable
#     print(f"\n2️⃣  create_custom_greeting() called with: '{name}'")
#     print(f"   Local greeting_message = '{greeting_message}'")
#     print(f"   Global greeting_message still = '{globals()['greeting_message']}'")
#     return greeting_message

# # ============ FUNCTION 3: Modify global status ============
# def set_user_status(new_status):
#     global status  # ✅ Modify global variable
#     print(f"\n3️⃣  set_user_status() called with: '{new_status}'")
#     print(f"   Before: status = '{status}'")
#     status = new_status
#     print(f"   After:  status = '{status}'")
#     return status

# # ============ EXECUTE FUNCTIONS ============
# print("─" * 60)
# print("EXECUTING FUNCTIONS:")
# print("─" * 60)

# result1 = login_user("Alice")
# print(f"   Returned: '{result1}'")

# result2 = create_custom_greeting("Alice")
# print(f"   Returned: '{result2}'")

# result3 = set_user_status("online")
# print(f"   Returned: '{result3}'")

# # ============ FINAL STATE ============
# print("\n" + "─" * 60)
# print("📌 FINAL STATE (Global Variables):")
# print(f"   user_name = '{user_name}'  ← CHANGED by login_user()")
# print(f"   greeting_message = '{greeting_message}'  ← UNCHANGED (local in function 2)")
# print(f"   status = '{status}'  ← CHANGED by set_user_status()\n\n")






 
# print("\nEx (6) : Math Operators /, //, %\n".center(120, '-'))
# #
# # Global variables
# global_dividend  , global_divisor = 100 , 7

# print("\nPART 1:Using Global Variables with Math Operations")
# # Example 1: Using global variables in calculations (read-only)
# def calculate_with_globals():
#     # Local variables for results
#     print(f"\nOriginal global_dividend = {global_dividend} ,\nOrginal global divisor = {global_divisor} ")
#     division_result = global_dividend / global_divisor
#     floor_div_result = global_dividend // global_divisor
#     modulo_result = global_dividend % global_divisor
#     V = floor_div_result * global_divisor + modulo_result

#     print("Example 1: Using Global Variables (Read-Only)")
#     print(f"  {global_dividend} / {global_divisor} = {division_result:0.2f}")
#     print(f"  {global_dividend} // {global_divisor} = {floor_div_result}")
#     print(f"  {global_dividend} % {global_divisor} = {modulo_result}")
#     print(f"  Verification: {floor_div_result} * {global_divisor} + {modulo_result} = {V}")
#     return division_result, floor_div_result, modulo_result
# # Call the function
# results1 = calculate_with_globals()
# print("\n" + "="*80)

# print("\nPART 2: Modifying Global Variables with Math Operations")
# # Example 2: Modifying global variables in calculations
# def modify_globals_with_math():
#     # print(f"Original global_dividend = {global_dividend} ,\nOrginal global divisor = {global_divisor} ") SyntaxError
   
#     global global_dividend, global_divisor
#     # Local variables for calculations
#     local_multiplier , local_addend  = 2 , 5
#     print(f" local_multiplier = {local_multiplier }, local_addend = {local_addend}")

#     # Modify globals using local variables and math operators
#     global_dividend = (global_dividend // global_divisor) * local_multiplier + local_addend
#     global_divisor = global_divisor % 5 + local_multiplier  # Ensure divisor doesn't become 0

#     print(f"  Modified global_dividend = ({results1[1]} // {global_divisor - local_multiplier}) * \
#         {local_multiplier} + {local_addend} = {global_dividend}")
#     print(f"  Modified global_divisor = ({global_divisor - local_multiplier} % 5) + {local_multiplier} = {global_divisor}")

#     # Perform calculations with modified globals
#     new_division = global_dividend / global_divisor
#     new_floor_div = global_dividend // global_divisor
#     new_modulo = global_dividend % global_divisor

#     print(f"  New calculations:")
#     print(f"   \t {global_dividend} / {global_divisor} = {new_division:0.2f}")
#     print(f"   \t {global_dividend} // {global_divisor} = {new_floor_div}")
#     print(f"   \t {global_dividend} % {global_divisor} = {new_modulo}")
#     return new_division, new_floor_div, new_modulo
# # Call the function
# results2 = modify_globals_with_math()
# print("\n" + "="*80)



# # Example 3: Local variables shadowing globals
# def local_shadowing_example():
     
#     # Local variables with same names as globals (shadowing)
#     global_dividend = 50  # Local variable, shadows global
#     global_divisor = 3    # Local variable, shadows global
#     print("\nPART 3: Local Variables Shadowing Globals")
#     print(f"  Local global_dividend = {global_dividend} (shadows global)")
#     print(f"  Local global_divisor = {global_divisor} (shadows global)")

#     # Calculations with local variables
#     local_division = global_dividend / global_divisor
#     local_floor_div = global_dividend // global_divisor
#     local_modulo = global_dividend % global_divisor

#     print(f"  Calculations with local variables:")
#     print(f"    {global_dividend} / {global_divisor} = {local_division}")
#     print(f"    {global_dividend} // {global_divisor} = {local_floor_div}")
#     print(f"    {global_dividend} % {global_divisor} = {local_modulo}")

#     # Show that global variables are unchanged
#     print(f"  Global variables unchanged:")
#     print(f"    Actual global_dividend = {globals()['global_dividend']}")
#     print(f"    Actual global_divisor = {globals()['global_divisor']}\n\n")
#     return local_division, local_floor_div, local_modulo
# # Call the function
# results3 = local_shadowing_example()





# print("\nEx (7) : Math Operators /, //, %\n".center(120, '-'))

# # Global variables
# global_num1 , global_num2 = 10 ,5

# def math_operations_local():
#     print(f'global_num1 = {global_num1} , global_num2 = {global_num2}')
#     # Local variables
#     local_num1 , local_num2 = 7 , 9
#     print(f"Local numbers: num1 = {local_num1}, num2 = {local_num2}\n")
    
#     print(f"Division: {local_num1} / {local_num2} = {local_num1 / local_num2 :0.2f}")
#     print(f"Integer Division: {local_num1} // {local_num2} = {local_num1 // local_num2}")
#     print(f"Modulo: {local_num1} % {local_num2} = {local_num1 % local_num2}")
#     print()
# # Call the function
# math_operations_local()


# def modify_global_variables():
#     code = """
#         print(f'global_num1 = {global_num1} , global_num2 = {global_num2}')
#         global global_num1, global_num2
#     """
#     try: exec(code)
#     except SyntaxError :print(f"Syntax Error:Error: global_num1' is used prior to global ")
 
    
#     print(f'\nglobal_num1 = {globals()["global_num1"]} , global_num2 = {globals()["global_num2"]}')
#     global global_num1, global_num2
#     # Modify global variables using math operations
#     global_num1 *= 2 ; global_num2 += 3
#     print(" Modifying global variables from function")
#     print(f"Modified global numbers:\n global_num1 = {global_num1} , global_num2 = {global_num2}")
#     print(f"New Addition: {global_num1} + {global_num2} = {global_num1 + global_num2}")
#     print()
# # Call the function to modify global variables
# modify_global_variables()
 



# print("\nEx (8) :Analysis pipeline\n".center(120, '-'))

# scores = []

# def analyze_scores():
#     global scores

#     # 1) load data
#     scores = [55, 70, None, 90, 100, None, 85]

#     # 2) clean data
#     scores = [s for s in scores if s is not None]

#     # 3) normalize
#     max_score = max(scores)
#     scores = [s / max_score for s in scores]

#     # 4) add bonus
#     for i in range(len(scores)):
#         scores[i] += 0.05

#     # 5) compute statistic
#     mean = sum(scores) / len(scores)
#     return mean


# result = analyze_scores()
# print(result)
# print(scores)

# print("\nanalyzing daily temperature changes")

# temperatures = []

# def analyze_temperatures():
#     global temperatures

#     # 1) load data (raw readings)
#     temperatures = [20, 22, None, 25, 24, None, 30]

#     # 2) clean data
#     temperatures = [t for t in temperatures if t is not None]

#     # 3) compute daily changes
#     changes = []
#     for i in range(1, len(temperatures)):
#         changes.append(temperatures[i] - temperatures[i - 1])

#     # 4) basic analysis
#     avg_change = sum(changes) / len(changes)

#     return avg_change
# avg_delta = analyze_temperatures()
# print(avg_delta)
# print(temperatures)

# print("\nExample: analyzing sales performance")

# total_sales = 0
# num_days = 0
# def analyze_sales():
#     global total_sales, num_days

#     # local variables (3)
#     daily_sales = (120, 150, 130, 160)   # local
#     threshold = 140                      # local
#     high_days = 0                        # local

#     # analysis
#     for sale in daily_sales:
#         total_sales += sale
#         num_days += 1

#         if sale > threshold:
#             high_days += 1

#     average_sales = total_sales / num_days  # local (computed)

#     return f'average_sales = {average_sales}', f'high_days = {high_days}'


# avg, strong_days = analyze_sales()
# print(avg)
# print(strong_days)
# print(f'total_sales = {total_sales}, num_days = {num_days}')





# print("\nEx (9) :Adding parameters\n".center(120, '-'))

# total_score = 0
# total_count = 0
# def analyze_batch(a, b, c):
#     global total_score, total_count

#     # local variables (3+)
#     batch_sum = a + b + c          # local
#     batch_count = 3                # local
#     batch_mean = batch_sum / batch_count   # local

#     # update global state
#     total_score += batch_sum
#     total_count += batch_count

#     # local decision variable
#     status = "high" if batch_mean >= 75 else "low"

#     return batch_mean, status

# m1, s1 = analyze_batch(80, 70, 90)
# print(m1, s1)
# print(total_score, total_count)

# m2, s2 = analyze_batch(60, 65, 70)
# print(m2, s2)
# print(total_score, total_count)

# print("----")

# total_sum = 0
# global_max = None


# def analyze_values(*values):
#     global total_sum, global_max

#     # local variables
#     local_sum = 0
#     local_max = values[0]

#     for v in values:
#         local_sum += v
#         if v > local_max:
#             local_max = v

#     # update global analysis state
#     total_sum += local_sum
#     if global_max is None or local_max > global_max:
#         global_max = local_max

#     return local_sum, local_max
# s1, m1 = analyze_values(10, 20, 30)
# s2, m2 = analyze_values(5, 50)

# print(s1, m1)
# print(s2, m2)
# print(total_sum, global_max)

# print("----")
# weighted_total = 0.0
# weight_sum = 0.0
# def analyze_weighted(**scores):
#     global weighted_total, weight_sum

#     # local variables
#     local_weighted = 0.0
#     local_weights = 0.0
#     threshold = 70  # local decision value

#     for value, weight in scores.values():
#         local_weighted += value * weight
#         local_weights += weight

#     # update global aggregates
#     weighted_total += local_weighted
#     weight_sum += local_weights

#     average = local_weighted / local_weights
#     status = "pass" if average >= threshold else "fail"

#     return average, status
# avg1, st1 = analyze_weighted(
#     math=(80, 0.4),
#     physics=(70, 0.3),
#     cs=(90, 0.3)
# )

# avg2, st2 = analyze_weighted(
#     english=(60, 0.5),
#     history=(75, 0.5)
# )

# print(avg1, st1)
# print(avg2, st2)
# print(weighted_total / weight_sum)



# print("----")
# global_total = 0
# global_product = 1
# def analyze_numbers(*values, **options):
#     global global_total, global_product

#     # local variables (3+)
#     scale = options.get("scale", 1)
#     offset = options.get("offset", 0)
#     local_result = 1

#     # process *args
#     for v in values:
#         adjusted = (v * scale) + offset
#         local_result = local_result * adjusted

#     # update globals (NO +=, NO *=)
#     global_total = global_total + local_result
#     global_product = global_product * local_result

#     return local_result
# r1 = analyze_numbers(2, 3, scale=2)
# r2 = analyze_numbers(1, 4, offset=1)

# print(r1)
# print(r2)
# print(global_total, global_product)
# #%%
# print("\nEx (10) Function using locals() and globals():\n".center(120, '-'))
# # Global variables
# total = 0
# factor = 2

# def analyze(*values):
#     global total, factor  # declare which globals we will use

#     # Local variables
#     local_sum = 0
#     scaled_values = []

#     # Process values
#     for v in values:
#         scaled = v * factor         # read global factor
#         scaled_values.append(scaled)
#         local_sum = local_sum + scaled

#     # Update global total
#     total = total + local_sum

#     # Inspect locals and globals
#     print("Inside locals():", locals())       # only function locals
#     print("Inside globals()['total']:", total)  # updated global

#     return local_sum, scaled_values

# # Run the function
# s, scaled = analyze(1, 2, 3)
# print("Returned sum:", s)
# print("Returned scaled:", scaled)
# print("Global total:", total)

# #%%
# # Global variables
# a = 2
# b = 3
# c = 4

# def solve_simple_equation(x):
#     y = a * x + b
#     z = y ** c
#     print("Local variables:", locals())
#     globals()['SOLUTION'] = z
#     return z

# result = solve_simple_equation(5)
# print("Solution from global variable:", SOLUTION)
# print("Global variables:", [k for k, v in globals().items() if k.isupper()])


# total_value = 0      # sum of f(x)
# eval_count = 0       # number of evaluations
# def evaluate_quadratic(a, b, c, x):
#     global total_value                    # modify global normally

#     y = a * x**2 + b * x + c              # local variable

#     total_value += y                      # update global sum
#     globals()['eval_count'] += 1          # update global counter

#     print("Locals:", locals())            # inspect local scope

#     return y
# print(evaluate_quadratic(1, -2, 1, 3))
# print(evaluate_quadratic(2, 0, -1, 2))

# print("Total value:", total_value)
# print("Evaluations:", eval_count)






# # Global variables for algebra configuration
# DEFAULT_X = 5
# DEFAULT_Y = 3
# OPERATION_TYPE = "linear"

# def solve_algebra_problem(x=None, y=None):
#     # Local variables for equation solving
#     equation_type = "linear equation"
#     solution_steps = []
    
#     # Use default values if parameters not provided
#     if x is None:
#         x = globals()['DEFAULT_X']
#     if y is None:
#         y = globals()['DEFAULT_Y']
    
#     print("=== Local Variables ===")
#     for key, value in locals().items():
#         print(f"{key}: {value}")
    
#     print("\n=== Global Configuration ===")
#     for key in ['DEFAULT_X', 'DEFAULT_Y', 'OPERATION_TYPE']:
#         print(f"{key}: {globals()[key]}")
    
#     # Solve algebra problems based on operation type
#     if globals()['OPERATION_TYPE'] == "linear":
#         equation = f"{x} * z + {y} = 20"
#         solution_steps.append(f"Equation: {equation}")
#         solution_steps.append(f"Step 1: {x}z = 20 - {y}")
#         numerator = 20 - y
#         solution_steps.append(f"Step 2: z = {numerator} / {x}")
#         z = numerator / x
#         solution_steps.append(f"Step 3: z = {z}")
        
#     else:
#         equation = f"{x} * z² + {y} * z - 10 = 0"
#         solution_steps.append(f"Equation: {equation}")
#         discriminant = y**2 - 4*x*(-10)
#         solution_steps.append(f"Discriminant: {discriminant}")
#         z1 = (-y + discriminant**0.5) / (2*x)
#         z2 = (-y - discriminant**0.5) / (2*x)
#         solution_steps.append(f"Solutions: z = {z1:.2f} or z = {z2:.2f}")
    
#     print("\n=== Solution Steps ===")
#     for step in solution_steps:
#         print(step)
    
#     # Store result as dynamic global variable
#     if OPERATION_TYPE == "linear":
#         globals()['LINEAR_SOLUTION'] = z
#     else:
#         globals()['QUADRATIC_SOLUTIONS'] = (z1, z2)
    
#     return solution_steps

# # Example 1: Linear equation
# print("=== Linear Equation Example ===")
# solve_algebra_problem()

# # Example 2: Quadratic equation (change global configuration)
# print("\n=== Quadratic Equation Example ===")
# OPERATION_TYPE = "quadratic"
# solve_algebra_problem(x=2, y=3)

# # Verify dynamic global variables created
# print("\n=== Dynamic Global Variables ===")
# if 'LINEAR_SOLUTION' in globals():
#     print(f"Linear solution: {globals()['LINEAR_SOLUTION']}")
# if 'QUADRATIC_SOLUTIONS' in globals():
#     print(f"Quadratic solutions: {globals()['QUADRATIC_SOLUTIONS'][0]:.2f}, {globals()['QUADRATIC_SOLUTIONS'][1]:.2f}")











# # Global configuration and data storage variables
# DATA_SIZE = 10
# TARGET_VARIABLE = "temperature"
# MEASUREMENT_UNIT = "Celsius"
# CONVERSION_FACTOR = 1.8

# def data_analysis_workflow():
#     # Local variables for data collection and processing
#     data_points = [22.5, 23.1, 21.8, 24.0, 22.7, 23.3, 21.5, 22.9, 23.5, 22.2]
#     processed_data = []
#     analysis_name = "Temperature Analysis"
    
#     print("=== Local Variables ===")
#     local_vars = locals()
#     for key, value in local_vars.items():
#         print(f"{key}: {value}")
    
#     print("\n=== Global Configuration Variables ===")
#     global_vars = globals()
#     for key in ['DATA_SIZE', 'TARGET_VARIABLE', 'MEASUREMENT_UNIT', 'CONVERSION_FACTOR']:
#         print(f"{key}: {global_vars[key]}")
    
#     # Data processing (conversion to Fahrenheit)
#     for temp in data_points:
#         processed_data.append(temp * CONVERSION_FACTOR + 32)
    
#     print("\n=== Processed Data ===")
#     print(f"Original temperature data ({MEASUREMENT_UNIT}): {data_points}")
#     print(f"Converted temperature data (Fahrenheit): {[round(x, 1) for x in processed_data]}")
    
#     # Math operations without libraries
#     local_mean = sum(data_points) / len(data_points)
#     local_std = (sum((x - local_mean) ** 2 for x in data_points) / len(data_points)) ** 0.5
#     local_min = min(data_points)
#     local_max = max(data_points)
#     local_range = local_max - local_min
#     local_median = sorted(data_points)[len(data_points) // 2]
    
#     print("\n=== Calculated Statistics ===")
#     stats = {
#         'mean': local_mean,
#         'std': local_std,
#         'min': local_min,
#         'max': local_max,
#         'range': local_range,
#         'median': local_median
#     }
    
#     for stat, value in stats.items():
#         print(f"{stat}: {value:.2f}")
    
#     # Store key results as dynamic global variables
#     globals()['CALCULATED_MEAN'] = local_mean
#     globals()['CALCULATED_STD'] = local_std
#     globals()['MEAN_FAHRENHEIT'] = local_mean * CONVERSION_FACTOR + 32
    
#     return processed_data

# # Execute the workflow
# print("Starting Temperature Data Analysis...")
# processed_temps = data_analysis_workflow()

# print("\n=== After Analysis ===")
# # Access dynamic global variables created during analysis
# print(f"Number of data points analyzed: {len(processed_temps)}")
# print(f"Mean temperature ({MEASUREMENT_UNIT}): {CALCULATED_MEAN:.2f}")
# print(f"Standard deviation ({MEASUREMENT_UNIT}): {CALCULATED_STD:.2f}")
# print(f"Mean temperature (Fahrenheit): {MEAN_FAHRENHEIT:.2f}")

# # Verify all dynamic variables exist
# print("\n=== Dynamic Global Variables ===")
# for var_name in ['CALCULATED_MEAN', 'CALCULATED_STD', 'MEAN_FAHRENHEIT']:
#     if var_name in globals():
#         print(f"{var_name}: {globals()[var_name]:.2f}")



# print("\nEx (10) :")
# import sympy as sp

# total_expr = 0     # global: accumulated symbolic expressions
# eval_count = 0     # global: number of evaluations

# def evaluate_quadratic_symbolic(a, b, c):
#     global total_expr                     # we will MODIFY this

#     x = sp.symbols('x')                   # local symbol
#     expr = a*x**2 + b*x + c               # local symbolic expression

#     total_expr += expr                    # update global expression
#     globals()['eval_count'] += 1          # update global counter

#     print("Locals:", locals())
#     # inspect local scope
#     sp.pprint(expr)

#     return expr


# e1 = evaluate_quadratic_symbolic(1, -2, 1)
# e2 = evaluate_quadratic_symbolic(2, 0, -1)

# print("Expression 1:", e1)
# print("Expression 2:", e2)

# print("Total symbolic expression:", total_expr)
# print("Evaluation count:", eval_count)


# # import sympy as sp
# PI = sp.pi   # global constant
# def circle_area(r): return PI * r**2
# r=sp.Symbol('r')
# print(circle_area(r) ,end='     ')

# def quadratic():
#     x = sp.symbols('x')   # local symbol
#     a = 2   ;   b = 3   ;   c = 1
#     result = a*x**2 + b*x + c
#     return result
# print(quadratic() ,end = '      ')


# g = sp.Symbol('g')  # gravity (global)
# def potential_energy(m, h):
#     energy = m * g * h   # local variable
#     return energy
# print(potential_energy(2, 10))

# def moon_gravity():
#     global g; g = 1.62
#     return g
# print( moon_gravity() ,g==moon_gravity(),sep= '\t   \t')


# def newton_step(x):
#     fx = x**2 - 2
#     dfx = 2*x
#     return x - fx/dfx
# x0 = 1.5
# x1 = newton_step(x0)
# print(x1,'\n')


# def newton_step(expr, x, x_n):
#     d_expr = sp.diff(expr, x)
#     return x_n - expr.subs(x, x_n) / d_expr.subs(x, x_n)

# x = sp.symbols('x')
# f = x**2 - 2

# print(sp.pprint(newton_step(f, x, x)),end= '\t=========> \t') ; print(newton_step(f, x, 1.5),'\n')




# def summation(n):
#     i = sp.symbols('i', integer=True)
#     return sp.summation(i, (i, 1, n))

# n = sp.symbols('n', integer=True, positive=True)
# print(sp.pprint(sp.simplify(summation(n))), end = '\t=========> \t')
# print(summation(5)) 



# def simplify_expr():
#     x = sp.symbols('x')
#     expr = (x**2 - 1) / (x - 1)
#     simplified = sp.simplify(expr)
#     return simplified

# print(simplify_expr())


# x = sp.Symbol('x')  # Global symbol
# def scope_demo():
#     x = 10  # Local variable (shadows global x)
#     y = x**2  # Uses local x
#     print(f"Local x = {x}, y = {y}")
#     return y

# print(f"Result: {scope_demo()}")
# print(f"Global x is still: {x}")  # Global x unchang




 


"PART 2"




# #%%
# print(" II Closure(Outer and Inner ) ".center(100,'='))
# print("\nEx 0 : -")

# def outer():
#     print("Start outer()")
#     x = "outer".upper()  # This is local to outer()
#     def inner():
#         print("Start inner()")
#         x = "inner".upper()  # This is LOCAL to inner() - shadows outer x
#         print(f"End Inner: {x}")
#     inner()
#     print(f"End Outer: {x}")
    
# outer()

# print('----'*10)


# def outer():
#     print("Start outer()")
#     secret = 42  # Not passed to inner, not defined in inner
#     def inner():
#         print("In inner()")
#         return secret+6  # Where does secret come from? ← CLOSURE!
#     return inner() , secret , 'Done with outer()'

# OUTETER = outer()
# inner_func  , message  = OUTETER[0:2] , OUTETER[2] 
# print(f"Inner function result: {inner_func}")
# print(f"Outer function message: {message}")



# print('----'*10)

# def Outer_Function(run=True):
#     if not run: return None

#     def Inner_Function_1():
#         print('start of Inner Function 1')
#         print('Inner Function 1 Result'.upper())
#     def Inner_Function_2():
#         print('start of Inner Function 2')
#         return 'Inner Function 2 Result'
#     def Inner_Function_3():
#         print('start of Inner Function 3')
#         return 'Inner Function 3 Result'
    
#     inner1_result = Inner_Function_1()
#     # inner2_result = Inner_Function_2().capitalize()
#     inner3_result = Inner_Function_3().title()
#     print("THE END OF INNER FUNCTIONS")
 
#     return  Inner_Function_2().upper(), 'End of Outer Function'

# OUT = Outer_Function()  # nothing executes
# # Outer_Function(run=True)   # normal behavior
# print('\\\\'*10)
# print(OUT)



# print('----'*10)

# def Main_Function(x=0):
#     print('Start of Main Function')
#     secret_value = 100  # Local variable to Main_Function, not passed to sub-functions
    
#     def sub_function_a():
#         print('Sub Function A')
#         print('Result = ',secret_value + 50 +x)  # Accessing secret_value from enclosing scope (closure)
#     def sub_function_b():
#         print('Sub Function B')
#         return f'Result = {int(secret_value * 0.9 + x)}'  # Accessing secret_value from enclosing scope (closure)
#     def sub_function_c():
#         print('Sub Function C')
#         return f'Result = {secret_value - 30 * x}'  # Accessing secret_value from enclosing scope (closure)
#     def sub_function_d():
#         print('Sub Function D')
#         print('Result = ',secret_value // 7 + 2*x)  # Accessing secret_value from enclosing scope (closure)
#     # print(sub_function_b(),'\t', sub_function_c())
#     # sub_function_a()
#     # sub_function_d()
#     print('End of Main Function')
#     return sub_function_b(), sub_function_c()

# R = Main_Function(3.2)
# print('\\\\'*10)

# # print(*R)

# # r2 , r3 = Outer_Function()
# # print("\n",[{r2,r3}])


    
        
    
    
# print("\nEx 1 : -")


# def string_operations(base_string = 'World'):
#     def prepend(text):
#         return text + base_string
#     def append(text):
#         return base_string + text
#     def surround(before, after = "!"):
#         return before + base_string + after
    
#     return prepend, append, surround
# # Usage
# prepend_func, append_func, surround_func = string_operations("Python")

# print(prepend_func("hello "))        # Output: "hello world"
# print(append_func("!"))              # Output: "world!"
# print(surround_func("Welcome To the "))  # Output: "Welcome To the world!"


# print('----')


# def account_manager(starting_balance):
#     # Three separate inner functions for banking operations
    
#     def deposit(amount):
#         return starting_balance + amount
    
#     def withdraw(amount):
#         return starting_balance - amount
    
#     def apply_interest(rate_percent):
#         return starting_balance * (1 + rate_percent/100)
    
#     return deposit, withdraw, apply_interest
# # Usage
# deposit_op, withdraw_op, interest_op = account_manager(1000)

# print(f"After deposit: ${deposit_op(500)}")      # $1500
# print(f"After withdrawal: ${withdraw_op(300)}")   # $700  
# print(f"With 5% interest: ${interest_op(5)}")     # $1050




# print('----')

 


# def outer_function(x):
#     print(f"Outer function received: {x}")
#     def inner_ADD_function(y):
#         print(f"Inner ADD function received: {y}")
#         return x + y
#     def inner_SUB_function(y):
#         print(f"Inner SUB function received: {y}")
#         return x - y
#     def inner_MUL_function(y=2):
#         print(f"Inner MUL function received: {y}")
#         return x * y
#     return inner_ADD_function , inner_SUB_function , inner_MUL_function()

# add_func, sub_func , mul_func = outer_function(10)
# print(f"ADD result  == : {add_func(5)}")      # 10 + 5 = 15
# print(f"SUB result ==  : {sub_func(8)}")      # 10 - 8 = 2
# print('***')
# print(f"MUL result ==  : {mul_func}")      # 10 * 20 = 200


# print('----')



# import sympy as sp

# x = sp.Symbol('x')
# def make_multiplier(factor):
#     def multiply(value):
#         return factor * value
#     def Power(value):
#         return value ** factor 
#     def root(value):
#         return sp.sqrt(value) * factor
#     return multiply, Power, root(x)
    
# double ,P2 ,R2 = make_multiplier(2) 
# sp.pprint(P2(x))
# print('####')
# print(double(x))
# print('####')
# sp.pprint(R2)




# print('------')


# def create_calculator(base):
#     def add(num):
#         return base + num
    
#     def multiply(num):
#         return base * num
    
#     def divide(num):
#         if num != 0:
#             return base / num
#         return "Error: Division by zero"
    
#     return add, multiply, divide

# # Create a calculator with base value 10
# add_10, multiply_10, divide_10 = create_calculator(x)

# # Use the inner functions
# print(add_10(5))      # 15
# print(multiply_10(3)) # 30
# print(divide_10(2))   # 5.0

# print('------')

# def make_calculator(initial_value):
#     # Three separate inner functions at the same level
    
#     def adder(x = x):
#         return initial_value + x
    
#     def multiplier(factor = x):
#         return initial_value * factor
    
#     def power(exponent = x):
#         return initial_value ** exponent
    
#     return adder(), multiplier(), power()

# # Usage
# add_func, multiply_func, power_func = make_calculator(5)

# print(add_func)      # Output: 8 (5 + 3)
# print(multiply_func) # Output: 20 (5 * 4)  
# print(power_func)    # Output: 25 (5 ** 2)






# print('\nEx 2 - : ')
# def create_list_operations(base_list):
#     def add_element(*element):
#         base_list.extend(element)
#         return base_list
    
#     # def remove_element(*element):
#     #     if element in base_list:
#     #         base_list.remove(element)
#     #     return base_list
#     def remove_element(*elements):
#         # for el in elements:
#         #     while el in base_list:
#         #         base_list.remove(el)
#         # return base_list
        
#         # [base_list.remove(el) for el in elements for _ in range(base_list.count(el))]
#         # return base_list
    
#         base_list[:] = [x for x in base_list if x not in elements]
#         return base_list
    
    
    
#     def clear_list():
#         base_list.clear()
#         return base_list
    
#     return add_element, remove_element, clear_list

# # Usage
# add, remove, clear = create_list_operations([1, 'Z', 3.14,True])
# print(add(5,6))    # [1, 2, 3, 4]
# print(remove('Z',3.14)) # [1, 3, 4]
# print(clear()) 


# print('------')

# def create_collection_operations(initial_tuple, initial_set): 
#     internal_tuple = list(initial_tuple)
#     internal_set = initial_set
    
#     def tuple_append(*elements):
#         # for element in elements:
#         #     internal_tuple.append(element)
#         # # return tuple(internal_tuple)
        
#         # return tuple([*internal_tuple, *elements])
        
#         # return internal_tuple + tuple(elements)
        
#         # return tuple(list(internal_tuple) + list(elements))
        
#         return tuple(internal_tuple.extend(elements) or internal_tuple)
        
    
#     def tuple_remove(*elements):
#         # for element in elements:
#         #     if element in internal_tuple:
#         #         internal_tuple.remove(element)
#         # return tuple(internal_tuple)
        
#         return tuple(e for e in internal_tuple if e not in elements)
    
#     def set_add(*elements):
#         internal_set.update(elements)
#         return internal_set
    
#     def set_remove(*elements):
#         # for element in elements:
#         #     internal_set.discard(element)
#         # return internal_set
        
#         # return internal_set - set(elements)
#         return internal_set.difference(set(elements))
     
#     def tuple_set_display():
#         return f"Current tuple: {tuple(internal_tuple)}, Current set: {internal_set}"
    
#     return tuple_append, tuple_remove, set_add, set_remove, tuple_set_display

# # Usage
# tuple_append, tuple_remove, set_add, set_remove, tuple_set_display = create_collection_operations((1, 2, 3), {4, 5}) 

# print("Initial state:", tuple_set_display())
# # Add multiple elements to tuple and set
# print("\nAfter adding 400, 500 to tuple:", tuple_append(400, 500))
# print("After adding 666, 777 to set:", set_add(666, 777))
# # Remove multiple elements
# print("\nAfter removing 2, 400 from tuple:", tuple_remove(2, 400))
# print("After removing 5, 666 from set:", set_remove(5, 666))
# # Display current state
# print("\nFinal state:", tuple_set_display())














# def create_dict_operations(base_dict):
#     def display():
#         return base_dict
    
#     def add_key_value(key, value):
#         base_dict[key] = value
#         return base_dict
    
    
#     def remove_key(key):
#         if key in base_dict:
#             del base_dict[key]
#         return base_dict
    
#     def update_values(factor):
#         return {k: v * factor for k, v in base_dict.items()}
    
#     def get_keys():
#         return list(base_dict.keys())
#     return display ,add_key_value ,remove_key, update_values, get_keys
# # Usage
# display,add_kv ,remove_k, update_vals, get_keys = create_dict_operations({'a': 1, 'b': 2})
# print(display())            

# print(add_kv('c', 3))    ; print(remove_k('b'))      ; print(update_vals(2))   ; print(get_keys())          






 
# print("\nEx 3 - : ")
# def create_enumerator(start=0):
#     def enumerate_list(items):
#         return list(enumerate(items, start=start))
    
#     def enumerate_string(text):
#         return list(enumerate(text, start=start))
    
#     return enumerate_list, enumerate_string
# # Usage
# enum_list, enum_str = create_enumerator(start=1)
# print(enum_list(['apple', 'banana', 'cherry']))
# # [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
# print(enum_str('hello'))
# # [(1, 'h'), (2, 'e'), (3, 'l'), (4, 'l'), (5, 'o')]

# print('------')


# def create_zipper(separator=" "):
#     def zip_lists(list1, list2):
#         zipped = zip(list1, list2)
#         return [f"{a}{separator}{b}" for a, b in zipped]
    
#     def zip_dicts(dict1, dict2):
#         keys = zip(dict1.keys(), dict2.keys())
#         return [f"{k1}{separator}{k2}" for k1, k2 in keys]
    
#     return zip_lists, zip_dicts

# # Usage
# zip_items, zip_keys = create_zipper(separator=": ")
# print(zip_items(['name', 'age', 'city'], ['John', 30, 'New York']))
# # ['name: John', 'age: 30', 'city: New York']

# print(zip_keys({'a': 1, 'b': 2}, {'x': 10, 'y': 20}))
# # ['a: x', 'b: y']

# print('------')


# def create_iterable_processor(prefix="Item"):
#     def process_with_enumerate(items):
#         return [f"{prefix} {i+1}: {item}" for i, item in enumerate(items)]
    
#     def process_with_zip(list1, list2):
#         return [f"{a} - {b}" for a, b in zip(list1, list2)]
    
#     return process_with_enumerate, process_with_zip
# # Usage
# enumerator, zipper = create_iterable_processor("Product")
# products = enumerator(['Apple', 'Banana', 'Cherry'])
# for product in products:
#     print(product)

# print()

# prices = zipper(['Apple', 'Banana', 'Cherry'], [1.99, 0.99, 2.99])
# for price in prices:
#     print(price)

# print('------')



# def create_list_processor(prefix="Item"):
#     def process_zip_enumerate(list1, list2):
#         zipped = zip(list1, list2)
#         return [f"{prefix} {i+1}: {a} - {b}" for i, (a, b) in enumerate(zipped)]
    
#     def process_zip_enumerate_start(start):
#         def inner(list1, list2):
#             zipped = zip(list1, list2)
#             return [f"{prefix} {i}: {a} - {b}" for i, (a, b) in enumerate(zipped, start=start)]
#         return inner
    
#     return process_zip_enumerate, process_zip_enumerate_start

# # Usage
# processor, processor_with_start = create_list_processor("Product")
# products = processor(['Apple', 'Banana', 'Cherry'], [1.99, 0.99, 2.99])
# for product in products:
#     print(product)

# print()

# # Create processor with custom start index
# custom_processor = processor_with_start(100)
# custom_products = custom_processor(['Orange', 'Grapes'], [3.49, 4.99])
# for product in custom_products:
#     print(product)






 
# print("\nEx 4 : -")
# def create_map_transformer(factor):
#     def map_multiply(numbers):
#         return list(map(lambda x: x * factor, numbers))
#     def map_add(numbers):
#         return list(map(lambda x: x + factor, numbers))
#     return map_multiply, map_add

# # Usage
# multiply_by_2, add_2 = create_map_transformer(2)
# print("Multiply by 2:", multiply_by_2([1, 2, 3, 4]))
# # Multiply by 2: [2, 4, 6, 8]

# print("Add 2:", add_2([1, 2, 3, 4]))
# # Add 2: [3, 4, 5, 6]
# print('------')


# def create_map_transformer(factor):
#     def map_multiply(numbers):
#         return list(map(lambda x: x * factor, numbers))
#     def map_add(numbers):
#         return list(map(lambda x: x + factor, numbers))
#     return map_multiply, map_add
# # Usage
# multiply_by_2, add_2 = create_map_transformer(2)
# print("Multiply by 2:", multiply_by_2([1, 2, 3, 4]))
# # Multiply by 2: [2, 4, 6, 8]
# print("Add 2:", add_2([1, 2, 3, 4]))
# # Add 2: [3, 4, 5, 6]

# print('------')


# def create_data_processor(value):
#     def apply_map(numbers):
#         return list(map(lambda x: x * value, numbers))
#     def apply_filter(numbers):
#         return list(filter(lambda x: x > value, numbers))
#     return apply_map, apply_filter
# # Usage
# map_func, filter_func = create_data_processor(3)
# print("Map result (x * 3):", map_func([1, 2, 3, 4]))
# # Map result (x * 3): [3, 6, 9, 12]
# print("Filter result (x > 3):", filter_func([1, 2, 3, 4]))
# # Filter result (x > 3): [4]

# print('------')


# def create_processing_chain(min_value, multiplier):
#     def filter_and_multiply(numbers):
#         filtered = filter(lambda x: x > min_value, numbers)
#         return list(map(lambda x: x * multiplier, filtered))
    
#     def process_string_lengths(strings):
#         filtered = filter(lambda s: len(s) > min_value, strings)
#         return list(map(lambda s: len(s) * multiplier, filtered))
#     return filter_and_multiply, process_string_lengths
# # Usage
# chain1, chain2 = create_processing_chain(min_value=2, multiplier=3)
# numbers = chain1([1, 2, 3, 4, 5])
# print("Numbers > 2 multiplied by 3:", numbers)
# # Numbers > 2 multiplied by 3: [9, 12, 15]
# string_lengths = chain2(["a", "ab", "abc", "abcd"])
# print("String lengths > 2 multiplied by 3:", string_lengths)
# # String lengths > 2 multiplied by 3: [9, 12]







 
# print('\nEx 8 - : ')
# def create_args_calculator(base=1):
#     def sum_args(*args):
#         return base + sum(args)
    
#     def multiply_args(*args):
#         result = base
#         for num in args:
#             result *= num
#         return result
    
#     def average_args(*args):
#         if args:
#             return (base + sum(args)) / (len(args) + 1)
#         return base
    
#     return sum_args, multiply_args, average_args
# # Usage
# sum_calc, multiply_calc, average_calc = create_args_calculator()
# print(sum_calc(1, 2, 3))       # 16
# print(multiply_calc(2, 3))     # 60
# print(average_calc(5, 15))     # 10.0
# print('------')


# def create_kwargs_formatter(prefix):
#     def format_name(**kwargs):
#         return f"{prefix}: {kwargs.get('first', '')} {kwargs.get('last', '')}".strip()
    
#     def format_address(**kwargs):
#         return f"{prefix}: {kwargs.get('street', '')}, {kwargs.get('city', '')}"
    
#     def format_contact(**kwargs):
#         return f"{prefix}: {kwargs.get('email', '')} | {kwargs.get('phone', '')}"
#     return format_name, format_address, format_contact
# # Usage
# format_name, format_address, format_contact = create_kwargs_formatter("Contact")
# print(format_name(first="John", last="Doe"))
# # Contact: John Doe
# print(format_address(street="123 Main St", city="New York"))
# # Contact: 123 Main St, New York
# print(format_contact(email="john@example.com"))
# # Contact: john@example.com | 
# print('------')





 
# print('\nEx 9 - : ')
# def create_simple_combiner(base):
#     def combine(*args, **kwargs):
#         result = base
#         for num in args:
#             result += num
#         for value in kwargs.values():
#             result += value
#         return result
    
#     def count_items(*args, **kwargs):
#         return len(args) + len(kwargs)
    
#     def average(*args, **kwargs):
#         total = combine(*args, **kwargs)
#         count = count_items(*args, **kwargs) + 1  # include base
#         return total / count
#     return combine, count_items, average
# # Usage
# combiner, counter, averager = create_simple_combiner(10)
# print(combiner(2, 3, x=4, y=5))  # 10 + 2 + 3 + 4 + 5 = 24
# print(counter(2, 3, x=4, y=5))   # 2 args + 2 kwargs = 4
# print(averager(2, 3, x=4, y=5))  # 24 / 5 = 4.8
# print('------')



# def create_combined_operations(operation):
#     def calculate(*args, **kwargs):
#         if operation == "sum":
#             return sum(args) + sum(kwargs.values())
#         elif operation == "multiply":
#             result = 1
#             for num in args: result *= num
#             for num in kwargs.values():result *= num
#             return result
#         elif operation == "average":
#             all_nums = list(args) + list(kwargs.values())
#             if all_nums:
#                 return sum(all_nums) / len(all_nums)
#             return 0
    
#     def display(*args, **kwargs):
#         items = []
#         for num in args:
#             items.append(f"arg={num}")
#         for key, value in kwargs.items():
#             items.append(f"{key}={value}")
#         return f"{operation}: {', '.join(items)}"
    
#     def process(*args, **kwargs):
#         return {
#             "operation": operation,
#             "input": display(*args, **kwargs),
#             "result": calculate(*args, **kwargs) }
#     return calculate, display, process
# # Usage
# sum_calc, sum_display, sum_process = create_combined_operations("average")
# print(sum_process(11, 22, 101,x=3, y=4))
# # {'operation': 'sum', 'input': 'arg=1, arg=2, x=3, y=4', 'result': 10}

# mult_calc, mult_display, mult_process = create_combined_operations("multiply")
# print(mult_process(20, 3, z=4))
# # {'operation': 'multiply', 'input': 'arg=2, arg=3, z=4', 'result': }
# print('------')


# def create_data_processor(prefix) :
#     def process_args(*args):
#         return f"{prefix}_args: {list(args)}"
    
#     def process_kwargs(**kwargs):
#         return f"{prefix}_kwargs: {dict(kwargs)}"
    
#     def process_both(*args, **kwargs):
#         args_str = ", ".join(str(arg) for arg in args)
#         kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())
#         return f"{prefix}_both: args({args_str}), kwargs({kwargs_str})"
    
#     return process_args, process_kwargs, process_both
# # Usage
# args_processor, kwargs_processor, both_processor = create_data_processor("Data")
# print(args_processor(1, 2, 3))
# # Data_args: [1, 2, 3]
# print(kwargs_processor(name="John", age=30))
# # Data_kwargs: {'name': 'John', 'age': 30}
# print(both_processor(1, 2, name="Jane", city="New York"))
# # Data_both: args(1, 2), kwargs(name=Jane, city=New York)





# print("\nEx 10 :")
# def outer_function(base_value):
#     print(f"Outer function base value: {base_value}")
#     def first_inner(x):
#         print(f"First inner function received: {x}")
#         def second_inner(y):
#             print(f"Second inner function received: {y}")
#             def third_inner(z):
#                 print(f"Third inner function received: {z}")
#                 # Each inner function adds its own parameter
#                 # without modifying outer variables
#                 return base_value + x + y + z
#             return third_inner
#         return second_inner
#     return first_inner

# # Usage example
# closure_example = outer_function(10)
# result = closure_example(5)(3)(2)
# print(result)  # Output: 20 (10 + 5 + 3 + 2)

# # Alternative usage
# step1 = outer_function(100)
# step2 = step1(20)
# step3 = step2(30)
# final_result = step3(5)
# print(final_result)  # Output: 155 (100 + 20 + 30 + 5)
# print('------')


# def text_formatter(prefix):
#     def add_middle(middle):
#         def add_suffix(suffix):
#             # Simply concatenating strings without modification
#             return prefix + " " + middle + " " + suffix
#         return add_suffix
#     return add_middle

# # Usage
# formatter = text_formatter("Hello")
# result = formatter("my")("friend")
# print(result)  # Output: "Hello my friend"
# print('------')

# def math_operations(initial):
#     def multiply_by(factor):
#         def add_to(addend):
#             def divide_by(divisor):
#                 # Each function applies its operation to the accumulated result
#                 return (initial * factor + addend) / divisor
#             return divide_by
#         return add_to
#     return multiply_by

# # Usage
# calc = math_operations(10)
# result = calc(3)(4)(2)
# print(result)  # Output: 17.0 ((10 * 3 + 4) / 2)

"PART 3"










#%%
# print("III Closure + Global,Local,Nonlocal".center(100,'-'))
# print("\nEx 1 - : ")
# def example():
#     value = 10
    
#     def local_version():
#         value = 20  # Shadows outer 'value'
#         return value  # Returns 20
    
#     def nonlocal_version():
#         nonlocal value  # Accesses outer 'value'
#         value = 30  # Modifies outer 'value'
#         return value  # Returns 30
    
#     result = []
#     result.append(f"Before: {value}")                    # 10
    
#     # Call local_version and get its return value
#     local_result = local_version()
#     result.append(f"Local returns: {local_result}")      # 20
#     result.append(f"After local: {value}")               # 10 (unchanged)
    
#     # Call nonlocal_version and get its return value
#     nonlocal_result = nonlocal_version()
#     result.append(f"Nonlocal returns: {nonlocal_result}") # 30
#     result.append(f"After nonlocal: {value}")            # 30 (changed!)
    
#     return "\n".join(result)
# print('-----*-----')

# # Test the function
# output = example()
# print(output)



# def example():
#     value = 10
    
#     def local_version():
#         value = 20  # Shadows outer 'value'
#         return value
    
#     def nonlocal_version():
#         nonlocal value  # Accesses outer 'value'
#         value = 30  # Modifies outer 'value'
#         return value
    
#     # Track all states
#     states = {
#         'before': value,
#         'local_return': local_version(),
#         'after_local': value,
#         'nonlocal_return': nonlocal_version(),
#         'after_nonlocal': value
#     }
    
#     return states

# # Test
# results = example()
# print(f"Before: {results['before']}")                # 10
# print(f"Local returns: {results['local_return']}")   # 20
# print(f"After local: {results['after_local']}")      # 10
# print(f"Nonlocal returns: {results['nonlocal_return']}") # 30
# print(f"After nonlocal: {results['after_nonlocal']}") # 30

# print('-----*-----')


# def example():
#     value = 10
    
#     def local_version():
#         value = 20
#         return value
    
#     def nonlocal_version():
#         nonlocal value
#         value = 30
#         return value
    
#     # Return a tuple with all information
#     return (
#         value,  # before: 10
#         local_version(),  # local returns: 20
#         value,  # after local: 10
#         nonlocal_version(),  # nonlocal returns: 30
#         value  # after nonlocal: 30
#     )

# # Unpack and display
# before, local_ret, after_local, nonlocal_ret, after_nonlocal = example()
# print(f"Before: {before}")                # 10
# print(f"Local returns: {local_ret}")      # 20
# print(f"After local: {after_local}")      # 10
# print(f"Nonlocal returns: {nonlocal_ret}") # 30
# print(f"After nonlocal: {after_nonlocal}") # 30


# print('-----*-----')

# def example():
#     value = 10
    
#     def local_version():
#         value = 20
#         return value
    
#     def nonlocal_version():
#         nonlocal value
#         value = 30
#         return value
    
#     # Return a tuple with all information
#     return (
#         value,  # before: 10
#         local_version(),  # local returns: 20
#         value,  # after local: 10
#         nonlocal_version(),  # nonlocal returns: 30
#         value  # after nonlocal: 30
#     )

# # Unpack and display
# before, local_ret, after_local, nonlocal_ret, after_nonlocal = example()
# print(f"Before: {before}")                # 10
# print(f"Local returns: {local_ret}")      # 20
# print(f"After local: {after_local}")      # 10
# print(f"Nonlocal returns: {nonlocal_ret}") # 30
# print(f"After nonlocal: {after_nonlocal}") # 30





# print('\nEx 2 - : ')
# def outer():
#     x = "outer"  # This is in the enclosing scope
    
#     def inner():
#         nonlocal x  # Refers to x in the nearest enclosing scope (not global)
#         x = "modified"  # MODIFIES outer's x
#         print(f"Inner: {x}")
    
#     inner()
#     print(f"Outer: {x}")

# outer()
# # Output:
# # Inner: modified  
# # Outer: modified

# def counter_with_local():
#     count = 0
    
#     def increment():
#         # This creates a NEW local variable 'count'
#         count = count + 15  # ERROR! UnboundLocalError
#         return count
#     return increment

# def counter_with_nonlocal():
#     count = 0
    
#     def increment():
#         nonlocal count  # Refers to outer count
#         count = count + 1  # MODIFIES outer count
#         return count
#     return increment


# try :
#     counter = counter_with_local()
#     print(counter())  # This will raise an error
# # Using nonlocal version
# except UnboundLocalError as e:
#     print("Error:", e)
# counter = counter_with_nonlocal()
# # print(counter() for counter() in range(4))  # 1
# print([counter() for _ in range(4)])  # [1, 2, 3, 4]

#    # 3

# def create_counter_system(initial_value=0):
#     count = initial_value

#     def increment():
#         nonlocal count
#         count += 1
#         return count

#     def decrement():
#         nonlocal count
#         count -= 1
#         return count

#     def reset(new_value=0):
#         nonlocal count
#         count = new_value
#         return count

#     def get_value():
#         return count

#     return increment, decrement, reset, get_value


# # Usage
# inc, dec, rst, get = create_counter_system(100)

# print([inc() for _ in range(6,30,6)],[dec() for _ in range(5,30,5)])      # 101
# print()      # 102
#      # 101
# print({rst(50) , rst(1.36)} , get())    # 50
# print()      # 50


# print("------")

# def outermost():
#     x = "level 1"
    
#     def middle():
#         x = "level 2"
        
#         def inner():
#             nonlocal x  # Refers to middle's x, not outermost's
#             x = "modified at level 2"
#             print(f"Inner sees: {x}")
        
#         inner()
#         print(f"Middle sees: {x}")
    
#     middle()
#     print(f"Outermost sees: {x}")

# outermost()








 
# def outer_function_with_math():

#     outer_dividend = 200
#     outer_divisor = 12

#     print("Example 4: Nonlocal Variables in Nested Functions")
#     print(f"  Outer dividend = {outer_dividend}, divisor = {outer_divisor}")

#     def inner_math_function():
#         nonlocal outer_dividend, outer_divisor

#         # Local calculations
#         local_quotient = outer_dividend // outer_divisor
#         local_remainder = outer_dividend % outer_divisor

#         print(f"    Inner function calculations:")
#         print(f"      {outer_dividend} // {outer_divisor} = {local_quotient}")
#         print(f"      {outer_dividend} % {outer_divisor} = {local_remainder}")

#         # Modify nonlocal variables
#         outer_dividend = local_remainder * 10  # Use remainder in new calculation
#         outer_divisor = outer_divisor // 2     # Reduce divisor

#         print(f"    Modified nonlocal variables:")
#         print(f"      outer_dividend = {local_remainder} * 10 = {outer_dividend}")
#         print(f"      outer_divisor = {outer_divisor * 2} // 2 = {outer_divisor}")

#         return outer_dividend / outer_divisor

#     result = inner_math_function()
#     print(f"  Final result from inner function: {result}")
#     print(f"  Outer variables after inner function: dividend={outer_dividend}, divisor={outer_divisor}")

#     return result

# # Call the function
# result4 = outer_function_with_math()

# print("\n" + "="*80)
# print("Summary:")
# print(f"Global variables after all operations:")
# print(f"  global_dividend = {global_dividend}")
# print(f"  global_divisor = {global_divisor}")



# print('\nEx 3 - : Nonlocal')
# def outer_function():
#     count = 0  # Local to outer_function 
#     def increment():
#         nonlocal count  # ✅ Refers to outer function's count
#         count += 1
#         return count
    
#     def decrement():
#         nonlocal count
#         count -= 1
#         return count
#     print(f"Initial count: {count}")
#     print(f"After increment: {increment()}")
#     print(f"After increment: {increment()}")
#     print(f"After decrement: {decrement()}")
#     return count
# result = outer_function()
# print(f"Final result: {result}")



# print('\nEx 4 - :')
# # Creating a counter using closure pattern
# def create_counter(start=0):
#     count = start  # Enclosing scope variable
    
#     def increment():
#         nonlocal count  # ✅ Access enclosing function's variable
#         count += 1
#         print(f"Count: {count}")
#         return count
    
#     return increment  # Return the inner function

# # Create two independent counters
# counter1 = create_counter(0)
# counter2 = create_counter(100)

# print("Counter 1:")
# counter1()  # 1
# counter1()  # 2
# counter1()  # 3

# print("\nCounter 2:")
# counter2()  # 101
# counter2()  # 102

# print("\nCounter 1 again:")
# counter1()  # 4 (maintains its own state!)




# print("\n\nEx (Bonus) : Understanding GLOBAL vs LOCAL vs NONLOCAL")
# print("="*60)

# # ============ EXAMPLE 1: GLOBAL ============
# print("\n 1️⃣   GLOBAL - Modifying a variable at the module level:")
# x = 100  # Global variable

# def modify_global():
#     global x  # ✅ Tell Python: use the global x
#     x = 200
#     print(f"  Inside function: x = {x}")

# print(f"Before: x = {x}")
# modify_global()
# print(f"After: x = {x}")  # x is changed globally!


# # ============ EXAMPLE 2: LOCAL (without global) ============
# print("\n 2️⃣  LOCAL - What happens WITHOUT 'global' keyword:")
# y = 100  # Global variable

# def modify_local():
#     y = 200  # ❌ Creates a NEW local variable (doesn't modify global y)
#     print(f"  Inside function: y = {y}")

# print(f"Before: y = {y}")
# modify_local()
# print(f"After: y = {y}")  # y is UNCHANGED! (still 100)


# # ============ EXAMPLE 3: NONLOCAL ============
# print("\n 3️⃣  NONLOCAL - Modifying a variable from the OUTER function:")
# print("(Note: nonlocal ONLY works with nested functions)")

# def outer():
#     z = 100  # Variable in outer function
#     print(f"  Outer function: z = {z}")
    
#     def inner():
#         nonlocal z  # ✅ Tell Python: use z from outer function
#         z = 200
#         print(f"    Inner function: z = {z}")
    
#     inner()  # Call inner function
#     print(f"  After inner(): z = {z}")  # z is changed!
#     return z

# result = outer()
# print(f"Final result: {result}")


# # ============ EXAMPLE 4: WITHOUT NONLOCAL ============
# print("\n4️⃣  What happens WITHOUT 'nonlocal' keyword:")

# def outer2():
#     w = 100  # Variable in outer function
#     print(f"  Outer function: w = {w}")
    
#     def inner2():
#         w = 200  # ❌ Creates a NEW local variable in inner function
#         print(f"    Inner function: w = {w}")
    
#     inner2()
#     print(f"  After inner2(): w = {w}")  # w is UNCHANGED! (still 100)
#     return w

# result2 = outer2()
# print(f"Final result: {result2}")


# # ============ SUMMARY ============
# print("\n" + "="*60)
# print("📚 SUMMARY:")
# print("  • GLOBAL   → Modify variables at module/file level")
# print("  • LOCAL    → Variables only exist inside the function")
# print("  • NONLOCAL → Modify variables from the OUTER function")
# print("              (only works in nested functions)")
# print("="*60)
 

