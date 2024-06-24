import math

def rectangle(print_result=True):
    lenght = int(input('What is the lenght of the rectangle? '))
    width = int(input('What is the width of the rectangle? '))
    area = lenght * width
    if print_result:
        print(f'The area of the rectangle is: {area}')
    return area

def circle(print_result=True):
    radius = int(input('Choose radius for a circle: '))
    area = (math.pi * radius ** 2)
    if print_result:
        print(f'The area of a circle is: {area:.2f}')
    return area

def triangle(print_result=True):
    base = float(input('What is the base of the triangle? '))
    height = float(input('What is the height of the triangle? '))
    area = 0.5 * base * height
    if print_result:
        print(f'The area of a triangle is: {area}')
    return area

def square_perimeter(print_result=True):
    side_lenght = int(input('Choose the side lenght of a square: '))
    perimeter = side_lenght * 4
    if print_result:
        print(f'The perimeter of a square is: {perimeter}')
    return perimeter

def circle_details(print_result=True):
    circumference = 2 * math.pi * circle(print_result=False) 
    if print_result:
        print(f'The circumference of a circle is: {circumference:.2f}')
    return circumference

def geometry():
    print('First Comparison')
    areas = "Circle" if circle(print_result=False) > square_perimeter(print_result=False) else "Square"
    print('Second Comparison')
    perimeters = 'Square' if square_perimeter(print_result=False) > circle_details(print_result=False) else 'Circle'
    print('Results:')
    print(f'The {areas} has a larger area.')
    print(f'The {perimeters} has a larger perimeter.')
    return areas, perimeters

geometry()