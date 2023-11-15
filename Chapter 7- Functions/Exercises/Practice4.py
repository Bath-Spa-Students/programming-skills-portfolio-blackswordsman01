# Calculating the area of a circle
import math

def calculate_circle_area(radius):
    """
    Calculates the area of a circle given its radius.

    Parameters:
    - radius (float): The radius of the circle.

    Returns:
    - float: The area of the circle.
    """
    area = math.pi * radius**2
    return area

radius = float(input("Enter the radius of the circle: "))
area_of_circle = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is: {area_of_circle:.2f}")
