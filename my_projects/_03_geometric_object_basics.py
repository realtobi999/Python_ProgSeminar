import math
import os
from dataclasses import dataclass
from utils import print_error, print_title, get_number_from_user


@dataclass
class Triangle:
    # lengths of the sides
    side_c: float
    side_a: float
    side_b: float

    # angles (in degrees)
    c_angle: float = 0.00
    a_angle: float = 0.00
    b_angle: float = 0.00


def get_triangle_from_user() -> Triangle:
    """
    Prompts the user to input three sides of a triangle, validates the input,
    and returns the sides as a Triangle object with the longest side as the side_c.

    Returns:
        Triangle: A Triangle object with sorted side lengths (side_c, side_a, side_b).
    """

    triangle_sides = []

    triangle_sides.append(
        get_number_from_user("[*] Zadej první stranu: ", conditions=[lambda n: n > 0])
    )
    triangle_sides.append(
        get_number_from_user("[*] Zadej druhou stranu: ", conditions=[lambda n: n > 0])
    )
    triangle_sides.append(
        get_number_from_user("[*] Zadej třetí stranu: ", conditions=[lambda n: n > 0])
    )

    triangle_sides.sort(reverse=True)

    return Triangle(
        side_c=triangle_sides[0],
        side_a=triangle_sides[1],
        side_b=triangle_sides[2],
    )


def is_valid_triangle(triangle: Triangle) -> bool:
    """
    Checks if the given triangle satisfies the triangle inequality theorem,
    ensuring it can be formed with the provided side lengths. (lengths also cannot be negative)
    Additionally, it checks if the sum of the triangle's angles equals 180 degrees.

    Returns:
        bool: True if the triangle is valid, False otherwise (with an error message).
    """

    if triangle.side_a <= 0 or triangle.side_b <= 0 or triangle.side_c <= 0:
        print_error(
            "ERROR! Not a valid triangle due to side lengths: side lengths cannot be less than or zero."
        )
        return False

    if (
        triangle.side_a + triangle.side_b <= triangle.side_c
        or triangle.side_a + triangle.side_c <= triangle.side_b
        or triangle.side_b + triangle.side_c <= triangle.side_a
    ):
        print_error("ERROR! Not a valid triangle due to side lengths.")
        return False

    return True


def calculate_triangle_angles(triangle: Triangle) -> Triangle:
    """
    Calculates the angles of a triangle based on the side lengths using the cosine rule.

    Returns:
        Triangle: The Triangle object with updated angles (a_angle, b_angle, c_angle).
    """

    # Using cosine rule to calculate the angles
    triangle.a_angle = math.degrees(
        math.acos(
            (triangle.side_b**2 + triangle.side_c**2 - triangle.side_a**2)
            / (2 * triangle.side_b * triangle.side_c)
        )
    )
    triangle.b_angle = math.degrees(
        math.acos(
            (triangle.side_a**2 + triangle.side_c**2 - triangle.side_b**2)
            / (2 * triangle.side_a * triangle.side_c)
        )
    )
    triangle.c_angle = 180 - (triangle.a_angle + triangle.b_angle)

    return triangle


def display_triangle_properties(triangle: Triangle) -> None:
    """
    Calculates circumference, area, circumradius and inradius of the triangle.
    """

    circumference = triangle.side_c + triangle.side_a + triangle.side_b

    # calculate semi-perimeter
    s = circumference / 2

    # calculate area: √s(s−a)(s−b)(s−c) where s: (a + b + c)/2
    area = math.sqrt(
        s * (s - triangle.side_a) * (s - triangle.side_b) * (s - triangle.side_c)
    )

    # calculate circumradius: abc/4S where S: area of the triangle
    circumscribe_r = (triangle.side_a * triangle.side_b * triangle.side_c) / (4 * area)

    # calculate inradius: S / s where S: area of the triangle; s: (a + b + c)/2
    inscribed_r = area / s

    print("\n---------------------------------------")
    print(f"[*] Strana a:\t{triangle.side_a}\tÚhel: {triangle.a_angle:.2f}")
    print(f"[*] Strana b:\t{triangle.side_b}\tÚhel: {triangle.b_angle:.2f}")
    print(f"[*] Strana c:\t{triangle.side_c}\tÚhel: {triangle.c_angle:.2f}\n")
    print(f"[*] Obvod:\t\t{circumference}")
    print(f"[*] Obsah:\t\t{area:.2f}")
    print(f"[*] Kruž. Opsaná:\t{circumscribe_r:.2f}")
    print(f"[*] Kruž. Vepsaná:\t{inscribed_r:.2f}")
    print("---------------------------------------")


def display_triangle_type(triangle: Triangle) -> None:
    """
    Determines and displays the type of triangle based on its side lengths and angles.
    """

    # determine triangle type based on side lengths
    if triangle.side_a == triangle.side_b == triangle.side_c:
        type_based_on_lengths = "Rovnostranný"
    elif (
        triangle.side_a == triangle.side_b
        or triangle.side_a == triangle.side_c
        or triangle.side_b == triangle.side_c
    ):
        type_based_on_lengths = "Rovnoramenný"
    else:
        type_based_on_lengths = "Různostranný"

    # determine triangle type based on angles
    if triangle.c_angle == 90 or triangle.b_angle == 90 or triangle.a_angle == 90:
        type_based_on_angles = "Pravoúhlý"
    elif triangle.c_angle > 90 or triangle.a_angle > 90 or triangle.b_angle > 90:
        type_based_on_angles = "Tupoúhlý"
    else:
        type_based_on_angles = "Ostroúhlý"

    print("\n---------------------------------------")
    print(f"[*] Typ trojúhelníka podle délek stran: {type_based_on_lengths}")
    print(f"[*] Typ trojúhelníka podle úhlů: {type_based_on_angles}")
    print("---------------------------------------")


def main():
    while True:
        while True:
            triangle = get_triangle_from_user()  # get triangle lengths from user

            if is_valid_triangle(triangle):  # validate the triangle
                calculate_triangle_angles(
                    triangle
                )  # calculate the angles of the triangle
                break

        # display properties and triangle type
        display_triangle_properties(triangle)
        display_triangle_type(triangle)

        print_title("\n[*] Chcete pokračovat? Y, X: ")
        continue_char = input("=> ")

        if continue_char.capitalize() == "Y":
            print()
            continue
        elif continue_char.capitalize() == "X":
            exit(0)
        else:
            print_error("ERROR! Invalid key input.")
            exit(1)


if __name__ == "__main__":
    os.system("clear")
    print_title("[*] 03 - Geometric Object Basics\n")

    main()
