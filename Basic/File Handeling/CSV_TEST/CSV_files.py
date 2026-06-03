 
print("\033c")
import csv
print("***"*10,"Example_1","***"*10)
# Create a sample CSV file first
sample_data = """Name,Age,City
John,25,New York
Sarah,30,London
Mike,22,Paris"""


with open("Example_1 people.csv", "w" , encoding="utf-8") as file:
    file.write(sample_data)


# Now read the CSV file
with open("Example_1 people.csv", "r") as file:
    csv_reader = csv.reader(file)
    # print(csv_reader.__next__())
    for row in csv_reader:print(row)  # Each row is a list



print("\n"+"="*60+"\n"+"="*60+"\n")




with open("Example_1 people.csv", "r") as file:
    csv_reader = csv.reader(file)
    
    # Skip the header
    next(csv_reader)
    for row in csv_reader:
        name, age, city = row
        print(f"{name} is {age} years old and lives in {city}")


print("\n"+"="*60+"\n"+"="*60+"\n")



with open("Example_1 people.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        name, age, city = row["Name"], row["Age"], row["City"]
        print("-" * 20)
        
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"City: {city}")


print("\n"+"="*80+"\n"+"="*20,"\t\t  Example_2  \t\t"+"="*20+"\n")        



print()
people = [
    ["Name", "Age", "City"],
    ["Alice", 28, "Boston"],
    ["Bob", 35, "Chicago"],
    ["Carol", 31, "Miami"]
]

