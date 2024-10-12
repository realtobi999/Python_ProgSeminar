import random
import os

# Global constants and variables
CORRECT_ANSWERS = 0
WRONG_ANSWERS = 0
TOTAL_SOLVED = 0

OPERATORS = ["-", "+", "*", "/"]

# Clear the console
os.system("clear")


def print_error(error: str):
    """
    Prints an error message in bold red.

    :param error: The error message to display.
    """
    print(f"\n\033[1;31m{error} \033[0m")


def get_number_from_user(input_text: str = "Vložte číslo: ", 
                         error_message: str = "Špatný vstup, zkuste znova!", 
                         conditions: list = None) -> float:
    """
    Prompts the user for a number input and validates it against optional conditions.

    :param input_text: The text to display when asking for input.
    :param error_message: The message to display for invalid input.
    :param conditions: A list of conditions (functions) to validate the input.
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


def update_globals(answer_is_correct: bool) -> None:
    """
    Updates global variables for correct, wrong answers, and total solved problems.

    :param answer_is_correct: Boolean indicating if the user's answer is correct.
    """
    global CORRECT_ANSWERS, WRONG_ANSWERS, TOTAL_SOLVED

    if answer_is_correct:
        CORRECT_ANSWERS += 1
    else:
        WRONG_ANSWERS += 1

    TOTAL_SOLVED += 1


def display_globals() -> None:
    """
    Displays the global count of total solved problems, correct answers, and wrong answers.
    """
    print(f"Total Solved: {TOTAL_SOLVED}")
    print(f"Correct Answers : \033[92m{CORRECT_ANSWERS}\033[0m")
    print(f"Wrong Answers : \033[91m{WRONG_ANSWERS}\033[0m")


def simple_problem():
    """
    Generates a simple arithmetic problem using two random numbers and a random operator. 
    Validates the user's answer and updates the global counts.
    """
    number_1 = float(random.randint(1, 10))
    number_2 = float(random.randint(1, 10))
    operator = random.choice(OPERATORS)

    print(f"Jaký je výsledek {number_1:.0f} {operator} {number_2:.0f}?")

    # calculate the correct result based on the operator
    if operator == "+":
        result = number_1 + number_2
    elif operator == "-":
        result = number_1 - number_2
    elif operator == "*":
        result = number_1 * number_2
    elif operator == "/":
        result = number_1 / number_2

    user_input_result = get_number_from_user(input_text="=> ")

    # check if the user's result matches the correct result
    if user_input_result == result:
        print(f"\n\033[1;32mSprávně! \033[0m")
        update_globals(answer_is_correct=True)
    else:
        print_error("Nesprávný výsledek!")
        update_globals(answer_is_correct=False)

    display_globals()


def complex_problem(number_of_elements: int):
    """
    Generates a complex arithmetic problem with multiple random numbers and random operators.
    Validates the user's answer and updates the global counts.

    :param number_of_elements: Number of elements (numbers) to include in the problem.
    """
    problem = ""
    result = 0
    numbers = []

    # generate random numbers
    for _ in range(number_of_elements):
        numbers.append(float(random.randint(1, 10)))

    # apply random operators to the numbers
    for i, number in enumerate(numbers):
        operator = random.choice(OPERATORS[0:2])  # limiting to "+" or "-"

        if operator == "+":
            result += number
        else:
            result -= number

        # construct the problem string
        if i == 0 and operator != "-":
            problem += f"{number:.0f} "
        else:
            problem += f"{operator} {number:.0f} "

    print(f"Jaký je výsledek {problem}?")

    user_input_result = get_number_from_user(input_text="=> ")

    # check if the user's result matches the correct result
    if user_input_result == result:
        print(f"\n\033[1;32mSprávně! \033[0m")
        update_globals(answer_is_correct=True)
    else:
        print_error("Nesprávný výsledek!")
        update_globals(answer_is_correct=False)

    display_globals()


if __name__ == "__main__":
    random.seed()

    print(f"\n\033[1;32mNahodné příklady generátor! \033[0m\n")
    difficulty = input("Vyberte obtížnost: [1 - lehká, 2 - obtížná]: ")
    print()

    if difficulty == "2":
        print("Kolik chcete čísel v příkladě?")
        amount_of_numbers = int(get_number_from_user(input_text="=> ", conditions=[lambda n: n > 0]))
        print()

    while True:
        if difficulty == "1":
            simple_problem()
        elif difficulty == "2":
            complex_problem(amount_of_numbers)
        else:
            print_error("Nesprávný input!")

        print(f"\n\033[1;32mChcete pokračovat? [Y/N] \033[0m\n")

        user_exit_input = input().upper()

        if user_exit_input == "Y":
            continue
        elif user_exit_input == "N":
            break
        else:
            print_error("Nesprávný input!")
            break
