# Data Entry Cleaning Tool
# Made by Aadarsh Sharma

import csv

print("=== Data Entry Cleaning Tool ===")
print("1. Duplicate data hatayega")
print("2. Khali row hatayega")

# Sample Data - Jaise Data Entry me milta hai
data = [
    ["Name", "City", "Phone"],
    ["Aadarsh", "Indore", "9876543210"],
    ["Rahul", "Bhopal", "9123456789"],
    ["Aadarsh", "Indore", "9876543210"],  # Duplicate
    ["Priya", "Delhi", "9988776655"],
    ["", "", ""],  # Khali row
    ["Amit", "Ujjain", "9123456780"],
]

# Cleaning
clean_data = []
seen = set()

for row in data:
    # Khali row skip karo
    if row == ["", "", ""]:
        continue
    # Duplicate skip karo
    row_tuple = tuple(row)
    if row_tuple not in seen:
        seen.add(row_tuple)
        clean_data.append(row)

print(f"\nPehle total rows: {len(data)-1}")
print(f"Saaf karne ke baad: {len(clean_data)-1}")
print("\nClean Data:")

for row in clean_data:
    print(row)

# Clean file save karo
with open("clean_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(clean_data)

print("\nHo gaya! clean_data.csv ban gayi.")
