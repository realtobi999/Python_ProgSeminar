"""
05_en_de_cryption_ASCII.py

* Příprava - napište funkci, která zobrazí tabulku ASCII jakkoliv
* Doplňte tabulku o hodnotu znaků BIN, OCT, HEX
* Doplňte možnost omezení od-do
* Napište funkci, která vám dle charu a typu vstupu vrátí hodnotu bin/hex/oct
** Pokuste se zobrazit výstup ve formě tabulky, nejde o ohraničení, ale o strukturu více sloupců
"""

import os


##############################################################
### Vypiš ASCII kódy DEC / CHAR od 1 do 127
# funkce ascii_table
def ascii_table():
    



##############################################################
### Vypiš ASCII kódy - rozšířený výpis, bin/oct/hex doplněný o omezení rozsahu
# funkce ascii_table_with_range:





##############################################################
### Preveď znak na ASCII=DEC hodnotu a poté vrať hodnotu znaku v BIN/OCT/HEX podle base
# funkce char_to_base
# využito v main




##############################################################
### Vypiš ASCII kódy - zformátovaná tabulka, DEC/CHAR/BIN/OCT/HEX = 1 sloupeček
# Možnost zvolit více sloupečků, default 1
# funkce ascii_table_multicolumn




##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("clear")

    char = "#"
    print(f"Znak '{char}' -> ASCII: ", ord(char))
    print(f"Znak '{char}' -> BIN: ", char_to_base(char, 'bin'))
    print(f"Znak '{char}' -> OCT: ", char_to_base(char, 'oct'))
    print(f"Znak '{char}' -> HEX: ", char_to_base(char, 'hex'))
    print(f"Znak '{char}' -> HIPIIII: ", char_to_base(char, 'hip'))
    print("------------------------------------------------\n")

    ascii_table_multicolumn(35,62,4)
