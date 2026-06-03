import json

print("=== Simple JSON Library Example ===")

# 1. BASIC JSON CONVERSION
print("\n1. Python to JSON and back")
print("-" * 40)

# Python data
Dic_data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "coding", "hiking"],
    "married": False,
    "children": None
}

print(f"Original Python data: {Dic_data}")
print(f"Type: {type(Dic_data)}")
# Convert to JSON string
json_string = json.dumps(Dic_data)
print(f"\nJSON string: {json_string}")
print(f"Type: {type(json_string)}")
# Convert back to Python
back_to_dic= json.loads(json_string)
print(f"\nBack to Python: {back_to_dic}")
print(f"Type: {type(back_to_dic)}")
 
print("\n" + "="*60)

# 2. WRITING JSON TO FILE
print("\n2. Writing JSON to File")
print("-" * 40)

# Student data
students_dict = [
    {"name": "John", "grade": 85, "subjects": ["Math", "Science"]},
    {"name": "Jane", "grade": 92, "subjects": ["English", "History"]},
    {"name": "Bob", "grade": 78, "subjects": ["Math", "Art"]}
]

print(f"Student data: {students_dict}")

#Save to JSON file
with open('students.json', 'w') as file:
    json.dump(students_dict, file, indent=3)  # indent=2 makes it pretty

print("✓ Saved to students.json")

# Show what the file looks like
with open('students.json', 'r') as file:
    print("\nFile contents:")
    print(file.read())
with open('students.json', 'r') as file:
    loaded_students = json.load(file)

print("Loaded from file:")
for i, student in enumerate(loaded_students):
    print(f"  Student {i+1}: {student['name']}, Grade: {student['grade']}")


 

print("\n" + "="*60)
 

data = {"users": [{"id": 1, "name": "Alice", "email": "alice@email.com"}, {"id": 2, "name": "Bob", "email": "bob@email.com"}]}

print("Ugly JSON:")
print(json.dumps(data))

print("\nPretty JSON:")
print(json.dumps(data, indent=4))

 

print("\n" + "="*60)

# 5. DATA TYPE CONVERSIONS
print("\n5. Python vs JSON Data Types")
print("-" * 40)

python_types = {
    "string": "hello",
    "integer": 42,
    "float": 3.14,
    "boolean_true": True,
    "boolean_false": False,
    "null_value": None,
    "list": [1, 2, 3],
    "dict": {"nested": "value"}
}

json_result = json.dumps(python_types, indent=1)
print("Python → JSON conversions:")
print(json_result)
print(type(json_result))
 

print("\n" + "="*60)

# 6. HANDLING ERRORS
print("\n6. Handling JSON Errors")
print("-" * 40)

# Invalid JSON string
dic = {"name": "John", "age": 25 }
invalid_json = str(dic)
print(invalid_json,type(invalid_json))
valid_json = '{"name": "John", "age": 25}'
print(valid_json,type(valid_json))
print()

try: result_1 = json.loads(invalid_json)
except json.JSONDecodeError: print("❌ JSON Error: Invalid JSON format")
try:
    result_2 = json.loads(valid_json)
    print(f"✓ Valid JSON parsed: {result_2}")
    print("JSON parsed successfully")
except json.JSONDecodeError: print("❌ JSON Error: Invalid JSON format")

# Output:
# ❌ JSON Error: Expecting property name enclosed in double quotes: line 1 column 27 (char 26)

# Valid JSON
 
print("\n" + "="*60)

# 7. REAL WORLD EXAMPLE - CONFIG FILE
print("\n7. Real World Example - Configuration")
print("-" * 40)

# Create a configuration file
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp"
    },
    "api": {
        "base_url": "https://api.example.com",
        "timeout": 30,
        "retries": 3
    },
    "features": {
        "debug_mode": True,
        "logging_enabled": True,
        "cache_enabled": False
    }
}

# Save config
with open('config.json', 'w') as file:
    json.dump(config, file, indent=2)

print("✓ Configuration saved")

# Load and use config
with open('config.json', 'r') as file:
    loaded_config = json.load(file)

print("Configuration loaded:")
print(f"Database host: {loaded_config['database']['host']}")
print(f"API URL: {loaded_config['api']['base_url']}")
print(f"Debug mode: {loaded_config['features']['debug_mode']}")

# Output:
# ✓ Configuration saved
# Configuration loaded:
# Database host: localhost
# API URL: https://api.example.com
# Debug mode: True

print("\n=== Summary ===")
print("✓ json.dumps() - Python → JSON string")
print("✓ json.loads() - JSON string → Python")
print("✓ json.dump() - Python → JSON file")
print("✓ json.load() - JSON file → Python")
print("✓ Use indent= for pretty printing")
print("✓ Always handle JSONDecodeError for invalid JSON")