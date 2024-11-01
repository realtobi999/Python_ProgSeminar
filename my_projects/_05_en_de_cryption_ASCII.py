import os
from iridis import print_error, print_title

def ascii_print_table(start: int, end: int) -> None:
    """
    Prints a formatted table of ASCII codes from 'start' to 'end'.

    :param start: The starting ASCII code (inclusive).
    :param end: The ending ASCII code (inclusive).
    :raises ValueError: If start or end values are out of range.
    """
    # input validation
    if start < 1 or start >= 127:
        raise ValueError("Start value must be between 1 and 126 (inclusive).")
    if end <= 1 or end > 127:
        raise ValueError("End value must be between 2 and 127 (inclusive).")

    for i in range(start, end + 1):
        char = (
            chr(i) if i >= 32 else "[Non-printable]"
        )  # characters 1 to 32 are non-printable
        print(
            f"Dec: {i} | Bin: {bin(i)[2:]} | Oct: {oct(i)[2:]} | Hex: {hex(i)[2:]} | Char: {char}"
        )


def ascii_print_table_multicolumn(start: int, end: int, columns: int = 1) -> None:
    """
    Prints a formatted table of ASCII codes in multiple columns from 'start' to 'end'.

    :param start: The starting ASCII code (inclusive).
    :param end: The ending ASCII code (exclusive).
    :param columns: The number of columns to display in the output (default is 1).
    :raises ValueError: If start or end values are out of range.
    """
    if start < 1 or start >= 127:
        raise ValueError("Start value must be between 1 and 126 (inclusive).")
    if end <= 1 or end > 127:
        raise ValueError("End value must be between 2 and 127 (inclusive).")

    output = []

    for i in range(start, end):
        char = chr(i) if i >= 32 else "[Non-printable]"
        output.append(
            f"Dec: {i} | Char: {char} | Bin: {bin(i)[2:]} | Oct: {oct(i)[2:]} | Hex: {hex(i)[2:]}"
        )

    for index in range(0, len(output), columns):
        print(" || ".join(output[index : index + columns]))


def ascii_convert(char: str, return_type: str) -> str:
    """
    Converts a character to its ASCII value in the specified format.

    :param char: The character to convert (must be a single character).
    :param return_type: The format to return the ASCII value ('oct', 'bin', or 'hex').
    :raises ValueError: If the input character is not a single character or if the return type is invalid.
    :return: The ASCII value in the specified format.
    """
    # input validation
    if len(char) != 1:
        raise ValueError("ERROR. Input must be a character!")

    dec_value = ord(char)

    if return_type.upper() == "OCT":
        return oct(dec_value)
    elif return_type.upper() == "HEX":
        return hex(dec_value)
    elif return_type.upper() == "BIN":
        return bin(dec_value)
    else:
        raise ValueError("ERROR. Invalid return type. Use 'oct', 'bin', or 'hex'.")


if __name__ == "__main__":
    os.system("clear")
    print_title("[*] 05 - Encryption/Decryption - ASCII\n")

    try:
        ascii_print_table(1, 127)

        char = "#"
        print(f"[*] Znak '{char}' -> ASCII: ", ord(char))
        print(f"[*] Znak '{char}' -> BIN: ", ascii_convert(char, "bin"))
        print(f"[*] Znak '{char}' -> OCT: ", ascii_convert(char, "oct"))
        print(f"[*] Znak '{char}' -> HEX: ", ascii_convert(char, "hex"))
    except ValueError as e:
        print_error(e)
