import math


def insert_numbers(input_str):
    total = sum(map(float, input_str.split()))
    print("The result is: ", round(total, 2))
