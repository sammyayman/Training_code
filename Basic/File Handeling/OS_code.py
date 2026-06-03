import os
os.system("cls")

def explore_directory():
    """Simple directory explorer"""
    current = os.getcwd()
    print(f"Currently in: {current}\n")
    
    
    items = os.listdir(current)
    print(items, "\n")
    print(os.path)
    print(os.path.basename(current), os.path.dirname(current))
    print(os.path.split(current))
    print(os.path.splitext("example.txt"))
    print(os.path.exists("OS_code.py"))
    
    for item in items:
        path = os.path.join(current, item)
        if os.path.isdir(path):
            print(f"📁 {item}/")
        else:
            print(f"📄 {item}")

# explore_directory()

original_dir = os.getcwd()

# Change to parent directory
os.chdir('OS_TEST')
print("Moved to:",os.getcwd())
# Go back to original
os.chdir(original_dir)
print("Back to:", original_dir)