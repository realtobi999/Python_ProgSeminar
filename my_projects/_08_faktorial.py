"""
* Napište funkce pro výpočet kombinatorických pravidel a vzorců - čistě jako procvičování kombinatoriky... využijte klidně Google
** Google, GPT: Optimalizujte rekurzivní verzi faktoriálu pomocí memoizace (ukládání výsledků).
** Google, GPT: Implementujte přibližný výpočet faktoriálu pomocí Stirlingova vzorce. Oveřte přesnost výpočtů.
** Google, GPT: Implementujte detailní měření výpočetního času pro obě verze výpočtu faktoriálu a porovnejte.
"""

import os
import time
from iridis import print_title, print_error


def factorial(num: int) -> int:
    """
    Computes the factorial of a given number using an iterative approach.

    The factorial of a number 'n' is the product of all positive integers less than or equal to 'n'.
    It is defined as: n! = n * (n-1) * (n-2) * ... * 1.

    :param num: A non-negative integer for which the factorial is to be calculated.
    :return: The factorial of the given number.
    :raises ValueError: If 'num' is a negative integer.
    """
    if num == 0:
        return 1

    result_num = 1
    for i in range(num, 0, -1):
        result_num *= i

    return result_num


def factorial_recursive(num: int) -> int:
    """
    Computes the factorial of a given number using a recursive approach.

    The factorial of a number 'n' is the product of all positive integers less than or equal to 'n'.
    It is defined as: n! = n * (n-1) * (n-2) * ... * 1.

    :param num: A non-negative integer for which the factorial is to be calculated.
    :return: The factorial of the given number.
    :raises ValueError: If 'num' is less than 1.
    """
    if num == 1:
        return num

    return num * factorial_recursive(num - 1)


def factorial_safe_input(num: any) -> int:
    """
    Validates the input and computes the factorial of a number.

    Ensures that the input is an integer and non-negative before calculating the factorial.

    :param num: The input value to be validated and used to compute the factorial.
    :return: The factorial of the validated number.
    :raises ValueError: If 'num' is not an integer or is negative.
    """
    if not isinstance(num, int):
        raise ValueError("Input must be an integer.")
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    return factorial(num)


def factorial_benchmark(num: int) -> None:
    """
    Benchmarks the performance of factorial calculations using both iterative and recursive methods.

    The function measures and compares the execution time for calculating the factorial using both methods.

    :param num: The integer for which the factorial is calculated and benchmarked.
    """
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
    factorial_benchmark(955)
    print("------------------------------------------------")
