#%%
print("==================(A) Basic while loop examples ==================")
# Example 1: Basic Counter
print("\n (1) Simple examples : ")
print("--- Example 1: Basic Counter ---")
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 2

# Example 2: Loop with an 'else' block
print("\n--- Example 2: Loop with 'else' ---")
num = 0
while num < 3:
    print(f"Number is: {num}")
    num += 1
else:
    print("Loop finished successfully.")


# Example 10: Simulating a Countdown
print("\n--- Example 4: Countdown ---")
countdown = 3
while countdown > 0:
    print(f"{countdown}...",end= ' ')
    countdown -= 1
print("Go!")

print("\n (2) Examples with break and continue : ")
# Example 3: Loop with 'continue' (changed from break)
print("\n--- Example 1 : Loop with 'continue' ---")
i = 1
while i <= 10:
    i += 1  # Need to increment i before continue to avoid infinite loop
    if i == 5:
        print("Skipping 5 with continue.")
        continue
    if i == 8 :
        print("break the loop")
        break
    print(f"i is: {i}")
    

print("\n--- Example 2: Loop with 'continue' ---")
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {x}")
    
print("\n (3) continue in a list")   
items = ["α", "+", 2, "β", "-", 3, "γ", "×", 4, "δ", "÷", 5, "ε", "="]
i = 0

while i < len(items):
    element = items[i]

    # Skip operators but mark them
    if element in ["+", "-", "×", "÷", "="]:
        items[i] = f"OP({element})"   # change operator into tagged form
        i += 1
        continue   # skip rest of loop, move to next item

    # Transform Greek letters into uppercase
    if isinstance(element, str) and element.isalpha():
        items[i] = element.upper()
        i += 1
        continue

    # Square numbers
    if isinstance(element, int):
        items[i] = element ** 2
        i += 1
        continue

    i += 1
print("Modified items:", items)

# Example: Difference between continue, pass, and break
print("\n(4)Difference between 'continue', 'pass', and 'break' ---")
print("\n1) Using 'continue' - Skips current iteration:")
i = 0
while i < 5:
    i += 1
    if i == 3:
        print(f"  Skipping {i} with continue")
        continue  # Skip iteration, go to next
    print(f"  Processing: {i}")
print("  Loop finished with continue\n")

print("2) Using 'pass' - Does nothing, continues normally:")
i = 0
while i < 5:
    i += 1
    if i == 3:
        pass  # Does nothing, just placeholder
    print(f"  Processing: {i}")
print("  Loop finished with pass\n")

print("3) Using 'break' - Stops the loop completely:")
i = 0
while i < 5:
    i += 1
    if i == 3:
        print(f"  Breaking at {i}")
        break  # Exit loop immediately
    print(f"  Processing: {i}")
print("  Loop finished with break\n")


print("\n(5) Using continue, pass, and break in a dictionary")
rules = {
    "α": "addition",
    "β": "subtraction",
    "γ": "multiplication",
    "δ": "division",
    "ε": "equals"
}

keys = list(rules.keys())
i = 0

while i < len(keys):
    key = keys[i]
    value = rules[key]

    # Skip (continue) for addition
    if value == "addition":
        rules[key] = "SKIPPED(+)"   # modify value
        i += 1
        continue   # jump to next iteration

    # Placeholder (pass) for subtraction
    if value == "subtraction":
        print("pass at key:", key)
        pass       # does nothing, loop continues
        rules[key] = "SUB(-)"  # still modify value

    # Stop (break) at multiplication
    if value == "multiplication":
        rules[key] = "STOP(×)"  # mark before breaking
        print("break at key:", key)
        break      # exit loop completely

    # Normal processing
    rules[key] = value.upper()
    i += 1

print("\nFinal dictionary:", rules)

print("\n(6) while with 'and' and 'or' ")
# Example 1: while with 'and' operator
print("\n1) while with 'and' operator ---")
x = 0
y = 10
while x < 5 and y > 5:
    print(f"x = {x}, y = {y}")
    x += 1
    y -= 1
print()
# Example 2: while with 'or' operator
print("\n2) while with 'or' operator ---")
num = 0
while num < 3 or num == 0:
    print(f"Number: {num}")
    num += 1
    if num > 3:
        break
print()

print("\n(7) while with bitwise AND (&) and OR (|) operator ---")
print("(3) while with bitwise AND (&) ---")
i = 0
while i < 10 and (i & 1) == 0:  # checks if number is even
    print(f"Even number: {i}")
    i += 2
