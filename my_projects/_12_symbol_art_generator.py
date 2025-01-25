import math
import os
import sys
from iridis import Color, get_number_from_user, get_string_from_user, print_with_color

DEFAULT_SYMBOL_1 = "*"
DEFAULT_SYMBOL_2 = "?"


def generate_triangle(rows: int) -> str:
    """
    Generates an isosceles triangle with the specified number of rows.

    :param rows: The number of rows in the triangle.
    :return: The triangle as a string.
    """
    triangle_str = ""

    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        symbols = DEFAULT_SYMBOL_1 * (2 * i - 1)
        triangle_str += spaces + symbols + spaces + "\n"

    return triangle_str


def generate_right_triangle(rows: int) -> str:
    """
    Generates a right triangle with the specified number of rows.

    :param rows: The number of rows in the triangle.
    :return: The triangle as a string.
    """
    triangle_str = ""

    for i in range(1, rows + 1):
        symbols = DEFAULT_SYMBOL_1 * i
        triangle_str += symbols + "\n"

    return triangle_str


def draw_triangle(rows: int, symbol: str, type: str = "normal") -> None:
    """
    Draws a triangle of the specified type and symbol.

    :param rows: The number of rows in the triangle.
    :param symbol: The symbol to use for drawing the triangle.
    :param type: The type of triangle ('normal' or 'right').
    :raises ValueError: If an invalid triangle type is specified.
    """
    if type == "normal":
        triangle = generate_triangle(rows=rows)
    elif type == "right":
        triangle = generate_right_triangle(rows=rows)
    else:
        raise ValueError("Invalid triangle type")

    print(triangle.replace(DEFAULT_SYMBOL_1, symbol))


def generate_rectangle(width: int, height: int) -> str:
    """
    Generates a rectangle with the specified width and height.

    :param width: The width of the rectangle.
    :param height: The height of the rectangle.
    :return: The rectangle as a string.
    """
    rectangle_str = ""

    for _ in range(height):
        symbol = DEFAULT_SYMBOL_1 * width
        rectangle_str += symbol + "\n"

    return rectangle_str


def draw_rectangle(width: int, height: int, symbol: str) -> None:
    """
    Draws a rectangle of the specified dimensions and symbol.

    :param width: The width of the rectangle.
    :param height: The height of the rectangle.
    :param symbol: The symbol to use for drawing the rectangle.
    """
    rectangle = generate_rectangle(width=width, height=height)

    print(rectangle.replace(DEFAULT_SYMBOL_1, symbol))


def generate_framed_rectangle(width: int, height: int) -> str:
    """
    Generates a framed rectangle with the specified dimensions.

    :param width: The width of the rectangle.
    :param height: The height of the rectangle.
    :return: The framed rectangle as a string.
    """
    framed_rect_str = ""

    for i in range(height):
        if i == 0 or i == height - 1:
            symbols = DEFAULT_SYMBOL_1 * width
        else:
            symbols = DEFAULT_SYMBOL_1 + " " * (width - 2) + DEFAULT_SYMBOL_1

        framed_rect_str += symbols + "\n"

    return framed_rect_str


def draw_framed_rectangle(width: int, height: int, symbol: str) -> None:
    """
    Draws a framed rectangle of the specified dimensions and symbol.

    :param width: The width of the rectangle.
    :param height: The height of the rectangle.
    :param symbol: The symbol to use for drawing the rectangle.
    """
    framed_rect = generate_framed_rectangle(width=width, height=height)

    print(framed_rect.replace(DEFAULT_SYMBOL_1, symbol))


def generate_chessboard(rows: int, cols: int) -> str:
    """
    Generates a chessboard pattern with the specified rows and columns.

    :param rows: The number of rows in the chessboard.
    :param cols: The number of columns in the chessboard.
    :return: The chessboard as a string.
    """
    chessboard_str = ""

    for row in range(rows):
        for col in range(cols):
            if (row + col) % 2 == 0:
                chessboard_str += DEFAULT_SYMBOL_1
            else:
                chessboard_str += DEFAULT_SYMBOL_2
        chessboard_str += "\n"

    return chessboard_str


def draw_chessboard(rows: int, cols: int, symbol_1: str, symbol_2: str) -> None:
    """
    Draws a chessboard pattern with the specified symbols.

    :param rows: The number of rows in the chessboard.
    :param cols: The number of columns in the chessboard.
    :param symbol_1: The symbol for light squares.
    :param symbol_2: The symbol for dark squares.
    """
    chessboard = generate_chessboard(rows=rows, cols=cols)

    print(chessboard.replace(DEFAULT_SYMBOL_1, symbol_1).replace(DEFAULT_SYMBOL_2, symbol_2))


def generate_christmas_tree(levels: int) -> str:
    """
    Generates a Christmas tree with the specified number of levels.

    :param levels: The number of levels in the tree.
    :return: The Christmas tree as a string.
    """
    christmas_tree_str = ""
    christmas_tree_str += generate_triangle(rows=levels)

    for _ in range(3):
        spaces = " " * (levels - 1)
        christmas_tree_str += spaces + "|" + spaces + "\n"

    return christmas_tree_str


def draw_christmas_tree(levels: int, symbol: str) -> None:
    """
    Draws a Christmas tree with the specified levels and symbol.

    :param levels: The number of levels in the tree.
    :param symbol: The symbol to use for drawing the tree.
    """
    christmas_tree = generate_christmas_tree(levels=levels)

    print(christmas_tree.replace(DEFAULT_SYMBOL_1, symbol))


