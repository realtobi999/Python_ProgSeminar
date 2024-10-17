import os

ENG_ALPHABET = [
    list("AÁBCČDĎEÉĚFGHIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽ"),
    list("aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž.!,"),
]


def caesar_cipher_encrypt(text: str, shift: int) -> str:
    encrypted_text = ""

    for char in text:
        if char == " ":
            encrypted_text += " "
            continue

        if char.isupper():
            alphabet = ENG_ALPHABET[0]
        else:
            alphabet = ENG_ALPHABET[1]

        index_to_add = alphabet.index(char) + shift

        if index_to_add > len(alphabet) - 1:
            index_to_add -= len(alphabet)

        encrypted_text += alphabet[index_to_add]

    return encrypted_text


def caesar_cipher_decrypt(encrypted_text: str, shift: int) -> str:
    text = ""

    for char in encrypted_text:
        if char == " ":
            text += " "
            continue

        if char.isupper():
            alphabet = ENG_ALPHABET[0]
        else:
            alphabet = ENG_ALPHABET[1]

        index_to_add = alphabet.index(char) - shift

        if index_to_add < 0:
            index_to_add += len(alphabet)

        text += alphabet[index_to_add]

    return text


if __name__ == "__main__":
    os.system("clear")

    encrypted_text = caesar_cipher_encrypt("Tečna je přímka, která má s křivkou společný jeden bod a vzdálenost křivky od přímky klesá při přibližování se k bodu dotyku rychleji než lineárně!", 2)
    print(encrypted_text)

    decrypted_text = caesar_cipher_decrypt(encrypted_text, 2)
    print(decrypted_text)
