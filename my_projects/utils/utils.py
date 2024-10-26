def print_title(text: any):
    """
    Prints the text in a bold green format into the terminal.

    :param text: The text to display in the terminal.
    """
    print(f"\033[1;32m{text} \033[0m")


def print_error(error: str):
    """
    Prints an error message in a bold red format into the terminal.

    :param error: The error message to display.
    """
    print(f"\033[1;31m{error} \033[0m")


def get_number_from_user(input_text: str = "Vložte číslo: ", 
                         error_message: str = "Špatný vstup, zkuste znova!", 
                         conditions: list = None) -> float:
    """
    Prompts the user for a number input and validates it against optional conditions.

    :param input_text: The prompt text to display when asking for input (default is in Czech: "Vložte číslo").
    :param error_message: The error message to display in case of invalid input (default is in Czech: "Špatný vstup, zkuste znova!").
    :param conditions: A list of boolean conditions to validate the number against. If any condition fails, the error message is shown.
    :return: The valid number entered by the user.
    """
    while True:
        try:
            number = float(input(input_text))

            if conditions and not all(condition(number) for condition in conditions):
                print_error(error_message)
                continue

            return number
        except ValueError:
            print_error(error_message)


