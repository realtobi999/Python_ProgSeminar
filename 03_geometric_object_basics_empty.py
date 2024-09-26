from dataclasses import dataclass
import math


@dataclass
class Triangle:
    # lengths of the sides
    hypotenuse: float
    ordinate_1: float
    ordinate_2: float

    # angles (in degrees)
    hypotenuse_angle: float = 0.00
    ordinate_1_angle: float = 0.00
    ordinate_2_angle: float = 0.00


def get_triangle_from_user() -> Triangle:
    """
    Prompts the user to input three sides of a triangle, validates the input,
    and returns the sides as a Triangle object with the longest side as the hypotenuse.

    Returns:
        Triangle: A Triangle object with sorted side lengths (hypotenuse, ordinate_1, ordinate_2).
    """

    triangle_sides = []

    while True:
        try:
            triangle_sides.append(float(input("[*] Zadej první stranu: ")))
            triangle_sides.append(float(input("[*] Zadej druhou stranu: ")))
            triangle_sides.append(float(input("[*] Zadej třetí stranu: ")))

            break
        except ValueError:
            print("ERROR! Please enter a valid number")

            triangle_sides.clear()

    triangle_sides.sort(reverse=True)

    return Triangle(
        hypotenuse=triangle_sides[0],
        ordinate_1=triangle_sides[1],
        ordinate_2=triangle_sides[2],
    )


def is_valid_triangle(triangle: Triangle) -> bool:
    """
    Checks if the given triangle satisfies the triangle inequality theorem,
    ensuring it can be formed with the provided side lengths.
    Additionally, it checks if the sum of the triangle's angles equals 180 degrees.

    Returns:
        bool: True if the triangle is valid, False otherwise (with an error message).
    """

    if (triangle.ordinate_1 + triangle.ordinate_2 <= triangle.hypotenuse
            or triangle.ordinate_1 + triangle.hypotenuse <= triangle.ordinate_2
            or triangle.ordinate_2 + triangle.hypotenuse <= triangle.ordinate_1):
        print("ERROR! Not a valid triangle due to side lengths.")
        return False

    total_angle_sum = triangle.hypotenuse_angle + triangle.ordinate_1_angle + triangle.ordinate_2_angle
    if round(total_angle_sum) != 180:  # rounding to avoid floating-point precision issues
        print(f"ERROR! Not a valid triangle due to angles: total is {total_angle_sum}° instead of 180°.")
        return False

    return True


def calculate_triangle_angles(triangle: Triangle) -> Triangle:
    """
    Calculates the angles of a triangle based on the side lengths using trigonometric functions.

    Returns:
        Triangle: The Triangle object with updated angles (ordinate_1_angle, ordinate_2_angle, hypotenuse_angle).
    """

    triangle.ordinate_1_angle = math.degrees(math.asin(triangle.ordinate_2 / triangle.hypotenuse))
    triangle.ordinate_2_angle = math.degrees(math.asin(triangle.ordinate_1 / triangle.hypotenuse))
    triangle.hypotenuse_angle = 180 - (triangle.ordinate_1_angle + triangle.ordinate_2_angle)

    return triangle


def display_triangle_properties(triangle: Triangle) -> None:
    """
    Calculates circumference, area, circumradius and inradius of the triangle.
    """

    circumference = triangle.hypotenuse + triangle.ordinate_1 + triangle.ordinate_2

    # calculate semi-perimeter
    s = circumference / 2

    # calculate area: √s(s−a)(s−b)(s−c) where s: (a + b + c)/2
    area = math.sqrt(s * (s - triangle.ordinate_1) *
                     (s - triangle.ordinate_2) * (s - triangle.hypotenuse))

    # calculate circumradius: abc/4S where S: area of the triangle
    circumscribe_r = (triangle.ordinate_1 *
                      triangle.ordinate_2 * triangle.hypotenuse) / (4 * area)

    # calculate inradius: S / s where S: area of the triangle; s: (a + b + c)/2
    inscribed_r = area / s

    print("\n---------------------------------------")
    print(f"[*] Odvěsna 1:\t{triangle.ordinate_1}\tÚhel: {triangle.ordinate_1_angle:.2f}")
    print(f"[*] Odvěsna 2:\t{triangle.ordinate_2}\tÚhel: {triangle.ordinate_2_angle:.2f}")
    print(f"[*] Hypotenuse:\t{triangle.hypotenuse}\tÚhel: {triangle.hypotenuse_angle:.2f}\n")
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
    if triangle.ordinate_1 == triangle.ordinate_2 == triangle.hypotenuse:
        type_based_on_lengths = "Rovnostranný"
    elif triangle.ordinate_1 == triangle.ordinate_2 or triangle.ordinate_1 == triangle.hypotenuse or triangle.ordinate_2 == triangle.hypotenuse:
        type_based_on_lengths = "Rovnoramenný"
    else:
        type_based_on_lengths = "Různostranný"

    # determine triangle type based on angles
    if triangle.hypotenuse_angle == 90:
        type_based_on_angles = "Pravoúhlý"
    elif triangle.hypotenuse_angle > 90 or triangle.ordinate_1_angle > 90 or triangle.ordinate_2_angle > 90:
        type_based_on_angles = "Tupoúhlý"
    else:
        type_based_on_angles = "Ostroúhlý"

    print("\n---------------------------------------")
    print(f"[*] Typ trojúhelníka podle délek stran: {type_based_on_lengths}")
    print(f"[*] Typ trojúhelníka podle úhlů: {type_based_on_angles}")
    print("---------------------------------------")


def main():
    while True:
        triangle = get_triangle_from_user()  # get triangle lengths from user
        calculate_triangle_angles(
            triangle)  # calculate the angles of the triangle

        if is_valid_triangle(triangle):  # validate the triangle
            break

    # display properties and triangle type
    display_triangle_properties(triangle)
    display_triangle_type(triangle)


if __name__ == "__main__":
    main()
