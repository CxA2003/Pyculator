import math


def calculate_circle_perimeter(radius):
    radius = int(radius)
    perimeter = 2 * math.pi * radius
    print("The perimeter is: ", round(perimeter, 2))
    return perimeter


def calculate_circle_area(radius):
    radius = int(radius)
    area = math.pi * pow(radius, 2)
    print("The area is: ", round(area, 2))
    return area


def calculate_circle_volume(radius):
    radius = int(radius)
    volume = (4 / 3) * math.pi * (radius**3)
    print("The volume of the sphere is:", round(volume, 2))
    return volume
