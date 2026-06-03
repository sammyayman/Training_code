# def outer_function(x):
#     print(f"Outer function received: {x}")
#     def inner_function(y):
#         print(f"Inner function received: {y}")
#         return x + y
#     return inner_function

# inner = outer_function(10)
# print(inner(5))

# def make_multiplier(factor, power):
#     def multiply(value):
#         print(f"Outer function received: {factor}")
#         return f"The result of {factor} * {value} is {factor * value}\n"

#     def raise_value(value):
#         print(f"Outer function received: {power}")
#         return f"The result of {value} ** {power} is {value**power}"

#     return multiply, raise_value



# double, double_power = make_multiplier(2, 5)
# triple, triple_power = make_multiplier(3, 3)

# print(double(5))
# print(double_power(2))
# print(triple(6))
# print(triple_power(2))



# def running_total(start=0):
#     total = start

#     def add(value):
#         nonlocal total
#         total += value
#         return total

#     return add


# tracker = running_total(10)
# print(tracker(5))
# print(tracker(20))


# def linear_equation(a, b):
#     def evaluate(x):
#         return a * x + b

#     return evaluate


# line = linear_equation(2, 3)
# print(line(4))


# def customizable_formatter(prefix):
#     def formatter(text):
#         return f"{prefix}: {text}"

#     return formatter


# warning = customizable_formatter("WARNING")
# info = customizable_formatter("INFO")

# print(warning("Disk usage high"))
# print(info("Task completed"))


# def threshold_checker(threshold):
#     def check(value):
#         if value > threshold:
#             return f"{value} is above {threshold}"
#         elif value == threshold:
#             return f"{value} equals {threshold}"
#         else:
#             return f"{value} is below {threshold}"

#     return check


# temperature_checker = threshold_checker(30)
# print(temperature_checker(28))
# print(temperature_checker(30))
# print(temperature_checker(35))


# def limited_counter(limit):
#     count = 0

#     def increment(step=1):
#         nonlocal count
#         if count + step > limit:
#             return f"Limit {limit} reached"
#         count += step
#         return f"Counter: {count}"

#     return increment


# counter = limited_counter(5)
# print(counter())
# print(counter(2))
# print(counter(3))


# def pattern_builder(pattern_type):
#     def build(size):
#         rows = []
#         for i in range(1, size + 1):
#             if pattern_type == "stars":
#                 rows.append("*" * i)
#             else:
#                 rows.append(str(i) * i)
#         return "\n".join(rows)

#     return build


# stars = pattern_builder("stars")
# numbers = pattern_builder("numbers")

# print(stars(3))
# print(numbers(4))


# def rectangle_analyzer(length):
#     def area(width):
#         return length * width

#     def perimeter(width):
#         return 2 * (length + width)

#     return area, perimeter


# area_calc, perimeter_calc = rectangle_analyzer(10)
# print(area_calc(5))
# print(perimeter_calc(5))


# def grading_rules(passing_score):
#     def is_pass(score):
#         return score >= passing_score

#     def status(score):
#         return "Pass" if score >= passing_score else "Fail"

#     return is_pass, status


# passes, status = grading_rules(60)
# print(passes(75))
# print(status(55))


# def bank_account(initial_balance):
#     balance = initial_balance

#     def deposit(amount):
#         nonlocal balance
#         balance += amount
#         return f"Balance after deposit: {balance}"

#     def withdraw(amount):
#         nonlocal balance
#         if amount > balance:
#             return "Insufficient funds"
#         balance -= amount
#         return f"Balance after withdrawal: {balance}"

#     return deposit, withdraw


# deposit_cash, withdraw_cash = bank_account(100)
# print(deposit_cash(50))
# print(withdraw_cash(30))




def outer(x):
    def inner(y):
        return x + y  # inner remembers x
    return inner

add5 = outer(5)
add10 = outer(10)

print(add5(3))   # ?
print(add10(3))  # ?


def outer(a):
    print(f"Outer function :{a}")
    def middle(b):
        print(f"Middle function received: {b}")
        def inner(c):
            print(f"Inner function received: {c}")
            return a + b + c
        return inner
    return middle

f = outer(1)     # remembers a = 1
g = f(2)         # remembers b = 2
print(g(3)) 