# # SIMPLE PYTHON io LIBRARY EXAMPLES
# print("\033c")
import io

buffer = io.StringIO()
buffer.write("Hello World!")
buffer.write(" How are you?")
buffer.write(" Nice day!")

print(f"\nWrote: 'Hello World! How are you? Nice day!'")

# Without seek - cursor is at the END
print(f"Current position: {buffer.tell()}")  # Shows current cursor position
data = buffer.read()
print(f"Reading from current position: '{data}'") 

buffer.seek(0)  # Go to position 0 (start)
print("After seek(0) - cursor at beginning:")
data = buffer.read()
print(f"Now reading: '{data}'")

# Move cursor to middle
buffer.seek(6)  # Go to position 6
print(f"\nAfter seek(6) - cursor at position 6:")
data = buffer.read()
print(f"Reading from position 6: '{data}'")

# Move cursor to specific position
buffer.seek(13)  # Go to position 13
print(f"\nAfter seek(13) - cursor at position 13:")
data = buffer.read()
print(f"Reading from position 13: '{data}'")

buffer.close()
print("\n" + "="*50)

print("\n3. Visual Example of Cursor Movement")
print("-" * 30)

text_buffer = io.StringIO()
content = "ABCDEFGHIJ"
text_buffer.write(content)

positions = [1, 3, 7, 9]

for pos in positions:
    text_buffer.seek(pos)
    remaining = text_buffer.read()
    
    # Visual representation
    visual = content[:pos] + "|" + content[pos:]
    print(f"seek({pos}): {visual} -→ reads: '{remaining}'")
text_buffer.close()
print("\n text_buffer closed")
try:
    text_buffer.seek(0)
    data = text_buffer.read()
    print(f"After close(): {data}")
except ValueError as e:
    print(f"❌ Error after close(): {e}")

print("\n" + "="*50)

with io.StringIO() as auto_buffer:
    auto_buffer.write("Hello Auto Close!")
    auto_buffer.seek(0)
    
    data = auto_buffer.read()
    print(f"Inside 'with': {data}")
try:
    auto_buffer.read()
except ValueError as e:
    print(f"❌ Buffer is closed after 'with' block: {e}")

    # No need to call close() - it's automatic!

print("✓ Buffer automatically closed when 'with' block ends")
# # 2. BYTES IO - Working with binary data
# print("\n\n2. BytesIO - Working with binary data")
# print("-" * 40)

# # Create a bytes buffer
# bytes_buffer = io.BytesIO()

# # Write binary data
# bytes_buffer.write(b"Hello ")
# bytes_buffer.write(b"Binary ")
# bytes_buffer.write(b"World!")

# # Get the binary content
# binary_content = bytes_buffer.getvalue()
# print(f"Binary content: {binary_content}")
# print(f"Decoded: {binary_content.decode('utf-8')}")

# # Reset and read
# # bytes_buffer.seek(0)
# data = bytes_buffer.read()
# print(f"Read data: {data.decode('utf-8')}")

# bytes_buffer.close()
report = io.StringIO()

# Write different sections
report.write("\nDAILY REPORT\n")
report.write("============\n")
report.write("Sales: $1000\n")
report.write("Costs: $300\n")
report.write("Profit: $700\n")

print("✓ Report written to buffer")

# Read the whole report
report.seek(0)  # Go to beginning
full_report = report.read()
print("Full report:"+full_report)

# Read just the first line
report.seek(0)  # Go to beginning again
first_line = report.readline()
print(f"First line only: '{first_line.strip()}'")

# Clean up
report.close()
print("✓ Report buffer closed")
# 3. PRACTICAL EXAMPLE - Processing CSV-like data
print("\n\n3. Practical Example - Processing data")
print("-" * 40)

# Simulate CSV data as a string
csv_data = """name,age,city
John,25,New York
Jane,30,London
Bob,35,Paris"""

# Use StringIO to process it like a file
csv_buffer = io.StringIO(csv_data)

print("Processing CSV-like data:")
header = csv_buffer.readline().strip().split(',')
print(f"Headers: {header}")

print("Data rows:")
for line in csv_buffer:
    row = line.strip().split(',')
    print(f"  {row}")

csv_buffer.close()

# # 4. BUILDING CONTENT DYNAMICALLY
print("\n\n4. Building content dynamically")

# Create a report dynamically
report = io.StringIO()

report.write("DAILY REPORT\n")
report.write("=" * 20 + "\n")

# Add some data
data = [("Sales", 1000), ("Expenses", 300), ("Profit", 700)]

for item, value in data:
    # print(f"{item}: ${value}")
    report.write(f"{item}: ${value}\n")

report.write("-" * 20 + "\n")
report.write("Report generated successfully!")

# Get the final report
final_report = report.getvalue()
print(final_report)

report.close()

# # 5. CONTEXT MANAGER (with statement)
print("\n\n5. Using with statement (recommended)")
print("-" * 40)

# Better way - using context manager
with io.StringIO() as buffer:
    buffer.write("Line 1\n")
    buffer.write("Line 2\n")
    buffer.write("Line 3\n")
    
    # Get content
    content = buffer.getvalue()
    print("Content:")
    print(content)
    
    # Buffer automatically closes when leaving the 'with' block

print("✓ Buffer automatically closed")

# # 6. CONVERTING BETWEEN STRING AND BYTES
print("\n\n6. Converting between string and bytes")
print("-" * 40)

text = "Hello, مرحبا 🌍"

# String to bytes
with io.BytesIO() as bytes_buf:
    bytes_buf.write(text.encode('utf-8'))
    binary_data = bytes_buf.getvalue()
    print(f"Text as bytes: {binary_data}")
print(binary_data)
# Bytes back to string
with io.StringIO() as string_buf:
    string_buf.write(binary_data.decode('utf-8'))
    decoded_text = string_buf.getvalue()

print(f"Bytes as text: {decoded_text}")

# print("\n=== Summary ===")
# print("• StringIO: For text data in memory")
# print("• BytesIO: For binary data in memory") 
# print("• Useful for testing, data processing, and building content")
# print("• Always use 'with' statement or call .close()")

 