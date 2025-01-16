import os
import sys
import traceback
from iridis import *

def decimal_to_binary(d_num: int) -> str:
    """
    Converts a decimal number to its binary representation.

    :param d_num: The decimal number to convert.
    :return: A string representing the binary equivalent of the decimal number.
    """
    if d_num == 0:
        return "0"

    b_num = ""

    while d_num > 0:
        b_num += str(d_num % 2)
        d_num //= 2

    return b_num[::-1]


def binary_to_decimal(b_num: str) -> int:
    """
    Converts a binary string to its decimal equivalent.

    :param b_num: The binary number as a string.
    :return: The decimal equivalent as an integer.
    """
    if b_num == "0":
        return 0

    d_num = 0

    for i, b in enumerate(b_num[::-1]):
        if b == "1":
            d_num += 2**i

    return d_num


def decimal_to_base(d_num: int, base: int) -> str:
    """
    Converts a decimal number to a specified base.

    Supports bases greater than or equal to 2. For bases greater than 10, 
    it uses letters A-Z to represent values above 9.

    :param d_num: The decimal number to convert.
    :param base: The base to convert to (e.g., 2, 8, 16).
    :return: A string representing the number in the specified base.
    :raises ValueError: If the base is less than 2.
    """
    if base < 2:
        raise ValueError("Base must be at least 2")
    if d_num == 0:
        return "0"

    b_num = ""

    while d_num > 0:
        r = d_num % base
        b_num += str(r) if r < 10 else chr(r + 55)  # Use A-Z for bases > 10.
        d_num //= base

    return b_num[::-1]


def base_to_decimal(b_num: str, base: int) -> int:
    """
    Converts a number in a specified base to its decimal equivalent.

    :param b_num: The number in the specified base as a string.
    :param base: The base of the number (e.g., 2, 8, 16).
    :return: The decimal equivalent as an integer.
    :raises ValueError: If the base is less than 2 or if the input contains invalid digits.
    """
    if base < 2:
        raise ValueError("Base must be at least 2")
    if b_num == "0":
        return 0

    d_num = 0

    for i, b in enumerate(b_num[::-1]):
        if b.isdigit():
            b = int(b)
        else:
            b = ord(b.upper()) - 55  # Get the value of A-Z for bases > 10.

        if b >= base:
            raise ValueError(f"Invalid digit '{b}' for base {base}")

        d_num += b * (base**i)

    return d_num


##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n---------------------------------------------------------\n")

        # Display menu options.
        print("[*] - 1. Převod z desítkové do binární soustavy")
        print("[*] - 2. Převod z binární do desítkové soustavy")
        print("[*] - 3. Převod z desítkové do libovolné soustavy")
        print("[*] - 4. Převod z libovolné soustavy do desítkové")
        print_with_color("[*] - 5. Konec programu", color=Color.RED)

        print("\n[*] - Zvolte akci:")
        choice = get_number_from_user(
            input_text="\t=> ",
            error_message="\tZadejte platné číslo mezi 1-5",
            conditions=[lambda n: 1 <= n <= 5],
        )

        # Handle menu selection.
        os.system("cls" if os.name == "nt" else "clear")
        print("\n---------------------------------------------------------\n")
        try:
            if choice == 1:
                # Convert from decimal to binary.
                d_number = get_number_from_user(
                    input_text="[*] - Zadejte číslo v desítkové soustavě: ",
                    error_message="Neplatné číslo",
                )
                print(f"\n[*] - Desítková reprezentace:\t{d_number:.0f}")
                print(f"[*] - Binární reprezentace:\t{decimal_to_binary(int(d_number))}\n")
                input()
            elif choice == 2:
                # Convert from binary to decimal.
                b_number = get_string_from_user(
                    input_text="[*] - Zadejte číslo v binární soustavé: ",
                    error_message="Neplatné číslo",
                    conditions=[lambda s: all(c in "01" for c in s)],
                )
                print(f"\n[*] - Binární reprezentace:\t{b_number}")
                print(f"[*] - Desítková reprezentace:\t{int(binary_to_decimal(b_number))}\n")
                input()
            elif choice == 3:
                # Convert from decimal to a custom base.
                d_number = get_number_from_user(
                    input_text="[*] - Zadejte číslo v desítkové soustavě: ",
                    error_message="Neplatné číslo",
                )
                base = get_number_from_user(
                    input_text="[*] - Zadejte základ soustavy (např. 2, 8, 16): ",
                    error_message="Neplatné číslo, musí být větší než 2",
                    conditions=[lambda n: n >= 2],
                )
                print(f"\n[*] - Reprezentace v soustave 10:\t{d_number:.0f}")
                print(f"[*] - Reprezentave v soustavě {base:.0f}:\t{decimal_to_base(int(d_number), int(base))}\n")
                input()
            elif choice == 4:
                # Convert from a custom base to decimal.
                base = get_number_from_user(
                    input_text="[*] - Zadejte základ soustavy (např. 2, 8, 16): ",
                    error_message="Neplatné číslo, musí být větší než 2",
                    conditions=[lambda n: n >= 2],
                )
                b_number = get_string_from_user(
                    input_text=f"[*] - Zadejte číslo v soustavě {base:.0f}: ",
                    error_message="Neplatné číslo",
                )
                print(f"\n[*] - Reprezentave v soustavě {base:.0f}:\t{b_number}")
                print(f"[*] - Reprezentace v soustave 10:\t{base_to_decimal(b_number, int(base))}\n")
                input()
            else:
                # Exit the program.
                os.system("cls" if os.name == "nt" else "clear")
                sys.exit(0)
        except Exception as e:
            os.system("cls" if os.name == "nt" else "clear")
            print_with_color("[*] - Chyba v systému", color=Color.RED)

            print("\nDEBUG MODE? (0/1)")
            should_debug = get_number_from_user(
                input_text="=> ",
                error_message="Invalid input.",
                conditions=[lambda n: n == 0 or n == 1],
            )
            if should_debug == 1:
                traceback.print_exception(e)

            # Ask the user if they want to restart the application.
            print("\nChcete restartovat aplikaci? (0/1)")
            should_continue = get_number_from_user(
                input_text="=> ",
                error_message="Invalid input.",
                conditions=[lambda n: n == 0 or n == 1],
            )
            if should_continue == 1:
                continue
            if should_continue == 0:
                sys.exit(1)