print()

# Example 4: while with bitwise OR (|)
print("(4) while with bitwise OR (|) operator ---")
a = 5
b = 3
result = a | b  # bitwise OR = 7
count = 0
while count < result:
    print(f"Count: {count}")
    count += 1
print()

print("(5) while with 'and' and 'or' combined ---")
num = 1
while (num > 0 and num <= 5) or num == 0:
    print(f"Valid number: {num}")
    num += 1
    if num > 5:
        break
print()

print("\n(8) while with multiple 'and' conditions")
age = 10
score = 50
while age >= 10 and age <= 20 and score < 100:
    print(f"Age: {age}, Score: {score}")
    age += 1
    score += 10
print()

print("\n(9) while with 'not' operator ")
is_done = False
counter = 0
while not is_done:
    print(f"Processing: {counter}")
    counter += 1
    if counter >= 3:
        is_done = True
print()

print("\n(10) while with comparison and logical operators ")
num1 = 1
num2 = 10
while num1 < num2 and (num1 % 2 == 0 or num1 < 3):
    print(f"num1: {num1}, num2: {num2}")
    num1 += 1
print()

    
    
print("\n (BONUS) : ")
steps = [1, 2, 6, 24, 120]
result = []
i = 0;S = 0  # Move outside the loop
while i < len(steps):
    S += steps[i]  # Accumulate the sum
    result.append(str(steps[i]))
    i += 1
print('+'.join(result) + ' = ', S)

 
steps = [1, 2, 6, 24, 120]
result = []
i = 0
F = 1  # Move outside the loop
while i < len(steps):
    F *= steps[i]  # Accumulate the sum
    result.append(str(steps[i]))
    i += 1
print('*'.join(result) + ' = ', F)
    
    

    

#%%
print("==================(B) Nested while loop examples ==================")
print("\n (1) Multiplication Table (1-3):")
row = 1
while row <= 3:
    col = 1
    while col <= 3:
        print(f"{row} * {col} = {row * col}", end="\t")
        col += 1
    print()  # Newline after each row
    row += 1
print()


print("\n (2) Iterating through a list of words and their characters:")
words = ["theta", "λambda", "π=3.14159", "∑(n=1→∞) 1/n²"]
i = 0
while i < len(words):
    word = words[i]
    print("\n Word:", word)

    j = 0
    while j < len(word):
        print(f" -> Char {j}:", word[j] , end='\t')
        j += 1

    i += 1
    
    
print()

print("\n (3) Iterating through a string and its Unicode code points:")
text = "Ayman"
i = 0
print("Text:", text)
while i < len(text):
    ch = text[i]
    print("\n Character:", ch)

    j = 0
    code = str(ord(ch))  # Unicode code point as string
    while j < len(code):
        print(" -> Digit of code:", code[j], end = '\t')
        j += 1

    i += 1


print()

print("\n (4) Iterating through a tuple of tuples:")
pairs = (("α", "∫x dx"), ("β", "√x"), ("γ", "Σn"))
i = 0
print("Tuple:", pairs , '\n')
while i < len(pairs):
    j = 0
    while j < len(pairs[i]):
        print(f"Tuple {i}, Index {j}:", pairs[i][j], end='\n')
        j += 1
    i += 1

#%%
print("\n (5) Iterating through a set of words and their characters:")
symbols = {"Ωmega", "Δelta", "π≈22/7", "∂f/∂x"}
items = list(symbols)
i = 0
while i < len(items):
    word = items[i]
    print("\nSet element:", word)

    j = 0
    while j < len(word):
        print(f" -> Char {j}:", word[j],end = '\t')
        j += 1

    i += 1


print("\n (6) Iterating through a dictionary of keys and their values:")
#%%
d = {
    "+": "add", 
     "-": "sub",
     "x": "multip", 
     "÷": "div", 
     "=": "equals"
}
keys = list(d.keys())
i = 0
while i < len(keys):
    key = keys[i]
    value = d[key]
    print("\nKey:", key,end= ' ')

    j = 0
    while j < len(value):
        print(f" -> Char {j}:", value[j] , end='\t')
        j += 1

    i += 1