# Write to CSV
with open("Example_2 new_people.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    
    for row in people:
        csv_writer.writerow(row)

print("CSV file created!")
with open("Example_2 new_people.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:print(row)


print("\n"+"="*80+"\n"+"="*20,"\t\t  Example_3  \t\t"+"="*20+"\n")        



# Create a CSV file
with open("Example_3 students.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    
    # Write header
    csv_writer.writerow(["Student", "Grade", "Subject"])
    
    # Write data rows
    csv_writer.writerow(["Emma", "A", "Math"])
    csv_writer.writerow(["Liam", "B+", "Science"])
    csv_writer.writerow(["Olivia", "A-", "English"])

print("Students CSV created!")
with open("Example_3 students.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:print(row)
    
    
    
    
print("\n"+"="*80+"\n"+"="*20,"\t\t  Example_4  \t\t"+"="*20+"\n")







students = [
    {"Student": "Emma", "Grade": "A", "Subject": "Math"},
    {"Student": "Liam", "Grade": "B+", "Subject": "Science"},
    {"Student": "Olivia", "Grade": "A-", "Subject": "English"}
]

with open("Example_4 students_dict.csv", "w", newline="") as file:
    fieldnames = ["Student", "Grade", "Subject"]
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Write header
    csv_writer.writeheader()
    
    # Write data
    for student in students:
        csv_writer.writerow(student)

print("Dictionary CSV created!")

print("\n"+"="*80+"\n"+"="*20+"\t\t  Example_5  \t\t"+"="*20+"\n")



print("\n"+"Gradebook Example:\n"+"-"*40)



def create_gradebook():
    """Create a sample gradebook CSV"""
    grades = [
        ["Student", "Math", "Science", "English"],
        ["Alice", 95, 88, 92],
        ["Bob", 87, 91, 85],
        ["Carol", 92, 95, 89],
        ["David", 78, 82, 88]
    ]
    
    with open("Example_5 gradebook.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(grades)
    with open("Example_5 gradebook.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:print(row)

def calculate_averages():
    """Read grades and calculate averages"""
    with open("Example_5 gradebook.csv", "r") as file:
        reader = csv.DictReader(file)
        
        print("Student Averages:")
        print("-" * 30)
        
        for row in reader:
            student = row["Student"]
            math_grade = int(row["Math"])
            science_grade = int(row["Science"])
            english_grade = int(row["English"])
            
            average = (math_grade + science_grade + english_grade) / 3
            print(f"{student}: {average:.1f}")

# Run the example
create_gradebook()
calculate_averages()





print("\n"+"="*80+"\n"+"="*20+"\t\t  Example_6  \t\t"+"="*20+"\n")

print("\nShopping List Example:\n"+"-"*40)

def add_item_to_list(item, quantity, price):
    """Add item to shopping list CSV"""
    with open("Example_6 shopping_list.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([item, quantity, price])

def create_shopping_list():
    """Create shopping list with headers"""
    with open("Example_6 shopping_list.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Item", "Quantity", "Price"])

def show_shopping_list():
    """Display the shopping list"""
    try:
        with open("Example_6 shopping_list.csv", "r") as file:
            reader = csv.DictReader(file)
            
            print("\nShopping List:")
            print("-" * 40)
            total = 0
            
            for row in reader:
                item = row["Item"]
                quantity = int(row["Quantity"])
                price = float(row["Price"])
                subtotal = quantity * price
                total += subtotal
                
                print(f"{item}: {quantity} x ${price:.2f} = ${subtotal:.2f}")
            
            print("-" * 40)
            print(f"Total: ${total:.2f}")
    
    except FileNotFoundError:
        print("No shopping list found. Create one first!")

# Use the shopping list
create_shopping_list()
add_item_to_list("Apples", 5, 0.50)
add_item_to_list("Bread", 2, 2.99)
add_item_to_list("Milk", 1, 3.49)
show_shopping_list()





print("\n"+"="*80+"\n"+"="*20+"\t\t  Example_7  \t\t"+"="*20+"\n")





def create_contact_book():
    """Initialize contact book CSV"""
    with open("Example_7 contacts.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact(name, phone, email):
    """Add a new contact"""
    with open("Example_7 contacts.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
    print(f"Added {name} to contacts!")

def find_contact(search_name):
    """Find a contact by name"""
    try:
        with open("Example_7 contacts.csv", "r") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                if search_name.lower() in row["Name"].lower():
                    print(f"Found: {row['Name']}")
                    print(f"Phone: {row['Phone']}")
                    print(f"Email: {row['Email']}")
                    return
            
            print(f"Contact '{search_name}' not found.")
    
    except FileNotFoundError:
        print("Contact book not found!")

def list_all_contacts():
    """Show all contacts"""
    try:
        with open("Example_7 contacts.csv", "r") as file:
            reader = csv.DictReader(file)
            
            print("\nAll Contacts:")
            print("-" * 50)
            
            for row in reader:
                print(f"{row['Name']} | {row['Phone']} | {row['Email']}")
    
    except FileNotFoundError:
        print("Contact book not found!")

# Use the contact book
create_contact_book()
add_contact("John Doe", "555-1234", "john@email.com")
add_contact("Jane Smith", "555-5678", "jane@email.com")
list_all_contacts()
find_contact("John")


print("\n"+"="*80+"\n"+"="*20+"\t\t  Example_8  \t\t"+"="*20+"\n")



data_semicolon = "Name;Age;City\nJohn;25;New York\nSarah;30;London"

with open("Example_8 semicolon.csv", "w") as file:
    file.write(data_semicolon)

# Read CSV with different delimiter
with open("Example_8 semicolon.csv", "r") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        print(row)

print("\n"+"="*80+"\n"+"="*20+"\t\t  Example_9  \t\t"+"="*20+"\n")

data_with_quotes = '''Name,Description,Price
"Super Widget","A great widget, very useful",19.99
"Mega Tool","The best tool, made in USA",29.99'''

with open("Example_9 products.csv", "w") as file:
    file.write(data_with_quotes)

# Reading works normally - CSV handles quotes automatically
with open("Example_9 products.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Product: {row['Name']}")
        print(f"Description: {row['Description']}")
        print(f"Price: ${row['Price']}")
        print("-" * 30)
   
   
   
        
print("\n"+"="*80+"\n"+"="*20+"\t\t  Example_10  \t\t"+"="*20+"\n")


def safe_read_csv(filename):
    """Safely read a CSV file with error handling"""
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            
            data = []
            for row in reader:
                data.append(row)
            
            return data
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return []
    
    except csv.Error as e:
        print(f"Error reading CSV: {e}")
        return []
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

def safe_write_csv(filename, data, headers):
    """Safely write data to CSV"""
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"Successfully wrote {len(data)} rows to {filename}")
        return True
    
    except Exception as e:
        print(f"Error writing CSV: {e}")
        return False

# Example usage
data = [
    {"Name": "Alice", "Age": 25},
    {"Name": "Bob", "Age": 30}
]

safe_write_csv("Example_10 safe_test.csv", data, ["Name", "Age"])
result = safe_read_csv("Example_10 safe_test.csv")
print("Data read:", result)


print("\n"+"="*80+"\n"+"="*20+"\t\t  Example_11  \t\t"+"="*20+"\n")



# Basic reading
with open("Example_11 file.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # row is a list

# Reading as dictionary
with open("Example_11 file.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"])  # row is a dictionary


with open("Example_11 file.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Header1", "Header2"])
    writer.writerow(["Value1", "Value2"])

# Writing with dictionaries
with open("Example_11 file.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Age"])
    writer.writeheader()
    writer.writerow({"Name": "John", "Age": 25})