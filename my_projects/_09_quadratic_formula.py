"""
* Vygenerujte náhodně rovnici na základě náhodně zvolených celých kořenů x1 a x2. Můžete rozšířit
  o možnost zadat počet generovaných rovnic, u každé pak uvést i řešení - vhodné jako procvičování
  pro mladší studenty.
** Vytvořte n náhodných kvadratických nerovnic s různými náhodnými znaménky (>, >=, =<, <).
   U nerovnic uveďte výsledek a zobrazte jej pomocí intervalů.
** Vykreslete graf kvadratické funkce podle zadaných koeficientů (matplotlib).
   Označte vrchol paraboly a kořeny, pokud existují.
"""

import os
import iridis
import cmath
from fractions import Fraction


class QuadraticEquation:
    """
    Represents a quadratic equation of the form:

    ax² + bx + c = 0, where 'a', 'b', and 'c' are coefficients.

    This class provides methods to solve the equation using the quadratic formula,
    calculate the number of real solutions, express the equation in string form,
    and return the factorized form of the quadratic equation.

    :param a: Coefficient of x² (must be a non-zero float).
    :param b: Coefficient of x.
    :param c: Constant term.

    :raises ValueError: If 'a' is equal to zero or any coefficient is not a float.
    """

    def __init__(self, a: float, b: float, c: float) -> None:
        """
        Initializes the quadratic equation with the given coefficients. It calculates
        the discriminant (b² - 4ac) immediately upon initialization to optimize
        further computations.

        :param a: Coefficient of x² (must be a non-zero float).
        :param b: Coefficient of x.
        :param c: Constant term.

        :raises ValueError: If 'a' is equal to zero or if any coefficient is not a float.
        """
        # validate input coefficients
        if not isinstance(a, float) or a == 0:
            raise ValueError("Koeficient 'a' musí být nenulové desetinné číslo.")
        if not isinstance(b, float):
            raise ValueError("Koeficient 'b' musí být desetinné číslo.")
        if not isinstance(c, float):
            raise ValueError("Koeficient 'c' musí být desetinné číslo.")

        self.a = a
        self.b = b
        self.c = c

        # calculate the discriminant (b² - 4ac) once at initialization
        self.discriminant = b**2 - 4 * a * c

    def count_real_solutions(self) -> int:
        """
        Determines the number of real solutions to the quadratic equation based on the
        discriminant value. A positive discriminant indicates two real solutions,
        zero discriminant indicates one real solution, and a negative discriminant indicates no real solutions.

        :return: The number of real solutions: 0, 1, or 2.
        """
        if self.discriminant < 0:
            return 0  # no real solutions
        elif self.discriminant == 0:
            return 1  # one real solution
        else:
            return 2  # two real solutions

    def solve(self) -> list:
        """
        Solves the quadratic equation using the quadratic formula:

        (-b ± √(b² - 4ac)) / 2a

        The method supports both real and complex solutions. It returns real roots
        when possible, and complex roots otherwise.

        :return: A list of roots (real or complex) of the quadratic equation.
        :raises ValueError: If there are no real solutions and complex solutions are not required.
        """
        solutions_count = self.count_real_solutions()

        # using cmath to handle complex solutions
        sqrt_discriminant = cmath.sqrt(self.discriminant)
        root1 = (-self.b + sqrt_discriminant) / (2 * self.a)
        root2 = (-self.b - sqrt_discriminant) / (2 * self.a)

        # based on the number of solutions, return the appropriate roots
        if solutions_count == 1:
            return [root1.real]
        elif solutions_count == 2:
            return [root1.real, root2.real]
        else:
            return [root1, root2]

    def factorized_form(self) -> str:
        """
        Returns the factorized form of the quadratic equation in the form:

        a(x - root1)(x - root2)

        :return: A string representing the factorized form of the equation.
        :raises ValueError: If the equation has complex roots or only one root.
        """
        solutions = self.solve()

        # if complex roots exist, factorization is not possible
        if any(isinstance(root, complex) for root in solutions):
            raise ValueError("Rozklad kvadratické rovnice s komplexními kořeny není možný.")

        if len(solutions) == 1:
            solutions.append(solutions[0])

        return f"{f'{self.__format_number(self.a)}' if self.a > 1 else ''}(x {'-' if solutions[0] > 0 else '+'} {self.__format_number(abs(solutions[0]))})(x {'-' if solutions[1] > 0 else '+'} {self.__format_number(abs(solutions[1]))})"

    def equation_string(self) -> str:
        """
        Returns the quadratic equation in its standard form as a string:

        ax² + bx + c = 0

        :return: The quadratic equation as a string.
        """
        return f"{f'-{self.__format_number(abs(self.a))}' if self.a < 0 else f'{self.__format_number(self.a)}'}x² {'-' if self.b < 0 else '+'} {self.__format_number(abs(self.b))}x {'-' if self.c < 0 else '+'} {self.__format_number(abs(self.c))}"

    def __format_number(self, number: float) -> str:
        """
        Helper method to format a number as either an integer or as a fraction if necessary.

        :param number: The number to be formatted.
        :return: The formatted number as a string.
        """
        # return as integer if the number is a whole number
        if number.is_integer():
            return f"{number:.0f}"

        # otherwise, return the number as a fraction
        fraction = Fraction(number).limit_denominator()
        return f"{fraction.numerator}/{fraction.denominator}"


##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("clear")
    iridis.print_rainbow("[*] - 09 Kvadratické rovnice\n")

    a = iridis.get_number_from_user(input_text="[*] Zadejte koeficient a: ", conditions=[lambda n: n != 0])
    b = iridis.get_number_from_user(input_text="[*] Zadejte koeficient b: ")
    c = iridis.get_number_from_user(input_text="[*] Zadejte koeficient c: ")

    equation = QuadraticEquation(a, b, c)

    real_solutions_count = equation.count_real_solutions()
    solutions = equation.solve()

    print("------------------------------------------------")

    iridis.print_title(f"[*] {equation.equation_string()} = 0\n")
    print(f"[*] Počet reálných řešení: {real_solutions_count}")
    print(f"[*] Řešení: {solutions}")

    try:
        print(f"[*] Rozklad: {equation.factorized_form()}")
    except ValueError as e:
        iridis.print_error(f"[*] Rozklad není možný: {e}")
