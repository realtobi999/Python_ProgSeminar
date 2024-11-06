"""
* Napište funkci, která vypočítá faktoriál čísla pomocí smyčky for, iterace.
* Napište funkci, která vypočítá faktoriál čísla pomocí rekurze.
* Upravte předchozí funkci tak, aby ošetřovala neplatné vstupy (např. záporná čísla nebo nečíselné hodnoty).
* Porovnejte efektivitu faktoriálu vypočítaného pomocí smyčky a pomocí rekurze pro větší čísla (např. 500). Knihovna time.
* Napište funkce pro výpočet kombinatorických pravidel a vzorců - čistě jako procvičování kombinatoriky... využijte klidně Google
** Google, GPT: Optimalizujte rekurzivní verzi faktoriálu pomocí memoizace (ukládání výsledků).
** Google, GPT: Implementujte přibližný výpočet faktoriálu pomocí Stirlingova vzorce. Oveřte přesnost výpočtů.
** Google, GPT: Implementujte detailní měření výpočetního času pro obě verze výpočtu faktoriálu a porovnejte.
"""

import os
import time
import math

# import matplotlib.pyplot as plt       # pip install matplotlib
from iridis import print_title, print_error

# Globální konstanty a proměnné
MEMO = {}  # list pro ukládání mezivýsledků, spočítaných faktoriálů, memoizace


##############################################################
### Faktoriál pomocí for cyklu, vypočet iterací
# Funkce factorial
def factorial(num: int) -> int:
    if num == 0:
        return 1

    result_num = 1
    for i in range(num, 0, -1):
        result_num *= i

    return result_num


##############################################################
### Faktoriál pomocí rekurze
# Funkce factorial_recursive


def factorial_recursive(num: int) -> int:
    if num == 1:
        return num

    return num * factorial_recursive(num - 1)


##############################################################
### Faktoriál s ošetřením vstupu
# Funkce factorial_safe_input


def factorial_safe_input(num: any) -> int:
    if not isinstance(num, int):
        raise ValueError("Input must be an integer.")
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    return factorial(num)


##############################################################
### Časová náročnost - srovnání for cyklu a rekurze, případně knihovny math
# Funkce faktorial_time_consuming


def factorial_benchmark(num: int) -> None:
    print(f"[*] Testovací hodnota faktoriálu je: {num}!\n")

    print_title("[*] Faktoriál pomocí iterace:")
    print("[*] Začíná měření...")

    start_time = time.time()
    print(f"[*] {num}! = {factorial(num)}")
    end_time = time.time()

    print("[*] Konec měření")
    iteration_time = end_time - start_time

    print_title("[*] Faktoriál pomocí rekurze:")
    print("[*] Začíná měření...")

    start_time = time.time()
    print(f"[*] {num}! = {factorial_recursive(num)}")
    end_time = time.time()

    print("[*] Konec měření")
    recursive_time = end_time - start_time

    print_title(f"\n[*] Výsledky benchmarku:")
    print(f"- Iterativní výpočet trval {iteration_time:.6f} sekund")
    print(f"- Rekurzivní výpočet trval {recursive_time:.6f} sekund")


##############################################################
### Kombinatorika
# např. funkce permutation, combination, permutation, variation


##############################################################
### Memoizace neboli ukládání mezivýsledků a snížení počtu opakovaných výpočtů
# funkce factorial_memo


##############################################################
### Přibližný výpočet faktoriálu (Stirlingův vzorec) + ** grafické znázornění přesnosti vzorce
# funkce stirling_approximation, compare_factorial_and_stirling


##############################################################
### Časová náročnost a její zobrazení
# funcke time_consumption, graph_time_consumption


##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("clear")
    print_title("[*] - 08 Faktoriál\n")

    n = 5

    # faktoriál pomocí iterace
    print("[*] Faktoriál pomocí cyklu for, iterace:")
    print(f"[*] {n}! = {factorial(n)}")
    print("------------------------------------------------")

    # faktoriál pomocí iterace
    print("[*] Faktoriál rekurzivně:")
    print(f"[*] {n}! = {factorial_recursive(n)}")
    print("------------------------------------------------")

    # faktoriál pomocí iterace
    print("[*] Faktoriál bezpečně:")
    print(f"[*] {n}! = {factorial_safe_input(n)}")

    try:
        print(f"ahoj! = {factorial_safe_input('ahoj')}")
        print(f"(-20)! = {factorial_safe_input(-20)}")
        print(f"3.7! = {factorial_safe_input(3.7)}")
        print(f"()! = {factorial_safe_input()}")
    except ValueError as e:
        print_error(e)
    print("------------------------------------------------")

    # srovnání časové náročnosti různých metod
    factorial_benchmark(939)
    print("------------------------------------------------")
    
