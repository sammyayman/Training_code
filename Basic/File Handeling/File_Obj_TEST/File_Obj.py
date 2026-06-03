print("\033c")
file = open("Example_1 people.csv", "r+", encoding="utf-8")
print(file.read())
file.close()
print("Is file closed?", file.closed)
print("File name:", file.name)
print("Mode:", file.mode)
print("Encoding:", file.encoding,"\n")



print("\n"+"="*80+"\n"+"="*20+"\t\t  Example_1  \t\t"+"="*20+"\n")

# This automatically closes the file for you!
try:
    with open("1-my_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")

with open("1-my_file.txt", "w") as file:
    file.write("First line\nSecond line\n")
    file.write("Third line\n")
    file.write("Fourth line")
    print("File written successfully!"+ f"({file.name})")
    
# File is automatically closed here
print("Is file closed?", file.closed)

# First, create a file
with open("2-diary.txt", "w") as file:
    file.write("Day 1: Started learning Python\n")

# Now add more content without erasing
with open("2-diary.txt", "a+") as file:
    file.write("Day 2: Learning file operations\n")
    file.write("Day 3: This is getting fun!\n")
    file.seek(0)
    content = file.read()
    print(content)

print("Diary updated!\n")

# Write a list of lines
lines = [
    "Welcome to my file\n",
    "This is the second line\n", 
    "And this is the third line\n"
]

with open("3-multiple_lines.txt", "w+") as file:
    file.writelines(lines)
    file.seek(0)
    print(file.read())

print("Multiple lines written!")

print("\n"+"="*80+"\n"+"="*20+"\t\t  Example_2  \t\t"+"="*20+"\n")



# Create a sample file first
with open("4-story.txt", "w") as file:
    file.write("Once upon a time\n")
    file.write("There was a Python programmer\n")
    file.write("Who loved to code\n")

# Read the entire file
with open("4-story.txt", "r") as file:
    content = file.read()
    print("Full content:")
    print(content)



