from madison_axi.axi import *
from random import *
initialize()

def polygon(num_sides, length):
  pen_up()
  pen_down()
  for angle in range(1, num_sides + 1):
    move_forward(length)
    turn_left(360//num_sides)
  pen_up()

def line(x, y):
  pen_down()
  move_to(int(x),int(y))
  pen_up()

def nested_squares_centered1(increase, squares, x, y):
  pen_up()
  move_to(0,-200)
  for num in range(1, squares + 1):
    pen_up()
    move_to(x,y)
    pen_down()
    polygon(4, (increase*num))
    x -= increase//2
    y -= increase//2
    pen_up()

def nested_squares_centered2(increase, squares, x, y):
  pen_up()
  turn_right(18)
  move_to(x/2,y/2)
  turn_right(-36)
  for num in range(1, squares + 1):
    pen_up()
    move_to(x,y)
    pen_down()
    polygon(4, (increase*num))
    x -= increase//2
    y -= increase//2
    pen_up()

def nested_squares_centered3(increase, squares, x, y):
  pen_up()
  for num in range(1, squares + 1):
    pen_up()
    move_to(x,y)
    pen_down()
    polygon(4, (increase*num))
    x -= increase//2
    y -= increase//2
    pen_up()

# BEGIN DRAWING

pen_up()
turn_right(18)
nested_squares_centered1(28, 10, 84, 22)
pen_up()
turn_right(18)
nested_squares_centered2(23, 10, 306, 208)
pen_up()
nested_squares_centered3(18, 10, 118, 247)
pen_up()

input("Switch to new color, press enter to continue")

move_to(101,33)
line(324, 211)
line(126,255)
line(101,33)

input("Switch to new color, press enter to continue")

pen_up()
nested_squares_centered1(28, 10, -380, 22)
turn_right(18)
nested_squares_centered2(23, 10, -158, 208)
pen_up()
nested_squares_centered3(18, 10, -346, 247)
pen_up()

input("Switch to new color, press enter to continue")

move_to(-363,33)
line(-145, 211)
line(-337,255)
line(-363,33)
cleanup()
