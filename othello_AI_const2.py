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
  for yp in range(0,8):
    for xp in range(0,8):
      sumv = 0
      if cboard[xp][yp] == 2*turn:
        rboard,rev = reverse(board,turn,xp,yp)
        #裏返した石の評価の総和を比較
        for y in range(0,8):
          for x in range(0,8):
            sumv += board_val[x][y] * rboard[x][y]
        #総和が暫定のものより大きければ更新
        if sumv > can:
          can = sumv
          cx = xp
          cy = yp
  return cx,cy
