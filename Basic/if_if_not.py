# Examples of 'if' and 'if not' statements
# 'if' checks if a condition is True.
# 'if not' checks if a condition is False (or "falsy").

print("--- Example 1: Boolean Flags (One-Liners) ---")
is_logged_in, is_premium_user = True, False

# Simple if (One-liner)
print("User is logged in.") if is_logged_in else None

# Simple if not (One-liner)
print("User is NOT a premium user (show ads).") if not is_premium_user else None

# is_logged_in = True
# is_premium_user = False

# # Simple if
# if is_logged_in:
#     print("User is logged in.")

# # Simple if not
# if not is_premium_user:
#     print("User is NOT a premium user (show ads).") 
print()


print("--- Example 2: Checking for Empty Data Structures ---")
# In Python, empty lists, strings, dictionaries, and 0 are considered "falsy".
username = ""
cart_items = []

# # Checking if string is empty using 'if not'
print("Username is empty! Please enter a name.") if not username else print("Welcome, " + username)
# if not username:
#     print("Username is empty! Please enter a name.")
# else:
#     print("Welcome ," + {username})

# # Checking if list is not empty using 'if'
print(f"You have {len(cart_items)} items in your cart.") if cart_items else print("Your cart is empty.")
# if cart_items:
#     print(f"You have {len(cart_items)} items in your cart.")
# else:
#     # This block runs if cart_items is empty (falsy)
#     print("Your cart is empty.")

# # Using 'if not' explicitly on the list
print("Cart is definitely empty (verified with 'if not').") if not cart_items else None
# if not cart_items:
#     print("Cart is definitely empty (verified with 'if not').")
print()


print("--- Example 3: Membership Testing (in / not in) ---")
banned_users = ["spammer1", "bot99", "hacker_x"]
current_user = "guest_123"

# Check if NOT in list
if current_user not in banned_users:
    print(f"Access granted for {current_user}.")

#OR : 
print(f"Access denied for {current_user}.") if current_user in banned_users else print("Access denied !")

# Check if IN list
suspect = "bot99"
if suspect in banned_users:
    print(f"ALERT: {suspect} is banned!")
else:
    print(f"{suspect} is NOT banned.")
# OR : 
print(f"ALERT: {suspect} is NOT banned!") if suspect not in banned_users else print(f"ALERT: {suspect} is banned!")
print()


print("--- Example 4: Checking for None (One-Liner) ---")
# 'if not' is often used to check if a variable is None (or empty)
config_settings = None

# Using explicit 'if not' in a one-line compound statement
if not config_settings: config_settings = {"theme": "dark", "version": 1.0}; print("No configuration found, loading defaults...")

# Using explicit 'if' in a one-line compound statement
if config_settings: print(f"Configuration loaded: {config_settings}")
print()


print("--- Example 5: Real-world filtering loop ---")
# Using 'if not' to filter out invalid or empty entries
raw_data = ["alice@email.com", "", "bob@email.com", None, "   ", "charlie@email.com"]
valid_emails = []

print(f"Raw data: {raw_data}")

for email in raw_data:
    # check if email is None OR if stripped string is empty
    if not email or not email.strip():
        continue # Skip this iteration
    
    valid_emails.append(email.strip())

print(f"Valid emails: {valid_emails}")
# OR : 
valid_emails = [email.strip() for email in raw_data if email and email.strip()]

print(f"Valid emails: {valid_emails}")

print()



print()
print()

print("--- Example 6: Probability validity and decision ---")
p = 0.7
valid = (p == min(1.0, max(0.0, p)))
likely = bool(int(p * 2))
if not valid: print("Invalid probability")
elif likely and valid: print("Event more likely than not")
else: print("Event less likely than not")
print()

print("--- Example 7: At least one success ---")
p, n = 0.3, 4
p_any = 1 - (1 - p) ** n
bucket = int(p_any * 10)
if bucket in {7, 8, 9, 10}: print(f"High chance: {p_any:.3f}")
elif (bucket in {4, 5}) or (bucket == 6): print(f"Moderate chance: {p_any:.3f}")
else: print(f"Low chance: {p_any:.3f}")
print()