#%%
print("\n(7) Statistics for each row (mean, median, mode) ---")
matrix = [
    [1, 2, 2, 3],
    [4, 5, 5, 6],
    [7, 8, 9, 9]
]
row = 0
print("Matrix:", matrix, '\n')
while row < len(matrix):
    data = matrix[row]
    # Calculate Mean
    i = 0
    total = 0
    while i < len(data):
        total += data[i]
        i += 1
    mean = total / len(data)
    
    # Calculate Median
    sorted_data = []
    i = 0
    while i < len(data):
        j = 0
        while j < len(sorted_data) and data[i] > sorted_data[j]:
            j += 1
        sorted_data.insert(j, data[i])
        i += 1
    n = len(sorted_data)
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    
    # Calculate Mode
    freq = {}
    i = 0
    while i < len(data):
        val = data[i]
        if val in freq:
            freq[val] += 1
        else:
            freq[val] = 1
        i += 1
    max_count = 0
    mode = None
    for key in freq:
        if freq[key] > max_count:
            max_count = freq[key]
            mode = key
    
    print(f"Row {row+1}: Mean = {mean:.2f}, Median = {median}, Mode = {mode}")
    row += 1



# Example: Nested while loop for Factorial and Summation
print("\n (8) Factorial and Summation using Nested While Loop ---")
numbers = [3, 4, 5]
n_idx = 0
while n_idx < len(numbers):
    num = numbers[n_idx]
    
    # Calculate Factorial
    factorial = 1
    i = 1
    while i <= num:
        factorial *= i
        i += 1
    
    # Calculate Summation (1 + 2 + 3 + ... + num)
    summation = 0
    i = 1
    while i <= num:
        summation += i
        i += 1
    
    print(f"Number: {num}, Factorial: {factorial}, Summation (1 to {num}): {summation}")
    n_idx += 1
print()

# Example: Nested while loop for Factorial of each row sum
print("\n(9) Factorial of Row Sums ---")
matrix = [
    [1, 2, 3],
    [2, 3, 4],
    [1, 1, 2]
]
row = 0
while row < len(matrix):
    # Calculate row sum
    col = 0
    row_sum = 0
    while col < len(matrix[row]):
        row_sum += matrix[row][col]
        col += 1
    
    # Calculate factorial of row sum
    factorial = 1
    i = 1
    while i <= row_sum:
        factorial *= i
        i += 1
    
    print(f"Row {row+1}: Sum = {row_sum}, Factorial of sum = {factorial}")
    row += 1
print()

 
# Example: Nested while loop for formula (2*n! + 1)/n!
print("\n(10)Formula: (2*n! + 1)/n! ---")
n_values = [1, 2, 3, 4, 5]
idx = 0
while idx < len(n_values):
    n = n_values[idx]
    
    # Calculate n!
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    
    # Calculate (2*n! + 1)/n!
    result = (2 * factorial + 1) / factorial
    
    print(f"n = {n}: n! = {factorial}, (2*{factorial} + 1)/{factorial} = {result:.4f}")
    idx += 1
print()




#%%
# Example 15: while with ==
print("==================(C) while == or while in loop examples ==================")
print("\n (1) : pending ")
status = "pending"
while status == "pending":
    print("Status is pending, checking again...")
    # In a real scenario, you might check something here
    status = "completed"
print("Status is now completed.")

# Example 16: while with != and user input
print("\n (2): while with != and user input ---")
# Simulating user input
user_inputs = ["hello", "world", "quit"]
input_index = 0
user_input = ""
while user_input != "quit":
    user_input = user_inputs[input_index]
    print(f"Simulating user input: {user_input}")
    input_index += 1




# Example 1: while == (checking status)
print("\n(3): while == (Status Check) ---")
status = "waiting"
attempts = 0
while status == "waiting":
    print(f"Attempt {attempts + 1}: Status is {status}, processing...")
    attempts += 1
    if attempts == 3:
        status = "completed"
print(f"Final status: {status}\n")

 

print("\n (4): while == (Password Verification) ---")
password = "wrong"
attempt = 1
correct_password = "python123"
simulated_inputs = ["wrong", "wrong", "python123"]
input_idx = 0
while password == "wrong":
    password = simulated_inputs[input_idx]
    input_idx += 1
    if password == correct_password:
        print(f"Attempt {attempt}: Password correct! Access granted.")
    else:
        print(f"Attempt {attempt}: Password is wrong, try again.")
    attempt += 1
print()

