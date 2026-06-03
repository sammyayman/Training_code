# PYTHON PICKLE LIBRARY EXAMPLES

import pickle
import datetime

print("=== Python Pickle Library Examples ===")

# ============================================
# 1. BASIC PICKLING AND UNPICKLING
# ============================================

print("\n1. Basic Pickling and Unpickling")
print("-" * 40)

# Original data
my_list = [1, 2, 3, 'hello', [4, 5]]
print(f"Original list: {my_list}")

# Pickle (serialize) the object
pickled_data = pickle.dumps(my_list)
print(f"Pickled data (binary): {pickled_data[:50]}...")  # Show first 50 bytes

# Unpickle (deserialize) the object
unpickled_list = pickle.loads(pickled_data)
print(f"Unpickled list: {unpickled_list}")
print(f"Are they equal? {my_list == unpickled_list}")

# ============================================
# 2. PICKLE TO/FROM FILES
# ============================================

print("\n\n2. Pickle to/from Files")
print("-" * 40)

# Data to save
student_data = {
    'name': 'Alice',
    'age': 25,
    'grades': [85, 92, 78, 95],
    'enrolled': datetime.date(2023, 9, 1)
}

print(f"Original data: {student_data}")

# Save to file
with open('student.txt', 'wb') as file:
                                    pickle.dump(student_data, file)
print("✓ Data saved to student.txt")

# Load from file
with open('student.txt', 'rb') as file:
                                    loaded_data = pickle.load(file)
print(f"Loaded data: {loaded_data}")
print(f"Date object preserved: {type(loaded_data['enrolled'])}")

# ============================================
# 3. COMPLEX OBJECTS - CUSTOM CLASSES
# ============================================

print("\n\n3. Pickling Custom Classes")
print("-" * 40)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []
    
    def add_friend(self, friend):
        self.friends.append(friend)
    
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age}, friends={len(self.friends)})"

# Create objects
john = Person("John", 30)
jane = Person("Jane", 28)
john.add_friend("Alice")
john.add_friend("Bob")

print(f"Original object: {john}")

# Pickle the object
with open('person.pkl', 'wb') as file:
    pickle.dump(john, file)

# Unpickle the object
with open('person.pkl', 'rb') as file:
    loaded_john = pickle.load(file)

print(f"Loaded object: {loaded_john}")
print(f"Friends preserved: {loaded_john.friends}")

# ============================================
# 4. MULTIPLE OBJECTS IN ONE FILE
# ============================================

print("\n\n4. Multiple Objects in One File")
print("-" * 40)

# Different types of objects
objects_to_save = [
    [1, 2, 3, 4, 5],
    {'key': 'value', 'number': 42},
    "Hello World",
    Person("Bob", 35)
]

# Save multiple objects
with open('multiple.pkl', 'wb') as file:
    for obj in objects_to_save:
        pickle.dump(obj, file)
print("✓ Multiple objects saved")

# Load multiple objects
loaded_objects = []
with open('multiple.pkl', 'rb') as file:
    try:
        while True:
            obj = pickle.load(file)
            loaded_objects.append(obj)
    except EOFError:
        pass  # End of file reached

print(f"Loaded {len(loaded_objects)} objects:")
for i, obj in enumerate(loaded_objects):
    print(f"  {i+1}: {obj} (type: {type(obj).__name__})")

# ============================================
# 5. PICKLE WITH DIFFERENT PROTOCOLS
# ============================================

print("\n\n5. Different Pickle Protocols")
print("-" * 40)

data = {'test': 'data', 'numbers': [1, 2, 3,5]}

# Different protocols (0-5, with 5 being newest)
for protocol in range(3):  # Show protocols 0, 1, 2
    pickled = pickle.dumps(data, protocol=protocol)
    print(f"Protocol {protocol}: {len(pickled)} bytes")

# Using highest protocol (most efficient)
pickled_highest = pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL)
print(f"Highest protocol: {len(pickled_highest)} bytes")

# ============================================
# 6. WHAT CAN AND CANNOT BE PICKLED
# ============================================

print("\n\n6. What Can and Cannot Be Pickled")
print("-" * 40)

# Things that CAN be pickled
pickleable = [
    [1, 2, 3],              # Lists
    {'a': 1, 'b': 2},       # Dictionaries  
    (1, 2, 3),              # Tuples
    {1, 2, 3},              # Sets
    "string",               # Strings
    42,                     # Numbers
    datetime.datetime.now(), # Datetime objects
    Person("Test", 25)      # Custom class instances
]

print("✓ Successfully pickled:")
for item in pickleable:
    try:
        pickle.dumps(item)
        print(f"  {type(item).__name__}: {str(item)}")
    except:
        print(f"  ❌ Failed: {type(item).__name__}")

# Things that CANNOT be pickled (examples)
print("\n❌ Cannot pickle:")
print("  - Lambda functions")
print("  - Open file objects")
print("  - Database connections") 
print("  - Thread locks")
print("  - Local functions (defined inside other functions)")

# ============================================
# 7. PRACTICAL EXAMPLE - CACHING RESULTS
# ============================================

print("\n\n7. Practical Example - Caching Expensive Results")
print("-" * 40)

import os

def expensive_calculation(n):
    """Simulate an expensive calculation"""
    print(f"  Performing expensive calculation for {n}...")
    result = sum(i*i for i in range(n))
    return result

def cached_calculation(n):
    """Cache results using pickle"""
    cache_file = f'cache_{n}.pkl'
    
    # Check if cached result exists
    if os.path.exists(cache_file):
        print("  Loading from cache...")
        with open(cache_file, 'rb') as file:
            return pickle.load(file)
    
    # Calculate and cache the result
    result = expensive_calculation(n)
    with open(cache_file, 'wb') as file:
        pickle.dump(result, file)
    print("  Result cached!")
    
    return result

# Demo caching
print("First call (will calculate):")
result1 = cached_calculation(1000)
print(f"Result: {result1}")

print("\nSecond call (will use cache):")
result2 = cached_calculation(1000)
print(f"Result: {result2}")

# ============================================
# 8. SECURITY WARNING
# ============================================

print("\n\n8. ⚠️  Security Warning")
print("-" * 40)
print("NEVER unpickle data from untrusted sources!")
print("Pickle can execute arbitrary code during unpickling.")
print("For untrusted data, use JSON or other safe formats.")

# Safe alternative for simple data
import json

safe_data = {'name': 'Alice', 'age': 25, 'scores': [85, 92, 78]}
json_string = json.dumps(safe_data)
loaded_safe = json.loads(json_string)
print(f"JSON alternative: {loaded_safe}")

print("\n=== Summary ===")
print("• pickle saves Python objects as binary data")
print("• Use dump()/load() for files, dumps()/loads() for bytes")
print("• Works with most Python objects including custom classes")
print("• Great for caching, data persistence, and object storage")
print("• ⚠️  Security risk: only unpickle trusted data!")