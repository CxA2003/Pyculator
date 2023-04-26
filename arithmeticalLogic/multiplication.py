import math
import numpy as np


def insert_numbers(input_str):
    total = np.array(list(map(float, input_str.split())))
    biggest_number = total[0]
    total = total[1:]
    for i in range(len(total)):
        result = biggest_number * total[i]
        biggest_number = result
        i += 1
        print(result)
