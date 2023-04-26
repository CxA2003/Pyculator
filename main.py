import geomtricalLogic.polygon as polygon
import geomtricalLogic.circle as circle
import arithmeticalLogic.sum as sum
import arithmeticalLogic.substraction as substraction
import arithmeticalLogic.division as division
import arithmeticalLogic.multiplication as multiplication
import arithmeticalLogic.squareRoot as squareRoot
import arithmeticalLogic.power as power
import arithmeticalLogic.logarithm as logarithm


def main():
    print(
        """
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    Welcome to CxA2003's Pyculator!
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    """
    )
    option1 = input(
        """
    Please, choose the operation type you'd like from one of the options below:

    1. Geometrical
    2. Arithmetical

    """
    )
    if option1 == "1":
        print(
            """
        xxxxxxxxxxxxxxxx
        GEOMETRICAL MENU
        xxxxxxxxxxxxxxxx

        """
        )
        option2 = input(
            """
        Please, choose the type of figure you'd like
        
        1. Regular Polygon
        2. Circle

        """
        )
        if option2 == "1":
            print(
                """
            xxxxxxxxxxxxxxx
            REGULAR POLYGON
            xxxxxxxxxxxxxxx

            """
            )
            option3 = input(
                """
            Select the value you'd like to find:
            1. Area
            2. Perimeter
            3. Volume

            """
            )
            if option3 == "1":
                print(
                    """
                xxxx
                AREA
                xxxx
                
                """
                )
                polygon.calculate_regular_polygon_area(
                    input(
                        "Please, enter the number of sides, and the length of them in order, separated by a space: \n"
                    )
                )
            elif option3 == "2":
                print(
                    """
                xxxxxxxxx
                PERIMETER
                xxxxxxxxx
                
                """
                )
                polygon.calculate_regular_polygon_perimeter(
                    input(
                        "Please, enter the number of sides, and the length of them in order, separated by a space: \n"
                    )
                )
            elif option3 == "3":
                print(
                    """
                xxxxxx
                VOLUME
                xxxxxx
                
                """
                )
                polygon.calculate_regular_polygon_volume(
                    input(
                        "Please, enter the number of sides, the length of them, and it's height in order, separated by a space: \n"
                    )
                )
            else:
                print(
                    """
                Option not valid
                Bye Bye!
                """
                )
        elif option2 == "2":
            print(
                """
            xxxxxx
            CIRCLE
            xxxxxx

            """
            )
            option3 = input(
                """
            Select the value you'd like to find:
            1. Area
            2. Perimeter
            3. Volume

            """
            )
            if option3 == "1":
                print(
                    """
                xxxx
                AREA
                xxxx

                """
                )
                circle.calculate_circle_area(
                    input("Please, enter the radius of the circle: \n")
                )
            elif option3 == "2":
                print(
                    """
                xxxxxxxxx
                PERIMETER
                xxxxxxxxx
                
                """
                )
                circle.calculate_circle_perimeter(
                    input("Please, enter the radius of the circle: \n")
                )
            elif option3 == "3":
                print(
                    """
                xxxxxx
                VOLUME
                xxxxxx
                
                """
                )
                circle.calculate_circle_volume(
                    input("Please, enter the radius of the sphere: \n")
                )
            else:
                print(
                    """
                Option not valid
                Bye Bye!
                """
                )
        else:
            print(
                """
            Option not valid
            Bye Bye!
            """
            )
    elif option1 == "2":
        print(
            """
        xxxxxxxxxxxxxxxxx
        ARITHMETICAL MENU
        xxxxxxxxxxxxxxxxx

        """
        )
        option2 = input(
            """
        Please, select one of the equations available below

        1. Sum
        2. Subtraction
        3. Division
        4. Multiplication
        5. Square Root
        6. Power
        7. Logarithm

        """
        )
        if option2 == "1":
            print(
                """
            xxx
            SUM
            xxx

            """
            )
            sum.insert_numbers(
                input(
                    "Please, enter the number you'd like to sum separated by a space: \n"
                )
            )
        elif option2 == "2":
            print(
                """
            xxxxxxxxxxx
            SUBTRACTION
            xxxxxxxxxxx

            The highest number will be the one substracted by the rest
            """
            )
            substraction.insert_numbers(
                input(
                    "Please, enter the number you'd like to substract separated by a space: \n"
                )
            )
        elif option2 == "3":
            print(
                """
            xxxxxxxx
            DIVISION
            xxxxxxxx

            """
            )
            division.insert_numbers(
                input(
                    "Please, enter the number you'd like to divide, and the its divisor: \n"
                )
            )
        elif option2 == "4":
            print(
                """
            xxxxxxxxxxxxxx
            MULTIPLICATION
            xxxxxxxxxxxxxx

            """
            )
            multiplication.insert_numbers(
                input("Please, enter the numbers you'd like to multiply: \n")
            )
        elif option2 == "5":
            print(
                """
            xxxxxxxxxxx
            SQUARE ROOT
            xxxxxxxxxxx

            """
            )
            squareRoot.insert_numbers(
                input(
                    "Please, enter the numbers you'd like to have the square root from: \n"
                )
            )
        elif option2 == "6":
            print(
                """
            xxxxx
            POWER
            xxxxx

            """
            )
            power.insert_numbers(
                input("Please, enter the numbers you'd like to power: \n")
            )
        elif option2 == "7":
            print(
                """
            xxxxxxxxx
            LOGARITHM
            xxxxxxxxx

            """
            )
            squareRoot.insert_numbers(
                input(
                    "Please, enter the numbers you'd like to get the logarithm from: \n"
                )
            )
        else:
            print(
                """
            Option not valid
            Bye Bye!
            """
            )


if __name__ == "__main__":
    main()
