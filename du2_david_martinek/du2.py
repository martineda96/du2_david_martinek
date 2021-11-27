import csv

def zapis(prumer,den,radek, writer):
    prumer /= den
    prumer = float("{0:.4f}".format(prumer))
    radek[5] = prumer
    writer.writerow(radek)

with open("Data_Libechovka.csv", encoding="utf-8") as csvinfile,\
     open("test_out7.csv", "w", encoding="utf-8") as csvoutfile7,\
     open("test_out365.csv", "w", encoding="utf-8") as csvoutfilerok:
    reader = csv.reader(csvinfile, delimiter =",")
    writer7 = csv.writer(csvoutfile7)
    writerrok = csv.writer(csvoutfilerok)
    
    den_7 = 0
    prumer_7 = 0
    aktualni_rok = 0
    den_rok = 0
    prumer_rok = 0

    for row in reader:
        if den_7 == 0:
            radek_7 = row
        den_7 += 1
        prumer_7 += float(row[5])
        if den_7 == 7:
            zapis(prumer_7,den_7,radek_7,writer7)
            den_7 = 0
            prumer_7 = 0
        if aktualni_rok != row[2]:
            aktualni_rok = row[2]
            if den_rok != 0:
                zapis(prumer_rok,den_rok,radek_rok,writerrok)
                den_rok = 0
                prumer_rok = 0
            radek_rok = row
        den_rok += 1
        prumer_rok += float(row[5])
    
    if den_7 != 0:
        zapis(prumer_7,den_7,radek_7,writer7)
    #Cyklus výše nikdy nezpracuje všechna data průtoků za rok. Tady se vypíše zbytek informace za poslední rok. 
    zapis(prumer_rok,den_rok,radek_rok,writerrok)