print("--- Example 8: Poisson occurrence ---")
import math
lam = 0.6
p_ge1 = 1 - math.exp(-lam)
likely = (int(p_ge1 * 10) in {5, 6, 7, 8, 9, 10}) and (lam == min(lam, 1.0))
unlikely = not (int(p_ge1 * 10) in {5, 6, 7, 8, 9, 10})
if likely: print(f"Likely occurrence: {p_ge1:.3f}")
elif unlikely: print(f"Unlikely occurrence: {p_ge1:.3f}")
else: print(f"Possible occurrence: {p_ge1:.3f}")
print()

print("--- Example 9: Expected value decision ---")
p_success, reward, cost = 0.55, 120, 60
ev = p_success * reward
risk_aversion_low = True
proceed = (ev == max(ev, cost)) or ((ev == max(ev, 0.9 * cost)) and risk_aversion_low)
if proceed: print("Proceed")
elif not proceed: print("Skip")
print()

print("--- Example 10: Confidence interval membership ---")
phat, n, z = 0.58, 300, 1.96
m = z * ((phat * (1 - phat)) / n) ** 0.5
p0 = 0.55
lower = phat - m
upper = phat + m
clamp = min(upper, max(lower, p0))
inside = clamp == p0
if inside: print("Within interval")
elif not inside: print("Outside interval")
print()


print("--- Example 11: Set Union (∪) and OR ---")
A = {"red", "green"}
B = {"green", "blue"}
U = A | B
want = ("red" in U) or ("blue" in U)
if want and U: print(f"Union: {sorted(list(U))}")
elif not U: print("Union empty")
else: print("Union present")
print()

print("--- Example 12: Set Intersection (∩) and AND ---")
A = {1, 2, 3}
B = {3, 4, 5}
I = A & B
ok = (3 in I) and bool(I)
if ok: print(f"Intersection includes 3: {I}")
elif I: print(f"Intersection non-empty: {I}")
else: print("Intersection empty")
print()

print("--- Example 13: XOR (exclusive OR) ---")
a, b = True, False
x = a ^ b
if x: print("Exactly one true")
elif not x: print("Both same truth value")
print()

print("--- Example 14: XAND (XNOR equivalence) ---")
a, b = True, True
xand = not (a ^ b)
if xand and (a or b): print("Both true or both false")
else: print("Mixed truth values")
print()

print("--- Example 15: NOT and Symmetric Difference ---")
A = {"apple", "banana", "cherry"}
B = {"banana", "date"}
sym = A ^ B
only_A = A - B
only_B = B - A
use_not = not ("date" in A)
if use_not and (("date" in B) or ("banana" in sym)): print(f"Exclusive items: {sym}")
elif (only_A and not only_B) or (only_B and not only_A): print("Exclusive in one set only")
else: print("Overlap present")

print("--- Example 16: printf-style formatting with %s and %d ---")
name = "alice"
count = len(valid_emails)
msg = "User %s has %d valid emails" % (name, count)
if (name and count) or (name and not count):
    print(msg if count else "User %s has %d valid emails" % (name, 0))
else:
    print("User %s not found" % ("unknown"))
print()

print("--- Example 17: mixed logic with %s and %d ---")
U_local = {"red", "green"} | {"green", "blue"}
union_size = len(U_local)
xor_flag = (True ^ False)
status = "xor=%s, union=%d" % ("true" if xor_flag else "false", union_size)
if xor_flag or union_size:
    print(status)
else:
    print("xor=%s, union=%d" % ("false", 0))

print("--- Example 18: Data type checking ---")
values = [42, 3.14, "hello"]
for v in values:
    is_int = isinstance(v, int)
    is_float = isinstance(v, float)
    is_str = isinstance(v, str)
    if is_int and not is_float and not is_str: print(f"{v} is int")
    elif is_float and not is_int and not is_str: print(f"{v} is float")
    elif is_str and not is_int and not is_float: print(f"{v} is string")
    else: print("unknown type")
print()

print("--- Example 19: Calculus continuity at x0 ---")
import math
def f(x): return (x * x) if (x < 1) else (2 * x - 1)
x0 = 1.0
h = 1e-6
left = f(x0 - h)
right = f(x0 + h)
value = f(x0)
cont = abs(left - value) < 1e-5 and abs(right - value) < 1e-5
if cont and (left == min(left, max(left, value)) or right == min(right, max(right, value))): print("Continuous at x0")
else: print("Not continuous at x0")
print()

