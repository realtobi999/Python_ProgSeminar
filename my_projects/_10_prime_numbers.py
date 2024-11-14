"""
** Eratosthenovo síto - optimalizace pomocí segmentace (import math), využijeme i bitarray optimalizaci 
*** Eratosthenovo síto - optimalizace vynecháním sudých čísel, využijeme i bitarray optimalizaci
*** Eratosthenovo síto - wheel faktorizace a segmented optimalizace 
*** Eratosthenovo síto - multiprocessing optimalizace, bitarray a segmentace 
*** Eratosthenovo síto - rozdíl ve spotřebě paměti
** Eratosthenovo síto - grafická interpretace četnosti

## Výsledky pro test 100 mil. na NTB:
## Eratosthénovo síto klasika pro N=100000000:      Peak paměť = 1010.76 MB,  18.549 s
## Eratosthénovo síto bitarray pro N=100000000:     Peak paměť = 223.26 MB,    5.884 s
## Eratosthénovo síto segmented pro N=100000000:    Peak paměť = 208.49 MB,   12.388 s 
## Eratosthénovo síto parity pro N=100000000:       Peak paměť = 263.10 MB,    7.485 s
## Eratosthénovo síto segm. wheel pro N=100000000:  Peak paměť = 208.49 MB,   29.994 s
## Eratosthénovo síto parallel pro N=100000000:     Peak paměť = 261.79 MB,    5.870 s (=10 thread) 5.299 s (=16 thread)
"""

import os
import time
from bitarray import bitarray
import math
import iridis


def is_prime(num: int) -> bool:
    """
    Determines whether a number is prime.

    A prime number is a natural number greater than 1 that is divisible only by 1 and itself.

    :param num: The number to check.
    :return: True if the number is prime, False otherwise.
    """
    if num == 0 or num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def get_primes_up_to(num: int) -> list:
    """
    Returns a list of all prime numbers up to a given number.

    This function iterates through all numbers up to 'num' and checks if each is prime.

    :param num: The upper limit for prime number generation.
    :return: A list of prime numbers less than 'num'.
    """
    primes = []

    for i in range(0, num):
        if is_prime(i):
            primes.append(i)

    return primes


def print_primes_up_to(num: int) -> None:
    """
    Prints all prime numbers up to a given number.

    If there are no prime numbers found, it prints "Žádná!".

    :param num: The upper limit for prime number generation.
    :return: None
    """
    primes = get_primes_up_to(num)

    if len(primes) == 0:
        print("Žádná!")

    for prime in primes:
        print(prime)


def get_n_primes(num: int) -> list:
    """
    Returns a list of the first 'num' prime numbers.

    The function keeps adding prime numbers until 'num' primes have been found.

    :param num: The number of primes to return.
    :return: A list of the first 'num' prime numbers.
    """
    primes = []

    i = 0
    while True:
        if len(primes) == num:
            break
        if is_prime(i):
            primes.append(i)
        i += 1

    return primes


def print_n_primes(num: int) -> None:
    """
    Prints the first 'num' prime numbers.

    If there are no primes to print (num <= 0), it will print "Žádná!".

    :param num: The number of primes to print.
    :return: None
    """
    primes = get_n_primes(num)

    if len(primes) == 0:
        print("Žádná!")

    for prime in primes:
        print(prime)


def sieve_of_eratosthenes(limit: int) -> list:
    """
    Generates a list of prime numbers up to a given limit using the Sieve of Eratosthenes.

    The algorithm iterates through all numbers up to 'limit', marking non-prime numbers as false.

    :param limit: The upper limit for prime number generation.
    :return: A list of all primes less than 'limit'.
    """
    all_numbers = list(range(2, limit))

    for num in all_numbers:
        if num > math.sqrt(all_numbers[-1]):
            break

        for other_num in all_numbers[num::]:
            if other_num % num == 0:
                all_numbers.remove(other_num)

    return all_numbers


def sieve_of_eratosthenes_bitarray(limit: int) -> list:
    """
    Generates a list of prime numbers up to a given limit using the Sieve of Eratosthenes with bitarray.

    This method uses a bitarray for more memory-efficient storage of prime number status.

    :param limit: The upper limit for prime number generation.
    :return: A list of all primes less than 'limit'.
    """
    all_numbers = bitarray(limit)
    all_numbers.setall(1)  # assume all numbers are prime initially
    all_numbers[0:2] = 0  # 0 and 1 are not prime numbers

    for num in range(2, limit):
        if num > math.sqrt(limit - 1):
            break

        for other_num in range(num + 1, limit):
            if other_num % num == 0:
                all_numbers[other_num] = 0

    return [i for i in range(2, limit) if all_numbers[i]]


##############################################################
### Eratosthenovo síto - optimalizace pomocí segmentace (import math), využijeme i bitarray optimalizaci
## (nejde ale o úsporu času, ale úsporu paměti)
# Funkce sieve_segmented

# TODO

##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("clear")
    iridis.print_rainbow("10 - Prvočísla\n")

    num = int(iridis.get_number_from_user(input_text="Zadejte hezké číslo: "))

    print("------------------------------------------------")

    print(f"Je to prvočíslo: {"Ano" if is_prime(num) == True else "Ne"}\n")
    print(f"Prvočísla do {num}:")
    print_primes_up_to(num)

    print(f"Prvních {num}. prvočísel:")
    print_n_primes(num)

    print("------------------------------------------------")

    start_time = time.time()
    sieve_of_eratosthenes(5000)
    end_time = time.time()
    print(f"Tradiční Eratosthenovo síto trvalo  {(end_time - start_time):.5f} sekund")

    start_time = time.time()
    sieve_of_eratosthenes_bitarray(5000)
    end_time = time.time()
    print(f"Eratosthenovo síto s bitarray trvalo {(end_time - start_time):.5f} sekund")