def generate_circle(radius: int) -> str:
    """
    Generates a circle with the specified radius.

    :param radius: The radius of the circle.
    :return: The circle as a string.
    """
    circle_str = ""
    diameter = radius * 2

    for y in range(diameter + 1):
        for x in range(diameter + 1):
            distance = math.sqrt((x - radius) ** 2 + (y - radius) ** 2)

            if radius - 0.5 <= distance <= radius + 0.5:
                circle_str += DEFAULT_SYMBOL_1
            else:
                circle_str += " "
        circle_str += "\n"

    return circle_str


def draw_circle(radius: int, symbol: str) -> None:
    """
    Draws a circle with the specified radius and symbol.

    :param radius: The radius of the circle.
    :param symbol: The symbol to use for drawing the circle.
    """
    circle = generate_circle(radius=radius)

    print(circle.replace(DEFAULT_SYMBOL_1, symbol))


def print_divider():
    print("\n---------------------------------------------------------\n")


def print_menu():
    print_divider()
    print("[*] - 1. Pravý trojúhelník")
    print("[*] - 2. Rovnoramenný trojúhelník")
    print("[*] - 3. Čtverec nebo obdélník")
    print("[*] - 4. Obdélníkový rámeček")
    print("[*] - 5. Šachovnice")
    print("[*] - 6. Vánoční stromeček")
    print("[*] - 7. Kruh")
    print_with_color("[*] - 0. Konec", color=Color.RED)


def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")


##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    while True:
        clear_screen()
        print_menu()

        print("\n[*] - Zvolte akci:")
        choice = get_number_from_user(
            input_text="\t=> ",
            error_message="\tZadejte platné číslo mezi 0-7",
            conditions=[lambda n: 0 <= n <= 7],
        )

        if choice == 0:
            sys.exit(0)
        elif choice == 1:
            rows = int(get_number_from_user(input_text="[*] - Zadejte počet řádků: ", conditions=[lambda n: n > 0]))
            symbol = get_string_from_user(input_text="[*] - Zadejte symbol: ", conditions=[lambda s: len(s.strip()) == 1])

            clear_screen()
            print_divider()
            draw_triangle(rows=rows, symbol=symbol, type="right")
            input()
        elif choice == 2:
            rows = int(get_number_from_user(input_text="[*] - Zadejte počet řádků: ", conditions=[lambda n: n > 0]))
            symbol = get_string_from_user(input_text="[*] - Zadejte symbol: ", conditions=[lambda s: len(s.strip()) == 1])

            clear_screen()
            print_divider()
            draw_triangle(rows=rows, symbol=symbol)
            input()
        elif choice == 3:
            width = int(get_number_from_user(input_text="[*] - Zadejte šířku: ", conditions=[lambda n: n > 0]))
            height = int(get_number_from_user(input_text="[*] - Zadejte výšku: ", conditions=[lambda n: n > 0]))
            symbol = get_string_from_user(input_text="[*] - Zadejte symbol: ", conditions=[lambda s: len(s.strip()) == 1])

            clear_screen()
            print_divider()
            draw_rectangle(width=width, height=height, symbol=symbol)
            input()
        elif choice == 4:
            width = int(get_number_from_user(input_text="[*] - Zadejte šířku: ", conditions=[lambda n: n > 0]))
            height = int(get_number_from_user(input_text="[*] - Zadejte výšku: ", conditions=[lambda n: n > 0]))
            symbol = get_string_from_user(input_text="[*] - Zadejte symbol: ", conditions=[lambda s: len(s.strip()) == 1])

            clear_screen()
            print_divider()
            draw_framed_rectangle(width=width, height=height, symbol=symbol)
            input()
        elif choice == 5:
            rows = int(get_number_from_user(input_text="[*] - Zadejte počet řádků: ", conditions=[lambda n: n > 0]))
            cols = int(get_number_from_user(input_text="[*] - Zadejte počet sloupců: ", conditions=[lambda n: n > 0]))
            symbol_1 = get_string_from_user(input_text="[*] - Zadejte první symbol: ", conditions=[lambda s: len(s.strip()) == 1])
            symbol_2 = get_string_from_user(input_text="[*] - Zadejte druhý symbol: ", conditions=[lambda s: len(s.strip()) == 1])

            clear_screen()
            print_divider()
            draw_chessboard(rows=rows, cols=cols, symbol_1=symbol_1, symbol_2=symbol_2)
            input()
        elif choice == 6:
            levels = int(get_number_from_user(input_text="[*] - Zadejte počet pater: ", conditions=[lambda n: n > 0]))
            symbol = get_string_from_user(input_text="[*] - Zadejte symbol: ", conditions=[lambda s: len(s.strip()) == 1])

            clear_screen()
            print_divider()
            draw_christmas_tree(levels=levels, symbol=symbol)
            input()
        elif choice == 7:
            radius = int(get_number_from_user(input_text="[*] - Zadejte rádius: ", conditions=[lambda n: n > 0]))
            symbol = get_string_from_user(input_text="[*] - Zadejte symbol: ", conditions=[lambda s: len(s.strip()) == 1])

            clear_screen()
            print_divider()
            draw_circle(radius=radius, symbol=symbol)
            input()
