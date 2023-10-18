import csv

#sort the data in 'CompanyName' column
with open('companies_names.csv', 'r') as f:
    reader = csv.DictReader(f)
    sorted_rows = sorted(reader, key=lambda row: row['CompanyName'])

with open('companies_names.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(sorted_rows)