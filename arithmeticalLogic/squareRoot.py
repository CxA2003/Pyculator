import math
import numpy as np


def insert_numbers(input_str):
    numbers = np.array(list(map(float, input_str.split())))
    for i in range(len(numbers)):
        result = math.sqrt(numbers[i])
        i += 1
        print("The result is: ", round(result, 2))
