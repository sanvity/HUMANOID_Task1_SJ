import pygame
import numpy as np
import sys 
import math

##N=4 ##CONNECT4
#t=N-1
ROW=6
COLUMN=7

def createboard():
    board=np.zeros((ROW,COLUMN))
    return board

def play_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_position(board,col):
    board[ROW-1][col]==0  
    return True

def next_openrow(board,col):
    for r in range((ROW)):
        if board[r][col]==0:
            return r

def print_board(board):
   print(np.flip(board,0))

def winning_move(board,piece):
    ## horizontal win
     for c in range(COLUMN-3):
        for r in range(ROW):
            if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece :
                return True
    ## vertical win
     for c in range(COLUMN):
        for r in range(ROW-3):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece :
                return True
    ## positive diagonal 
     for c in range(COLUMN-3):
        for r in range(ROW-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece :
                return True
    ## negative diagonal 
     for c in range(3,COLUMN+1):
        for r in range(ROW-3):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece :
                return True
       
    





board=createboard()
print_board(board)
game_over= False
turn=0

while not game_over:
    if turn==0:
        print('Player 1 select(0-6)',end='')
        col= int(input())  #player1
        
       # col=int(input("Player 1 select(0-7): "))

        if is_valid_position(board,col):
            row = next_openrow(board,col)
            play_piece(board,row,col,1)  
            print_board(board)     

            if winning_move(board,1):
                print("PLAYER 1 WINS!!!")
                game_over=True





    else:        #player2
         print('Player 2 select(0-6)',end='')
         col= int(input())
         
         if is_valid_position(board,col):
            row = next_openrow(board,col)
            play_piece(board,row,col,2)
            print_board(board)     

            if winning_move(board,2):
                print("PLAYER 2 WINS!!!")
                game_over=True


   
    turn+=1
    turn=turn%2    
    
