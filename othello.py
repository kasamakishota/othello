# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import random
import copy
import time
import numpy as np
#from othello_AI_const1 import *
#from othello_AI_const2 import *
from othello_AI_const3 import *
#from othello_AI_const4 import *

board = 0
cboard = 0
turn = 0
screen = 0
gamemode = 0

#画面の初期設定
def othello_setting():
    global board, turn, screen, gamemode
    #ゲームモード（1:対人対戦)(2:CPU対戦）
    print "Please select mode 1 or 2 (1:human, 2:CPU)"
    gamemode = int(raw_input())
    #画面サイズ
    screen_size = (481,481)
    #screen_sizeの画面を作成
    screen = pygame.display.set_mode(screen_size)
    #タイトルバーの文字列
    pygame.display.set_caption("AI_Othello")
    #画面の背景
    screen.fill((0,255,0))
    #枠線の描写
    for line in range(0,481,60):
        pygame.draw.line(screen,(0,0,0),(0,line),(480,line))
        pygame.draw.line(screen,(0,0,0),(line,0),(line,480))
    #盤面の状況を表すリスト
    board = [[0 for i in range(8)] for j in range(8)]
    board[3][3] = 1
    board[3][4] = -1
    board[4][3] = -1
    board[4][4] = 1
    #順番を表すパラメータ
    turn = 1

#盤面の状態を取得して画面出力
def board_state(board,screen):
    for y in range(0,8):
        for x in range(0,8):
            #状態が-1ならば黒
            if board[x][y] == 1:
                pygame.draw.circle(screen,(0,0,0),(y*60+30,x*60+30),20)
            #状態が1ならば白
            if board[x][y] == -1:
                pygame.draw.circle(screen,(255,255,255),(y*60+30,x*60+30),20)

#どちらのターンかを左上に表示
def turn_display(turn,screen):
    if turn == 1:
        color = "B"
    else:
        color = "W"
    pygame.draw.rect(screen,(0,255,0),Rect(1,1,12,12))
    sysfont = pygame.font.SysFont(None,20)
    text = sysfont.render(color,False,(255,0,0))
    screen.blit(text,(1,1))

#石を裏返す
def reverse(board,turn,xp,yp):
    rev = 0
    rboard = [[0 for i in range(8)] for j in range(8)]
    rboard[xp][yp] = 10
    #縦ライン（↓）
    flag = 0
    count = 1
    for y in range(yp+1,8):
        if np.abs(board[xp][y]) != 1:
            break
        if board[xp][y] == turn and flag == 0:
            break
        if board[xp][y] == -turn:
            flag = 1
            count += 1
        if board[xp][y] == turn and flag == 1:
            for rev in range(1,count):
                rboard[xp][y-rev] = 10
            rev = 1
            break
    #縦ライン（↑）
    flag = 0
    count = 1
    for y in range(yp-1,-1,-1):
        if np.abs(board[xp][y]) != 1:
            break
        if board[xp][y] == turn and flag == 0:
            break
        if board[xp][y] == -turn:
            flag = 1
            count += 1
        if board[xp][y] == turn and flag == 1:
            for rev in range(1,count):
                rboard[xp][y+rev] = 10
            rev = 1
            break
    #横ライン（→）
    flag = 0
    count = 1
    for x in range(xp+1,8):
        if np.abs(board[x][yp]) != 1:
            break
        if board[x][yp] == turn and flag == 0:
            break
        if board[x][yp] == -turn:
            flag = 1
            count += 1
        if board[x][yp] == turn and flag == 1:
            for rev in range(1,count):
                rboard[x-rev][yp] = 10
            rev = 1
            break
    #横ライン（←）
    flag = 0
    count = 1
    for x in range(xp-1,-1,-1):
        if np.abs(board[x][yp]) != 1:
            break
        if board[x][yp] == turn and flag == 0:
            break
        if board[x][yp] == -turn:
            flag = 1
            count += 1
        if board[x][yp] == turn and flag == 1:
            for rev in range(1,count):
                rboard[x+rev][yp] = 10
            rev = 1
            break
    #斜めライン（↘）
    flag = 0
    count = 1
    mxy = max(xp,yp)
    for i in range(mxy+1,8):
        i -= mxy 
        if np.abs(board[xp+i][yp+i]) != 1:
            break
        if board[xp+i][yp+i] == turn and flag == 0:
            break
        if board[xp+i][yp+i] == -turn:
            flag = 1
            count += 1
        if board[xp+i][yp+i] == turn and flag == 1:
            for rev in range(1,count):
                rboard[xp+i-rev][yp+i-rev] = 10
            rev = 1
            break
    #斜めライン（↖）
    flag = 0
    count = 1
    mxy = min(xp,yp)
    for i in range(mxy-1,-1,-1):
        i -= mxy
        if np.abs(board[xp+i][yp+i]) != 1:
            break
        if board[xp+i][yp+i] == turn and flag == 0:
            break
        if board[xp+i][yp+i] == -turn:
            flag = 1
            count += 1
        if board[xp+i][yp+i] == turn and flag == 1:
            for rev in range(1,count):
                rboard[xp+i+rev][yp+i+rev] = 10
            rev = 1
            break
    #斜めライン（↗）
    flag = 0
    count = 1
    mxy = max(xp,7-yp)
    for i in range(mxy+1,8):
        i -= mxy 
        if np.abs(board[xp+i][yp-i]) != 1:
            break
        if board[xp+i][yp-i] == turn and flag == 0:
            break
        if board[xp+i][yp-i] == -turn:
            flag = 1
            count += 1
        if board[xp+i][yp-i] == turn and flag == 1:
            for rev in range(1,count):
                rboard[xp+i-rev][yp-i+rev] = 10
            rev = 1
            break
    #斜めライン（↙）
    flag = 0
    count = 1
    mxy = max(7-xp,yp)
    for i in range(mxy+1,8):
        i -= mxy 
        if np.abs(board[xp-i][yp+i]) != 1:
            break
        if board[xp-i][yp+i] == turn and flag == 0:
            break
        if board[xp-i][yp+i] == -turn:
            flag = 1
            count += 1
        if board[xp-i][yp+i] == turn and flag == 1:
            for rev in range(1,count):
                rboard[xp-i+rev][yp+i-rev] = 10
            rev = 1
            break
    return rboard,rev

