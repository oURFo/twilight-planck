import csv

# Source Data (Left) - With Empty Column "Notes"
source_data = [
    ["ID", "Name", "Role", "Notes", "Status"],
    ["101", "Alice", "Engineer", "", "Active"],
    ["102", "Bob", "Designer", "Urgent", "Active"],
    ["103", "Charlie", "Manager", "", "Leaver"], 
    ["104", "David", "Engineer", "", "Active"], 
]

# Target Data (Right)
target_data = [
    ["ID", "Name", "Role", "Notes", "Status"],
    ["101", "Alice", "Engineer", "", "Active"],
    ["102", "Bob", "Senior Designer", "", "Active"], # Diff: Role, Notes (Empty vs Urgent)
    ["103", "Charlie", "Manager", "", "Leaver"],
    ["106", "Frank", "Director", "", "Active"], # ID 106
]

with open('source_v2.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(source_data)

with open('target_v2.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(target_data)

print("Created V2 test files")
