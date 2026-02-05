import csv

# Source Data (Left)
source_data = [
    ["ID", "Name", "Role", "Status"],
    ["101", "Alice", "Engineer", "Active"],
    ["102", "Bob", "Designer", "Active"],
    ["103", "Charlie", "Manager", "Leaver"], # Modified in Target?
    ["104", "David", "Engineer", "Active"], # Only in Source (New)
]

# Target Data (Right)
target_data = [
    ["ID", "Name", "Role", "Status"],
    ["101", "Alice", "Engineer", "Active"],
    ["102", "Bob", "Senior Designer", "Active"], # Modified
    ["103", "Charlie", "Manager", "Leaver"],
    ["105", "Eve", "HR", "Active"], # Only in Target
]

with open('source.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(source_data)

with open('target.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(target_data)

print("Created source.csv and target.csv")
