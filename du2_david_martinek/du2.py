import csv

with open("test.csv", encoding="utf-8") as csvinfile,\
     open("test_out7.csv", "w", encoding="utf-8") as csvoutfile7,\
     open("test_out365.csv", "w", encoding="utf-8") as csvoutfile365:
    reader = csv.reader(csvinfile, delimiter =",")
    writer7 = csv.writer(csvoutfile7)
    for row in reader:
        print(row[5])
        