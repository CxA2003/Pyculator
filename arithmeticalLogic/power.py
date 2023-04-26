import math
import numpy as np


def insert_numbers(input_str):
    numbers = np.array(list(map(float, input_str.split())))
    while len(numbers) > 1:
        if len(numbers) == 2:
            total = numbers[0] ** numbers[1]
            print("The result is: ", round(total, 2))
            break
        else:
            print("ERROR: Please, enter only 2 values")
            break
