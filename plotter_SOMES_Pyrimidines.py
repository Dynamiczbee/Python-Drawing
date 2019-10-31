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
nested_squares_centered1(30, 10, 90, 0)
pen_up()
turn_right(18)
nested_squares_centered2(25, 10, 322, 204)
pen_up()
nested_squares_centered3(20, 10, 114, 248)
pen_up()

input("Switch to new color, press enter to continue")

move_to(107,11)
line(340, 207)
line(122,256)
line(107,11)

input("Switch to new color, press enter to continue")

pen_up()
nested_squares_centered1(30, 10, -390, 0)
turn_right(18)
nested_squares_centered2(25, 10, -158, 204)
pen_up()
nested_squares_centered3(20, 10, -366, 248)
pen_up()

input("Switch to new color, press enter to continue")

move_to(-373,11)
line(-140, 207)
line(-358,256)
line(-373,11)
cleanup()
