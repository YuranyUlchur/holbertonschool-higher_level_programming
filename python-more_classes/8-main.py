#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(1, 8)

try:
    print(my_rectangle_2 == Rectangle.bigger_or_equal(my_rectangle_1, "Rect"))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))