#ユーザが置ける場所を表示
def canput_display(board,turn):
    skip = 0
    cboard = copy.deepcopy(board)
    for yp in range(0,8):
        for xp in range(0,8):
            rboard,rev = reverse(cboard,turn,xp,yp)
            if rev == 1 and cboard[xp][yp] == 0:
                skip = 1
                cboard[xp][yp] = 2*turn
    return cboard,skip

#ゲーム終了時に盤面の石の数を数える
def result(board,screen):
    white = 0
    black = 0
    xplace = 220
    yplace = 50
    for y in range(0,8):
        for x in range(0,8):
            #状態が1ならば白
            if board[x][y] == 1:
                black += 1
            #状態が-1ならば黒
            if board[x][y] == -1:
                white += 1
    if white > black:
        result ="White Win(W"+str(white)+":B"+str(black)+")"
    if white < black:
        result ="Black Win(W"+str(white)+":B"+str(black)+")"
    if white == black:
        place = 100
        result ="Draw(W"+str(white)+":B"+str(black)+")"
    sysfont = pygame.font.SysFont(None,60)
    text = sysfont.render(result,False,(255,0,0))
    screen.blit(text,(yplace,xplace))

#ユーザインターフェース
def othello_UI(event):
    global board, cboard, turn
    #クリック時のマウスの座標を取得
    yp,xp = event.pos
    #480PXで8マスずつなので60で割るとクリックしたマスの配列が特定できる
    xp = xp/60
    yp = yp/60
    #ユーザがそのマスに石を置けるか確認（phase=1）（rev=0or1）
    if cboard[xp][yp] == 2*turn:
        board[xp][yp] = turn
        #実際に石を置いて裏返す（phase=2）（rev=0or1）
        rboard,rev = reverse(board,turn,xp,yp)
        for x in range(0,8):
            for y in range(0,8):
                if rboard[x][y] == 10:
                    board[x][y] = turn
        turn *= -1

#AIインターフェース
def othello_AI():
    global board, turn
    cx,cy = othello_AI_const(board,turn)
    board[cx][cy] = turn
    rboard,rev = reverse(board,turn,cx,cy)
    for x in range(0,8):
        for y in range(0,8):
            if rboard[x][y] == 10:
                board[x][y] = turn

#ゲームのループプログラム
def othello_game():
    global board, cboard, turn
    end = 0
    AIturn = random.randrange(-1,2,2)
    #ゲームループ
    while True:
        #AIのターン
        if turn == AIturn and end == 0 and gamemode == 2:
            time.sleep(0.7)
            othello_AI()
            turn *= -1
            #ユーザが置けるマスを表示
            cboard,skip = canput_display(board,turn)
            if skip == 0:
                turn *= -1
                cboard,skip = canput_display(board,turn)
                if skip == 0:
                    end = 1
        #イベント処理
        for event in pygame.event.get():
            #終了イベント
            if event.type == QUIT:
                sys.exit()
            #クリックしたマスに石を設置
            if event.type == MOUSEBUTTONDOWN:
                othello_UI(event)
                for out in board:
                    print out
                print ""
                #ユーザが置けるマスを表示
                cboard,skip = canput_display(board,turn)
                if skip == 0:
                    turn *= -1
                    cboard,skip = canput_display(board,turn)
                    if skip == 0:
                        end = 1 
                for out in cboard:
                    print out
                print ""
                print "******************************************\n"
        #盤面の状態を取得して画面表示
        board_state(board,screen)
        #どちらのターンか表示
        turn_display(turn,screen)
        cboard,skip = canput_display(board,turn)
        if end == 1:
            result(board,screen)
        #画面を更新
        pygame.display.update()
        #ゲーム終了時に盤面の石の数を数える
        if end == 1:
            print "GameFinish?(y/n)"
            fin = raw_input()
            if fin == "y":
                sys.exit()
            if fin == "n":
                end = 0
                for y in range(0,8):
                    for x in range(0,8):
                        board[x][y] = 0
                turn = 1
                main()

#メインプログラム
def main():
    #Pygameを初期化
    pygame.init()
    #画面表示、変数の初期設定
    othello_setting()
    #ゲームのループ
    othello_game()

#動作プログラム
if __name__ == '__main__':
    main()
