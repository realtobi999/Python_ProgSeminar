import os
import hashlib
import csv

from utils import print_title, print_error, get_number_from_user


# Global constants and variables
FILE_NAME = "./../data/users.csv"


def hash_text(text: str) -> str:
    """
    Hashes the provided text using SHA-256.

    :param text: The string to be hashed.
    :return: The SHA-256 hash of the text as a hexadecimal string.
    """
    sha256 = hashlib.sha256()
    sha256.update(text.encode())
    return sha256.hexdigest()


def register_user() -> None:
    """
    Registers a new user by collecting their email and password,
    hashing the password, and storing both in the users CSV file.
    """
    print_title("\n[*] Registration Form")
    email = input("[*] Enter email: ")
    hashed_password = hash_text(input("[*] Enter password: "))

    with open(FILE_NAME, "a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([email, hashed_password])
    csv_file.close()


def login_user() -> None:
    """
    Authenticates a user by comparing their entered email and password hash
    against stored records in the users CSV file.

    :raises ValueError: If the credentials are incorrect.
    """
    print_title("\n[*] Login Form")
    email = input("[*] Enter email: ")
    password = input("[*] Enter password: ")

    with open(FILE_NAME, "r", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            user_email = row[0]
            user_hashed_password = row[1]

            if user_email == email and hash_text(password) == user_hashed_password:
                print("\n[*] Welcome to the application!")
                break
        else:
            raise ValueError("Invalid credentials! Please try again.")


if __name__ == "__main__":
    os.system("clear")
    print_title("[*] 07 - Hash\n")

    print("[*] Register - 1 ")
    print("[*] Login - 2 ")

    print("\n[*] What would you like to do?")
    user_choice = get_number_from_user(
        input_text="=> ", conditions=[lambda n: n == 1 or n == 2]
    )

    if user_choice == 1:
        register_user()
    elif user_choice == 2:
        while True:
            try:
                login_user()
                break
            except ValueError as e:
                print_error(e)
