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

def nested_squares_centered1(increase, squares):
  pen_up()
  x = 0
  y = 0
  move_to(0,-200)
  for num in range(1, squares + 1):
    pen_up()
    move_to(x,y)
    pen_down()
    polygon(4, (increase*num))
    x -= increase//2
    y -= increase//2
    pen_up()

def nested_squares_centered2(increase, squares):
  pen_up()
  x = 232
  y = 204
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

def nested_squares_centered3(increase, squares):
  pen_up()
  x = 24
  y = 248
  for num in range(1, squares + 1):
    pen_up()
    move_to(x,y)
    pen_down()
    polygon(4, (increase*num))
    x -= increase//2
    y -= increase//2
    pen_up()
    
pen_up()
turn_right(18)
nested_squares_centered1(30, 10)
pen_up()
turn_right(18)
nested_squares_centered2(25, 10)
pen_up()
nested_squares_centered3(20, 10)
pen_up()
move_to(17,11)
line(250, 207)
line(32,256)
line(17,11)
cleanup()
