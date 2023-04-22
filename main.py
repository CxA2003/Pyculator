def main():
    print("""
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    Welcome to CxA2003's Pyculator!
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    """)
    option1 = input("""
    Please, choose the operation type you'd like from one of the options below:

    1. Geometrical
    2. Arithmetical

    """)
    if (option1 == '1'):
        print("""
        xxxxxxxxxxxxxxxx
        GEOMETRICAL MENU
        xxxxxxxxxxxxxxxx

        """)
        option2 = input("""
        Please, choose the type of figure you'd like
        
        1. Regular Polygon
        3. Circle

        """)
        if (option2 == '1'):
            print("""
            xxxxxxxxxxxxxxx
            REGULAR POLYGON
            xxxxxxxxxxxxxxx

            """)
            option3 = input("""
            Select the value you'd like to find:
            1. Area
            2. Perimeter
            3. Volume

            """)
            if (option3 == '1'):
                print("""
                xxxx
                AREA
                xxxx

                """)
                #Area formula
            elif (option3 == '2'):
                print("""
                xxxxxxxxx
                PERIMETER
                xxxxxxxxx
                
                """)
                #Perimeter formula
            elif (option3 == '3'):
                print("""
                xxxxxx
                VOLUME
                xxxxxx
                
                """)
                #Volume Formula
            else:
                print("""
                Option not valid
                Bye Bye!
                """)
        elif (option2 == '2'):
            print("""
            xxxxxx
            CIRCLE
            xxxxxx

            """)
            option3 = input("""
            Select the value you'd like to find:
            1. Area
            2. Perimeter
            3. Volume

            """)
            if (option3 == '1'):
                print("""
                xxxx
                AREA
                xxxx

                """)
                #Area formula
            elif (option3 == '2'):
                print("""
                xxxxxxxxx
                PERIMETER
                xxxxxxxxx
                
                """)
                #Perimeter formula
            elif (option3 == '3'):
                print("""
                xxxxxx
                VOLUME
                xxxxxx
                
                """)
                #Volume Formula
            else:
                print("""
                Option not valid
                Bye Bye!
                """)
        else:
            print("""
            Option not valid
            Bye Bye!
            """)
    elif (option1 == '2'):
        print("""
        xxxxxxxxxxxxxxxxx
        ARITHMETICAL MENU
        xxxxxxxxxxxxxxxxx

        """)
        option2 = input("""
        Please, select one of the equations available below

        1. Sum
        2. Subtraction
        3. Division
        4. Multiplication
        5. Square Root
        6. Power
        7. Logarithm

        """)
        if (option2 == '1'):
            print("""
            xxx
            SUM
            xxx

            """)
            numbers = []
            numbers = input("""
            Please enter the numbers you'd like to sum separated by a ',' 
            
            """)
            #Sum Operation
        elif (option2 == '2'):
            print("""
            xxxxxxxxxxx
            SUBTRACTION
            xxxxxxxxxxx

            """)
            numbers = []
            numbers = input(
                """Please enter the numbers you'd like to Subtract separated by a ',' 
                
                """)
            #Subtraction Operation
        elif (option2 == '3'):
            print("""
            xxxxxxxx
            DIVISION
            xxxxxxxx

            """)
            numbers = []
            numbers = input(
                """Please enter the numbers you'd like to Divide separated by a ',' 
                
                """)
            #Division Operation
        elif (option2 == '4'):
            print("""
            xxxxxxxxxxxxxx
            MULTIPLICATION
            xxxxxxxxxxxxxx

            """)
            numbers = []
            numbers = input(
                """Please enter the numbers you'd like to Multiply separated by a ',' 
                
                """)
            #Multiplication Operation
        elif (option2 == '5'):
            print("""
            xxxxxxxxxxx
            SQUARE ROOT
            xxxxxxxxxxx

            """)
            number = input(
                """Please enter the number you'd like to get the square root from
                
                """)
            #SquareRoot Operation
        elif (option2 == '6'):
            print("""
            xxxxx
            POWER
            xxxxx

            """)
            number = input(
                """Please enter the numbers you want to get the power from (order = base, power)
                
                """)
            #SquareRoot Operation
        elif (option2 == '7'):
            print("""
            xxxxxxxxx
            LOGARITHM
            xxxxxxxxx

            """)
            number = input(
                """Please enter the base and argument you want to use (order = base, argument)
                
                """)
            #SquareRoot Operation
        else:
            print("""
            Option not valid
            Bye Bye!
            """)


if __name__ == '__main__':
    main()