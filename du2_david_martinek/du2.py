import csv

with open("test.csv", encoding="utf-8") as csvinfile,\
     open("test_out7.csv", "w", encoding="utf-8") as csvoutfile7,\
     open("test_out365.csv", "w", encoding="utf-8") as csvoutfile365:
    reader = csv.reader(csvinfile, delimiter =",")
    writer7 = csv.writer(csvoutfile7)
    writer365 = csv.writer(csvoutfile365)

    den_7 = 0
    prumer_7 = 0
    den_rok = 0
    prumer_rok = 0

    for row in reader:
        if den_7 == 0:
            radek_7 = row
        den_7 += 1
        prumer_7 += float(row[5])
        if den_7 == 6:
            prumer_7 /= (den_7+1)
            radek_7[5] = prumer_7
            writer7.writerow(radek_7)
            den_7 = 0
            prumer_7 = 0
    
    if prumer_7 != 0:
        prumer_7 /= (den_7+1)
        radek_7[5] = prumer_7
        writer7.writerow(radek_7)


        '''if aktualni_rok != row[2]:
            aktualni_rok = row[2]
            radek_rok[5] = prumer_rok/
            writer365.writerow(radek_rok)
            radek_rok = row
            #a něco se stane'''