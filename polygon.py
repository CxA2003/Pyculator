import math


def calculate_regular_polygon_area(input_str):
    num_sides, side_length = map(float, input_str.split())
    perimeter = num_sides * side_length
    apothem = side_length / (2 * math.tan(math.pi / num_sides))
    area = (perimeter * apothem) / 2
    print("The area is: ", round(area, 2))
    return area


def calculate_regular_polygon_perimeter(input_str):
    num_sides, side_length = map(float, input_str.split())
    perimeter = num_sides * side_length
    print("The perimeter is: ", round(perimeter, 2))


def calculate_regular_polygon_volume(input_str):
    num_sides, side_length, height = map(float, input_str.split())
    perimeter = num_sides * side_length
    apothem = side_length / (2 * math.tan(math.pi / num_sides))
    area = (perimeter * apothem) / 2
    volume = area * height
    print("The volume is: ", round(volume, 2))
    return volume
