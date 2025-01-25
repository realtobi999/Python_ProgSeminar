import os
from iridis import print_title

ENG_ALPHABET = "aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž.!,AÁBCČDĎEÉĚFGHIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽ"
# Anglická abeceda s českými znaky


def caesar_cipher_encrypt(text: str, shift: int, alphabet: str) -> str:
    """
    Encrypts a given text using Caesar cipher by shifting characters in the alphabet.

    :param text: The text to encrypt.
    :param shift: The number of positions to shift each character in the alphabet.
    :param alphabet: The alphabet to use for encryption.
    :return: The encrypted text.
    """
    encrypted_text = ""
    alphabet = list(alphabet)

    for char in text:
        if char == " ":
            encrypted_text += " "
            continue

        index_to_add = alphabet.index(char) + shift

        if index_to_add > len(alphabet) - 1:
            index_to_add -= len(alphabet)

        encrypted_text += alphabet[index_to_add]

    return encrypted_text


def caesar_cipher_decrypt(encrypted_text: str, shift: int, alphabet: str) -> str:
    """
    Decrypts a given encrypted text that was ciphered using Caesar cipher.

    :param encrypted_text: The encrypted text to decrypt.
    :param shift: The number of positions to shift back each character in the alphabet.
    :param alphabet: The alphabet to use for decryption.
    :return: The decrypted text.
    """
    text = ""
    alphabet = list(alphabet)

    for char in encrypted_text:
        if char == " ":
            text += " "
            continue

        try:
            index_to_add = alphabet.index(char) - shift
        except ValueError:
            text += char
            continue

        if index_to_add < 0:
            index_to_add += len(alphabet)

        text += alphabet[index_to_add % len(alphabet)]

    return text


if __name__ == "__main__":
    os.system("clear")

    print_title("[*] 05 - Encryption/Decryption - Basics 01\n")

    encrypted_text = caesar_cipher_encrypt(
        "Tečna je přímka, která má s křivkou společný jeden bod a vzdálenost křivky od přímky klesá při přibližování se k bodu dotyku rychleji než lineárně!",
        2,
        ENG_ALPHABET,
    )
    print_title(f"[*] Encrypted: ")
    print(encrypted_text)

    decrypted_text = caesar_cipher_decrypt(encrypted_text, 2, ENG_ALPHABET)
    print_title(f"[*] Decrypted: ")
    print(decrypted_text)