# Read one line at a time
with open("4-story.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    
    print("Line 1:", line1.strip())  # strip() removes \n
    print("Line 2:", line2.strip())
    print("Line 3:", line3)
    
    
# Read all lines as a list
with open("4-story.txt", "r") as file:
    lines = file.readlines()  # Read all lines into a list
    
    for i, line in enumerate(lines, 1):
        if i in [1, 2]:  # For lines 1 and 2
            print(f"Line {i}:", line.strip())
        else:  # For all other lines (including line 3)
            print(f"Line {i}:", line)  # end='' to avoid double newlines
            
            
            
with open("4-story.txt", "r") as file:
    lines = file.readlines()  # Read all lines into a list
    
    for i, line in enumerate(lines, 1):
        if i == 2:  # Skip line 2
            continue
        print(f"Line {i}:", line.strip() if i != 3 else line)
        
print("\n"+"="*80+"\n"+"="*20+"\t\t  Example_3  \t\t"+"="*20+"\n")


def write_note():
    """Let user write a note"""
    note = input("Enter your note: ")
    
    with open("5-notes.txt", "a") as file:
        file.write(f"{note}\n")
    
    print("Note saved!")

def read_notes():
    """Read and display all notes"""
    try:
        with open("5-notes.txt", "r") as file:
            print("\n--- Your Notes ---")
            for line_num, note in enumerate(file, 1):
                print(f"{line_num}. {note.strip()}")
    except FileNotFoundError:
        print("No notes found. Write some first!")

# Use the note app
# write_note()
# write_note()
# read_notes()

print("\n"+"="*80+"\n"+"="*20+"\t\t  Example_4  \t\t"+"="*20+"\n")
def count_words_in_file(filename):
    """Count words in a text file"""
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            
            print(f"File: {filename}")
            print(f"Characters: {len(content)}:\n{content}")
            print(f"Words: {len(words)}:\n{words}")
            print(f"Lines: {content.count('\n')  }")
    
    except FileNotFoundError:
        print(f"File {filename} not found!")

# Create a test file
with open("6- test_document.txt", "w") as file:
    file.write("This is a test document.\n")
    file.write("It has multiple lines.\n")
    file.write("We will count the words in it.")

# Count words
count_words_in_file("6- test_document.txt")

print("\n"+"="*80+"\n"+"="*20+"\t\t  Example_5  \t\t"+"="*20+"\n")

def add_task():
    """Add a task to the to-do list"""
    task = input("Enter new task: ")
    
    with open("todo.txt", "a") as file:
        file.write(f"[ ] {task}\n")
    
    print("Task added!")

def show_tasks():
    """Show all tasks"""
    try:
        with open("todo.txt", "r") as file:
            print("\n--- To-Do List ---")
            tasks = file.readlines()
            
            if not tasks:
                print("No tasks found!")
                return
            
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
    
    except FileNotFoundError:
        print("No to-do list found!")

def clear_tasks():
    """Clear all tasks"""
    with open("todo.txt", "w") as file:
        file.write("")  # Write empty string to clear file
    print("All tasks cleared!")

# Use the to-do list
add_task()
add_task()
show_tasks()
x = input("Press Enter to clear tasks...")  
clear_tasks()
show_tasks()



print("\n"+"="*80+"\n"+"="*20+"\t\t  Example_6  \t\t"+"="*20+"\n")



from datetime import datetime

def log_message(message):
    """Add timestamped message to log file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("7-app.log", "a") as file:
        file.write(f"[{timestamp}] {message}\n")

def read_log():
    """Read and display log file"""
    try:
        with open("7-app.log", "r") as file:
            print("\n--- Log File ---")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No log file found!")

# Use the logger
log_message("Application started")
log_message("User logged in")
log_message("File saved successfully")
read_log()

print("\n"+"="*80+"\n"+"="*20+"\t\t  Example_7  \t\t"+"="*20+"\n")




def safe_read_file(filename):
    """Safely read a file with error handling"""
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None
    
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'!")
        return None
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def safe_write_file(filename, content):
    """Safely write to a file"""
    try:
        with open(filename, "w") as file:
            file.write(content)
        print(f"Successfully wrote to {filename}")
        return True
    
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'!")
        return False
    
    except Exception as e:
        print(f"Error writing file: {e}")
        return False

# Test error handling
content = safe_read_file("8-nonexistent.txt")
if content:
    print("File content:", content)

safe_write_file("8-test_safe.txt", "This is a test!")
print("File written successfully!")



def file_exists(filename):
    """Check if a file exists without using os module"""
    try:
        with open(filename, "r") as file:
            pass  # Just try to open, don't read
        return True
    except FileNotFoundError:
        return False

# Use it
if file_exists("important.txt"):
    print("File exists!")
else:
    print("File doesn't exist, creating it...")
    with open("9- important.txt", "w") as file:
        file.write("This is important data!")
        
        
print("\n"+"="*80+"\n"+"="*20,"\t\t  Example_8  \t\t"+"="*20+"\n")



def copy_binary_file(source, destination):
    """Copy a binary file (like an image)"""
    try:
        # Read binary file
        with open(source, "rb") as src_file:
            data = src_file.read()
        
        # Write binary file
        with open(destination, "wb") as dst_file:
            dst_file.write(data)
        
        print(f"Copied {source} to {destination}")
        return True
    
    except FileNotFoundError:
        print(f"Source file {source} not found!")
        return False
    
    except Exception as e:
        print(f"Error copying file: {e}")
        return False

# Example: Create a simple binary file
binary_data = bytes([72, 101, 108, 108, 111])  # "Hello" in ASCII
with open("10- binary_test.bin", "wb") as file:
    file.write(binary_data)

# Read it back
with open("10- binary_test.bin", "rb") as file:
    data = file.read()
    print("Binary data:", data)
    print("As text:", data.decode("ascii"))