print("--- Example 20: Algebra distributive property ---")
a, b, c = 3, 4, 5
left = a * (b + c)
right = a * b + a * c
holds = (left == right)
assoc = ((a + b) + c) == (a + (b + c))
if holds and assoc: print("Distributive and associative hold")
elif holds or assoc: print("One property holds")
else: print("Properties fail")
print()

print("--- Example 21: Types with type() ---")
x = 5
y = 3.14
s = "Hello"
A = [1, 2, 3]
B = {1, 2, 3}
D = {"name": "Ayman", "age": 30}
items = [("x", x), ("y", y), ("s", s), ("A", A), ("B", B), ("D", D)]
for label, val in items:
    is_known = type(val) in (int, float, str, list, set, dict)
    if is_known and (type(val) is int or type(val) is float or type(val) is str):
        print("%s: %s" % (label, type(val).__name__) ,end=", ")
        
        
        
    elif is_known and (type(val) is list or type(val) is set or type(val) is dict):
        
        print("%s: %s" % (label, type(val).__name__) ,end=", ")
        
    elif not is_known: print("%s: unknown" % label)

print(type(items).__name__)
print()

print("--- Example 22: Calculus – derivative sign ---")
def g(x): return x**3 - 2*x
x0 = 1.0
h = 1e-4
d = (g(x0 + h) - g(x0 - h)) / (2*h)
if d > 0: print("Increasing at x0")
elif d < 0: print("Decreasing at x0")
elif not (d > 0 or d < 0): print("Stationary at x0")
print()

print("--- Example 23: Calculus – limit near zero ---")
def lfun(x): return (math.sin(x) / x) if x != 0 else 1.0
vals = [lfun(t) for t in [1e-1, 1e-2, 1e-3]]
eps = 1e-3
near_all = all(abs(v - 1.0) < eps for v in vals)
far_any = any(abs(v - 1.0) > eps for v in vals)
if near_all and not far_any: print("Limit ~ 1")
else: print("Limit not close to 1")
print()

print("--- Example 24: Algebra – quadratic roots ---")
a, b, c = 1, -3, 2
disc = b*b - 4*a*c
if disc > 0: print("Two real roots")
elif not (disc > 0 or disc < 0): print("One real root")
else: print("Complex roots")
print()

print("--- Example 25: Algebra – matrix invertibility ---")
a, b, c, d = 2, 3, 1, 4
det = a*d - b*c
if (det > 0 or det < 0): print("Invertible matrix")
elif not (det > 0 or det < 0): print("Singular matrix")


























# PYTHON EXAMPLES

# 1. Basic if and if not
age = 18
if age: print(f"Age is {age} (truthy)")
age = 0
if not age: print("Age is 0 or None (falsy)")

# 2. Checking for empty/filled collections
users = ["Alice", "Bob"]
empty_list = ["A"]

if users:
     print("We have users!", " | ".join(f"{i+1} - {user}" for i, user in enumerate(users)))
 

print("No items in empty_list"if not empty_list else "empty_list is not empty")

# 3. Checking for None vs actual values
name = None
valid_name = "John"

if name is None: print("Name is not set")

if valid_name is not None:print(f"Name is set to: {valid_name}")

# 4. String checking
message = "Hello"
empty_string = ""


print(f"Message exists: '{message}'"if message else "No message")

print("Empty string is ","falsy"if not empty_string else "not falsy")

# 5. Multiple conditions
import pandas as pd
from IPython.display import display
student_data = pd.DataFrame({"score": [85,80,90,75], "passed": [True,False,True,False]})
student_data.index = ["Student 1","Student 2","Student 3","Student 4" ]
display(student_data)

for i, data in student_data.iterrows():
    # print(i,data["score"], data["passed"])
    if data["score"] <= 80 and not data["passed"]:
        print(f"{i} passed but lower than 80 {data['passed']}")
    elif data["score"] > 80 and data["passed"]:
        print(f"{i} passed with high score! {data['passed']}")
    print(f"{i} result :","\tfailed! "if not data["passed"] else "\tSuccess!")



# 6. Membership testing
fruits = ["apple", "banana", "orange"]

for i in range(len(fruits)):
    if fruits[i] in fruits: print(f"{i+1} - {fruits[i]} is available")

print("This fruit is not available" if "grape" not in fruits else "This fruit is available")

