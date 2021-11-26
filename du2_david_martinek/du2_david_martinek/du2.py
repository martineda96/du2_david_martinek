import csv

with open("test.csv", encoding="utf-8") as csvinfile,\
     open("test_out.csv", "w", encoding="utf-8") as csvoutfile:
    reader = csv.reader(csvinfile, delimiter =";")
    for row in reader:
        print(row[0])
        