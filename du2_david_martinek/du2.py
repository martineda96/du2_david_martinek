import csv

#Domácí úkol 2 - průměrné sedmidenní a roční průtoky
#Definice funkce pro zápis dat (použitá výjimka umožňuje chod programu, reálně v cyklu nemůže nastat)
def zapis(prumer,den,radek, writer):
    try:
        prumer /= den
        radek[5] = "{0:.4f}".format(prumer)
        writer.writerow(radek)
    except ZeroDivisionError:
        pass
    except IndexError:
        pass
    
#Ošetření existence vstupu ve složce    
try:
#Otevření a čtení vstupu, definice výstupu
    with open("Data_Libechovka.csv", encoding="utf-8") as csvinfile,\
        open("Libechovka_prutoky_7.csv", "w", newline="", encoding="utf-8") as csvoutfile7,\
        open("Libechovka_prutoky_rok.csv", "w", newline="", encoding="utf-8") as csvoutfilerok:
        reader = csv.reader(csvinfile, delimiter =",")
        writer7 = csv.writer(csvoutfile7)
        writerrok = csv.writer(csvoutfilerok)
        
        #Výchozí proměněnné
        den_7 = 0
        prumer_7 = 0
        aktualni_rok = 0
        den_rok = 0
        prumer_rok = 0
        den_max = 0
        den_min = float('inf')
        cteny_radek = 0

        #Cyklus čte vstup po řádcích. Na každém řádku si sčítá hodnoty průtoků a upravuje proměnné
        #Pokud cyklus vyhodnotí, že již nasbíral hodnoty za po sobě jdoucích sedm dní nebo rok, tak je zapíše do výstupu 
        for row in reader:
            cteny_radek += 1
            if den_7 == 0:
                prvni_radek_7 = row
            try:
                den_7 += 1
                prumer_7 += float(row[5])
                if den_7 == 7:
                    zapis(prumer_7,den_7,prvni_radek_7,writer7)
                    den_7 = 0
                    prumer_7 = 0
                if aktualni_rok != row[2]:
                    aktualni_rok = row[2]
                    if den_rok != 0:
                        zapis(prumer_rok,den_rok,prvni_radek_rok,writerrok)
                        den_rok = 0
                        prumer_rok = 0
                    prvni_radek_rok = row
                den_rok += 1
                prumer_rok += float(row[5])

                #Vyhodnocení maximálního a minimálního průtoku
                if float(row[5]) > den_max:
                    den_max = float(row[5])
                    radek_max = row
                if float(row[5]) < den_min:
                    den_min = float(row[5])
                    radek_min = row
            #Ošetřování výjimek, které se naskytly při testování
            except ValueError:
                print("V souboru je na řádku",cteny_radek,"chybná nebo žádná hodnota.")
                den_7 -= 1
                den_rok -= 1
            except IndexError:
                print("Řádek",cteny_radek,"chybí nebo hodnoty v něm jsou příliš dlouhé.")


        #Vyhodnocení a zápis průtoků, které nezapsal cyklus výše
        if den_7 != 0:
            zapis(prumer_7,den_7,prvni_radek_7,writer7)
        zapis(prumer_rok,den_rok,prvni_radek_rok,writerrok)

        #Výpis největšího a nejmenšího průtoku
        print(f"{radek_max[4]}.{radek_max[3]}.{radek_max[2]} byl naměřen největší průtok o hodnotě {radek_max[5]}.")
        print(f"{radek_min[4]}.{radek_min[3]}.{radek_min[2]} byl naměřen nejmenší průtok o hodnotě    {radek_min[5]}.")
except FileNotFoundError:
    print("Zadaný vstup není ve složce nebo neexistuje.")
