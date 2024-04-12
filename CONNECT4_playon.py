import pygame
import numpy as np
import sys 
import math

BLUE=(0,0,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)

ROW=6
COLUMN=7

def createboard():
    board=np.zeros((ROW,COLUMN))
    return board

def play_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_position(board,col):
    return board[ROW-1][col] == 0

def next_openrow(board,col):
    for r in range(ROW):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board,0))

def winning_move(board,piece):
    for c in range(COLUMN-3):
        for r in range(ROW):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    for c in range(COLUMN):
        for r in range(ROW-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    for c in range(COLUMN-3):
        for r in range(ROW-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    for c in range(3,COLUMN):
        for r in range(ROW-3):
            if board[r][c] == piece and board[r+1][c-1] == piece and board[r+2][c-2] == piece and board[r+3][c-3] == piece:
                return True

def draw_board(board):
    for c in range(COLUMN):
        for r in range(ROW):
            pygame.draw.rect(screen,BLUE,(c*SQUARESIZE,r*SQUARESIZE+SQUARESIZE,SQUARESIZE,SQUARESIZE))
            pygame.draw.circle(screen,BLACK,(int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)
    for c in range(COLUMN):
        for r in range(ROW):  
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()

board=createboard()
print_board(board)
game_over= False
turn=0

pygame.init()
SQUARESIZE=100
width=COLUMN*SQUARESIZE
height=(ROW+1)*SQUARESIZE
size=(width,height)
RADIUS=int(SQUARESIZE/2-5)

screen= pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

text=pygame.font.SysFont("caliny",80)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]

            if turn == 0:     ##player1 input
                col = int(math.floor(posx/SQUARESIZE))
                if is_valid_position(board,col):
                    row = next_openrow(board,col)
                    play_piece(board,row,col,1)  
                   
                    print_board(board)     
                    if winning_move(board,1):
                        label=text.render("PLAYER 1 WINS!!!",1,RED)
                        screen.blit(label,(40,10))
                        game_over=True

            else:            ##player2 input
                col = int(math.floor(posx/SQUARESIZE))
                if is_valid_position(board,col):
                    row = next_openrow(board,col)
                    play_piece(board,row,col,2)
                    
                    print_board(board)     
                    if winning_move(board,2):
                        label=text.render("PLAYER 2 WINS!!!",2,YELLOW)
                        screen.blit(label,(40,10))
                        game_over=True

            turn += 1
            turn = turn % 2    
            draw_board(board)

            if game_over:
                pygame.time.wait(5000)  #5 seconds
