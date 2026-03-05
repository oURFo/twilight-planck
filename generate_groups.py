import csv

source_data = [
    ["ID", "Prop A", "Prop B", "Note"],
    ["1", "Group 1", "Header", "Has children"],
    ["...", "Child 1.1", "Data", "Keep this"],
    ["...", "Child 1.2", "Data", "Source modified diff"],
    ["2", "Group 2", "Header", "Has 1 child"],
    ["...", "Child 2.1", "Data", "Also keep"],
    ["3", "Group 3", "Header", "New Group entirely"],
    ["...", "Child 3.1", "Data", "New child"],
]

target_data = [
    ["ID", "Prop A", "Prop B", "Note"],
    ["1", "Group 1", "Header", "Has children"],
    ["...", "Child 1.1", "Data", "Keep this"],
    ["...", "Child 1.2", "Data", "Target OLD data"],
    ["2", "Group 2", "Header", "Has 1 child"],
    ["...", "Child 2.1", "Data", "Also keep"],
    ["4", "Group 4", "Header", "Old Group"],
]

with open('test_groups_source.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(source_data)

with open('test_groups_target.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(target_data)

print("Created test files")
