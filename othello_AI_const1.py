# -*- coding: utf-8 -*-
from othello import *
import numpy as np

def othello_AI_const(board,turn):
  board_val = ([ 30,-12,  0, -1, -1,  0,-12, 30],
               [-12,-15, -3, -3, -3, -3,-15,-12],
               [  0, -3,  0, -1, -1,  0, -3,  0],
               [ -1, -3, -1, -1, -1, -1, -3, -1],
               [ -1, -3, -1, -1, -1, -1, -3, -1],
               [  0, -3,  0, -1, -1,  0, -3,  0],
               [-12,-15, -3, -3, -3, -3,-15,-12],
               [ 30,-12,  0, -1, -1,  0,-12, 30])

  cboard,skip = canput_display(board,turn)
  can = -1000
  cx = 0
  cy = 0
  for y in range(0,8):
    for x in range(0,8):
      if cboard[x][y] == 2*turn:
        if board_val[x][y] > can:
          can = board_val[x][y]
          cx = x
          cy = y
  return cx,cy