# Example 3: while == (game state check)
print("\n (5): while == (Game State) ---")
game_state = "playing"
score = 0
moves = [10, 20, 15, 30, 25]
move_idx = 0
while game_state == "playing":
    score += moves[move_idx]
    move_idx += 1
    print(f"Move {move_idx}: Score increased to {score}")
    if score >= 50:
        game_state = "won"
print(f"Game {game_state}! Final score: {score}\n")


#%%
print("\n(6): while == (Perfect Square Check) ---")
numbers = [16, 25, 30, 49]
index = 0
test_numbers = [16, 25, 30, 49]
while index == 0 or index == 1 or index == 2 or index == 3:
    num = test_numbers[index]
    i = 0
    found = False
    while i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8:
        if i * i == num:
            found = True
        i += 1
    result = "yes" if found else "no"
    print(f"{num} is perfect square: {result}")
    index += 1
print()

# Example 2: while == (Fibonacci Number Check)
print("\n(7): while == (Fibonacci Number Check) ---")
test_nums = [5, 8, 10, 13, 21]
idx = 0
while idx in (0, 1, 2, 3, 4):
    target = test_nums[idx]
    a = 0
    b = 1
    is_fib = False
    while a in (0, 1, 2, 3, 5, 8, 13, 21):
        if a == target:
            is_fib = True
        temp = a + b
        a = b
        b = temp
    fib_status = "yes" if is_fib else "no"
    print(f"{target} is Fibonacci: {fib_status}")
    idx += 1
print()

# Example 3: while == (Even Number Sum Check)
print("\n(8): while == (Even Number Sum Check) ---")
lists = [[2, 4, 6], [1, 2, 3], [2, 2, 2]]
list_idx = 0
while list_idx == 0 or list_idx == 1 or list_idx == 2:
    data = lists[list_idx]
    total = 0
    item_idx = 0
    while item_idx == 0 or item_idx == 1 or item_idx == 2:
        if data[item_idx] % 2 == 0:
            total += data[item_idx]
        item_idx += 1
    print(f"List {list_idx + 1}: {data}, Sum of evens: {total}")
    list_idx += 1
print()


# Example 1: while == (Dictionary Value Search)
print("\n(9): while == (Dictionary Value Search) ---")
student_grades = {
    "Ali": "A",
    "Sara": "B",
    "Ahmed": "A",
    "Fatima": "C",
    "Hassan": "A"
}
target_grade = "A"
keys = list(student_grades.keys())
key_idx = 0
students_with_A = []
while key_idx in (0, 1, 2, 3, 4):
    key = keys[key_idx]
    if student_grades[key] == target_grade:
        students_with_A.append(key)
    key_idx += 1
print(f"Students with grade {target_grade}: {students_with_A}")
print()

# Example 2: while == (Dictionary Key Existence Check)
print("\n(10): while == (Dictionary Key Existence) ---")
inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "grape": 3
}
search_items = ["apple", "banana", "mango", "grape"]
item_idx = 0
while item_idx in (0, 1, 2, 3):
    item = search_items[item_idx]
    found_status = "Found" if item in inventory else "Not Found"
    if item in inventory:
        print(f"{item}: {found_status} - Quantity: {inventory[item]}")
    else:
        print(f"{item}: {found_status}")
    item_idx += 1
print()

# Example 3: while in (List of Tuples - Coordinates Check)
print("\n(11): while in (List of Tuples - Coordinates Check) ---")
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
target_coordinate = (3, 4)
coord_idx = 0
while coord_idx in (0, 1, 2, 3):
    if coordinates[coord_idx] == target_coordinate:
        print(f"Target coordinate {target_coordinate} found at index {coord_idx}")
    coord_idx += 1
print()


#%%       
print("\n================== (D) while with != ==================")
print("\n (1) counter != 5 : ")
counter = 0
while counter != 5:
    print(f"Counter is {counter}")
    counter += 1

