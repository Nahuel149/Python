import math

lenght = int(input('What is the lenght of the rectangle? '))
width = int(input('What is the width of the rectangle? '))

print('The area of the rectangle is: ', lenght * width)

radius = int(input('What radius for a circle? '))
result = (math.pi * radius ** 2)

print(f'The area of a circle is: {result:.2f}')

base = float(input('What is the base of the triangle? '))
height = float(input('What is the height of the triangle? '))

print('The area of a triangle is: ', 0.5 * base * height)