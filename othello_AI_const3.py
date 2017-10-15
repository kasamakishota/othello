# -*- coding: utf-8 -*-
from othello import *

def othello_AI_const(board,turn):
	board_val = ([100,-20,  3,  5,  5,  3,-20,100],
							 [-20,-30, -3, -3, -3, -3,-30,-20],
							 [  3, -3,  0, -1, -1,  0, -3,  3],
							 [  5, -3, -1, -1, -1, -1, -3,  5],
							 [  5, -3, -1, -1, -1, -1, -3,  5],
							 [  3, -3,  0, -1, -1,  0, -3,  3],
							 [-20,-30, -3, -3, -3, -3,-30,-20],
							 [100,-20,  3,  5,  5,  3,-20,100])

	#横の行の評価を変化
	for x in range(1,7):
		#端の辺において、相手の石の隣には置かない
		if board[x][0] == -turn and board[x-1][0] == 0:
			board_val[x-1][0] -= 15
		if board[x][0] == -turn and board[x+1][0] == 0:
			board_val[x+1][0] -= 15
		if board[x][7] == -turn and board[x-1][7] == 0:
			board_val[x-1][7] -= 15
		if board[x][7] == -turn and board[x+1][7] == 0:
			board_val[x+1][7] -= 15
		#端の辺において、自分の石の隣が空いている時、空いているマスの隣には置かない
		if board[x-1][0] == turn and board[x][0] == 0 and board[x+1][0] == 0:
			board_val[x+1][0] -= 15
		if board[x-1][7] == turn and board[x][7] == 0 and board[x+1][7] == 0:
			board_val[x+1][7] -= 15
		#端の辺において、相手の石と石の間が空いていれば置く
		if board[x][0] == 0 and board[x-1][0] == -turn and board[x+1][0] == -turn:
			board_val[x][0] = 50
		if board[x][7] == 0 and board[x-1][7] == -turn and board[x+1][7] == -turn:
			board_val[x][7] = 50
		#端の辺において、自分の石の隣に相手の石があれば取る
		if board[x][0] == -turn and board[x+1][0] == 0:
			for i in range(1,x):
				if board[x-i][0] == turn:
					board_val[x+1][0] = 50
					break
				if board[x-i][0] == 0:
					break
		if board[x][7] == -turn and board[x+1][7] == 0:
			for i in range(1,x):
				if board[x-i][7] == turn:
					board_val[x+1][7] = 50
					break
				if board[x-i][7] == 0:
					break
		if board[x][0] == -turn and board[x-1][0] == 0:
			for i in range(1,x):
				if board[x+i][0] == turn:
					board_val[x-1][0] = 50
					break
				if board[x+i][0] == 0:
					break
		if board[x][7] == -turn and board[x-1][7] == 0:
			for i in range(1,x):
				if board[x+i][7] == turn:
					board_val[x-1][7] = 50
					break
				if board[x+i][7] == 0:
					break
	#横の行の時と同様に縦の列の評価を変化
	for y in range(1,7):
		if board[0][y] == -turn and board[0][y-1] == 0:
			board_val[0][y-1] -= 15
		if board[0][y] == -turn and board[0][y+1] == 0:
			board_val[0][y+1] -= 15
		if board[7][y] == -turn and board[7][y-1] == 0:
			board_val[7][y-1] -= 15
		if board[7][y] == -turn and board[7][y+1] == 0:
			board_val[7][y+1] -= 15
		if board[0][y-1] == turn and board[0][y] == 0 and board[0][y+1] == 0:
			board_val[0][y+1] -= 15
		if board[7][y-1] == turn and board[7][y] == 0 and board[7][y+1] == 0:
			board_val[7][y+1] -= 15
		if board[0][y] == 0 and board[0][y-1] == -turn and board[0][y+1] == -turn:
			board_val[0][y] = 50
		if board[7][y] == 0 and board[7][y-1] == -turn and board[7][y+1] == -turn:
			board_val[7][y] = 50
		if board[0][y] == -turn and board[0][y+1] == 0:
			for i in range(1,y):
				if board[0][y-i] == turn:
					board_val[0][y+1] = 50
					break
				if board[0][y-i] == 0:
					break
		if board[7][y] == -turn and board[7][y+1] == 0:
			for i in range(1,y):
				if board[7][y-i] == turn:
					board_val[7][y+1] = 50
					break
				if board[7][y-i] == 0:
					break
		if board[0][y] == -turn and board[0][y-1] == 0:
			for i in range(1,y):
				if board[0][y+i] == turn:
					board_val[0][y-1] = 50
					break
				if board[0][y+i] == 0:
					break
		if board[7][y] == -turn and board[7][y-1] == 0:
			for i in range(1,y):
				if board[7][y+i] == turn:
					board_val[7][y-1] = 50
					break
				if board[7][y+i] == 0:
					break
	#角に自分の石があればその周辺に置く
	if board[0][0] == turn:
		if board[0][1] == 0:
			board_val[0][1] = 40
		if board[1][0] == 0:
			board_val[1][0] = 40
		if board[1][1] == 0:
			board_val[1][1] = 0
	if board[0][7] == turn:
		if board[0][6] == 0:
			board_val[0][6] = 40
		if board[1][7] == 0:
			board_val[1][7] = 40
		if board[1][6] == 0:
			board_val[1][6] = 0
	if board[7][0] == turn:
		if board[6][0] == 0:
			board_val[6][0] = 40
		if board[7][1] == 0:
			board_val[7][1] = 40
		if board[6][1] == 0:
			board_val[6][1] = 0
	if board[7][7] == turn:
		if board[6][7] == 0:
			board_val[6][7] = 40
		if board[7][6] == 0:
			board_val[7][6] = 40
		if board[6][6] == 0:
			board_val[6][6] = 0

	for line in board_val:
		print line
	print ""

	cboard,skip = canput_display(board,turn)
	can = -1000
	cx = 0
	cy = 0
	max_val = -1000
	for yp in range(0,8):
		for xp in range(0,8):
			if cboard[xp][yp] == 2*turn:
				sumv = 0
				rboard,rev = reverse(board,turn,xp,yp)
				#裏返した石の評価の総和を比較
				for y in range(0,8):
					for x in range(0,8):
						sumv += board_val[x][y] * rboard[x][y]
				if sumv > can:
					can = sumv
					cx = xp
					cy = yp
	return cx,cy
