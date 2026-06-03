"""
Pathlib Tutorial - A Comprehensive Guide
"""
from pathlib import Path

# 1. Basic Path Creation
print("1. Basic Path Creation:")
current_file = Path(__file__).resolve()  # Get absolute path of current file
current_dir = Path.cwd()  # Get current working directory
home_dir = Path.home()  # Get user's home directory

print(f"Current file: {current_file}")
print(f"Current directory: {current_dir}")
print(f"Home directory: {home_dir}")

# 2. Joining Paths
print("\n2. Joining Paths:")
new_path = current_dir / "NEW_FOLDER" / "my_file.txt"
print(f"New path: {new_path}")
new_path.parent.mkdir(exist_ok=True)
new_path.write_text("Hello, pathlib!")

# 3. Path Components
print("\n3. Path Components:")
print(f"Parent: {current_file.parent}")
print(f"Name: {current_file.name}")
print(f"Stem: {current_file.stem}")
print(f"Suffix: {current_file.suffix}")

# 4. Directory Listing
print("\n4. Directory Listing:")
print("\nFiles in current directory:")
for item in Path().iterdir():
    if item.is_file():
        print(f"File: {item.name} (Size: {item.stat().st_size} bytes)")
    elif item.is_dir():
        print(f"Directory: {item.name}")

# 5. File Operations
print("\n5. File Operations:")
# Create a test file
test_file = Path("test_file.txt")
# Write to file
test_file.write_text("Welcome to pathlib!")
print(f"Created and wrote to {test_file}")

# Read from file
content = test_file.read_text()
print(f"File content: {content}")

# Get file info
print(f"File exists: {test_file.exists()}")
print(f"File size: {test_file.stat().st_size} bytes")

# Rename file
new_name = Path("renamed_file.txt")
test_file.rename(new_name)
print(f"Renamed to {new_name}")

# Clean up
new_name.unlink()
print(f"Deleted {new_name}")
     

# 6. Directory Operations
print("\n6. Directory Operations:")
test_dir = Path("test_directory")
try:
    # Create directory
    test_dir.mkdir(exist_ok=True)
    print(f"Created directory: {test_dir}")
    
    # Create files in directory
    (test_dir / "file1.txt").touch()
    (test_dir / "file2.txt").touch()
    print("Created test files")
    
    # List directory contents
    print("\nDirectory contents:")
    for item in test_dir.iterdir():
        print(f"  - {item.name}")
    
    # Remove directory and contents
    for item in test_dir.iterdir():
        item.unlink()
    test_dir.rmdir()
    print("\nCleaned up test directory")
    
except Exception as e:
    print(f"An error occurred: {e}")

# 7. Path Matching
print("\n7. Path Matching:")
print("\nPython files in current directory:")
for py_file in Path().glob("*.py"):
    print(f"  - {py_file}")

print("\nAll text files (recursive):")
for txt_file in Path().rglob("*.txt"):
    print(f"  - {txt_file}")

print("\nPathlib tutorial completed!")