print("\n(2): User Input Validation ---")
user_input = ""
while user_input.lower() != "yes":
    user_input = input("Do you want to exit? (yes/no): ")
    if user_input.lower() == "no":
        print("Continuing the loop.")
        continue
    elif user_input.lower() == "yes":
        print("Exiting now.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
print("Exiting now.\n".upper())

print("\n(3) while != (Status Not Completed) ---")
task_status = "in_progress"
attempts = 0
statuses = ["in_progress", "in_progress", "completed"]
status_idx = 0
while task_status != "completed":
    task_status = statuses[status_idx]
    attempts += 1
    print(f"Attempt {attempts}: Task status is {task_status}")
    status_idx += 1
print(f"Final status: {task_status}\n")

print("\n(4) while != (Different Values Check) ---")
colors = ["red", "red", "blue", "red", "green"]
color_idx = 0
target_color = "red"
count = 0
while color_idx != 5:
    current_color = colors[color_idx]
    if current_color != target_color:
        print(f"Found different color: {current_color}")
    else:
        count += 1
    color_idx += 1
print(f"Total {target_color} colors: {count}\n")

print("\n(5) while != (Perfect Square Check) ---")
numbers = [4, 9, 16, 25, 36]
num_idx = 0
while num_idx != 5:
    num = numbers[num_idx]
    # Check if number is not a perfect square
    i = 0
    is_perfect_square = False
    while i != 20:
        if i * i == num:
            is_perfect_square = True
        i += 1
    status = "Perfect Square" if is_perfect_square else "Not Perfect Square"
    print(f"{num} is {status}")
    num_idx += 1
print()

print("\n(6) while != (Sum Until Target Reached) ---")
numbers = [2, 3, 5, 4, 6]
target_sum = 15
current_sum = 0
idx = 0
while current_sum != target_sum:
    current_sum += numbers[idx]
    print(f"Step {idx + 1}: Added {numbers[idx]}, Sum = {current_sum}")
    idx += 1
    if idx == 5:
        break
print(f"Target sum reached: {current_sum}\n")

# Example 5: while != (Factorial Comparison Check)
print(" \n(7) while != (Factorial Comparison) ---")
numbers = [3, 4, 5]
num_idx = 0
while num_idx != 3:
    num = numbers[num_idx]
    # Calculate factorial
    factorial = 1
    i = 1
    while i != num + 1:
        factorial *= i
        i += 1
    # Check if factorial is not equal to a target value
    target_factorial = 120
    result_status = "Equals 120" if factorial == target_factorial else "Not Equal to 120"
    print(f"Factorial of {num}: {factorial} - {result_status}")
    num_idx += 1
print()

# Example 6: while != (String Character Comparison)
print("\n(8) while != (String Character Comparison) ---")
text = "programming"
char_idx = 0
target_char = "m"
count = 0
while char_idx != len(text):
    current_char = text[char_idx]
    if current_char != target_char:
        print(f"Index {char_idx}: '{current_char}' is different from '{target_char}'")
    else:
        count += 1
        print(f"Index {char_idx}: '{current_char}' matches '{target_char}'")
    char_idx += 1
print(f"Total matches of '{target_char}' in '{text}': {count}\n")


# Example 7: while != (Dictionary Value Check)
print("\n(9) while != (Dictionary Value Check) ---")
student_scores = {
    "Ali": 85,
    "Sara": 90,
    "Ahmed": 75,
    "Fatima": 90,
    "Hassan": 80
}
target_score = 90
keys = list(student_scores.keys())
key_idx = 0
while key_idx != 5:
    student = keys[key_idx]
    score = student_scores[student]
    if score != target_score:
        print(f"{student}: Score {score} is different from {target_score}")
    else:
        print(f"{student}: Score {score} matches {target_score}")
    key_idx += 1
print()










#%%
print("================== (E) while True loop examples ==================")
# Example 7: Infinite Loop with a Break Condition
print("\n(1): Infinite Loop with a Break ---")
counter = 0
while True:
    print(f"Infinite loop iteration: {counter}")
    counter += 1
    if counter >= 3:
        break

print("\n(2): while True - User Input Validation ---")
print("Simulating user input validation...")
# Simulating user input instead of actual input to prevent blocking
simulated_inputs = ["hello", "world", "exit"]
input_index = 0
while True:
    # user_input = input("Enter 'exit' to quit: ")
    user_input = simulated_inputs[input_index]  # Simulated input
    input_index += 1
    if user_input.lower() == "exit":
        print("Exiting the loop.")
        break
    print(f"You entered: {user_input}")
    if input_index >= len(simulated_inputs):
        break
    
print("\n(3): while True - Menu System ---")
print("Simulating menu system...")
# Simulating menu choices instead of actual input
simulated_choices = ["1", "2", "3", "4"]
choice_index = 0
while True:
    print("\nMenu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")
    
    # choice = input("Enter your choice: ")
    choice = simulated_choices[choice_index]  # Simulated choice
    choice_index += 1
    
    if choice == "1":
        print("You selected Option 1")
    elif choice == "2":
        print("You selected Option 2")
    elif choice == "3":
        print("You selected Option 3")
    elif choice == "4":
        print("Exiting menu...")
        break
    else:
        print("Invalid choice, please try again.")
    
    if choice_index >= len(simulated_choices):
        break
 
# Example 4: while True (String Palindrome Check)
print("\n(4): while True - String Palindrome Check ---")
text = "racecar"
char_idx = 0
is_palindrome = True
while True:
    if char_idx >= len(text) // 2:
        break
    if text[char_idx] != text[len(text) - 1 - char_idx]:
        is_palindrome = False
        break
    print(f"Position {char_idx}: '{text[char_idx]}' == '{text[len(text) - 1 - char_idx]}'")
    char_idx += 1
result = "Yes, it's a palindrome!" if is_palindrome else "No, it's not a palindrome!"
print(f"String '{text}' palindrome check: {result}\n")

# Example 5: while True (Dictionary Key Search)
print("(5): while True - Dictionary Key Search ---")
phone_book = {
    "Ali": "123456",
    "Sara": "234567",
    "Ahmed": "345678",
    "Fatima": "456789",
    "Hassan": "567890"
}
search_keys = ["Ali", "Sara", "Mariam", "Ahmed", "NotFound"]
key_idx = 0
while True:
    if key_idx >= len(search_keys):
        break
    search_name = search_keys[key_idx]
    if search_name in phone_book:
        print(f"Found: {search_name} -> {phone_book[search_name]}")
    else:
        print(f"Not found: {search_name}")
    key_idx += 1
print()

# Example 6: while True (Power/Exponent Calculation)
print("(6): while True - Power Calculation ---")
numbers = [2, 3, 4]
num_idx = 0
while True:
    if num_idx >= len(numbers):
        break
    base = numbers[num_idx]
    exponent = 3
    result = 1
    exp_idx = 0
    while True:
        if exp_idx >= exponent:
            break
        result *= base
        exp_idx += 1
    print(f"{base}^{exponent} = {result}")
    num_idx += 1
print()

# Example 7: while True (GCD - Greatest Common Divisor)
print("(7): while True - GCD Calculation ---")
pairs = [(48, 18), (100, 50), (17, 5)]
pair_idx = 0
while True:
    if pair_idx >= len(pairs):
        break
    a, b = pairs[pair_idx]
    while True:
        if b == 0:
            break
        temp = b
        b = a % b
        a = temp
    print(f"GCD of {pairs[pair_idx][0]} and {pairs[pair_idx][1]}: {a}")
    pair_idx += 1
print()

# Example 8: while True (Sum of Series 1+2+3+...+n)
print("(8): while True - Sum of Series ---")
numbers = [5, 10, 15]
num_idx = 0
while True:
    if num_idx >= len(numbers):
        break
    n = numbers[num_idx]
    sum_result = 0
    i = 1
    while True:
        if i == 0:
            break
        sum_result += i
        i += 1
        if i > n:
            break
    print(f"Sum of series 1 to {n}: {sum_result}")
    num_idx += 1
print()

# Example 9: while True (Probability - Coin Flip Count Until Heads)
print("(9): while True - Probability (Coin Flip) ---")
import random
trials = 3
trial_idx = 0
while True:
    if trial_idx >= trials:
        break
    flip_count = 0
    result = ""
    while True:
        flip = random.choice(["Heads", "Tails"])
        flip_count += 1
        result = flip
        print(f"Trial {trial_idx + 1}, Flip {flip_count}: {flip}")
        if flip == "Heads":
            break
    print(f"Got Heads after {flip_count} flips\n")
    trial_idx += 1
print()

# Example 10: while True (Passcode Validation)
print("(10): while True - Passcode Validation ---")
correct_passcode = "1234"
attempts = 0
max_attempts = 4
attempted_codes = ["5678", "1111", "1234"]
attempt_idx = 0
while True:
    if attempts >= max_attempts:
        print("Maximum attempts reached. Access denied!")
        break
    passcode = attempted_codes[attempt_idx]
    attempts += 1
    print(f"Attempt {attempts}: Entered passcode '{passcode}'")
    if passcode == correct_passcode:
        print("Passcode correct! Access granted!")
        break
    else:
        print(f"Incorrect passcode. Attempts remaining: {max_attempts - attempts}\n")
    attempt_idx += 1
print()










#%%
print("================== (F) while loop with variables ==================")
# Example 9: Processing items from a list with pop()
print("\n(1)Processing items with pop() ---")
tasks = ['Task 1', 'Task 2', 'Task 3']
while tasks:
    current_task = tasks.pop(0) # Process from the front
    print(f"Processing: {current_task}")
print("All tasks processed.")

# Example 10: Processing items from a dictionary with popitem()
print("\n(2) Processing items with popitem() ---")
student_scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
while student_scores:
    name, score = student_scores.popitem()
    print(f"{name} scored {score}")
print("All scores processed.")


print("\n(3) while variable with string , tuple , set , dictionary ---")
text = "Python"
symbols = ("π", "√", "Σ")
s = {"Δ", "Ω", "θ"}
d = {"α": "+", "β": "-", "γ": "×"}

print('\n',text)
while text:  # runs while string is not empty
    print("Current:", text , end= '')
    text = text[1:]  # remove first character each time
print('\n',symbols)
while symbols:  # runs while tuple is not empty
    print("Symbol:", symbols[0] , end= ' ')
    symbols = symbols[1:]  # drop first element
print('\n',s)
while s:  # runs while set is not empty
    item = s.pop()  # remove an element
    print("Removed:", item)
    
print('\n',d)
while d:  # runs while dictionary is not empty
    key, value = d.popitem()  # remove one key-value pair
    print("Rule:", key, "->", value)
    
    
print("\n(4 Factorial Builder with and)")   
n = 5
result = 1
sum = 0
while n and result:   # runs while n != 0 AND result != 0
    result *= n
    sum += n
    n -= 1

print("Factorial =", result , "Sum =", sum)

print("\n(5)Polynomial Term Collector with or")    
terms = ["x²", "2x", "3"]
symbols = ["+", "-"]

while terms or symbols:   # runs while at least one list is non-empty
    if terms:
        print("Term:", terms.pop(0))
    if symbols:
        print("Symbol:", symbols.pop(0))

print("\n(6) ummation Until Zero with and or")
numbers = [1, 2, 3, 4]
total = 0

while numbers and (total == 0 or total):  # numbers must be non-empty AND total is valid
    total += numbers.pop(0)
    print("Running total:", total)

print("Final sum =", total)

print("\n(7) while variable (List Processing with Data Validation) ---")
data = [100, 50, 200, 75, 150]
while data:
    value = data.pop(0)
    print(f"Processing value: {value}")
print("All data processed!\n")

print("(8) while variable (Dictionary Temperature Readings) ---")
temperatures = {
    "Monday": 25,
    "Tuesday": 28,
    "Wednesday": 26,
    "Thursday": 30,
    "Friday": 27
}
while temperatures:
    day, temp = temperatures.popitem()
    print(f"{day}: {temp}°C")
print("All readings processed!\n")

print("(9) while variable (Fibonacci Sequence Generation) ---")
fib_list = []
a, b = 0, 1
while a != 0 or b != 1 or len(fib_list) == 0:
    fib_list.append(a)
    next_fib = a + b
    a = b
    b = next_fib
    if b > 100:
        break
print(f"Fibonacci sequence: {fib_list}\n")

print("(10) while variable (Prime Factorization without pop) ---")
numbers_to_factor = [12, 28, 35]
num_idx = 0
while num_idx != len(numbers_to_factor):
    num = numbers_to_factor[num_idx]
    factors = []
    temp = num
    divisor = 2
    while divisor != temp:
        if temp % divisor == 0:
            factors.append(divisor)
            temp = temp // divisor
        else:
            divisor += 1
        if temp == 1:
            break
    print(f"Prime factors of {num}: {factors}")
    num_idx += 1
print()

print("(11) while variable (Powers and Exponents Sum without pop) ---")
exponents = [1, 2, 3, 4, 5]
base = 2
power_sum = 0
idx = 0
while idx != len(exponents):
    exp = exponents[idx]
    power = 1
    counter = 0
    while counter != exp:
        power *= base
        counter += 1
    power_sum += power
    print(f"{base}^{exp} = {power}")
    idx += 1
print(f"Sum of all powers: {power_sum}\n")

# %%