# 7. Dictionary checking
user_data = {"name": "Alice", "age": 25}
empty_dict = {}

if user_data:
    print("User data exists")
    if "name" and "age" in user_data:
        print(f"User name: {user_data['name']}", f"User age: {user_data['age']}")


print("Dictionary is empty"if not empty_dict else "Dictionary is not empty")

# 8. Boolean logic combinations
is_weekend , is_sunny , has_plans = True, False, True

print("Good day to go out!"if is_weekend and (is_sunny or has_plans) else "Not a good day to go out!")
print("Either not weekend or not sunny"if not (is_weekend and is_sunny) else "Weekend and sunny")

# 9. File/object existence checking
file_path = "/path/to/file.txt"

# Simulating file existence check
file_exists = False  # This would normally be os.path.exists(file_path)

print("File found, processing...") if file_exists else print("File not found")
print("Creating new file...") if not file_exists else None

# 10. Nested conditions
user_role = ""
is_logged_in = True

if is_logged_in and user_role:
    print(f"{user_role} access granted")
    
elif is_logged_in and user_role is None:
    print("No role, limited access")

else: print("Please log in")

# Alternative using 'and'
user_role = "admin"
if is_logged_in and user_role == "admin":
    print("Direct admin check")

# 11. Falsy values in Python
falsy_values = [False, 0, 0.0, "", [], {}, None,45]

for value in falsy_values:
    if not value:print(f"{value} is falsy")
    else:print(f"{value} is truthy")

# 12. Exception handling context
def process_data(data = None): return data
DATA = process_data(48645)
if DATA is   None: print("No data to process")
else:print(f"Data processed  : {DATA}")

# 13. Function return checking
def get_user_input(text = ""): return text  

user_input = get_user_input("Enter something: ")
if user_input:
    print(f"User entered: {user_input}")
else:
    print("No input provided")

if not user_input:
    print("Please enter something")

# 14. Complex boolean expressions
temperature, humidity, is_raining = 75, 60, False
result = "Perfect weather for outdoor activities!"if temperature > 70 and humidity < 80 and not is_raining else "Not perfect weather"
print(result)

# 15. Short-circuit evaluation
def expensive_operation(): return True

condition1 = False
print("Both conditions met"if condition1 and expensive_operation() else "At least one condition not met")
print("Both conditions met"if condition1 and not expensive_operation() else "At least one condition not met")
print("Both conditions met"if not condition1 and expensive_operation() else "At least one condition not met")

print("At least one condition met"if condition1 or not expensive_operation() else "Not all conditions met")
print("At least one condition met"if not condition1 or  not expensive_operation() else "Not all conditions met")

condition2 = True
print("At least one condition met"if condition2 or expensive_operation() else "At least one condition not met")
print("At least one condition met"if not condition2 or not expensive_operation() else "Not all conditions met")

# IF TRUE - Examples and Use Cases

# 1. LITERAL "if True" - Always executes
if True:
    print("This will always run")
    print("Used for testing or temporary code blocks")

# 2. VARIABLE CONTAINING True
is_valid = True
if is_valid:  # This is preferred
    print("Variable is True")

# Alternative (less Pythonic):
if is_valid == True:
    print("Explicitly checking if equals True")

# Even more explicit (rarely needed):
if is_valid is True:
    print("Checking if variable IS the True object")

# 3. FUNCTION RETURNING True
def check_permission():
    return True

if check_permission():
    print("Permission granted")

# 4. COMPARISON RESULTING IN True
age = 25
if age > 18:  # This evaluates to True
    print("Adult")

# 5. BOOLEAN EXPRESSIONS
has_license = True
is_sober = True

if has_license and is_sober:  # Both must be True
    print("Can drive")

# 6. TEMPORARY CODE BLOCKS (common use of literal "if True")
if True:  # Used to temporarily enable code
    print("Debug mode enabled")
    debug_var = "test"
    print(f"Debug: {debug_var}")

# You might change to "if False:" to disable
if False:  # This block won't run
    print("This debug code is disabled")

# 7. WHILE TRUE LOOPS (infinite loops)
counter = 0
while True:
    print(f"Count: {counter}")
    counter += 1
    if counter >= 3:
        break  # Exit the infinite loop

