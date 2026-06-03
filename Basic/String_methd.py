
# %%
# print("All method of Function in string (str) :")
data = [m for m in dir(str) if not m.startswith("_")]
for i in range(0, len(data), 7): print(data[i:i+7])

print("\n the Object of __obj__ : ")
data_obj = [m for m in dir(str) if  m.startswith("_")]
for i in range(0, len(data_obj), 7):print(data_obj[i:i+7])
print()

#%%
s = "  Ayman2030@gmail.com  "
clean = s.strip()
methods_no_args = [
    "isalpha",
    "isdigit",
    "isnumeric",
    "isdecimal",
    "isalnum",
    "islower",
    "isupper",
    "istitle",
    "isspace",
    "isidentifier",
    "isascii",
    "isprintable",
    "istitle"
]

methods_with_args = {
    "startswith": "sami",
    "endswith": ".com",
}

for method in methods_no_args:
    result = getattr(clean, method)()
    print(f"{method} : {result}",end = '\t\t')
print('\n'*2)

for method, value in methods_with_args.items():
    result = getattr(clean, method)(value)
    print(f"{method}('{value}') -> {result}")
    
    
    
    

        
#%%        
# Original email string
email = "            Ayman2030@gmail.com              "
print("=== Methods without arguments ===")
for method in methods_no_args:
    try:
        result = getattr(email, method)()
        print(f"{method:<12} -> {result}")
    except Exception as e:
        print(f"{method:<12} -> Error: {e}")
        
clean = email.strip()  # remove leading/trailing spaces

# Split email into username and domain for meaningful formatting
parts = clean.split("@")            # ['samiayman2030', 'gmail.com']
mapping = {'user': parts[0], 'domain': parts[1]}

# Template strings for format methods
template_format = "User: {}, Domain: {}"
template_map = "Username: {user}, Domain: {domain}"

# Methods without arguments
methods_no_args = ['lower','capitalize', 'casefold', 'swapcase', 'title', 'upper']

# Methods with arguments and safe defaults
methods_with_args = {
    'count': 'a','encode': 'utf-8','expandtabs': 4,
    
    'find': '@','rfind': '@','rindex': '@', 'index': '@',
    
    'format': template_format,'format_map': template_map
    
}


        
print("=== Methods with arguments ===")
        
for method, arg in methods_with_args.items():
    try:
        if method == 'format':
            result = getattr(arg, method)(*parts)
        elif method == 'format_map':
            result = getattr(arg, method)(mapping)
        elif method == 'center':
            width, fillchar = arg
            result = getattr(clean, method)(width, fillchar)
        else:
            result = getattr(clean, method)(arg)
        print(f"{method:<12}({arg}) -> {result}")
    except Exception as e:
        print(f"{method:<12}({arg}) -> Error: {e}")


#%%
methods_no_args = [ 'lstrip', 'rstrip', 'strip']


print("=== Methods without arguments ===")
for method in methods_no_args:
    try:
        result = getattr(email, method)()
        print(f"string.{method}() -> {result}")
    except Exception as e:
        print(f"{method:<12} -> Error: {e}")
        
        
        
        
methods_with_args = {
    'join': '-','center': (50, '-'), 'rjust': (50, '-'),'ljust': (50, '-'), 
    
    'maketrans': ('a', 'A'),'removeprefix': 'sami','removesuffix': '.com',    
            
    'replace': ('a', 'A'), 'translate': ('a', 'A'),          
               
    'partition': '@','rpartition': '@', 'split': ('@', 1),'rsplit': ('@', 1),   
                
    'splitlines': False,  'zfill': (25)                      
}

print("\n=== Methods with arguments ===")
for method, arg in methods_with_args.items():
    try:
        if method in ['ljust', 'rjust', 'center']:
            
            width, fillchar = arg
            result = getattr(clean, method)(width, fillchar)
            
        elif method == 'join':
            result = getattr(arg, method)(clean)  # '-'.join(clean)
            
        elif method == 'maketrans':
            result = str.maketrans(*arg)
            
        elif method == 'translate':
            table = str.maketrans(*arg)
            result = getattr(clean, method)(table)
            
        elif method in ['replace', 'rsplit', 'split']:
            result = getattr(clean, method)(*arg)
            
        else:
            result = getattr(clean, method)(arg)
        print(f"sting.{method:<12}({arg}) -> {result}")
        
    except Exception as e:
        print(f"{method:<12}({arg}) -> Error: {e}")

# %%


text = "   Hello,   World!   "

# strip() example
print(text.strip(" "))  # "Hello, World!"

# rstrip() example
print(text.rstrip())  # "   Hello, World!"

# split() example
print(text.split())  # ["Hello,", "World!"]
print(text.split(','))  # ["Hello,", "World!"]
print("one,two,three".split(','))  # ["one", "two", "three"]




#%%
# The original string has spaces at the start and spaces + newline at the end
log_entry = "   INFO,2023-10-27     ,Login Success       \n"

# Use strip() to remove all leading/trailing whitespace
cleaned_entry = log_entry.strip()

print(f"Original: '{log_entry}'")
print(f"After strip(): '{cleaned_entry}'")
print(f"After rstrip(): '{cleaned_entry.rstrip()}'")
# Output: After strip(): 'INFO,2023-10-27,Login Success'
# We use the cleaned string from the previous step

# Split the string by the comma delimiter
parts = cleaned_entry.split(',')

print(f"After split(','): {parts}")
# Output: After split(','): ['INFO', '2023-10-27', 'Login Success']

messy_entry = "   WARNING,2023-10-28,Disk Full;"

# rstrip(';') will remove semicolons ONLY from the right side
clean_end = messy_entry.rstrip(';')

print(f"Original: '{messy_entry}'")
print(f"After rstrip(''): '{clean_end}'")
# Output: After rstrip(';'): '   WARNING,2023-10-28,Disk Full'

#%%
username = "   Ayman   "
right = username.rstrip()
print(right)
left = username.lstrip()
clean_username = username.strip()

print(f"Original: '{username}'")
print(f"Right: '{right}'")
print(f"Left: '{left}'")
print(f"Cleaned: '{clean_username}'")

print("\n" + "="*50,"\n")

filename = "___-==report.txt==-___"
print(f"Original: '{filename}'")

print("left strip:",filename.lstrip("_-="))
print("right strip:",filename.rstrip("_-="))
clean_filename = filename.strip("_-=")

print(f"left: '{filename.lstrip("_-=")}'")
print(f"right: '{filename.rstrip("_-=")}'")
print(f"Cleaned: '{clean_filename}'")

# Output:
# Original: '___-==report.txt==-___'
# Cleaned: 'report.txt'00-