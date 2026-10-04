import json

# Step 1: Read data from the JSON file
with open("employee.json", "r") as file:
    employees = json.load(file)

# Step 2: Filter employees earning more than 50,000
high_earners = []

for employee in employees:
    if employee["salary"] > 50000:
        high_earners.append(employee)

# Step 3: Calculate average salary
total_salary = 0

for employee in employees:
    total_salary += employee["salary"]

average_salary = total_salary / len(employees)

# Step 4: Create the output dictionary
result = {
    "total_employees": len(employees),
    "average_salary": average_salary,
    "high_earners": high_earners
}

# Step 5: Write processed data to a new JSON file
with open("output.json", "w") as file:
    json.dump(result, file, indent=4)

print("Data processing completed successfully!")
print(f"Total employees: {len(employees)}")
print(f"Average salary: {average_salary}")
print(f"High earners: {len(high_earners)}")


# import json - Imports Python's built-in JSON module
# open() - Opens a file
# "r" - Opens a file in read mode
# "w" - Opens a file in write mode
# json.load() - Converts JSON file data into Python objects
# json.dump() - Converts Python objects into JSON and writes them to a file
# indent=4 - Formats the output for readability
# append() - Adds an item to a list
# json.load() reads JSON directly from a file.
# json.loads() reads JSON from a string.
# json.dump() writes JSON to a file.
# json.dumps() converts Python data into a JSON string.