# 8. TESTING CONDITIONS
import pandas as pd
from IPython.display import display
def test_conditions():
    # Testing different scenarios
    test_cases = [
        (True, "Should pass"),
        (False, "Should fail"),
        (1, "Truthy number"),
        (0, "Falsy number"),
        ("hello", "Truthy string"),
        ("", "Falsy string")
    ]
    df_test_cases = pd.DataFrame(test_cases, columns=["Condition", "Description"])
    
    for idx, row in df_test_cases.iterrows():
        condition ,description = row["Condition"], row["Description"]
        print(f"{idx}. {'✓' if condition else '✗'} {description} - {'PASSED' if condition else 'FAILED'}")

test_conditions()

# 9. CONFIGURATION FLAGS
DEBUG_MODE = True
ENABLE_LOGGING = True

if DEBUG_MODE:
    print("Debug information will be shown")

if ENABLE_LOGGING:
    print("Logging is enabled")

# 10. CONDITIONAL COMPILATION/EXECUTION
DEVELOPMENT = True
PRODUCTION = False

if DEVELOPMENT:
    print("Running in development mode")
    # Development-specific code
elif PRODUCTION:
    print("Running in production mode")
    # Production-specific code

# 11. TRUTHINESS EXAMPLES
# These all evaluate to True in if statements:# Your original data
truthy_values = [
    True,False,None,
    1, 2, "",           # Non-zero numbers and empty string
    "hello", " ",       # Non-empty strings
    [1, 2], [0], [],0,       # Lists and zero
    {"": ""},{},   # Dictionaries
    (None,), () ,((),())            # Tuples
]

print("=== Filter True from False ===")

# Filter TRUE values (truthy)
true_values = list(filter(None, truthy_values))
print("TRUE values:")
print(true_values)

# Filter FALSE values (falsy)
false_values = list(filter(lambda x: not x, truthy_values))
print("\nFALSE values:")
print(false_values)

print("\n=== With formatting ===")
print("✓:", [f"{repr(v)} " for v in true_values])
print("✗:", [f"{repr(v)} " for v in false_values])
# 12. EXPLICIT TRUE CHECKING (when you specifically need True, not just truthy)
def explicit_true_check():
    values = [True, 1, "hello", [1]]
    
    print([f"  {repr(value)} is {'✓' if value else '✗'}" for value in values])
    
    print("\nChecking 'if value is True:'")
    for value in values:
        if value is True:
            print(f"  {repr(value)} is exactly True")
        else:
            print(f"  {repr(value)} is truthy but not True")

explicit_true_check()

# 13. EARLY RETURN PATTERN
def process_data(data):
    if not data:  # Same as: if data == False or data is None, etc.
        return "No data provided"
    
    # Process the data
    return f"Processed: {data}"

print(f"\n{process_data('')}")      # No data provided
print(f"{process_data('hello')}")   # Processed: hello

# 14. TOGGLE FUNCTIONALITY
feature_enabled = True

if feature_enabled:
    print("New feature is active")
    # Feature code here
else:
    print("Using legacy functionality")
    # Legacy code here

# 15. ERROR HANDLING WITH BOOLEAN FLAGS
success = True
error_occurred = False

if success and not error_occurred:
    print("Operation completed successfully")
elif not success:
    print("Operation failed")
elif error_occurred:
    print("An error occurred during operation")

# 16. COMMON PATTERNS TO AVOID
# Instead of this:
if is_valid == True:
    pass

# Do this:
if is_valid:
    pass

# Instead of this:
if is_valid != False:
    pass

# Do this:
if is_valid:
    pass

# 17. WHEN TO USE "if True:" LITERALLY
print("\nLegitimate uses of 'if True:':")
print("1. Temporarily enabling code blocks during development")
print("2. Creating code blocks for organization (though functions are better)")
print("3. Placeholder for future conditional logic")

# Example of placeholder:
if True:  # TODO: Add actual condition later
    print("Temporary code block")
    # Will be replaced with real condition like:
    # if user.is_authenticated() and user.has_permission():

# 18. BEST PRACTICES
print("\nBest Practices:")
print("- Use 'if variable:' instead of 'if variable == True:'")
print("- Use 'if not variable:' instead of 'if variable == False:'")
print("- Only use 'if True:' for temporary/debug code")
print("- Use 'if variable is True:' only when you need exactly True (rare)")