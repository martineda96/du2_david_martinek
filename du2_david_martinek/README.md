Domácí úkol 2 - průměrné sedmidenní a roční průtoky [David Martínek]
Program pracuje s daty ČHMÚ uložených ve formátu .csv podle stanovené normy. Program si načte soubor s daty průtoků podle 
zadané cesty (Data_Libechovka) a vytvoří dva .csv výstupy. Program vyhodnocuje data postupně po řádcích v naprogramovaném cyklu a uživatele upozorní, pokud se ve výpočtu vyskytla chyba (vlivem nesprávného formátu vstupních dat).

Sedmidenní průtoky:
Jakmile program přečte sedm řádků, tak zprůměruje přečtené hodnoty průtoků a vytvoří ve výstupu Libechovka_prutoky_7.csv 
řádek nesoucí informaci o prvním dni z těchto 7 měření, akorát jeho hodnotu průtoku nahradí spočteným průměrným průtokem.

Roční průtoky:
Jakmile program zjistí, že začíná měřit data z dalšího roku, tak vyhodnotí rok předchozí. Zápis je analogický se 
zápisem sedmidenních průtoků (Libechovka_prutoky_rok.csv). Hodnota průtoku je opět nahrazena průměrným průtokem za celý rok.

Zbytkové hodnoty:
Pokud nebyly vyhodnoceny všechny hodnoty (protože cyklus nenapočítal sedm po sobě jdoucích hodnot), tak jsou vyhodnoceny mimo cyklus na poslední řádek výstupu. V případě ročních průtoků bude poslední řádek vždy vyhodnocován mimo cyklus. 

Maxima a minima:
Program průběžně porovnává hodnoty průtoky mezi sebou, aby nakonec vypsal údaje o největším a nejmenším průtoku do konzole.
