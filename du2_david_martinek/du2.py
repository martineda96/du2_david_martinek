import csv

with open("D:\\Python\Data\\test.csv", encoding="utf-8") as csvinfile:
    reader = csv.reader(csvinfile, delimiter =";")
    for row in reader:
        print(row[0])