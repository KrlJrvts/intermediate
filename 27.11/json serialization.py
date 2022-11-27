import csv

doc = "data.csv"

data = [
    ["cat", "dog", "rat"],
    ["audi", "BMW", "lada"],
    ["13", "18", "48"]
]

with open(doc, "a", newline="") as f:
    writer = csv.writer(f)
    for line in data:
        writer.writerow(line)

with open(doc, "r") as f:
    for line in csv.reader(f):
        print(line)
